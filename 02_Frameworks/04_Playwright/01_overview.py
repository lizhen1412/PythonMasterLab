#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Playwright 1.58.0 学习索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_install_and_version.py", "安装与版本检查"),
    ("03_persistent_context_and_cdp_intro.py", "持久化上下文与 CDP 连接入门"),
    ("04_sync_playwright_start.py", "sync_playwright 启动与最小页面流程"),
    ("05_page_set_content_and_locator.py", "set_content + locator 定位与断言"),
    ("06_forms_and_events.py", "表单输入、点击、事件监听"),
    ("07_wait_for_and_timeouts.py", "等待机制与超时处理"),
    ("08_network_route_mock.py", "route 拦截与 mock 接口"),
    ("09_screenshot_and_trace.py", "截图与 trace 录制"),
    ("10_context_cookies_storage.py", "context、cookie 与 storage_state"),
    ("11_error_handling_and_retries.py", "常见异常处理与重试"),
    ("12_headless_and_launch_args.py", "headless/headed 与启动参数"),
    ("13_chapter_summary.py", "基础总结"),
    ("14_async_api_basics.py", "Async API 入门"),
    ("15_navigation_and_auto_wait.py", "导航与自动等待"),
    ("16_assertions_expect_api.py", "expect 断言 API"),
    ("17_frames_and_iframe.py", "Frame/IFrame 操作"),
    ("18_dialogs_and_popup.py", "对话框与弹窗"),
    ("19_download_and_upload.py", "下载与上传"),
    ("20_video_recording.py", "视频录制"),
    ("21_api_request_context.py", "APIRequestContext"),
    ("22_browser_context_isolation.py", "context 隔离"),
    ("23_emulation_and_devices.py", "设备模拟"),
    ("24_evaluate_and_js_handle.py", "evaluate 与 JSHandle"),
    ("25_console_and_network_events.py", "console/network 事件"),
    ("26_route_continue_abort.py", "route continue/abort/fulfill"),
    ("27_clock_mock_time.py", "clock 时间控制"),
    ("28_cross_browser_matrix.py", "跨浏览器矩阵"),
    ("29_pytest_plugin_basics.py", "pytest 插件入门"),
    ("30_codegen_and_debug_commands.py", "codegen 与调试命令"),
    ("31_todomvc_reference_walkthrough.py", "third_party Todomvc 用例走读"),
    ("32_chapter_summary.py", "全章总结（intro + guides 覆盖）"),
    ("33_writing_tests_official_flow.py", "官网 Writing tests 首个示例完整复刻"),
    ("34_locator_actions_all.py", "locator 常用动作全示例"),
    ("35_expect_assertions_all.py", "expect 常用断言全示例"),
    ("36_waiters_request_response.py", "waiter + request/response 监听"),
    ("37_context_route_and_unroute.py", "context.route / unroute / clear_cookies"),
    ("38_keyboard_mouse_actions.py", "keyboard / mouse 设备操作"),
    ("39_route_fallback_chain.py", "route.fallback 链式处理"),
    ("40_methods_coverage_summary.py", "方法覆盖说明与后续学习建议"),
    ("41_dom_query_legacy_apis.py", "query_selector/eval_on_selector 兼容 API"),
    ("42_advanced_events_and_context.py", "高级事件、context 配置与导航"),
    ("43_advanced_launch_parameters.py", "launch_persistent_context 高级参数大全"),
    ("44_advanced_page_navigation.py", "page.goto 高级参数大全"),
    ("45_advanced_new_context_parameters.py", "new_context 高级参数大全"),
    ("46_advanced_locator_usage.py", "locator 高级用法大全"),
    ("47_real_ecommerce_crawler.py", "真实场景：电商爬虫系统"),
    ("48_real_test_suite.py", "真实场景：Web 自动化测试套件"),
    ("49_real_monitoring.py", "真实场景：网站健康监控系统"),
    ("50_websocket_worker_advanced.py", "高级 API：WebSocket + Worker"),
    ("51_har_cdp_advanced.py", "高级 API：HAR + CDP"),
    ("52_accessibility_other_advanced.py", "高级 API：Accessibility + Coverage + 其他"),
    ("90_method_coverage_check.py", "方法覆盖检查脚本（对照 third_party）"),
    ("99_api_surface_full_catalog.py", "全 API 知识点目录（含稀有高级方法）"),
    ("Exercises/01_overview.py", "练习索引"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
