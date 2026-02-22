#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：Playwright 章节总结。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/13_chapter_summary.py

本示例总结 Playwright 的核心知识点和最佳实践。

本章涵盖的主题：
- 基础启动：sync_playwright、browser、context、page
- 元素定位：locator、get_by_test_id、CSS 选择器
- 页面交互：fill、click、set_content、goto
- 等待机制：wait_for_selector、wait_for_function、timeout
- 网络拦截：route、fulfill、mock API
- 状态管理：cookies、storage_state、持久化上下文
- 调试工具：screenshot、trace、CDP 连接
- 启动配置：headless、args、context 选项
- 错误处理：异常捕获、重试逻辑、expect()

核心概念回顾：
1. 生命周期：sync_playwright -> Browser -> BrowserContext -> Page
2. 定位策略：优先使用 data-testid，其次使用稳定的 CSS 选择器
3. 自动等待：Playwright 会自动等待元素可操作
4. 隔离性：每个 BrowserContext 有独立的 cookies 和 storage
5. 可复现性：使用 trace 和 screenshot 帮助调试问题

最佳实践：
1. 使用上下文管理器确保资源正确清理
2. 使用 ImportError 而非 Exception 捕获导入错误
3. 优先使用 locator() 而非 page.querySelector()
4. 使用 expect() 进行断言，它会自动重试
5. 网络测试使用 mock，避免依赖外部服务
6. CI/CD 环境使用 headless=True
7. 容器环境添加 --no-sandbox 和 --disable-dev-shm-usage

进阶主题（后续章节）：
- 异步 API：async_playwright、async/await
- 多浏览器：Firefox、WebKit 的使用
- 移动端：模拟 iPhone、Android 设备
- API 测试：直接使用 REST API 测试
- 可视化测试：截图对比、像素匹配
"""

from __future__ import annotations


# 章节核心知识点总结
SUMMARY: list[str] = [
    "确认 playwright==1.58.0 并安装浏览器驱动（playwright install）",
    "掌握 sync_playwright -> browser -> context -> page 的生命周期",
    "优先使用 locator，减少脆弱选择器",
    "等待要显式：wait_for_selector / wait_for_function / timeout",
    "网络测试尽量 mock（route.fulfill），避免依赖外网稳定性",
    "调试和排障建议输出 screenshot + trace",
]


def main() -> None:
    """打印章节总结和最佳实践"""
    print("=" * 60)
    print("Playwright 章节总结（v1.58.0）")
    print("=" * 60)

    # 核心知识点
    print("\n核心知识点：")
    for i, line in enumerate(SUMMARY, start=1):
        print(f"  {i}. {line}")

    # 最佳实践
    print("\n最佳实践：")
    practices = [
        "使用 with 语句管理资源（上下文管理器）",
        "异常处理使用 ImportError，避免过度捕获",
        "CI/CD 使用 headless=True，本地调试用 headless=False",
        "容器环境添加 args=['--no-sandbox', '--disable-dev-shm-usage']",
        "使用 data-testid 进行测试定位",
        "使用 expect() 进行断言，自动重试",
        "API 测试使用 mock，不依赖真实后端",
        "失败时保存 screenshot 和 trace 便于调试",
    ]
    for i, practice in enumerate(practices, start=1):
        print(f"  {i}. {practice}")

    # 常见陷阱
    print("\n常见陷阱：")
    pitfalls = [
        "使用脆弱的选择器（如 #div > div > span:nth-child(3)）",
        "使用 time.sleep() 而非显式等待",
        "忘记关闭 browser 或 context 导致资源泄漏",
        "依赖外部网站导致测试不稳定",
        "在测试中使用 hard-coded 的 URL 和数据",
        "不处理 TimeoutError 导致测试意外失败",
    ]
    for i, pitfall in enumerate(pitfalls, start=1):
        print(f"  {i}. {pitfall}")

    print("\n" + "=" * 60)
    print("下一步：学习异步 API (async_playwright)")
    print("=" * 60)


if __name__ == "__main__":
    main()
