#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 25：Console 与 Network 事件监听。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/25_console_and_network_events.py

本示例展示如何监听浏览器的控制台和网络事件：
1. page.on("console"): 监听控制台输出
2. page.on("request"): 监听网络请求
3. page.on("response"): 监听网络响应
4. page.route(): 拦截和修改网络请求

核心概念：
- Playwright 可以监听浏览器的各种事件
- 事件监听器在事件发生时被调用
- 适合调试和验证页面行为
- 可以结合网络拦截实现 mock

Console 事件：
- console.log/warn/error 都会触发 "console" 事件
- msg.text 获取日志文本
- msg.type 获取日志类型（log, warn, error 等）

Network 事件：
- "request": 网络请求发送前触发
- "response": 网络响应接收后触发
- "requestfailed": 请求失败时触发

常见事件类型：
- console: 控制台消息
- request: HTTP 请求
- response: HTTP 响应
- dialog: 对话框（alert/confirm/prompt）
- load: 页面加载完成
- error: 页面错误

事件监听的用途：
- 调试 JavaScript 错误
- 验证 API 请求
- 收集性能数据
- 实现自定义日志记录
"""

from __future__ import annotations


# 模拟包含控制台输出和网络请求的页面
HTML = """
<button id="go">Go</button>
<script>
  document.querySelector('#go').addEventListener('click', async () => {
    console.log('clicked-go');
    await fetch('https://api.example.local/ping');
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 用于收集事件数据
    logs: list[str] = []
    requests: list[str] = []
    responses: list[int] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()

            # === 注册事件监听器 ===
            # page.on(event, handler): 注册事件处理器
            # "console": 控制台输出事件
            page.on("console", lambda msg: logs.append(msg.text))
            # "request": 网络请求事件
            page.on("request", lambda req: requests.append(req.url))
            # "response": 网络响应事件
            page.on("response", lambda resp: responses.append(resp.status))

            # === 网络请求拦截 ===
            # 拦截匹配的请求，返回 mock 响应
            # 这样可以避免真实网络请求，确保测试稳定性
            page.route(
                "**/ping",
                lambda route: route.fulfill(
                    status=200,
                    content_type="application/json",
                    body='{"ok": true}',
                ),
            )

            # 设置页面内容并触发事件
            page.set_content(HTML)
            page.click("#go")
            page.wait_for_timeout(200)

            # 打印收集到的事件数据
            print("console logs ->", logs)
            print("request count ->", len(requests))
            print("response statuses ->", responses)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
