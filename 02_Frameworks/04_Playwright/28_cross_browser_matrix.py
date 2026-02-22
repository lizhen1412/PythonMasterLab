#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 28：跨浏览器矩阵（Chromium / Firefox / WebKit）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/28_cross_browser_matrix.py

本示例展示如何在多个浏览器上运行相同的测试：
1. p.chromium: Chromium 浏览器（Chrome、Edge 的基础）
2. p.firefox: Firefox 浏览器
3. p.webkit: WebKit 浏览器（Safari 的基础）

核心概念：
- Playwright 支持三大浏览器引擎：Chromium、Firefox、WebKit
- 同一套 API 可以在不同浏览器上运行
- 适合跨浏览器兼容性测试

浏览器引擎：
- Chromium: Chrome、Edge、Opera 等浏览器的基础
- Firefox: 独立的 Gecko 引擎
- WebKit: Safari 浏览器的基础

跨浏览器测试：
- 使用相同的代码测试不同浏览器
- 验证跨浏览器兼容性
- 发现浏览器特定的问题

注意事项：
- 需要安装相应的浏览器驱动：playwright install
- 不同浏览器可能有细微差异
- 某些浏览器可能在特定平台上不可用
"""

from __future__ import annotations


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        # 遍历三大浏览器引擎
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = None
            try:
                # 启动浏览器（直接赋值，不使用 with 语句）
                browser = browser_type.launch(headless=True)
                page = browser.new_page()
                page.set_content(f"<h2>{browser_type.name}</h2>")
                text = page.locator("h2").inner_text()
                print(f"[{browser_type.name}] ->", text)
            except Exception as exc:
                # 浏览器启动失败时继续尝试其他浏览器
                # 这里使用 Exception 是合理的，因为要处理多种可能的失败原因
                print(f"[{browser_type.name}] 启动失败 -> {exc}")
            finally:
                # 显式关闭浏览器
                if browser:
                    browser.close()


if __name__ == "__main__":
    main()
