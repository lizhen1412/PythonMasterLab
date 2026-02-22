#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：截图与 trace 录制。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/09_screenshot_and_trace.py

本示例展示 Playwright 的调试和记录功能：
1. screenshot(): 截取页面截图
2. tracing.start(): 开始 trace 录制
3. tracing.stop(): 停止录制并保存 trace 文件

核心概念：
- screenshot() 可以保存页面当前状态的截图
- full_page=True 表示截取整个页面（包括需要滚动的内容）
- tracing 会记录所有操作，可以在 Playwright Inspector 中回放
- trace 文件包含：网络请求、控制台日志、页面快照等
- 使用 npx playwright show trace.zip 查看 trace 文件

常见用途：
- 调试：保存页面状态用于分析问题
- 测试记录：保存截图和 trace 作为测试证据
- 回放问题：通过 trace 文件重现问题场景
"""

from __future__ import annotations

from pathlib import Path


# 输出目录
# 截图和 trace 文件将保存在这个目录下
OUT_DIR = Path("/tmp/playwright_demo")


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 确保输出目录存在
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 定义输出文件路径
    screenshot_path = OUT_DIR / "demo.png"
    trace_path = OUT_DIR / "trace.zip"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = None
        try:
            context = browser.new_context()

            # === 开始 trace 录制 ===
            # screenshots=True: 自动保存截图
            # snapshots=True: 保存页面快照
            context.tracing.start(screenshots=True, snapshots=True)

            page = context.new_page()

            # 设置页面内容
            page.set_content("<h1 style='color:teal'>Playwright Screenshot Demo</h1>")

            # === 截取页面截图 ===
            # full_page=True: 截取整个页面（包括需要滚动的内容）
            page.screenshot(path=str(screenshot_path), full_page=True)

            # === 停止 trace 录制并保存 ===
            context.tracing.stop(path=str(trace_path))

            context.close()
            context = None  # 标记已关闭
        finally:
            if context:
                context.close()
            browser.close()

    # 输出文件路径
    print("screenshot ->", screenshot_path)
    print("trace ->", trace_path)
    print("\n提示: 使用 npx playwright show", trace_path, "查看 trace")


if __name__ == "__main__":
    main()
