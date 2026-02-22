#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 41：query_selector / eval_on_selector 兼容 API。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/41_dom_query_legacy_apis.py

本示例展示 Playwright 的传统 DOM 查询 API：
1. query_selector(): 查询单个元素
2. query_selector_all(): 查询多个元素
3. eval_on_selector(): 对元素执行 JavaScript
4. eval_on_selector_all(): 对多个元素执行 JavaScript

核心概念：
- 这些是 Playwright 早期的 API
- 官网现在更推荐使用 locator 风格
- 但很多第三方代码仍在使用这些 API
- 学习这些 API 有助于阅读和理解老代码

传统 API vs Locator：
- query_selector 返回 ElementHandle，locator 返回 Locator 对象
- query_selector 立即执行查询，locator 是懒加载
- locator 支持自动重试，query_selector 不支持

传统 API 用法：
- query_selector(selector): 查询单个元素
- query_selector_all(selector): 查询所有匹配元素
- eval_on_selector(selector, js): 对元素执行 JS
- eval_on_selector_all(selector, js): 对多个元素执行 JS

何时使用传统 API：
- 阅读第三方代码时
- 需要立即获取 ElementHandle 时
- 与某些兼容性工具集成时
"""

from __future__ import annotations


HTML = """
<ul>
  <li class="it">A</li>
  <li class="it">B</li>
  <li class="it">C</li>
</ul>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === query_selector(): 查询单个元素 ===
        first = page.query_selector(".it")
        if first is None:
            print("query_selector 未找到元素")
            browser.close()
            return
        print("query_selector first ->", first.inner_text())

        # === query_selector_all(): 查询所有匹配元素 ===
        all_items = page.query_selector_all(".it")
        print("query_selector_all count ->", len(all_items))

        # === eval_on_selector(): 对元素执行 JavaScript ===
        second = page.eval_on_selector(".it:nth-child(2)", "el => el.textContent")
        print("eval_on_selector second ->", second)

        # === eval_on_selector_all(): 对多个元素执行 JavaScript ===
        joined = page.eval_on_selector_all(
            ".it",
            "els => els.map(el => el.textContent).join('-')",
        )
        print("eval_on_selector_all joined ->", joined)

        print("page.content length ->", len(page.content()))

        browser.close()


if __name__ == "__main__":
    main()

