#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：断言（expect API）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/16_assertions_expect_api.py

本示例展示 Playwright 的 expect 断言 API：
1. expect(): 创建断言对象
2. to_have_count(): 断言元素数量
3. to_have_text(): 断言元素文本

核心概念：
- expect() 是 Playwright 推荐的断言方式，比原生 assert 更强大
- expect 断言会自动重试（默认超时 5 秒）
- 这对于异步加载的页面特别有用
- 失败时会自动截图（在测试环境中）

expect vs assert：
- assert: 立即检查，失败就抛出异常
- expect: 自动重试直到超时，提供更好的错误信息

常用断言方法：
- to_have_text(): 断言文本内容
- to_have_count(): 断言元素数量
- to_be_visible(): 断言元素可见
- to_be_enabled(): 断言元素可用
- to_have_attribute(): 断言属性值
- to_have_url(): 断言页面 URL
"""

from __future__ import annotations


HTML = """
<ul>
  <li class="todo">learn</li>
  <li class="todo">practice</li>
  <li class="todo">share</li>
</ul>
"""


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
            page.set_content(HTML)

            # 定位所有 todo 项
            todos = page.locator("li.todo")

            # === expect 断言 ===
            # expect() 会自动重试，直到断言成功或超时
            # 这对于异步加载的内容特别有用

            # to_have_count(3): 断言匹配的元素数量为 3
            expect(todos).to_have_count(3)

            # to_have_text("learn"): 断言第一个元素的文本是 "learn"
            expect(todos.nth(0)).to_have_text("learn")

            # to_have_text("share"): 断言第三个元素的文本是 "share"
            expect(todos.nth(2)).to_have_text("share")

            print("[OK] expect 断言通过")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
