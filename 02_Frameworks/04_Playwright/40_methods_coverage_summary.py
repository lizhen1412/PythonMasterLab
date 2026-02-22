#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 40：方法覆盖说明（给学习者看的结论页）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/40_methods_coverage_summary.py

本示例总结已覆盖的 Playwright 方法和知识点：
1. 官网入门高频方法
2. 进阶知识点覆盖

已覆盖的方法类别：
- 页面导航和元素定位
- 交互操作（click、fill、check 等）
- 断言验证（expect API）
- 等待机制（wait_for_*）
- 网络拦截（route）
- Cookie 和存储管理
- 键盘鼠标操作

进阶内容：
- 高级事件处理
- Context 高级用法
- HAR/CDP/WebSocket
- Tracing 和调试

自动检查：
- 90_method_coverage_check.py: 自动对照查漏
- 99_api_surface_full_catalog.py: 完整 API 目录
"""

from __future__ import annotations


SECTIONS: list[tuple[str, list[str]]] = [
    (
        "已覆盖（官网入门高频）",
        [
            "page.goto / get_by_role / locator / frame_locator",
            "兼容 API: query_selector / eval_on_selector（读老代码）",
            "locator.fill / click / check / uncheck / hover / focus / press / set_input_files / select_option",
            "expect: to_have_title / to_have_url / to_be_visible / to_be_checked / to_be_enabled",
            "expect: to_contain_text / to_have_attribute / to_have_count / to_have_text / to_have_value",
            "page.expect_request / page.expect_response / wait_for_url / wait_for_function",
            "route.fulfill / continue_ / abort / fallback",
            "context.route / unroute / clear_cookies / storage_state",
            "keyboard.type/press/down/up/insert_text + mouse.move/click/dblclick/wheel",
        ],
    ),
    (
        "进阶知识点覆盖（高级 + 目录）",
        [
            "41_advanced_events_and_context.py：高级事件 / context / 导航 / 页面状态",
            "99_api_surface_full_catalog.py：HAR / CDP / WebSocket / tracing chunk / persistent context 等方法入口",
            "90_method_coverage_check.py：用于和 third_party_refs 自动对照查漏",
        ],
    ),
]


def main() -> None:
    print("== Playwright 方法覆盖说明 ==\n")
    for title, lines in SECTIONS:
        print(title + ":")
        for line in lines:
            print("- " + line)
        print()

    print("自动检查命令：")
    print("python3 02_Frameworks/04_Playwright/90_method_coverage_check.py")


if __name__ == "__main__":
    main()
