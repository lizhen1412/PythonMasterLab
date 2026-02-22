#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 18：Dialog 与 Popup。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/18_dialogs_and_popup.py

本示例展示如何处理浏览器的原生对话框和弹出窗口：
1. page.on("dialog", handler): 处理 alert、confirm、prompt 对话框
2. expect_popup(): 等待并捕获新窗口/标签页
3. popup.wait_for_load_state(): 等待弹出页面加载完成

核心概念：
- JavaScript 原生对话框（alert/confirm/prompt）会阻塞页面
- 必须注册 dialog 事件处理器来处理这些对话框
- dialog.accept() 或 dialog.dismiss() 用于关闭对话框
- expect_popup() 用于处理 window.open() 打开的新窗口

Dialog 对话框处理：
- alert(): 只需 accept()，无法获取输入
- confirm(): 返回 true（accept）或 false（dismiss）
- prompt(): 可以接受或设置默认值

Popup 弹出窗口处理：
- expect_popup() 返回 PopupContext，通过 .value 获取 Page 对象
- 可以在多个新窗口打开时使用 expect_popup() 精确捕获特定窗口
"""

from __future__ import annotations


# 模拟包含对话框和弹出窗口的 HTML
HTML = """
<button id="alert">Alert</button>
<button id="pop">Popup</button>
<script>
  document.querySelector('#alert').addEventListener('click', () => alert('hello dialog'));
  document.querySelector('#pop').addEventListener('click', () => window.open('data:text/html,<h3 id=ok>popup</h3>', '_blank'));
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 用于记录对话框消息
    dialogs: list[str] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.set_content(HTML)

            # === 处理 Dialog 对话框 ===
            # Dialog 对话框（alert/confirm/prompt）会阻塞页面执行
            # 必须注册 dialog 事件处理器来自动处理这些对话框
            def on_dialog(dialog) -> None:  # type: ignore[no-untyped-def]
                """对话框事件处理器"""
                dialogs.append(dialog.message)
                # accept(): 接受对话框（相当于点击"确定"）
                # dismiss(): 拒绝对话框（相当于点击"取消"）
                dialog.accept()

            # 注册 dialog 事件监听器
            page.on("dialog", on_dialog)

            # 点击按钮触发 alert 对话框
            # 由于注册了处理器，对话框会被自动接受
            page.click("#alert")

            # === 处理 Popup 弹出窗口 ===
            # expect_popup() 等待并捕获 window.open() 打开的新窗口
            # 返回 PopupContext 对象，通过 .value 获取新页面的 Page 对象
            with page.expect_popup() as popup_info:
                page.click("#pop")

            # 获取新打开的页面
            popup = popup_info.value
            # 等待弹出页面加载完成
            popup.wait_for_load_state()

            # 打印结果
            print("dialog messages ->", dialogs)
            print("popup text ->", popup.locator("#ok").inner_text())
        finally:
            browser.close()


if __name__ == "__main__":
    main()
