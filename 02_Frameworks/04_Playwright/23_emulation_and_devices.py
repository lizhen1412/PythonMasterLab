#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 23：设备模拟（Devices Emulation）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/23_emulation_and_devices.py

本示例展示如何模拟移动设备和不同浏览器：
1. p.devices: 预定义的设备配置
2. new_context(**device): 应用设备配置
3. User-Agent 和 viewport 模拟

核心概念：
- Playwright 可以模拟各种移动设备（iPhone、iPad、Android 等）
- 设备配置包括 viewport、User-Agent、触摸支持等
- 使用 webkit 浏览器可以更好地模拟 iOS 设备
- 设备模拟适合移动端网页测试

设备配置包含：
- viewport: 窗口大小（宽 x 高）
- userAgent: 浏览器用户代理字符串
- deviceScaleFactor: 设备像素比
- isMobile: 是否为移动设备
- hasTouch: 是否支持触摸

预定义设备：
- p.devices["iPhone 13"]
- p.devices["iPad Pro"]
- p.devices["Pixel 5"]
- 更多设备见 Playwright 文档

自定义设备模拟：
- 可以手动配置 viewport、userAgent 等参数
- 适合测试自定义设备配置

常见用途：
- 移动端网页测试
- 响应式设计验证
- 跨设备兼容性测试
- 移动端专用功能测试（如触摸事件）
"""

from __future__ import annotations


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        # === 获取预定义设备配置 ===
        # p.devices 包含多种移动设备的预定义配置
        # iPhone 13 配置包含 viewport、User-Agent、触摸支持等
        iphone = p.devices["iPhone 13"]

        # 使用 webkit 浏览器可以更好地模拟 iOS 设备
        browser = p.webkit.launch(headless=True)
        context = None
        try:
            # === 创建模拟设备的 Context ===
            # **iphone 展开设备配置，包括：
            # - viewport: 屏幕尺寸
            # - userAgent: iOS Safari 的 UA
            # - deviceScaleFactor: 设备像素比
            # - isMobile: 标记为移动设备
            # - hasTouch: 支持触摸事件
            context = browser.new_context(**iphone)
            page = context.new_page()
            page.set_content("<h1>device emulation</h1>")

            # 验证设备模拟是否生效
            ua = page.evaluate("() => navigator.userAgent")
            print("viewport ->", iphone.get("viewport"))
            print("userAgent has iPhone ->", "iPhone" in ua)

            context.close()
            context = None  # 标记已关闭
        finally:
            if context:
                context.close()
            browser.close()


if __name__ == "__main__":
    main()
