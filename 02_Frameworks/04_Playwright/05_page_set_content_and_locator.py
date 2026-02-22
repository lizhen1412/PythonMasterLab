#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：set_content + locator 定位与断言。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/05_page_set_content_and_locator.py

本示例展示元素定位的核心方法：
1. set_content(): 设置页面 HTML 内容
2. get_by_test_id(): 通过 data-testid 属性定位（推荐用于测试）
3. locator(): 通过 CSS 选择器定位元素
4. count(): 获取匹配元素的数量
5. nth(n): 获取第 n 个匹配的元素（从 0 开始）
6. inner_text(): 获取元素的内部文本
7. assert: 断言验证结果

核心概念：
- Locator 是 Playwright 推荐的定位方式，它是惰性的（调用方法时才查找）
- get_by_test_id() 是最稳定的测试选择器（需要 HTML 有 data-testid 属性）
- CSS 选择器（如 "li.item"）用于通过类名定位
- nth() 用于选择多个匹配元素中的某一个
"""

from __future__ import annotations


# 测试用的 HTML 内容
HTML = """
<div>
  <h2 data-testid="headline">Todo</h2>
  <ul>
    <li class="item">buy milk</li>
    <li class="item">read docs</li>
    <li class="item">sleep early</li>
  </ul>
</div>
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
            # 可以直接从 browser 创建 page（会自动创建一个 context）
            page = browser.new_page()

            # 设置页面内容
            page.set_content(HTML)

            # === 方式 1: 使用 get_by_test_id() 定位 ===
            # 这是最推荐的测试定位方式，因为它对页面结构变化不敏感
            # 需要元素有 data-testid 属性
            headline = page.get_by_test_id("headline").inner_text()
            print("headline ->", headline)

            # === 方式 2: 使用 locator() + CSS 选择器 ===
            # locator() 返回 Locator 对象，可以链式调用
            # "li.item" 表示选择所有 class="item" 的 <li> 元素
            items = page.locator("li.item")

            # count() 返回匹配元素的数量
            count = items.count()
            print("item count ->", count)

            # nth(0) 获取第一个匹配的元素（索引从 0 开始）
            # inner_text() 获取元素的文本内容
            first_item = items.nth(0).inner_text()
            print("first item ->", first_item)

            # === 断言验证结果 ===
            # 使用 assert 验证结果是否符合预期
            assert headline == "Todo", "标题应该是 'Todo'"
            assert count == 3, "应该有 3 个 todo 项"

            # 验证所有 todo 项的内容
            second_item = items.nth(1).inner_text()
            third_item = items.nth(2).inner_text()
            assert second_item == "read docs"
            assert third_item == "sleep early"

            print("所有断言通过！")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
