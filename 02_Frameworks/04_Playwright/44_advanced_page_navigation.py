#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 44：page.goto 高级参数配置大全。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/44_advanced_page_navigation.py

本示例展示 page.goto 的所有重要参数及其详细说明。
"""

from __future__ import annotations

from urllib.parse import quote


def example_01_basic_navigation() -> None:
    """示例 01：基本导航配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # === 基本导航 ===
        # 最简单的用法：只提供 URL
        page.goto("https://example.com")

        # 使用 wait_until 控制等待条件
        page.goto(
            "https://example.com",
            wait_until="load",  # 等待 'load' 事件
        )

        # 等待条件选项：
        # - 'load': 等待 load 事件触发（默认）
        # - 'domcontentloaded': 等待 DOMContentLoaded 事件触发
        # - 'networkidle': 等待网络空闲（至少 500ms 无网络活动）
        # - 'commit': 等待导航提交到服务器

        browser.close()


def example_02_navigation_with_timeout() -> None:
    """示例 02：带超时的导航"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # === 导航超时配置 ===
        # 设置单次导航的超时时间（毫秒）
        page.goto(
            "https://example.com",
            timeout=60000,  # 60 秒超时，默认 30000 (30秒)
        )

        # 也可以设置页面的默认导航超时
        page.set_default_navigation_timeout(60000)

        # 或在 context 级别设置
        context.set_default_navigation_timeout(60000)

        browser.close()


def example_03_referer_and_headers() -> None:
    """示例 03：带 Referer 和请求头的导航"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # === 导航时的额外 HTTP 头 ===
        page.goto(
            "https://example.com",
            # 导航时发送的请求头
            headers={
                "X-Custom-Header": "custom-value",
                "Accept-Language": "zh-CN,zh;q=0.9",
            },
        )

        # 注意：Referer 头建议使用 set_extra_http_headers 设置
        context.set_extra_http_headers({"Referer": "https://google.com"})

        browser.close()


def example_04_wait_strategies() -> None:
    """示例 04：不同的等待策略"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # === wait_until 详解 ===

        # 1. 'load' - 等待 load 事件
        # 页面及其所有依赖资源（如图片、样式表）已加载完成
        page.goto("https://example.com", wait_until="load")

        # 2. 'domcontentloaded' - 等待 DOM 解析完成
        # DOM 已完全构建和解析，但图片和样式表可能还在加载
        # 这是最快的选项，适合不需要图片的场景
        page.goto("https://example.com", wait_until="domcontentloaded")

        # 3. 'networkidle' - 等待网络空闲
        # 至少 500ms 内没有超过 2 个网络连接
        # 适合等待 AJAX 请求完成的场景
        page.goto("https://example.com", wait_until="networkidle")

        # 4. 'commit' - 等待导航提交
        # 只要文档已从服务器接收并开始解析
        # 这是最快的选项，但页面可能还在加载
        page.goto("https://example.com", wait_until="commit")

        browser.close()


def example_05_navigation_error_handling() -> None:
    """示例 05：导航错误处理"""
    try:
        from playwright.sync_api import Error, sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # === 错误处理 ===
        try:
            # 访问不存在的页面
            page.goto("https://this-domain-does-not-exist-12345.com")
        except Error as exc:
            # 捕获导航错误
            print(f"导航失败: {exc}")

        # === 处理特定状态码 ===
        try:
            response = page.goto("https://example.com/404-page")
            if response:
                print(f"状态码: {response.status}")
                if response.status >= 400:
                    print("页面返回错误状态码")
                else:
                    print("页面加载成功")
        except Error as exc:
            print(f"导航异常: {exc}")

        browser.close()


def example_06_url_variations() -> None:
    """示例 06：不同格式的 URL"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    import tempfile

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 设置 baseURL（后续相对路径会基于此）
        context = browser.new_context(base_url="https://example.com")
        page = context.new_page()

        # === 不同格式的 URL ===

        # 1. 完整 URL
        page.goto("https://example.com")

        # 2. 相对路径（需要设置 baseURL）
        page.goto("/")

        # 3. data URL（直接加载内容）
        html_content = "<h1>Data URL Example</h1>"
        page.goto(f"data:text/html,{quote(html_content)}")

        # 4. file URL（本地文件）- 使用临时文件
        with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as f:
            f.write("<h1>Local File Example</h1><p>This is from a local file.</p>")
            temp_file_path = f.name
        page.goto(f"file://{temp_file_path}")
        print(f"本地文件内容: {page.inner_text('h1')}")
        import os
        os.unlink(temp_file_path)

        browser.close()


def example_07_navigation_with_retry() -> None:
    """示例 07：带重试机制的导航"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    import time

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # === 重试机制 ===
        max_retries = 3
        url = "https://example.com"

        for attempt in range(max_retries):
            try:
                page.goto(url, timeout=10000)
                print(f"导航成功（尝试 {attempt + 1}/{max_retries}）")
                break
            except Exception as exc:
                print(f"导航失败（尝试 {attempt + 1}/{max_retries}）: {exc}")
                if attempt < max_retries - 1:
                    # 等待后重试
                    time.sleep(2)
                else:
                    raise

        browser.close()


def example_08_persistent_navigation() -> None:
    """示例 08：保持会话的导航"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    from pathlib import Path

    USER_DATA_DIR = Path("/tmp/playwright_demo/nav_profile")

    with sync_playwright() as p:
        # 使用持久化上下文
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,
        )

        page = context.new_page()

        # 第一次访问：可能需要登录
        page.goto("https://example.com")
        # ... 登录操作 ...

        # 导航到其他页面（会保持登录状态）
        page.goto("https://example.com")
        print("已保持登录状态访问")

        # 下次启动时，仍然保持登录状态
        context.close()


def main() -> None:
    """主函数：运行所有示例"""
    examples = [
        ("基本导航配置", example_01_basic_navigation),
        ("带超时的导航", example_02_navigation_with_timeout),
        ("Referer 和请求头", example_03_referer_and_headers),
        ("等待策略", example_04_wait_strategies),
        ("错误处理", example_05_navigation_error_handling),
        ("URL 格式变体", example_06_url_variations),
        ("重试机制", example_07_navigation_with_retry),
        ("持久化导航", example_08_persistent_navigation),
    ]

    print("== Playwright page.goto 高级参数配置示例 ==\n")

    for name, func in examples:
        try:
            print(f"\n--- {name} ---")
            func()
        except Exception as exc:
            print(f"[skip] {name}: {exc}")

    print("\n== 所有示例执行完毕 ==")


if __name__ == "__main__":
    main()
