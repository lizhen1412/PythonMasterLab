#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：等待机制与超时处理。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/07_wait_for_and_timeouts.py

本示例展示 Playwright 的等待机制：
1. wait_for(): 等待元素达到指定状态
2. wait_for_function(): 等待 JavaScript 函数返回 true
3. set_default_timeout(): 设置默认超时时间
4. TimeoutError: 捕获超时异常

核心概念：
- Playwright 会自动等待元素可操作（可见、启用、稳定）
- 大多数操作（如 click、fill）内置了自动等待
- 可以显式使用 wait_for* 方法进行更精确的控制
- 默认超时时间是 30 秒，可以根据需要调整

等待策略：
- wait_for(state="visible"): 等待元素可见
- wait_for(state="attached"): 等待元素存在于 DOM
- wait_for(state="hidden"): 等待元素隐藏
- wait_for(state="detached"): 等待元素从 DOM 移除
- wait_for_function(): 等待自定义条件
"""

from __future__ import annotations


# 模拟一个异步加载的页面
HTML = """
<div id="status">loading</div>
<script>
  // 200ms 后改变状态
  setTimeout(() => {
    document.querySelector('#status').textContent = 'ready';
  }, 200);
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import TimeoutError, sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()

            # 设置默认超时时间为 1000ms（1秒）
            # 这会影响后续所有等待操作的超时时间
            page.set_default_timeout(1000)

            page.set_content(HTML)

            # === wait_for() ===
            # 等待元素达到指定状态
            # state="visible" 表示等待元素可见
            # 这是默认状态，可以省略
            page.locator("#status").wait_for(state="visible")

            # === wait_for_function() ===
            # 等待 JavaScript 函数返回 true
            # 这里我们等待状态文本变为 "ready"
            page.wait_for_function(
                "() => document.querySelector('#status').textContent === 'ready'"
            )

            # 获取最终状态
            status_text = page.locator("#status").inner_text()
            print("status ->", status_text)

            # === 超时处理 ===
            # 尝试等待一个不存在的元素
            # 使用 try-except 捕获 TimeoutError
            try:
                # 设置很短的超时时间（150ms）
                page.wait_for_selector("#never-exists", timeout=150)
            except TimeoutError:
                print("捕获超时：#never-exists 未出现（符合预期）")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
