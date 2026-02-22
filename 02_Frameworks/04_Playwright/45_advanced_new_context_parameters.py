#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 45：browser.new_context 高级参数配置大全。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/45_advanced_new_context_parameters.py

本示例展示 browser.new_context 的所有重要参数及其详细说明。

核心概念：
- new_context 创建一个隔离的浏览器上下文
- 每个 context 有独立的 cookie、缓存、localStorage 等
- 相比 launch_persistent_context，new_context 的数据不会持久化到磁盘
"""

from __future__ import annotations

from pathlib import Path


def example_01_basic_context() -> None:
    """示例 01：基本上下文配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # === 最简配置 ===
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://example.com")

        browser.close()


def example_02_context_with_storage() -> None:
    """示例 02：带存储状态的上下文"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    STORAGE_FILE = Path("/tmp/playwright_demo/storage_state.json")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # === 使用存储状态创建上下文 ===
        # storage_state 可以从之前保存的文件加载
        # 这样可以恢复之前登录的 cookies
        if STORAGE_FILE.exists():
            context = browser.new_context(
                storage_state_path=str(STORAGE_FILE),
            )
        else:
            context = browser.new_context()

        page = context.new_page()
        page.goto("https://example.com")

        # 保存当前存储状态（包括 cookies）
        context.storage_state(path=str(STORAGE_FILE))
        print(f"存储状态已保存到: {STORAGE_FILE}")

        # 也可以获取存储状态的 JSON 字符串
        state_json = context.storage_state()
        print(f"存储状态: {len(state_json)} 字节")

        browser.close()


def example_03_context_with_viewport_and_device() -> None:
    """示例 03：设备模拟和视口配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # === 使用预设设备 ===
        # Playwright 内置了常见设备的配置
        # 包括 iPhone、iPad、Android 设备等
        context = browser.new_context(
            # 使用 iPhone 13 配置
            **p.devices["iPhone 13"],
        )

        # iPhone 13 配置包括：
        # - viewport: 390x844
        # - user_agent: iPhone 的 UA
        # - device_scale_factor: 3.0
        # - is_mobile: true
        # - has_touch: true
        # - default_browser_type: 'webkit'

        # === 或手动配置设备参数 ===
        context2 = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Custom User Agent",
            device_scale_factor=1.0,
            is_mobile=False,
            has_touch=False,
        )

        browser.close()


def example_04_context_with_locale_and_timezone() -> None:
    """示例 04：语言和时区配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            # === 语言设置 ===
            # 影响浏览器的语言设置和页面内容
            locale="zh-CN",  # 中文（中国）
            # 其他常见值：
            # - "en-US": 英语（美国）
            # - "ja-JP": 日语（日本）
            # - "de-DE": 德语（德国）
            # - "fr-FR": 法语（法国）

            # === 时区设置 ===
            # IANA 时区数据库标识符
            timezone_id="Asia/Shanghai",  # 中国时区
            # 其他常见值：
            # - "America/New_York": 美国东部时区
            # - "Europe/London": 英国时区
            # - "Asia/Tokyo": 日本时区
            # - "UTC": 协调世界时

            # === 权限配置 ===
            # 预授予的权限列表
            permissions=[
                "geolocation",      # 地理位置
                "notifications",   # 通知
                "clipboard-read",   # 剪贴板读取
                "clipboard-write",  # 剪贴板写入
            ],

            # === 地理位置 ===
            geolocation={
                "latitude": 31.2304,   # 纬度（上海）
                "longitude": 121.4737,  # 经度
                "accuracy": 100,        # 精度（米）
            },
        )

        page = context.new_page()
        # 验证语言设置
        page.goto("https://example.com")
        locale_val = page.evaluate("() => navigator.language")
        print(f"浏览器语言: {locale_val}")
        timezone_val = page.evaluate("() => Intl.DateTimeFormat().resolvedOptions().timeZone")
        print(f"浏览器时区: {timezone_val}")

        browser.close()


def example_05_context_with_color_scheme() -> None:
    """示例 05：颜色方案和无障碍配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # === 浅色模式 ===
        context_light = browser.new_context(
            color_scheme="light",  # 浅色主题
            forced_colors=None,    # 不强制颜色
            reduced_motion="no-preference",  # 不减少动画
        )

        # === 深色模式 ===
        context_dark = browser.new_context(
            color_scheme="dark",   # 深色主题
            forced_colors=None,
            reduced_motion="no-preference",
        )

        # === 高对比度模式 ===
        context_high_contrast = browser.new_context(
            color_scheme="light",
            forced_colors="active",  # 强制高对比度
            contrast="high",          # 高对比度
            reduced_motion="reduce",  # 减少动画
        )

        # === 无障碍配置 ===
        # forced_colors: 'active' | 'none' | null
        #   - 'active': 用户系统设置了高对比度
        #   - 'none': 正常颜色
        #   - null: 自动检测

        # reduced_motion: 'reduce' | 'no-preference' | null
        #   - 'reduce': 减少动画（适合动作敏感用户）
        #   - 'no-preference': 正常动画
        #   - null: 自动检测

        browser.close()


def example_06_context_with_network_config() -> None:
    """示例 06：网络配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            # === 代理配置 ===
            proxy={
                "server": "http://proxy.example.com:8080",
                # 可选的代理认证
                "username": "proxy_user",
                "password": "proxy_pass",
            },

            # === 忽略 HTTPS 错误 ===
            # 对于自签名证书的网站很有用
            ignore_https_errors=True,

            # === 离线模式 ===
            # 模拟网络断开的情况
            offline=False,

            # === HTTP 凭证 ===
            http_credentials={
                "username": "http_user",
                "password": "http_pass",
                # 可选：指定凭证应用的源
                "origin": "https://example.com",
            },

            # === 额外的 HTTP 头 ===
            extra_http_headers={
                "X-Custom-Header": "custom-value",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Authorization": "Bearer token123",
            },
        )

        browser.close()


def example_07_context_with_recording() -> None:
    """示例 07：录制配置（HAR 和视频）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    RECORD_DIR = Path("/tmp/playwright_demo/recordings")
    RECORD_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            # === HAR 录制 ===
            # HAR (HTTP Archive) 格式记录网络请求
            record_har_path=str(RECORD_DIR / "network.har"),
            record_har_content="embed",  # 响应体嵌入 HAR
            record_har_mode="full",      # 完整模式
            record_har_url_filter="**",  # 记录所有请求

            # === 视频录制 ===
            record_video_dir=str(RECORD_DIR / "videos"),
            record_video_size={"width": 1920, "height": 1080},

            # === 追踪 ===
            # 追踪文件保存目录
            traces_dir=str(RECORD_DIR / "traces"),
        )

        page = context.new_page()
        page.goto("https://example.com")

        # 关闭后自动保存 HAR 和视频
        print(f"录制文件已保存到: {RECORD_DIR}")

        browser.close()


def example_08_context_for_crawler() -> None:
    """示例 08：爬虫专用配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    STORAGE_FILE = Path("/tmp/playwright_demo/crawler_storage.json")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            # 启动参数：隐藏自动化特征
            args=[
                "--disable-blink-features=AutomationControlled",
            ],
        )
        # === 爬虫优化的上下文配置 ===
        if STORAGE_FILE.exists():
            context = browser.new_context(
                # 恢复登录状态
                storage_state_path=str(STORAGE_FILE),

                # 视口：常见桌面分辨率
                viewport={"width": 1920, "height": 1080},

                # 用户代理：真实浏览器
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",

                # 语言：中文
                locale="zh-CN",
                timezone_id="Asia/Shanghai",

                # 权限：网站可能需要的权限
                permissions=["geolocation"],

                # 减慢速度：更像人类操作
                # 注意：slow_mo 在 new_context 中不可用，需要在 launch 中设置
            )
        else:
            context = browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                locale="zh-CN",
                timezone_id="Asia/Shanghai",
            )

        page = context.new_page()

        # 添加初始化脚本：进一步隐藏自动化特征
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });
        """)

        page.goto("https://example.com")

        # 保存登录状态
        context.storage_state(path=str(STORAGE_FILE))

        browser.close()


def example_09_context_with_service_workers() -> None:
    """示例 09：Service Worker 配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # === Service Worker 策略 ===
        # 'allow': 允许 Service Worker（默认）
        # 'block': 阻止 Service Worker 注册
        context = browser.new_context(
            service_workers="allow",
        )

        # 注意：Service Worker 只在非持久化上下文中生效
        # launch_persistent_context 不支持此参数

        browser.close()


def example_10_context_with_client_certificates() -> None:
    """示例 10：客户端证书配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # === 客户端证书认证 ===
        # 注意：此示例需要实际的服务器和证书
        # 这里仅展示配置方法
        print("[skip] 客户端证书配置需要实际的服务器和证书文件")

        browser.close()


def example_11_context_with_ignore_https_errors() -> None:
    """示例 11：忽略 HTTPS 错误的配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # === 忽略 HTTPS 错误 ===
        # 对于使用自签名证书的网站很有用
        # 注意：这会降低安全性，请确保在受信任的环境中使用
        context = browser.new_context(
            ignore_https_errors=True,
        )

        page = context.new_page()
        # 访问自签名证书的网站不会报错
        page.goto("https://example.com")
        print("成功访问网站（HTTPS 错误已忽略）")

        browser.close()


def main() -> None:
    """主函数：运行所有示例"""
    examples = [
        ("基本上下文", example_01_basic_context),
        ("存储状态", example_02_context_with_storage),
        ("设备模拟", example_03_context_with_viewport_and_device),
        ("语言时区", example_04_context_with_locale_and_timezone),
        ("颜色方案", example_05_context_with_color_scheme),
        ("网络配置", example_06_context_with_network_config),
        ("录制配置", example_07_context_with_recording),
        ("爬虫专用", example_08_context_for_crawler),
        ("Service Worker", example_09_context_with_service_workers),
        ("客户端证书", example_10_context_with_client_certificates),
        ("忽略 HTTPS 错误", example_11_context_with_ignore_https_errors),
    ]

    print("== Playwright new_context 高级参数配置示例 ==\n")

    for name, func in examples:
        try:
            print(f"\n--- {name} ---")
            func()
        except Exception as exc:
            print(f"[skip] {name}: {exc}")

    print("\n== 所有示例执行完毕 ==")


if __name__ == "__main__":
    main()
