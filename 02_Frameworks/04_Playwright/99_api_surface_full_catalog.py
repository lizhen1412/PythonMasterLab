#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 99：Playwright 全 API 知识点目录（静态方法清单）。
Author: Lambert

说明：
- 这个文件用于“全覆盖学习导航”。
- `if False` 代码块不会执行，只用于展示 API 入口，方便对照 third_party_refs。
- 复杂场景（HAR/CDP/WebSocket/持久化上下文）建议配合官方文档和本章其他示例学习。

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/99_api_surface_full_catalog.py
"""

from __future__ import annotations

from typing import Any


def api_surface_catalog(
    page: Any,
    context: Any,
    browser: Any,
    route: Any,
    request: Any,
    response: Any,
    locator: Any,
    frame: Any,
    keyboard: Any,
    mouse: Any,
    clock: Any,
    tracing: Any,
    dialog: Any,
    download: Any,
    video: Any,
    expect: Any,
    browser_type: Any,
    playwright: Any,
    popup: Any,
    websocket_route: Any,
) -> None:
    if False:
        # page / locator / frame advanced
        page.add_init_script()
        page.add_locator_handler(locator, lambda: None)
        page.remove_locator_handler(locator)
        page.add_script_tag()
        page.add_style_tag()
        page.expect_console_message()
        page.expect_event("event")
        page.wait_for_event("event")
        page.expect_file_chooser()
        page.expect_navigation()
        page.expect_worker()
        page.expect_websocket()
        page.expose_binding("name", lambda source: None)
        page.expose_function("name", lambda: None)
        page.frame("frame-name")
        page.route_from_har("demo.har")
        page.route_web_socket("**/*", lambda ws: None)
        page.go_back()
        page.go_forward()
        page.reload()
        page.dispatch_event("#id", "click")
        page.drag_and_drop("#a", "#b")
        page.tap("#id")
        page.pause()
        page.pdf()
        page.remove_listener("console", lambda msg: None)
        page.request_gc()
        page.requests()
        page.console_messages()
        page.page_errors()
        page.input_value("#name")
        page.is_checked("#agree")
        page.is_closed()
        page.is_disabled("#btn")
        page.is_editable("#name")
        page.is_enabled("#name")
        page.is_hidden("#x")
        page.is_visible("#name")
        page.get_by_alt_text("alt")
        page.get_by_placeholder("placeholder")
        page.get_by_title("title")
        page.set_checked("#agree", True)
        page.set_default_navigation_timeout(1000)
        page.set_extra_http_headers({"X-Demo": "1"})
        page.set_viewport_size({"width": 1200, "height": 800})
        page.emulate_media(color_scheme="dark")
        page.once("console", lambda msg: None)

        locator.text_content()
        locator.inner_html()
        locator.get_attribute("data-id")
        locator.set_checked(True)
        locator.aria_snapshot()

        frame.frame_element()
        frame.add_script_tag()
        frame.query_selector("#id")
        frame.press("#id", "Enter")
        frame.wait_for_load_state()
        frame.expect_navigation()
        frame.evaluate("() => 1")
        frame.evaluate_handle("() => ({})")
        frame.eval_on_selector("#id", "el => el.textContent")
        frame.locator("#id")

        # context / browser / browser_type / playwright
        context.add_init_script()
        context.expect_console_message()
        context.expect_event("page")
        context.wait_for_event("page")
        context.expect_page()
        context.expose_binding("b", lambda source: None)
        context.expose_function("f", lambda: None)
        context.new_cdp_session(page)
        context.route_from_har("demo.har")
        context.unroute_all()
        context.set_default_navigation_timeout(1000)
        context.set_extra_http_headers({"X-Context": "1"})
        context.set_geolocation({"latitude": 0, "longitude": 0})
        context.set_offline(True)
        context.grant_permissions(["geolocation"])
        context.on("page", lambda p: None)

        browser.on("disconnected", lambda _: None)
        browser.is_connected()
        browser.start_tracing(page=page)
        browser.stop_tracing()

        browser_type.connect("ws://127.0.0.1:9222")
        browser_type.connect_over_cdp("http://127.0.0.1:9222")
        browser_type.launch_persistent_context("/tmp/persistent-profile")

        playwright.stop()

        # route / request / response / websocket route style methods
        route.fetch()
        route.send("message")
        route.close()

        request.all_headers()
        request.header_value("x")
        request.headers_array()
        request.is_navigation_request()
        request.sizes()
        request.response()
        request.finish()
        request.write("bytes")
        request.getHeader("x")
        request.setHeader("x", "1")
        request.setResponseCode(200)
        request.serve_file("/tmp/demo.txt")
        request.loseConnection()

        response.all_headers()
        response.body()
        response.finished()
        response.header_value("x")
        response.header_values("x")
        response.headers_array()
        response.security_details()
        response.server_addr()
        response.finish()
        response.write("bytes")
        response.setHeader("x", "1")

        # clock / tracing / dialog / download / video
        clock.pause_at(1000)
        clock.run_for(1000)
        clock.set_fixed_time(1000)
        clock.set_system_time(1000)

        tracing.group("group-name")
        tracing.group_end()
        tracing.start_chunk(name="chunk")
        tracing.stop_chunk(path="/tmp/chunk.zip")

        dialog.dismiss()

        download.path()
        download.failure()
        download.cancel()
        download.delete()
        download.save_as("/tmp/demo.txt")

        video.save_as("/tmp/video.webm")
        expect.set_options(timeout=2000)

        # mouse down/up (mouse.move/click/dblclick/wheel 已在其他示例)
        mouse.down()
        mouse.up()

        # popup opener
        popup.opener()


def main() -> None:
    print("这个文件是 Playwright API 全量学习目录（静态清单）。")
    print("建议先跑 03~41 的可运行示例，再回看这里补齐稀有 API 认知。")


if __name__ == "__main__":
    main()
