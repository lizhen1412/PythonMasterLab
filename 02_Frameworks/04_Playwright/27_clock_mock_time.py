#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 27：Clock 时间控制（v1.45+）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/27_clock_mock_time.py

本示例展示如何使用 Playwright 的 Clock API 控制时间：
1. page.clock.install(): 安装时钟模拟
2. page.clock.fast_forward(): 快进时间
3. page.clock.set_fixed_time(): 设置固定时间

核心概念：
- Clock API 允许控制 JavaScript 的时间相关函数
- 可以加速测试，无需等待真实时间流逝
- 适合测试定时器、过期时间等时间相关功能

Clock API 功能：
- install(): 安装时钟模拟，接管 setTimeout、setInterval、Date 等
- fast_forward(ms): 快进指定毫秒数，触发期间的所有定时器
- set_fixed_time(time): 设置固定时间，时间不再流逝
- run_for(ms): 类似 fast_forward 但时间流逝可被观察

时间相关的 JavaScript API：
- setTimeout / setInterval: 定时器
- Date.now() / new Date(): 当前时间
- performance.now(): 高精度时间戳

使用场景：
- 测试倒计时功能
- 测试过期时间
- 加速包含定时器的测试
- 模拟特定时间点

注意事项：
- Clock API 是 Playwright v1.45+ 的功能
- 安装时钟后，所有 JavaScript 时间操作都会被模拟
- clock 不会影响真实系统时间
"""

from __future__ import annotations


# 模拟包含定时器的页面
# setTimeout 会在 1 秒后更新状态
HTML = """
<p id="status">idle</p>
<script>
  setTimeout(() => {
    document.querySelector('#status').textContent = 'done';
  }, 1000);
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
            page.set_content(HTML)

            # 检查 Clock API 是否可用
            # Clock API 是 Playwright v1.45+ 的功能
            if not hasattr(page, "clock"):
                print("当前 API 不包含 page.clock，跳过")
                return

            # === 安装时钟模拟 ===
            # install() 会接管 JavaScript 的时间相关函数
            # 包括 setTimeout、setInterval、Date 等
            page.clock.install()

            # === 快进时间 ===
            # fast_forward(1000) 快进 1000 毫秒
            # 这会触发所有在这期间应该触发的定时器
            # 无需真实等待 1 秒，测试会立即完成
            page.clock.fast_forward(1000)

            # 验证定时器是否被触发
            print("status ->", page.locator("#status").inner_text())
        finally:
            browser.close()


if __name__ == "__main__":
    main()
