#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：sync_playwright 启动与最小页面流程。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/04_sync_playwright_start.py

本示例展示 Playwright 的最小可运行流程：
1. 使用 sync_playwright() 启动 Playwright
2. 启动 Chromium 浏览器（headless 模式）
3. 创建浏览器上下文（BrowserContext）
4. 创建新页面（Page）
5. 设置页面内容并定位元素
6. 关闭上下文和浏览器

核心概念：
- sync_playwright(): 同步 API 的入口点，使用上下文管理器自动清理资源
- Browser: 浏览器实例，通过 launch() 启动
- BrowserContext: 浏览器上下文，类似隐身模式，可隔离 cookie 和缓存
- Page: 页面对象，用于与网页交互
- headless=True: 无头模式，不显示浏览器窗口（适合 CI/CD 环境）
"""

from __future__ import annotations


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        print("请先安装并初始化浏览器：")
        print("- python3 -m pip install playwright==1.58.0")
        print("- python3 -m playwright install")
        return

    print("== 最小可运行流程 ==")

    # sync_playwright() 是上下文管理器，会自动处理资源清理
    with sync_playwright() as p:
        # 1. 启动 Chromium 浏览器
        #    headless=True 表示无头模式（不显示浏览器窗口）
        #    对于调试，可以设置为 headless=False
        browser = p.chromium.launch(headless=True)

        # 2. 创建浏览器上下文
        #    BrowserContext 类似于浏览器的隐身模式
        #    每个 context 有独立的 cookie、缓存、localStorage 等
        context = browser.new_context()

        # 3. 创建新页面
        #    Page 是与网页交互的主要对象
        #    一个 context 可以创建多个 page
        page = context.new_page()

        # 4. 设置页面 HTML 内容
        #    set_content() 用于设置页面的 HTML（适合测试）
        #    实际使用中通常用 goto() 导航到 URL
        page.set_content("<h1 id='title'>Hello Playwright 1.58.0</h1>")

        # 5. 定位元素并获取文本
        #    locator() 是推荐的定位方式，返回 Locator 对象
        #    Locator 是惰性的，只在调用方法时才查找元素
        #    inner_text() 获取元素的内部文本
        title_text = page.locator("#title").inner_text()
        print("页面标题元素文本 ->", title_text)

        # 6. 清理资源
        #    注意：使用 with 语句时，这些会自动调用
        #    这里显式调用是为了演示完整流程
        context.close()   # 关闭上下文（释放所有页面）
        browser.close()   # 关闭浏览器


if __name__ == "__main__":
    main()
