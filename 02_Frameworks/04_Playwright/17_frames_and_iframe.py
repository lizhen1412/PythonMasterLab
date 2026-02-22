#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：Frames / IFrame 定位。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/17_frames_and_iframe.py

本示例展示如何处理 iframe 和 frame：
1. frame_locator(): 定位 iframe/frame
2. 在 iframe 中定位元素

核心概念：
- iframe（内嵌框架）是页面中的独立文档，有自己的 DOM
- 使用 frame_locator() 进入 iframe，然后继续定位元素
- frame_locator() 返回 FrameLocator 对象，可以链式调用
- 支持嵌套的 iframe

常见用途：
- 处理使用 iframe 的第三方组件（如编辑器、支付界面）
- 处理传统 frameset 布局
- 与嵌入式内容交互
"""

from __future__ import annotations


# 包含 iframe 的 HTML
# srcdoc 属性直接指定 iframe 的 HTML 内容
HTML = """
<iframe id="inner" srcdoc="<p id='msg'>hello from frame</p>"></iframe>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.set_content(HTML)

            # === frame_locator() ===
            # frame_locator() 用于定位 iframe 或 frame
            # 返回 FrameLocator 对象，可以继续链式调用 locator()
            #
            # 语法：page.frame_locator("#iframe-id").locator("#element-in-iframe")
            #
            # 这里：
            # 1. frame_locator("#inner") 进入 id="inner" 的 iframe
            # 2. locator("#msg") 在 iframe 中定位 id="msg" 的元素
            # 3. inner_text() 获取元素的文本内容
            msg = page.frame_locator("#inner").locator("#msg").inner_text()
            print("frame message ->", msg)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
