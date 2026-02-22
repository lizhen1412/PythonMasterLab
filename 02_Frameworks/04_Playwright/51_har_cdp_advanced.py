#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 51：HAR 和 CDP 高级用法（完整 API 覆盖）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/51_har_cdp_advanced.py

本示例演示 Playwright 的 HAR（HTTP Archive）和 CDP（Chrome DevTools Protocol）API：

## HAR 相关
1. HAR 录制：record_har_path, record_har_content, record_har_mode
2. HAR 回放：route_from_har
3. HAR 内容模式：omit, embed, attach
4. HAR ZIP 格式支持
5. HAR 更新模式

## CDP 相关
1. CDP Session 创建：context.new_cdp_session
2. CDP 命令发送：send(method, params)
3. CDP 事件监听：on(event, handler)
4. CDP 连接：connect_over_cdp
5. CDP 调试端口配置

## 其他高级功能
1. Client Certificates（客户端证书）
2. Network 域（Network Domain）
3. Fetch 继续阶段控制

## 涉及的 Playwright API
- record_har_path: HAR 录制路径
- record_har_content: HAR 内容模式
- record_har_mode: HAR 录制模式
- route_from_har: 从 HAR 回放请求
- context.new_cdp_session: 创建 CDP 会话
- cdpsession.send: 发送 CDP 命令
- browser_type.connect_over_cdp: 通过 CDP 连接
- client_certificates: 客户端证书配置
"""

from __future__ import annotations

import json
import zipfile
from dataclasses import dataclass, field
from dataclasses import dataclass as dc_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


# =============================================================================
# HAR 录制和回放示例
# =============================================================================

# 统一使用 /tmp/playwright_demo 目录
HAR_DEMO_DIR = Path("/tmp/playwright_demo/har")


def example_01_har_record_basic() -> None:
    """示例 01：HAR 录制基础（完整录制网络请求）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    har_output_path = HAR_DEMO_DIR / "basic.har"
    har_output_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        # === 创建启用 HAR 录制的上下文 ===
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            # HAR 录制路径
            record_har_path=str(har_output_path),

            # HAR 内容模式：
            # - "omit": 不记录响应体
            # - "embed": 将响应体嵌入 HAR（默认）
            # - "attach": 响应体保存为单独文件
            record_har_content="embed",

            # HAR 录制模式：
            # - "full": 完整模式，记录所有请求
            # - "minimal": 最小模式，只记录必要信息
            record_har_mode="full",

            # URL 过滤器（glob 模式）
            # 只记录匹配的 URL
            record_har_url_filter="**/*",
        )

        page = context.new_page()

        # 访问一些页面，生成网络请求
        page.goto("https://example.com")

        # 加载一些资源
        page.evaluate("""
            // 触发额外的网络请求
            fetch('https://example.com/api/test').then(r => r.text());
        """)

        # 等待所有请求完成
        page.wait_for_load_state("networkidle")

        browser.close()

    print(f"HAR 文件已保存: {har_output_path}")
    print(f"文件大小: {har_output_path.stat().st_size} 字节")


def example_02_har_record_options() -> None:
    """示例 02：HAR 录制各种选项"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    har_path = HAR_DEMO_DIR / "options.har"
    har_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # === 选项 1: omit 模式（不记录响应体）===
        context1 = browser.new_context(
            record_har_path=str(har_path).replace(".har", "_omit.har"),
            record_har_content="omit",  # 不记录响应体，文件更小
        )
        page1 = context1.new_page()
        page1.goto("https://example.com")
        page1.wait_for_load_state("networkidle")

        # === 选项 2: attach 模式（响应体单独存储）===
        # 响应体存储在单独文件中，HAR 中引用文件路径
        context2 = browser.new_context(
            record_har_path=str(har_path).replace(".har", "_attach.zip"),
            record_har_content="attach",
        )
        page2 = context2.new_page()
        page2.goto("https://example.com")
        page2.wait_for_load_state("networkidle")

        # === 选项 3: minimal 模式（最小录制）===
        context3 = browser.new_context(
            record_har_path=str(har_path).replace(".har", "_minimal.har"),
            record_har_mode="minimal",  # 只记录基本信息
        )
        page3 = context3.new_page()
        page3.goto("https://example.com")
        page3.wait_for_load_state("networkidle")

        # === 选项 4: URL 过滤 ===
        # 只记录特定 URL 模式的请求
        context4 = browser.new_context(
            record_har_path=str(har_path).replace(".har", "_filtered.har"),
            record_har_url_filter="**/*.css",  # 只记录 CSS 文件
        )
        page4 = context4.new_page()
        page4.goto("https://example.com")
        page4.wait_for_load_state("networkidle")

        browser.close()

    print("各种 HAR 录制选项测试完成")

    # 比较文件大小
    base_path = har_path.parent
    for f in base_path.glob("*.har"):
        print(f"  {f.name}: {f.stat().st_size} 字节")


def example_03_har_replay_basic() -> None:
    """示例 03：HAR 回放基础（从 HAR 文件回放请求）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 首先创建一个 HAR 文件
    har_path = HAR_DEMO_DIR / "replay_source.har"
    har_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        # 步骤 1：录制 HAR
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_har_path=str(har_path),
            record_har_content="embed",
        )
        page = context.new_page()
        page.goto("https://example.com")
        page.wait_for_load_state("networkidle")
        browser.close()

    # 步骤 2：从 HAR 回放
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # === 使用 route_from_har 从 HAR 回放 ===
        page = context.new_page()

        # 从 HAR 文件设置路由
        page.route_from_har(
            har=str(har_path),
            # not_found: 当 URL 不在 HAR 中时的行为
            # - "abort": 中止请求
            # - "fallback": 继续正常请求（默认）
            not_found="fallback",
        )

        # 现在访问 example.com 会从 HAR 中读取响应
        # 而不是实际访问网络
        page.goto("https://example.com")

        content = page.inner_text("body")
        print(f"从 HAR 回放的内容: {content[:100]}...")

        browser.close()

    print(f"HAR 回放完成，使用文件: {har_path}")


def example_04_har_replay_update() -> None:
    """示例 04：HAR 回放并更新（录制新的请求到 HAR）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    har_path = HAR_DEMO_DIR / "update.har"
    har_path.parent.mkdir(parents=True, exist_ok=True)

    # 创建初始 HAR
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_har_path=str(har_path),
        )
        page = context.new_page()
        page.goto("https://example.com")
        browser.close()

    # 使用 HAR 并更新
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # === 从 HAR 回放，并记录新请求 ===
        page.route_from_har(
            har=str(har_path),
            # update: 将新请求更新到 HAR 文件
            update=True,

            # update_content: 更新的内容模式
            # - "embed": 嵌入响应体
            # - "attach": 响应体单独存储
            update_content="embed",

            # update_mode: 更新模式
            # - "full": 完整更新
            # - "minimal": 最小更新
            update_mode="full",

            # url: 只处理匹配的 URL
            url="**/*",
        )

        # 这个请求会被记录到 HAR
        page.goto("https://example.com")

        browser.close()

    # 检查更新的 HAR
    with open(har_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)
        print(f"更新后的 HAR 包含 {len(har_data['log']['entries'])} 个请求")


def example_05_har_with_zip() -> None:
    """示例 05：HAR ZIP 格式（支持外部内容）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    har_zip_path = HAR_DEMO_DIR / "content.zip"
    har_zip_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            # 使用 .zip 扩展名会自动创建 ZIP 格式的 HAR
            record_har_path=str(har_zip_path),

            # attach 模式会将响应体存储为外部文件
            record_har_content="attach",
        )

        page = context.new_page()
        page.goto("https://example.com")
        page.wait_for_load_state("networkidle")

        browser.close()

    # ZIP 文件包含 HAR 文件和外部内容
    if har_zip_path.exists():
        with zipfile.ZipFile(har_zip_path, 'r') as zip_file:
            print(f"ZIP 文件内容:")
            for name in zip_file.namelist():
                print(f"  - {name}")

    print(f"HAR ZIP 文件已保存: {har_zip_path}")


# =============================================================================
# CDP (Chrome DevTools Protocol) 高级示例
# =============================================================================


def example_06_cdp_session_basic() -> None:
    """示例 06：CDP Session 基础用法"""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # === 创建 CDP Session ===
        # CDP Session 允许直接使用 Chrome DevTools Protocol
        cdp = context.new_cdp_session(page)

        # === 发送 CDP 命令 ===
        # 启用 Performance domain
        cdp.send("Performance.enable")

        # 获取性能指标
        metrics = cdp.send("Performance.getMetrics")
        print("性能指标:")
        for metric in metrics.get("metrics", [])[:5]:
            print(f"  {metric['name']}: {metric['value']}")

        # === 监听 CDP 事件 ===
        def on_console_api_message(event: Any) -> None:
            """监听 Console API 调用"""
            if event.get("type") == "log":
                args = event.get("args", [])
                print(f"[CDP Console] {' '.join(str(arg.get('value', arg)) for arg in args)}")

        cdp.on("Runtime.consoleAPICalled", on_console_api_message)

        # 在页面中执行 JavaScript，触发 CDP 事件
        page.evaluate("console.log('来自 CDP 的消息')")

        page.wait_for_timeout(1000)

        # 清理
        cdp.detach()
        context.close()
        browser.close()


def example_07_cdp_network_domain() -> None:
    """示例 07：使用 CDP 控制 Network 行为"""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        cdp = context.new_cdp_session(page)

        # === Network Domain 命令 ===

        # 1. 启用 Network domain
        cdp.send("Network.enable")

        # 2. 设置忽略 HTTPS 错误
        cdp.send("Network.setIgnoreCertificateErrors", {"ignore": True})

        # 3. 设置 User Agent
        cdp.send("Network.setUserAgentOverride", {
            "userAgent": "CDP Custom User Agent"
        })

        # 4. 监听网络事件
        network_requests: list[dict] = []

        def on_request_will_be_sent(event: Any) -> None:
            """请求将要发送"""
            request = event.get("request", {})
            network_requests.append({
                "url": request.get("url"),
                "method": request.get("method"),
            })

        cdp.on("Network.requestWillBeSent", on_request_will_be_sent)

        # 访问页面
        page.goto("https://example.com")

        page.wait_for_timeout(1000)

        print(f"捕获到 {len(network_requests)} 个网络请求")
        for req in network_requests[:3]:
            print(f"  {req['method']}: {req['url']}")

        cdp.detach()
        context.close()
        browser.close()


def example_08_cdp_page_domain() -> None:
    """示例 08：使用 CDP Page Domain 控制"""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        cdp = context.new_cdp_session(page)

        # === Page Domain 命令 ===

        # 1. 启用 Page domain
        cdp.send("Page.enable")

        # 2. 获取页面布局指标
        page.goto("https://example.com")
        layout_metrics = cdp.send("Page.getLayoutMetrics")

        print("页面布局指标:")
        print(f"  内容大小: {layout_metrics.get('contentSize', {})}")
        print(f"  布局视口: {layout_metrics.get('layoutViewport', {})}")

        # 3. 设置设备_metrics_override
        cdp.send("Emulation.setDeviceMetricsOverride", {
            "width": 1920,
            "height": 1080,
            "deviceScaleFactor": 1,
            "mobile": False,
        })

        # 4. 获取页面资源树
        resource_tree = cdp.send("Page.getResourceTree")
        frame_tree = resource_tree.get("frameTree", {})
        print(f"页面框架: {frame_tree.get('frame', {}).get('url')}")

        cdp.detach()
        context.close()
        browser.close()


def example_09_cdp_runtime_domain() -> None:
    """示例 09：使用 CDP Runtime Domain 执行代码"""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://example.com")

        cdp = context.new_cdp_session(page)

        # === Runtime Domain 命令 ===

        # 1. 启用 Runtime
        cdp.send("Runtime.enable")

        # 2. 执行 JavaScript 表达式
        result = cdp.send("Runtime.evaluate", {
            "expression": "document.title",
            "returnByValue": True,
        })

        print(f"页面标题: {result.get('result', {}).get('value')}")

        # 3. 执行异步函数
        async_result = cdp.send("Runtime.evaluate", {
            "expression": """
                (async function() {
                    return new Promise(resolve => {
                        setTimeout(() => resolve('async result'), 100);
                    });
                })()
            """,
            "awaitPromise": True,
            "returnByValue": True,
        })

        print(f"异步执行结果: {async_result.get('result', {}).get('value')}")

        # 4. 获取对象属性
        obj_result = cdp.send("Runtime.evaluate", {
            "expression": "({a: 1, b: 2})",
            "returnByValue": False,  # 返回 RemoteObject
        })

        obj_id = obj_result.get("result", {}).get("objectId")
        if obj_id:
            properties = cdp.send("Runtime.getProperties", {
                "objectId": obj_id,
                "ownProperties": True,
            })

            print("对象属性:")
            for prop in properties.get("result", []):
                print(f"  {prop.get('name')}: {prop.get('value', {}).get('value')}")

        cdp.detach()
        context.close()
        browser.close()


def example_10_cdp_debugger_domain() -> None:
    """示例 10：使用 CDP Debugger Domain 控制执行"""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        cdp = context.new_cdp_session(page)

        # === Debugger Domain 命令 ===

        # 1. 启用 Debugger
        cdp.send("Debugger.enable")

        # 2. 暂停/恢复 JavaScript 执行
        cdp.send("Debugger.pause")

        # 在暂停状态下执行代码
        page.evaluate("console.log('这行会被暂停')")

        # 恢复执行
        cdp.send("Debugger.resume")

        # 3. 设置断点（通过脚本）
        page.set_content("""
            <html><body>
                <h1>Debugger Test</h1>
                <script>
                    function testFunction() {
                        debugger; // 断点
                        console.log('断点之后');
                    }
                    testFunction();
                </script>
            </body></html>
        """)

        # 监听 debugger 暂停事件
        paused_events: list = []

        def on_paused(event: Any) -> None:
            """JavaScript 执行暂停"""
            paused_events.append(event)
            reason = event.get("reason", "")
            print(f"[Debugger] 暂停原因: {reason}")

        cdp.on("Debugger.paused", on_paused)

        page.wait_for_timeout(1000)

        print(f"捕获到 {len(paused_events)} 次暂停事件")

        # 禁用 Debugger
        cdp.send("Debugger.disable")

        cdp.detach()
        context.close()
        browser.close()


def example_11_connect_over_cdp() -> None:
    """示例 11：通过 CDP 连接到已有浏览器"""
    from playwright.sync_api import sync_playwright

    # 注意：此示例需要有一个 Chrome 浏览器以调试模式运行
    # 启动命令示例：
    #   chrome --remote-debugging-port=9222
    # 或
    #   chromium --remote-debugging-port=9222

    with sync_playwright() as p:
        # === 尝试通过 CDP 连接 ===
        try:
            # connect_over_cdp 连接到已运行的浏览器
            browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")

            # 获取已存在的上下文
            contexts = browser.contexts
            print(f"已连接的浏览器有 {len(contexts)} 个上下文")

            if contexts:
                # 使用第一个上下文
                context = contexts[0]
                pages = context.pages
                print(f"上下文有 {len(pages)} 个页面")

                if pages:
                    page = pages[0]
                    print(f"页面 URL: {page.url}")
                    print(f"页面标题: {page.title()}")

            browser.close()
            print("CDP 连接成功！")

        except Exception as exc:
            print(f"[skip] CDP 连接失败（需要浏览器以调试模式运行）: {exc}")
            print("提示：可以使用以下命令启动 Chrome：")
            print("  chrome --remote-debugging-port=9222")


def example_12_cdp_multiple_sessions() -> None:
    """示例 12：多个 CDP Session 协同工作"""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://example.com")

        # === 为同一 Page 创建多个 CDP Session ===
        cdp_network = context.new_cdp_session(page)
        cdp_runtime = context.new_cdp_session(page)
        cdp_page = context.new_cdp_session(page)

        # 各 Session 独立工作
        # Network Session：控制网络
        cdp_network.send("Network.enable")
        cdp_network.send("Network.setCacheDisabled", {"cacheDisabled": False})

        # Runtime Session：执行代码
        cdp_runtime.send("Runtime.enable")

        # Page Session：控制页面
        cdp_page.send("Page.enable")

        # 使用 Runtime Session 执行代码
        result = cdp_runtime.send("Runtime.evaluate", {
            "expression": "location.href",
            "returnByValue": True,
        })
        print(f"当前 URL: {result.get('result', {}).get('value')}")

        # 使用 Page Session 获取资源树
        tree = cdp_page.send("Page.getResourceTree")
        print(f"框架树: {tree.get('frameTree', {}).get('frame', {}).get('name')}")

        # 清理所有 Session
        cdp_network.detach()
        cdp_runtime.detach()
        cdp_page.detach()

        context.close()
        browser.close()


# =============================================================================
# Client Certificates 示例
# =============================================================================


def example_13_client_certificates() -> None:
    """示例 13：客户端证书配置"""
    from playwright.sync_api import sync_playwright

    # 注意：此示例需要实际的服务器和证书
    # 这里仅展示配置方法

    with sync_playwright() as p:
        # === 配置客户端证书 ===
        context = p.chromium.launch(headless=True).new_context(
            # 使用证书文件
            client_certificates=[{
                "origin": "https://secure.example.com",  # 证书适用的源
                # 方式 1: 使用证书文件路径
                # "certPath": "/path/to/client.crt",
                # "keyPath": "/path/to/client.key",

                # 方式 2: 使用证书内容（bytes）
                # "cert": b"-----BEGIN CERTIFICATE-----\n...",
                # "key": b"-----BEGIN PRIVATE KEY-----\n...",

                # PKCS#12 格式（.p12/.pfx 文件）
                # "pfxPath": "/path/to/cert.pfx",
                # "passphrase": "password123",
            }],
        )

        # 对于需要客户端认证的请求，浏览器会自动使用配置的证书

        # 也可以在 launch_persistent_context 中使用
        persistent_context = p.chromium.launch_persistent_context(
            user_data_dir="/tmp/profile",
            headless=True,
            client_certificates=[{
                "origin": "https://another-secure.example.com",
                "certPath": "/path/to/another.crt",
                "keyPath": "/path/to/another.key",
            }],
        )

        # 证书配置后，访问对应的 HTTPS 网站会自动使用证书

        context.close()
        persistent_context.close()

    print("客户端证书配置示例（需要实际服务器验证）")


def example_14_cdp_fetch_domain() -> None:
    """示例 14：使用 CDP Fetch Domain 控制请求"""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        cdp = context.new_cdp_session(page)

        # === Fetch Domain 命令 ===

        # 1. 启用 Fetch domain
        cdp.send("Fetch.enable", {
            "patterns": [
                # 拦截所有请求
                {"urlPattern": "*"},
            ]
        })

        # 2. 监听请求并决定如何处理
        fetch_requests: list = []

        def on_request_paused(event: Any) -> None:
            """请求被暂停"""
            request_id = event.get("requestId")
            request = event.get("request", {})
            network_id = event.get("networkId")

            fetch_requests.append({
                "url": request.get("url"),
                "method": request.get("method"),
            })

            print(f"[Fetch] 拦截请求: {request.get('method')} {request.get('url')}")

            # 继续请求
            cdp.send("Fetch.continueRequest", {
                "requestId": request_id,
            })

        cdp.on("Fetch.requestPaused", on_request_paused)

        # 访问页面
        page.goto("https://example.com")

        page.wait_for_timeout(1000)

        print(f"拦截到 {len(fetch_requests)} 个请求")

        # 禁用 Fetch
        cdp.send("Fetch.disable")

        cdp.detach()
        context.close()
        browser.close()


def example_15_cdp_dom_domain() -> None:
    """示例 15：使用 CDP DOM Domain 获取 DOM 信息"""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.set_content("""
            <html>
                <body>
                    <h1 id="title">CDP DOM Test</h1>
                    <div class="container">
                        <p>段落 1</p>
                        <p>段落 2</p>
                    </div>
                </body>
            </html>
        """)

        cdp = context.new_cdp_session(page)

        # === DOM Domain 命令 ===

        # 1. 启用 DOM
        cdp.send("DOM.enable")

        # 2. 获取文档根节点
        document = cdp.send("DOM.getDocument")
        root_node_id = document.get("root", {}).get("nodeId")
        print(f"根节点 ID: {root_node_id}")

        # 3. 查询节点
        h1_node = cdp.send("DOM.querySelector", {
            "nodeId": root_node_id,
            "selector": "#title",
        })

        h1_node_id = h1_node.get("nodeId")
        print(f"H1 节点 ID: {h1_node_id}")

        # 4. 获取节点属性
        attributes = cdp.send("DOM.getAttributes", {
            "nodeId": h1_node_id,
        })

        print(f"H1 属性: {attributes.get('attributes')}")

        # 5. 获取节点的外部 HTML
        outer_html = cdp.send("DOM.getOuterHTML", {
            "nodeId": h1_node_id,
        })

        print(f"H1 HTML: {outer_html.get('outerHTML')}")

        cdp.detach()
        context.close()
        browser.close()


# =============================================================================
# 主程序
# =============================================================================


def main() -> None:
    """主函数：运行所有示例"""
    examples = [
        ("HAR 录制基础", example_01_har_record_basic),
        ("HAR 录制选项", example_02_har_record_options),
        ("HAR 回放基础", example_03_har_replay_basic),
        ("HAR 回放更新", example_04_har_replay_update),
        ("HAR ZIP 格式", example_05_har_with_zip),
        ("CDP Session 基础", example_06_cdp_session_basic),
        ("CDP Network Domain", example_07_cdp_network_domain),
        ("CDP Page Domain", example_08_cdp_page_domain),
        ("CDP Runtime Domain", example_09_cdp_runtime_domain),
        ("CDP Debugger Domain", example_10_cdp_debugger_domain),
        ("CDP 连接", example_11_connect_over_cdp),
        ("多个 CDP Session", example_12_cdp_multiple_sessions),
        ("客户端证书", example_13_client_certificates),
        ("CDP Fetch Domain", example_14_cdp_fetch_domain),
        ("CDP DOM Domain", example_15_cdp_dom_domain),
    ]

    print("== HAR 和 CDP 高级用法示例 ==\n")

    for name, func in examples:
        try:
            print(f"\n{'='*60}")
            print(f"示例: {name}")
            print('='*60)
            func()
        except Exception as exc:
            print(f"[skip] {name}: {exc}")

    print("\n== 所有示例执行完毕 ==")


if __name__ == "__main__":
    main()
