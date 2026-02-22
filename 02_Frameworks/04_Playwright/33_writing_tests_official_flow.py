#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 33：官网 Writing tests 首个示例（Python 版）复刻。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/33_writing_tests_official_flow.py

本示例复刻 Playwright 官网文档中的第一个测试示例：
1. 使用 get_by_role 语义化定位器
2. 使用 expect 断言 API
3. 演示完整的测试流程

核心概念：
- get_by_role(): 使用 ARIA 角色定位元素（推荐）
- expect(): Playwright 的断言 API，自动重试
- 官方推荐的最佳实践

语义化定位器（优先级顺序）：
1. get_by_role(): 按角色定位（link、button、heading 等）
2. get_by_text(): 按文本内容定位
3. get_by_label(): 按标签关联定位
4. get_by_placeholder(): 按占位符定位
5. get_by_alt_text(): 按图片 alt 文本定位

expect 断言方法：
- to_have_title(): 断言页面标题
- to_have_url(): 断言页面 URL
- to_be_visible(): 断言元素可见
- to_have_text(): 断言元素文本
- to_be_enabled(): 断言元素可用

测试流程：
1. 访问页面
2. 断言页面标题
3. 点击链接
4. 断言 URL 和可见性
"""

from __future__ import annotations

import re
from urllib.parse import quote


# 模拟一个简单的 HTML 页面
HTML = """
<!doctype html>
<html>
  <head>
    <title>Playwright Docs Demo</title>
  </head>
  <body>
    <a href="#intro">Get started</a>
    <h1 id="intro">Installation</h1>
  </body>
</html>
"""


def to_data_url(html: str) -> str:
    """将 HTML 转换为 data URL"""
    return "data:text/html," + quote(html)


def main() -> None:
    try:
        from playwright.sync_api import expect, sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()

            # 导航到测试页面
            page.goto(to_data_url(HTML))
            print("page.title() ->", page.title())

            # === 官方推荐测试流程 ===
            # 1. 断言页面标题
            expect(page).to_have_title(re.compile("Playwright Docs Demo"))

            # 2. 使用语义化定位器点击链接
            # get_by_role("link", name="...") 按角色和名称定位
            page.get_by_role("link", name="Get started").click()

            # 3. 断言 URL 包含锚点
            expect(page).to_have_url(re.compile(r".*#intro$"))

            # 4. 断言标题可见
            expect(page.get_by_role("heading", name="Installation")).to_be_visible()

            # 5. 断言文本可见
            expect(page.get_by_text("Installation")).to_be_visible()

            print("[OK] 官网 Writing tests 核心流程通过")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
