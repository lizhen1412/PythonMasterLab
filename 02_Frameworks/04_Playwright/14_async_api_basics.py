#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：Async API 入门（async_playwright）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/14_async_api_basics.py

本示例展示 Playwright 的异步 API 使用：
1. async_playwright(): 异步 API 的入口点
2. async/await 语法
3. asyncio.run(): 运行异步主函数

核心概念：
- Playwright 提供同步（sync_api）和异步（async_api）两套 API
- 异步 API 适合需要高并发的场景（同时控制多个浏览器/页面）
- 异步 API 使用 Python 的 async/await 语法
- 需要使用 asyncio.run() 来运行异步主函数

同步 vs 异步 API：
- 同步（sync_api）：简单直观，适合单线程脚本
- 异步（async_api）：高性能，适合并发控制和复杂测试场景
"""

from __future__ import annotations

import asyncio


# 异步主函数
# 使用 async def 定义，可以使用 await 关键字
async def main_async() -> None:
    try:
        from playwright.async_api import async_playwright
    except ImportError as exc:
        print(f"无法导入 playwright async_api: {exc}")
        return

    # async_playwright() 也是异步上下文管理器
    # 使用 async with 进入，会自动处理资源清理
    async with async_playwright() as p:
        # 启动浏览器（直接赋值，不使用 async with）
        browser = await p.chromium.launch(headless=True)
        try:
            # 创建新页面
            page = await browser.new_page()

            # 设置页面内容
            await page.set_content("<h1 id='title'>async demo</h1>")

            # 定位元素并获取文本
            title = await page.locator("#title").inner_text()
            print("title ->", title)
        finally:
            # 显式关闭浏览器
            await browser.close()


# 同步主函数（入口点）
# asyncio.run() 用于运行异步函数
def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
