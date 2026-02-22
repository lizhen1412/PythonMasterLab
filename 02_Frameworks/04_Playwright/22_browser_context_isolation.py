#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 22：BrowserContext 隔离。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/22_browser_context_isolation.py

本示例展示 BrowserContext 的隔离特性：
1. 每个 BrowserContext 有独立的 cookies、storage、cache
2. 不同 context 之间的数据完全隔离
3. 适合测试多用户场景或并行测试

核心概念：
- BrowserContext 是浏览器的隔离实例（类似隐身模式）
- 每个 context 有独立的 cookies、localStorage、sessionStorage
- context 之间不共享数据，互不影响
- 一个 browser 可以创建多个 context

Context 隔离的用途：
- 多用户测试：同时测试不同用户登录状态
- 并行测试：多个测试可以并行运行而不互相干扰
- 数据隔离：确保测试之间的数据独立
- 性能优化：多个 context 共享同一个 browser 进程

Context vs Page：
- Context: 隔离的浏览器环境（独立 cookies/storage）
- Page: Context 中的单个页面/标签页
- 一个 context 可以有多个 page

Context 的生命周期：
- new_context(): 创建新的 context
- context.close(): 关闭 context 及其所有页面
- 使用 with 语句自动管理生命周期
"""

from __future__ import annotations


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        c1, c2 = None, None
        try:
            # === 创建两个独立的 Context ===
            # 每个 context 有独立的 cookies、localStorage 等
            c1 = browser.new_context()
            c2 = browser.new_context()

            # 为 c1 添加 cookies
            c1.add_cookies([
                {
                    "name": "uid",
                    "value": "user-a",
                    "domain": "example.local",
                    "path": "/",
                }
            ])

            # 为 c2 添加 cookies（值不同）
            c2.add_cookies([
                {
                    "name": "uid",
                    "value": "user-b",
                    "domain": "example.local",
                    "path": "/",
                }
            ])

            # 验证两个 context 的 cookies 互不影响
            print("context1 cookie ->", c1.cookies()[0]["value"])
            print("context2 cookie ->", c2.cookies()[0]["value"])
        finally:
            # 确保资源正确清理
            if c1:
                c1.close()
            if c2:
                c2.close()
            browser.close()


if __name__ == "__main__":
    main()
