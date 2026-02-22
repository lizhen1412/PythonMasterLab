#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 43：launch_persistent_context 高级参数配置大全。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/43_advanced_launch_parameters.py

本示例展示 launch_persistent_context 的所有重要参数及其详细说明。
对于生产环境的爬虫或自动化项目，正确的参数配置非常重要。

核心概念：
- launch_persistent_context 会创建一个持久化的浏览器上下文
- 所有数据（cookies、localStorage、缓存等）会保存在 user_data_dir
- 相比普通的 new_context，持久化上下文更适合需要保持登录状态的场景
"""

from __future__ import annotations

from pathlib import Path


def example_01_basic_persistent_context() -> None:
    """示例 01：最基本的持久化上下文配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    USER_DATA_DIR = Path("/tmp/playwright_demo/profile_01")

    with sync_playwright() as p:
        # 最简配置：只需要指定 user_data_dir
        # launch_persistent_context 返回 BrowserContext，无需额外包装
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,
        )

        page = context.new_page()
        page.goto("https://example.com")

        # 下次启动时，cookies 和其他数据会保留
        context.close()


def example_02_with_viewport_and_device() -> None:
    """示例 02：配置视口大小和设备模拟"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    USER_DATA_DIR = Path("/tmp/playwright_demo/profile_02")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,

            # === 视口和显示配置 ===
            # 视口大小（浏览器窗口大小）
            viewport={"width": 1920, "height": 1080},  # 默认: 1280x720

            # 屏幕大小（用于计算 window.screen）
            screen={"width": 1920, "height": 1080},

            # 设备像素比（DPI），默认为 1.0
            # 2.0 表示视网膜屏幕
            device_scale_factor=1.0,

            # 是否模拟移动设备
            is_mobile=False,  # 默认: False

            # 是否支持触摸
            has_touch=False,  # 默认: False

            # 颜色方案：'light' | 'dark' | 'no-preference'
            color_scheme="light",  # 默认: 'light'

            # 减少动画：'reduce' | 'no-preference'
            reduced_motion="no-preference",

            # 强制颜色：'active' | 'none' | null
            forced_colors=None,
        )

        page = context.new_page()
        print("视口配置示例完成")
        context.close()


def example_03_network_and_performance() -> None:
    """示例 03：网络和性能相关配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    USER_DATA_DIR = Path("/tmp/playwright_demo/profile_03")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,

            # === 网络配置 ===
            # 代理设置
            proxy={
                "server": "http://myproxy.com:8080",  # 代理服务器地址
                "username": "user",  # 代理用户名（可选）
                "password": "pass",  # 代理密码（可选）
            },

            # 忽略 HTTPS 错误（如自签名证书）
            ignore_https_errors=True,  # 默认: False

            # 离线模式
            offline=False,  # 默认: False

            # HTTP 凭证
            http_credentials={
                "username": "user",
                "password": "password",
                "origin": "https://example.com",  # 可选
            },

            # 额外的 HTTP 头（所有请求都会带上）
            extra_http_headers={
                "X-Custom-Header": "value",
                "Authorization": "Bearer token123",
            },

            # === 性能配置 ===
            # 减慢操作速度（毫秒），用于调试
            slow_mo=100,  # 每个操作延迟 100ms，默认: 0

            # 启动超时时间（毫秒）
            timeout=30000,  # 默认: 30000 (30秒)
        )

        print("网络和性能配置示例完成")
        context.close()


def example_04_user_agent_and_locale() -> None:
    """示例 04：用户代理和语言设置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    USER_DATA_DIR = Path("/tmp/playwright_demo/profile_04")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,

            # === 用户代理和语言 ===
            # 自定义用户代理字符串
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",

            # 语言设置（如 zh-CN, en-US, ja-JP）
            locale="zh-CN",  # 默认: 'en-US'

            # 时区 ID（IANA 时区数据库）
            timezone_id="Asia/Shanghai",  # 默认: 浏览器默认时区

            # 地理位置
            geolocation={
                "latitude": 31.2304,  # 纬度（上海）
                "longitude": 121.4737,  # 经度
                "accuracy": 100,  # 精度（米，可选）
            },

            # 权限列表
            permissions=["geolocation", "notifications"],
        )

        print("用户代理和语言配置示例完成")
        context.close()


def example_05_security_and_content() -> None:
    """示例 05：安全和内容相关配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    USER_DATA_DIR = Path("/tmp/playwright_demo/profile_05")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,

            # === 安全和内容配置 ===
            # 是否启用 JavaScript
            java_script_enabled=True,  # 默认: True

            # 绕过内容安全策略（CSP）
            # 注意：这会降低安全性，但某些网站可能需要
            bypass_csp=False,  # 默认: False

            # 是否自动接受下载
            accept_downloads=True,  # 默认: True

            # 严格选择器模式（要求选择器更严格）
            strict_selectors=False,  # 默认: False

            # Service Worker 策略：'allow' | 'block'
            service_workers="allow",  # 默认: 'allow'

            # 基础 URL（用于相对路径解析）
            base_url="https://example.com",
        )

        print("安全和内容配置示例完成")
        context.close()


def example_06_recording_and_tracing() -> None:
    """示例 06：录制和追踪配置"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    USER_DATA_DIR = Path("/tmp/playwright_demo/profile_06")
    RECORD_DIR = Path("/tmp/playwright_demo/recordings")

    # 创建录制目录
    RECORD_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,

            # === HAR 录制 ===
            # HAR 文件保存路径
            record_har_path=str(RECORD_DIR / "test.har"),

            # HAR 内容策略：'omit' | 'embed' | 'attach'
            # - omit: 不记录响应体
            # - embed: 响应体嵌入 HAR 文件
            # - attach: 响应体单独保存
            record_har_content="embed",

            # HAR URL 过滤（只记录匹配的请求）
            record_har_url_filter="**/api/**",  # glob 模式或正则表达式

            # HAR 模式：'full' | 'minimal'
            record_har_mode="full",

            # === 视频录制 ===
            # 视频保存目录
            record_video_dir=str(RECORD_DIR / "videos"),

            # 视频分辨率
            record_video_size={"width": 1920, "height": 1080},

            # === 追踪 ===
            # 追踪文件保存目录
            traces_dir=str(RECORD_DIR / "traces"),
        )

        page = context.new_page()
        page.goto("https://example.com")

        # 关闭上下文会自动保存 HAR 和视频
        context.close()

        print(f"HAR 和视频已保存到: {RECORD_DIR}")


def example_07_browser_channel_and_args() -> None:
    """示例 07：浏览器通道和启动参数"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    USER_DATA_DIR = Path("/tmp/playwright_demo/profile_07")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,

            # === 浏览器通道 ===
            # 使用系统安装的浏览器：'chrome' | 'msedge' | 'chrome-beta' 等
            channel="chrome",  # 默认: None（使用打包的 Chromium）

            # 浏览器可执行文件路径
            # executable_path="/path/to/chrome",

            # === 命令行参数 ===
            # 传递给浏览器的额外参数
            args=[
                "--disable-blink-features=AutomationControlled",  # 隐藏自动化特征
                "--no-sandbox",  # 禁用沙箱（Docker 环境可能需要）
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",  # 解决共享内存问题
                "--disable-gpu",  # 禁用 GPU
            ],

            # 忽略默认参数
            # True: 忽略所有默认参数
            # List: 忽略指定的默认参数
            ignore_default_args=["--enable-automation"],

            # === 信号处理 ===
            # 是否处理 SIGINT 信号（Ctrl+C）
            handle_sigint=True,  # 默认: True

            # 是否处理 SIGTERM 信号
            handle_sigterm=True,  # 默认: True

            # 是否处理 SIGHUP 信号
            handle_sighup=True,  # 默认: True

            # === 环境变量 ===
            # 设置浏览器进程的环境变量
            env={
                "DISPLAY": ":99",  # Linux 虚拟显示
                "LANG": "zh_CN.UTF-8",
            },

            # === Chromium 特定 ===
            # 是否使用沙箱（Linux 上建议启用）
            chromium_sandbox=True,  # 默认: True

            # === Firefox 特定 ===
            # Firefox 用户偏好设置
            # firefox_user_prefs={
            #     "dom.ipc.processCount": 8,
            #     "network.proxy.type": 0,
            # },
        )

        print("浏览器通道和启动参数配置示例完成")
        context.close()


def example_08_anti_detection_config() -> None:
    """示例 08：反检测配置（爬虫常用）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    USER_DATA_DIR = Path("/tmp/playwright_demo/profile_08")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=True,  # 某些网站可能需要 headless=False

            # === 反检测配置 ===
            # 使用真实的浏览器（更容易通过检测）
            channel="chrome",

            # 隐藏自动化特征
            args=[
                "--disable-blink-features=AutomationControlled",
            ],

            # 设置真实的用户代理
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",

            # 设置视口为常见大小
            viewport={"width": 1920, "height": 1080},

            # 设置语言和时区
            locale="zh-CN",
            timezone_id="Asia/Shanghai",

            # 减慢操作速度（更像人类）
            slow_mo=50,  # 每个操作延迟 50ms

            # 权限（某些网站会检查）
            permissions=["geolocation"],

            # 启用 JavaScript（大部分网站需要）
            java_script_enabled=True,
        )

        # 在页面中执行脚本进一步隐藏自动化特征
        page = context.new_page()
        page.add_init_script("""
            // 隐藏 webdriver 属性
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });

            // 伪装 plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5],
            });

            // 伪装 languages
            Object.defineProperty(navigator, 'languages', {
                get: () => ['zh-CN', 'zh', 'en-US', 'en'],
            });
        """)

        page.goto("https://example.com")
        print("反检测配置示例完成")
        context.close()


def main() -> None:
    """主函数：运行所有示例"""
    examples = [
        ("基本持久化上下文", example_01_basic_persistent_context),
        ("视口和设备模拟", example_02_with_viewport_and_device),
        ("网络和性能配置", example_03_network_and_performance),
        ("用户代理和语言", example_04_user_agent_and_locale),
        ("安全和内容配置", example_05_security_and_content),
        ("录制和追踪配置", example_06_recording_and_tracing),
        ("浏览器通道和启动参数", example_07_browser_channel_and_args),
        ("反检测配置", example_08_anti_detection_config),
    ]

    print("== Playwright 高级参数配置示例 ==\n")

    for name, func in examples:
        try:
            print(f"\n--- {name} ---")
            func()
        except Exception as exc:
            print(f"[skip] {name}: {exc}")

    print("\n== 所有示例执行完毕 ==")


if __name__ == "__main__":
    main()
