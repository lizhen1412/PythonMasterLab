#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 50：WebSocket 和 Worker 高级用法（完整 API 覆盖）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/50_websocket_worker_advanced.py

本示例演示 Playwright 的 WebSocket 和 Worker API：
1. WebSocket 连接、消息收发、事件监听
2. WebSocket 拦截和 Mock (route_web_socket)
3. Web Worker 和 Service Worker 操作
4. CDP Session 与 Worker 交互
5. Worker 中的代码执行

## 涉及的 Playwright API
- page.expect_websocket: 等待 WebSocket 创建
- ws.on: WebSocket 事件监听
- ws.url: WebSocket URL
- ws.is_closed: 检查是否关闭
- page.route_web_socket: WebSocket 拦截
- WebSocketRoute: 拦截后的 WebSocket 路由
- page.expect_worker: 等待 Worker 创建
- page.workers: 获取所有 Worker
- worker.evaluate: 在 Worker 中执行代码
- context.service_workers: Service Worker 列表
"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any


# =============================================================================
# WebSocket 基础示例
# =============================================================================


def example_01_websocket_basic() -> None:
    """示例 01：WebSocket 基础用法（连接、事件、收发消息）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 创建一个带 WebSocket 的测试页面
    HTML = """
    <!DOCTYPE html>
    <html>
    <head><title>WebSocket Test</title></head>
    <body>
        <h1>WebSocket 测试</h1>
        <div id="status">未连接</div>
        <div id="messages"></div>
        <input id="message" type="text" placeholder="输入消息">
        <button onclick="sendMessage()">发送</button>
        <script>
            const status = document.getElementById('status');
            const messages = document.getElementById('messages');
            let ws = null;

            function connect() {
                // 使用 echo.websocket.org 作为测试服务器
                ws = new WebSocket('wss://echo.websocket.org');

                ws.onopen = function() {
                    status.textContent = '已连接';
                };

                ws.onmessage = function(event) {
                    const msg = document.createElement('div');
                    msg.textContent = '收到: ' + event.data;
                    messages.appendChild(msg);
                };

                ws.onclose = function() {
                    status.textContent = '已关闭';
                };

                ws.onerror = function(error) {
                    status.textContent = '错误: ' + error;
                };
            }

            function sendMessage() {
                const input = document.getElementById('message');
                if (ws && ws.readyState === WebSocket.OPEN) {
                    ws.send(input.value);
                    input.value = '';
                }
            }

            // 页面加载后自动连接
            window.addEventListener('load', connect);
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.set_content(HTML)

        # === 1. 使用 expect_websocket 等待 WebSocket 创建 ===
        # WebSocket 是异步创建的，使用 expect_websocket 等待
        print("等待 WebSocket 连接...")
        ws = page.expect_websocket(timeout=10000)
        print(f"WebSocket 已连接: {ws.url}")

        # === 2. 检查 WebSocket 状态 ===
        print(f"WebSocket 是否关闭: {ws.is_closed()}")

        # === 3. 监听 WebSocket 事件 ===
        messages_received = []

        def on_frame_received(payload: Any) -> None:
            """收到帧事件"""
            print(f"[收到帧] 类型: {type(payload).__name__}, 数据: {payload}")
            messages_received.append(payload)

        def on_frame_sent(payload: Any) -> None:
            """发送帧事件"""
            print(f"[发送帧] 类型: {type(payload).__name__}, 数据: {payload}")

        def on_close() -> None:
            """关闭事件"""
            print("[WebSocket 已关闭]")

        # 注册事件监听器
        ws.on("framesent", on_frame_sent)
        ws.on("framereceived", on_frame_received)
        ws.on("close", on_close)

        # === 4. 通过页面发送消息 ===
        page.fill("#message", "Hello WebSocket!")
        page.click("button")

        # 等待消息被处理
        page.wait_for_timeout(2000)

        # === 5. 使用 wait_for_event 等待特定事件 ===
        # 等待下一个接收到的帧
        def check_frame(payload: Any) -> bool:
            return isinstance(payload, str) and "Hello" in payload

        try:
            frame = ws.wait_for_event("framereceived", predicate=check_frame, timeout=5000)
            print(f"等待到匹配的帧: {frame}")
        except Exception as exc:
            print(f"等待帧超时: {exc}")

        # === 6. 关闭页面，触发 WebSocket 关闭 ===
        page.close()

        print(f"共收到 {len(messages_received)} 条消息")

        browser.close()


def example_02_websocket_interception() -> None:
    """示例 02：WebSocket 拦截和 Mock"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>WebSocket 拦截测试</h1>
        <div id="messages"></div>
        <script>
            const ws = new WebSocket('ws://localhost:8080/chat');
            ws.onmessage = function(event) {
                const msg = document.createElement('div');
                msg.textContent = event.data;
                document.getElementById('messages').appendChild(msg);
            };
            // 发送测试消息
            setTimeout(() => {
                if (ws.readyState === WebSocket.OPEN) {
                    ws.send('client message');
                }
            }, 100);
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # === WebSocket 拦截 ===
        # 使用 route_web_socket 拦截 WebSocket 连接

        intercepted_messages: list[str] = []

        def web_socket_handler(ws: Any) -> None:
            """WebSocket 拦截处理器"""
            print(f"[拦截] WebSocket 连接: {ws.url}")

            # 监听客户端发送的消息
            ws.on("framesent", lambda payload: intercepted_messages.append(payload))

            # 连接到真实服务器
            ws.connect_to_server()

            # 监听服务器消息并修改
            def on_server_message(payload: Any) -> None:
                print(f"[服务器] 原始消息: {payload}")
                # 可以修改消息后发送给客户端
                modified = f"[已修改] {payload}"
                ws.send(modified)

            ws.on("framereceived", on_server_message)

        # 注册 WebSocket 拦截器
        page.route_web_socket("**/chat", web_socket_handler)

        # 设置页面内容
        page.set_content(HTML)

        # 等待 WebSocket 和消息处理
        page.wait_for_timeout(2000)

        print(f"拦截到的客户端消息: {intercepted_messages}")

        browser.close()


def example_03_websocket_route_mock() -> None:
    """示例 03：WebSocket 完全 Mock（不连接真实服务器）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>WebSocket Mock 测试</h1>
        <div id="messages"></div>
        <script>
            const ws = new WebSocket('ws://localhost:9999/mock');
            ws.onopen = function() {
                document.getElementById('messages').innerHTML =
                    '<div>连接已建立</div>';
            };
            ws.onmessage = function(event) {
                const msg = document.createElement('div');
                msg.textContent = event.data;
                document.getElementById('messages').appendChild(msg);
            };
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # === WebSocket Mock（不连接真实服务器）===
        def mock_websocket_handler(ws: Any) -> None:
            """Mock WebSocket 处理器"""
            print(f"[Mock] WebSocket 连接请求: {ws.url}")

            # 模拟服务器发送消息
            ws.send("欢迎连接到 Mock WebSocket 服务器！")

            # 监听客户端消息并自动回复
            def handle_client_message(payload: Any) -> None:
                print(f"[Mock] 收到客户端消息: {payload}")
                # 自动回复
                ws.send(f"服务器回复: {payload}")

            ws.on("framesent", handle_client_message)

        # 注册 Mock 处理器
        page.route_web_socket("**/mock", mock_websocket_handler)

        # 设置页面内容
        page.set_content(HTML)

        # 等待消息处理
        page.wait_for_timeout(2000)

        browser.close()


# =============================================================================
# Worker 基础示例
# =============================================================================


def example_04_worker_basic() -> None:
    """示例 04：Web Worker 基础用法"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Web Worker 测试</h1>
        <div id="result"></div>
        <script>
            // 创建 Worker
            const worker = new Worker(URL.createObjectURL(new Blob([`
                self.onmessage = function(e) {
                    const result = e.data.a + e.data.b;
                    self.postMessage({result: result});
                };
            `], {type: 'application/javascript'})));

            worker.onmessage = function(e) {
                document.getElementById('result').textContent =
                    '计算结果: ' + e.data.result;
            };

            // 发送数据到 Worker
            worker.postMessage({a: 10, b: 20});
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === 1. 使用 expect_worker 等待 Worker 创建 ===
        print("等待 Worker 创建...")
        worker = page.expect_worker(timeout=5000)
        print(f"Worker 已创建: {worker.url}")

        # === 2. 获取所有 Workers ===
        # page.workers 返回当前页面的所有活跃 Worker
        all_workers = page.workers
        print(f"当前页面有 {len(all_workers)} 个 Worker")

        # === 3. 在 Worker 中执行代码 ===
        # worker.evaluate 可以在 Worker 上下文中执行 JavaScript
        result = worker.evaluate("() => self.location.href")
        print(f"Worker URL: {result}")

        # === 4. 监听 Worker 事件 ===
        def on_worker_close() -> None:
            print("[Worker] 已关闭")

        worker.on("close", on_worker_close)

        # === 5. Worker 的 JSHandle 操作 ===
        # evaluate_handle 返回 JSHandle，可以传递复杂对象
        handle = worker.evaluate_handle("() => ({workerType: 'webWorker', ready: true})")
        handle_value = handle.json_value()
        print(f"Worker 信息: {handle_value}")

        browser.close()


def example_05_service_worker() -> None:
    """示例 05：Service Worker 操作"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 创建一个带 Service Worker 的页面
    HTML = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Service Worker Test</title>
    </head>
    <body>
        <h1>Service Worker 测试</h1>
        <div id="status"></div>
        <script>
            // 注册 Service Worker
            if ('serviceWorker' in navigator) {
                const swCode = `
                    self.addEventListener('install', (e) => {
                        self.skipWaiting();
                    });
                    self.addEventListener('activate', (e) => {
                        e.waitUntil(self.clients.claim());
                    });
                    self.addEventListener('fetch', (e) => {
                        e.respondWith(
                            new Response('Service Worker 响应: ' + e.request.url)
                        );
                    });
                `;
                const blob = new Blob([swCode], {type: 'application/javascript'});
                const swUrl = URL.createObjectURL(blob);

                navigator.serviceWorker.register(swUrl)
                    .then((reg) => {
                        document.getElementById('status').textContent =
                            'Service Worker 已注册: ' + reg.scope;
                    })
                    .catch((err) => {
                        document.getElementById('status').textContent =
                            'Service Worker 注册失败: ' + err;
                    });
            }
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        # Service Worker 需要非持久化上下文
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            # 允许 Service Worker（默认）
            service_workers="allow",
        )
        page = context.new_page()
        page.set_content(HTML)

        # 等待 Service Worker 注册
        page.wait_for_timeout(2000)

        # === 1. 获取所有 Service Workers ===
        # context.service_workers 返回所有 Service Worker
        service_workers = context.service_workers
        print(f"当前上下文有 {len(service_workers)} 个 Service Worker")

        # Service Worker 本质上也是一种 Worker
        for sw in service_workers:
            print(f"Service Worker URL: {sw.url}")

            # === 2. 在 Service Worker 中执行代码 ===
            try:
                # Service Worker 可能无法直接 evaluate，因为它是独立的上下文
                result = sw.evaluate("() => self.constructor.name")
                print(f"Service Worker 类型: {result}")
            except Exception as exc:
                print(f"Service Worker evaluate 失败（可能已分离）: {exc}")

        # === 3. 阻止 Service Worker 注册 ===
        # 创建一个新上下文，阻止 Service Worker
        context_blocked = browser.new_context(service_workers="block")
        page_blocked = context_blocked.new_page()

        # 在这个上下文中，Service Worker 注册会被阻止
        # 这对测试很有用，可以避免 Service Worker 的缓存影响

        browser.close()


def example_06_worker_with_cdp() -> None:
    """示例 06：使用 CDP Session 与 Worker 交互"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Worker + CDP 测试</h1>
        <script>
            const worker = new Worker(URL.createObjectURL(new Blob([`
                let counter = 0;
                setInterval(() => {
                    counter++;
                    postMessage('tick: ' + counter);
                }, 1000);
            `], {type: 'application/javascript'})));

            worker.onmessage = function(e) {
                console.log('Worker message:', e.data);
            };
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.set_content(HTML)

        # 等待 Worker 创建
        worker = page.expect_worker()

        # === 使用 CDP Session 获取 Worker 调试信息 ===
        # 创建 CDP Session 用于 Page
        cdp_session = context.new_cdp_session(page)

        # 启用调试器
        cdp_session.send("Debugger.enable")

        # 获取所有 Target（包括 Worker）
        targets_result = cdp_session.send("Target.getTargets")

        print("CDP Targets:")
        for target in targets_result.get("targetInfos", []):
            print(f"  - {target.get('type')}: {target.get('url')}")

        # Worker 的详细信息可以通过 CDP 获取
        # 注意：这需要 Chrome 启动时支持远程调试

        cdp_session.detach()

        browser.close()


def example_07_worker_and_console() -> None:
    """示例 07：Worker 中的 Console 消息"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Worker Console 测试</h1>
        <script>
            const worker = new Worker(URL.createObjectURL(new Blob([`
                console.log('Worker 日志 1');
                console.warn('Worker 警告');
                console.error('Worker 错误');

                // 发送消息通知主线程
                postMessage('worker ready');
            `], {type: 'application/javascript'})));

            worker.onmessage = function(e) {
                console.log('主线程收到:', e.data);
            };
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === 收集所有 Console 消息 ===
        console_messages: list[dict[str, Any]] = []

        def on_console(msg: Any) -> None:
            """处理 console 消息"""
            console_messages.append({
                "type": msg.type,
                "text": msg.text,
                "page": msg.page if hasattr(msg, "page") else None,
                "worker": msg.worker if hasattr(msg, "worker") else None,
            })
            print(f"[Console {msg.type}] {msg.text}")

        page.on("console", on_console)

        # === Worker 的 Console 消息 ===
        # Worker 中的 console.log 不会触发 page 的 console 事件
        # Worker 有独立的 console 上下文

        worker = page.expect_worker()

        # 监听 Worker 的 console 消息
        def on_worker_console(msg: Any) -> None:
            """处理 Worker console 消息"""
            print(f"[Worker Console {msg.type}] {msg.text}")

        worker.on("console", on_worker_console)

        # 等待消息处理
        page.wait_for_timeout(2000)

        print(f"\n共收集到 {len(console_messages)} 条 console 消息")

        browser.close()


def example_08_shared_worker() -> None:
    """示例 08：Shared Worker（跨页面共享的 Worker）"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Shared Worker 测试</h1>
        <div id="messages"></div>
        <script>
            // 创建 Shared Worker
            const sharedWorker = new SharedWorker(
                URL.createObjectURL(new Blob([`
                    let connections = 0;
                    self.onconnect = function(e) {
                        connections++;
                        const port = e.ports[0];
                        port.postMessage('已连接，当前连接数: ' + connections);
                        port.onmessage = function(event) {
                            port.postMessage('Echo: ' + event.data);
                        };
                    };
                `], {type: 'application/javascript'})),
                'my-shared-worker'
            );

            sharedWorker.port.onmessage = function(e) {
                const msg = document.createElement('div');
                msg.textContent = e.data;
                document.getElementById('messages').appendChild(msg);
            };

            sharedWorker.port.start();
            sharedWorker.port.postMessage('来自页面的消息');
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # 创建多个页面，它们将共享同一个 Shared Worker
        page1 = context.new_page()
        page1.set_content(HTML)

        page2 = context.new_page()
        page2.set_content(HTML)

        # 等待消息
        page1.wait_for_timeout(2000)

        # Shared Worker 会在 workers 列表中显示
        print(f"Context 中的 Workers 数量: {len(context.workers)}")

        browser.close()


# =============================================================================
# 主程序
# =============================================================================


def main() -> None:
    """主函数：运行所有示例"""
    examples = [
        ("WebSocket 基础", example_01_websocket_basic),
        ("WebSocket 拦截", example_02_websocket_interception),
        ("WebSocket Mock", example_03_websocket_route_mock),
        ("Worker 基础", example_04_worker_basic),
        ("Service Worker", example_05_service_worker),
        ("Worker + CDP", example_06_worker_with_cdp),
        ("Worker Console", example_07_worker_and_console),
        ("Shared Worker", example_08_shared_worker),
    ]

    print("== WebSocket 和 Worker 高级用法示例 ==\n")

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
