#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：导航与自动等待（auto-wait）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/15_navigation_and_auto_wait.py

本示例展示 Playwright 的页面导航和自动等待机制：
1. goto(): 导航到指定 URL
2. click(): 点击元素（自动等待可点击）
3. 自动等待：Playwright 的核心特性

核心概念：
- Playwright 会自动等待元素可操作（可见、启用、稳定）
- 大多数操作（如 click、fill）都内置了自动等待
- 无需使用 time.sleep() 或复杂的等待逻辑
- 自动等待超时时间默认为 30 秒

自动等待的工作原理：
1. 执行操作前检查元素状态
2. 如果元素不可操作，等待并重试
3. 超过超时时间后抛出 TimeoutError

自动等待的优势：
- 代码更简洁：无需手动编写等待逻辑
- 更稳定：不会因为时序问题导致测试失败
- 更快速：只在需要时等待，不会固定等待

常见操作及其自动等待：
- click(): 等待元素可见、启用、不被遮挡
- fill(): 等待输入框可见、可编辑
- select_option(): 等待 select 元素可见
- wait_for_selector(): 显式等待元素出现
"""

from __future__ import annotations


# 模拟一个异步加载的页面
# 按钮初始状态为禁用（disabled），200ms 后变为可用
HTML = """
<button id="submit" disabled>Submit</button>
<script>
  setTimeout(() => {
    document.querySelector('#submit').disabled = false;
    document.querySelector('#submit').textContent = 'Ready';
  }, 200);
</script>
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

            # === goto(): 导航到 URL ===
            # Playwright 会自动等待页面加载完成（load 事件）
            # 这里使用 data URL 直接加载 HTML 内容
            page.goto("data:text/html,<h2>nav ok</h2>")
            nav_text = page.locator("h2").inner_text()
            print("goto data url ->", nav_text)

            # === set_content(): 设置页面内容 ===
            page.set_content(HTML)

            # === click(): 自动等待示例 ===
            # 按钮初始为禁用状态，Playwright 会自动等待变为可用
            # 无需使用 time.sleep() 或显式等待
            page.click("#submit")

            # 获取点击后的按钮文本
            button_text = page.locator("#submit").inner_text()
            print("button text after click ->", button_text)
        finally:
            browser.close()

    # === 自动等待的优势 ===
    print("\n自动等待的优势:")
    print("  - 代码简洁：无需手动编写等待逻辑")
    print("  - 更稳定：不会因时序问题导致测试失败")
    print("  - 更快速：只在需要时等待，不浪费时间")


if __name__ == "__main__":
    main()
