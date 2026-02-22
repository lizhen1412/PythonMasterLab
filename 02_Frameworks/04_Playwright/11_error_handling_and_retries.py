#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：常见异常处理与重试。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/11_error_handling_and_retries.py

本示例展示 Playwright 的错误处理和重试机制：
1. 自定义重试逻辑：处理不稳定操作
2. 异常捕获：处理超时、元素未找到等错误
3. expect(): Playwright 内置的重试机制

核心概念：
- Playwright 的自动等待机制会处理大多数时序问题
- 但某些场景仍需要自定义重试逻辑
- 不稳定的网络、随机加载的元素等场景需要重试
- expect() 提供了更优雅的断言重试方式

常见不稳定场景：
- 网络请求偶尔失败
- 元素偶尔未渲染
- 动态内容加载延迟
- 第三方服务不稳定

重试策略：
- 固定次数重试：最多尝试 N 次
- 指数退避：每次重试间隔时间递增
- 条件重试：直到满足某个条件
- 超时控制：设置最长等待时间
"""

from __future__ import annotations


# 模拟一个不稳定的操作
# 前 2 次执行会失败，第 3 次才成功
def flaky_action(page) -> bool:  # type: ignore[no-untyped-def]
    """模拟一个不稳定的操作，前 2 次失败，第 3 次成功

    Args:
        page: Playwright Page 对象

    Returns:
        bool: 操作是否成功
    """
    current = page.evaluate("() => window.__tries")
    if current < 2:
        page.evaluate("() => { window.__tries += 1; }")
        return False
    return True


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

            # 初始化计数器，模拟不稳定场景
            page.set_content("<script>window.__tries = 0;</script>")

            # === 自定义重试逻辑 ===
            # 对于不稳定的操作，可以使用循环重试
            max_retries = 3
            ok = False

            print("开始执行不稳定的操作...")
            for i in range(1, max_retries + 1):
                if flaky_action(page):
                    ok = True
                    print(f"  第 {i} 次执行成功 ✓")
                    break
                print(f"  第 {i} 次执行失败，准备重试...")

            # 验证是否成功
            assert ok, "超过最大重试次数"

            # === 使用 expect() 进行断言 ===
            # Playwright 提供了 expect() 方法，它会自动重试
            # 这比手动编写重试逻辑更优雅
            page.expect_timeout(5000).to_pass(lambda _: (
                print("  expect() 断言通过 ✓")
            ))

            print("\n演示完成！")
            print("\n提示:")
            print("  - 对于不稳定操作，可以使用循环重试")
            print("  - Playwright 的 expect() 会自动重试断言")
            print("  - 大多数操作都有自动等待，无需手动处理时序")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
