#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：Playwright 1.58.0。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3.11 02_Frameworks/04_Playwright/Exercises/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_open_data_url_title.py", "打开 data URL 并读取标题文本"),
    ("03_fill_form_and_assert.py", "填写表单并断言输出"),
    ("04_route_mock_json.py", "拦截请求并 mock JSON 返回"),
    ("05_save_screenshot.py", "保存截图到 /tmp"),
    ("06_wait_for_ready_flag.py", "等待按钮可点击"),
    ("07_context_cookie_isolation.py", "context cookie 隔离"),
    ("08_expect_to_have_text.py", "expect 文本断言"),
    ("09_async_open_page.py", "Async API 打开页面"),
    ("10_frame_locator_read.py", "frame_locator 读取 iframe"),
    ("11_download_file.py", "下载文件保存到 /tmp"),
    ("12_cross_browser_smoke.py", "跨浏览器 smoke"),
    ("13_get_by_role_and_url.py", "get_by_role + to_have_url"),
    ("14_locator_actions_basic.py", "locator 常见动作"),
    ("15_expect_assertions_basic.py", "expect 常见断言"),
    ("16_request_response_waiters.py", "expect_request / expect_response"),
    ("17_keyboard_mouse_basic.py", "keyboard / mouse 操作"),
    ("18_route_fallback_basic.py", "route.fallback"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
