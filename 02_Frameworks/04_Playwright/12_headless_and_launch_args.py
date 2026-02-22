#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：headless/headed 与启动参数。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/12_headless_and_launch_args.py

本示例展示 Playwright 浏览器启动的配置选项：
1. headless：无头模式 vs 有头模式
2. args：传递给浏览器的命令行参数
3. 其他常用启动选项

核心概念：
- headless=True：无头模式，不显示浏览器窗口（适合 CI/CD）
- headless=False：有头模式，显示浏览器窗口（适合调试）
- args：传递 Chrome/Chromium 命令行参数
- 常用参数：--disable-dev-shm-usage、--no-sandbox、--disable-gpu 等

headless vs headed：
- headless：更快、更省资源、适合服务器环境
- headed：可以看到浏览器操作、适合本地调试

常用启动参数：
- --disable-dev-shm-usage：解决 /dev/shm 空间不足问题
- --no-sandbox：在某些容器环境中需要
- --disable-gpu：禁用 GPU 加速
- --window-size=1920,1080：设置窗口大小
- --user-agent：自定义 User-Agent

常见用途：
- CI/CD：使用 headless=True
- 本地调试：使用 headless=False
- 容器环境：添加 --no-sandbox、--disable-dev-shm-usage
- 性能优化：添加 --disable-gpu、--disable-software-rasterizer
"""

from __future__ import annotations


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        # headless=True：无头模式（适合 CI/CD 环境）
        # args：传递给浏览器的命令行参数
        #   --disable-dev-shm-usage：避免 /dev/shm 空间不足导致崩溃
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-dev-shm-usage"],
        )
        try:
            page = browser.new_page()

            # 设置页面内容并验证
            page.set_content("<div id='mode'>headless demo</div>")
            mode_text = page.locator("#mode").inner_text()
            print("mode text ->", mode_text)
        finally:
            browser.close()

        # === 其他常用启动参数示例 ===
        # 如果需要使用，可以取消注释：
        #
        # browser = p.chromium.launch(
        #     headless=False,  # 有头模式，可以看到浏览器窗口
        #     args=[
        #         "--disable-dev-shm-usage",  # 避免 /dev/shm 问题
        #         "--no-sandbox",              # 容器环境可能需要
        #         "--disable-gpu",              # 禁用 GPU
        #         "--window-size=1920,1080",   # 设置窗口大小
        #     ],
        # )
        # page = browser.new_page()
        # ...
        # browser.close()

    # === 调试提示 ===
    print("\n提示:")
    print("  - headless=True 适合 CI/CD 环境（当前设置）")
    print("  - headless=False 适合本地调试，可以看到浏览器操作")
    print("  - 常用参数：--disable-dev-shm-usage、--no-sandbox")
    print("  - 容器环境建议：headless=True + args=['--no-sandbox']")


if __name__ == "__main__":
    main()
