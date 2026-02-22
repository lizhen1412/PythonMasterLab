#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 35：expect 常见断言全示例。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/35_expect_assertions_all.py

本示例展示 expect 断言 API 的常见用法：
1. to_have_title(): 断言页面标题
2. to_be_checked(): 断言复选框已勾选
3. to_be_enabled(): 断言元素可用
4. to_be_visible(): 断言元素可见
5. to_contain_text(): 断言包含文本
6. to_have_attribute(): 断言属性值
7. to_have_count(): 断言元素数量
8. to_have_text(): 断言元素文本
9. to_have_value(): 断言输入框值
10. to_have_url(): 断言页面 URL

核心概念：
- expect() 是 Playwright 推荐的断言方式
- 自动重试直到断言成功或超时
- 提供清晰的错误信息

常见断言分类：
- 页面状态：to_have_title、to_have_url
- 元素状态：to_be_visible、to_be_enabled、to_be_checked
- 文本内容：to_have_text、to_contain_text
- 属性值：to_have_attribute、to_have_value
- 数量统计：to_have_count
"""

from __future__ import annotations

import re
from urllib.parse import quote


HTML = """
<!doctype html>
<html>
  <head>
    <title>Assertions Demo</title>
  </head>
  <body>
    <input id="name" value="alice" />
    <label>
      <input id="agree" type="checkbox" checked />
      Agree
    </label>
    <button id="save" type="button">Save</button>

    <p id="msg" data-role="notice">hello playwright learner</p>

    <ul>
      <li class="item">A</li>
      <li class="item">B</li>
    </ul>

    <a href="#done">Jump</a>
    <h2 id="done">Done</h2>
  </body>
</html>
"""


def to_data_url(html: str) -> str:
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
            page.goto(to_data_url(HTML))

            # === 页面状态断言 ===
            expect(page).to_have_title("Assertions Demo")

            # === 元素状态断言 ===
            expect(page.locator("#agree")).to_be_checked()
            expect(page.locator("#save")).to_be_enabled()
            expect(page.get_by_role("heading", name="Done")).to_be_visible()

            # === 文本和属性断言 ===
            expect(page.locator("#msg")).to_contain_text("playwright")
            expect(page.locator("#msg")).to_have_attribute("data-role", "notice")

            # === 数量和值断言 ===
            expect(page.locator(".item")).to_have_count(2)
            expect(page.locator(".item").nth(0)).to_have_text("A")
            expect(page.locator("#name")).to_have_value("alice")

            # === URL 断言 ===
            page.get_by_role("link", name="Jump").click()
            expect(page).to_have_url(re.compile(r".*#done$"))

            print("[OK] expect 常见断言全部通过")
        finally:
            browser.close()


if __name__ == "__main__":
    main()

