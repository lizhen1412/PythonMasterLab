#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 42：高级事件、context 配置与导航（可运行）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/42_advanced_events_and_context.py

本示例展示 Playwright 的高级功能：
1. Context 高级配置：超时、headers、权限、地理位置、离线模式
2. 页面事件：console、dialog、popup、file chooser
3. 页面操作：双击、拖拽、导航、历史记录
4. 暴露函数：expose_function、expose_binding
5. 事件等待：expect_event、wait_for_event

核心概念：
- Context 提供浏览器环境级别的配置
- 页面事件可以监听和等待
- 可以向页面注入 Python 函数
- 支持复杂的交互操作

Context 配置：
- set_default_timeout(): 设置默认超时
- set_extra_http_headers(): 设置默认 headers
- grant_permissions(): 授予权限（如地理位置）
- set_geolocation(): 设置地理位置
- set_offline(): 设置离线模式
- add_init_script(): 注入初始化脚本

页面事件：
- console: 控制台消息
- dialog: 对话框
- popup: 弹出窗口
- file_chooser: 文件选择器

暴露函数：
- expose_function(name, func): 暴露 Python 函数给页面
- expose_binding(name, func): 暴露带页面上下文的函数

交互操作：
- dblclick(): 双击
- drag_and_drop(): 拖拽
- tap(): 触摸点击
- dispatch_event(): 触发 DOM 事件

导航操作：
- go_back(): 后退
- go_forward(): 前进
- reload(): 刷新
- expect_navigation(): 等待导航
"""

from __future__ import annotations

from urllib.parse import quote


HTML = """
<!doctype html>
<html>
  <head>
    <title>Advanced Demo</title>
  </head>
  <body>
    <label for="name">Name</label>
    <input id="name" placeholder="your-name" value="lizhen" />

    <img alt="demo-image" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==" />
    <button id="title-btn" title="settings-title">Title Button</button>

    <label>
      <input id="agree" type="checkbox" checked />
      Agree
    </label>
    <button id="disabled-btn" disabled>Disabled</button>
    <button id="double-btn" type="button">Double</button>
    <button id="open-file" type="button">Open File Chooser</button>
    <button id="open-popup" type="button">Open Popup</button>
    <button id="go-next" type="button">Go Next</button>

    <div id="drag-source" draggable="true">S</div>
    <div id="drag-target">T</div>
    <p id="drop-state"></p>
    <p id="event-state"></p>
    <input id="hidden-file" type="file" style="display:none" />

    <script>
      document.querySelector('#open-file').addEventListener('click', () => {
        document.querySelector('#hidden-file').click();
      });

      document.querySelector('#open-popup').addEventListener('click', () => {
        window.open('data:text/html,<h3 id=pop-ok>popup-ok</h3>', '_blank');
      });

      document.querySelector('#go-next').addEventListener('click', () => {
        location.href = 'data:text/html,<title>Next</title><h2 id=next>next page</h2>';
      });

      const source = document.querySelector('#drag-source');
      const target = document.querySelector('#drag-target');
      source.addEventListener('dragstart', (e) => {
        e.dataTransfer.setData('text/plain', 'drag-data');
      });
      target.addEventListener('drop', (e) => {
        e.preventDefault();
        document.querySelector('#drop-state').textContent = e.dataTransfer.getData('text/plain');
      });
      target.addEventListener('dragover', (e) => e.preventDefault());

      document.querySelector('#double-btn').addEventListener('dblclick', () => {
        document.querySelector('#event-state').textContent = 'double-clicked';
      });
    </script>
  </body>
</html>
"""


def to_data_url(html: str) -> str:
    return "data:text/html," + quote(html)


def safe_call(label: str, func) -> None:  # type: ignore[no-untyped-def]
    try:
        result = func()
        print(f"{label} -> {result}")
    except Exception as exc:
        print(f"[skip] {label}: {exc}")


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        context.set_default_timeout(2500)
        context.set_default_navigation_timeout(2500)
        context.set_extra_http_headers({"X-Playwright-Advanced": "yes"})
        context.add_init_script("window.__ctx_init = true;")
        safe_call("context.grant_permissions", lambda: context.grant_permissions(["geolocation"]))
        safe_call(
            "context.set_geolocation",
            lambda: context.set_geolocation({"latitude": 31.2304, "longitude": 121.4737}),
        )
        safe_call("context.set_offline(true)", lambda: context.set_offline(True))
        safe_call("context.set_offline(false)", lambda: context.set_offline(False))

        context.route(
            "**/ctx-api",
            lambda route: route.fulfill(
                status=200,
                content_type="application/json",
                body='{"ok": true, "from": "context.route"}',
            ),
        )

        page = context.new_page()
        page.set_viewport_size({"width": 960, "height": 720})
        safe_call("page.emulate_media", lambda: page.emulate_media(color_scheme="light"))
        page.add_init_script("window.__page_init = 'ok';")
        page.goto(to_data_url(HTML))
        page.add_style_tag(content="body{font-family:sans-serif}")
        page.add_script_tag(content="window.__script_tag_loaded = true")

        safe_call("page.expose_function", lambda: page.expose_function("py_add", lambda a, b: a + b))
        safe_call(
            "page.expose_binding",
            lambda: page.expose_binding("py_echo", lambda source, value: f"{source.page.url}|{value}"),
        )
        safe_call("call exposed function", lambda: page.evaluate("() => window.py_add(2, 3)"))
        safe_call("call exposed binding", lambda: page.evaluate("() => window.py_echo('ok')"))

        safe_call("page.get_by_placeholder", lambda: page.get_by_placeholder("your-name").input_value())
        safe_call("page.get_by_alt_text", lambda: page.get_by_alt_text("demo-image").is_visible())
        safe_call(
            "page.get_by_title",
            lambda: page.get_by_title("settings-title").inner_text(),
        )

        safe_call("page.input_value", lambda: page.input_value("#name"))
        safe_call("page.is_visible", lambda: page.is_visible("#name"))
        safe_call("page.is_hidden", lambda: page.is_hidden("#not-exists"))
        safe_call("page.is_enabled", lambda: page.is_enabled("#name"))
        safe_call("page.is_disabled", lambda: page.is_disabled("#disabled-btn"))
        safe_call("page.is_checked", lambda: page.is_checked("#agree"))
        safe_call("page.is_editable", lambda: page.is_editable("#name"))

        console_logs: list[str] = []

        def on_console(msg) -> None:  # type: ignore[no-untyped-def]
            console_logs.append(msg.text)

        page.on("console", on_console)
        page.once("console", lambda msg: console_logs.append("once:" + msg.text))
        page.evaluate("() => console.log('from-once-and-on')")
        safe_call("page.wait_for_event(console)", lambda: page.wait_for_event("console"))

        try:
            with page.expect_event("console"):
                page.evaluate("() => console.log('expect-event')")
            print("page.expect_event(console) -> ok")
        except Exception as exc:
            print(f"[skip] page.expect_event(console): {exc}")

        try:
            with page.expect_console_message():
                page.evaluate("() => console.log('expect-console')")
            print("page.expect_console_message -> ok")
        except Exception as exc:
            print(f"[skip] page.expect_console_message: {exc}")

        with page.expect_file_chooser() as fc_info:
            page.click("#open-file")
        file_chooser = fc_info.value
        print("file chooser ready ->", bool(file_chooser))

        with context.expect_page() as new_page_info:
            page.click("#open-popup")
        popup = new_page_info.value
        popup.wait_for_load_state()
        print("popup opener exists ->", popup.opener() is not None)
        popup.close()

        page.dblclick("#double-btn")
        page.drag_and_drop("#drag-source", "#drag-target")
        safe_call("page.tap", lambda: page.tap("#double-btn"))
        page.dispatch_event("#title-btn", "click")
        print("event-state ->", page.locator("#event-state").inner_text())
        print("drop-state ->", page.locator("#drop-state").inner_text())

        with page.expect_navigation():
            page.click("#go-next")
        safe_call("page.go_back", lambda: page.go_back())
        safe_call("page.go_forward", lambda: page.go_forward())
        safe_call("page.reload", lambda: page.reload())

        page.remove_listener("console", on_console)
        safe_call("page.console_messages", lambda: page.console_messages())
        safe_call("page.page_errors", lambda: page.page_errors())
        safe_call("page.request_gc", lambda: page.request_gc())

        # === Context 事件等待 ===
        try:
            with context.expect_event("page") as popup_info:
                page.click("#open-popup")
            popup2 = popup_info.value
            popup2.close()
            print("context.expect_event(page) -> ok")
        except Exception as exc:
            print(f"[skip] context.expect_event(page): {exc}")

        safe_call("context.wait_for_event(page)", lambda: context.wait_for_event("page", timeout=100))
        try:
            with context.expect_console_message():
                page.evaluate("() => console.log('context-console')")
            print("context.expect_console_message -> ok")
        except Exception as exc:
            print(f"[skip] context.expect_console_message: {exc}")

        context.unroute("**/ctx-api")
        safe_call("context.unroute_all", lambda: context.unroute_all())

        print("console logs ->", console_logs[:5])
        print("browser is_connected ->", browser.is_connected())

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
