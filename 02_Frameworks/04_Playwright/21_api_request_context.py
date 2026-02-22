#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 21：APIRequestContext（离线可跑版）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/21_api_request_context.py

本示例展示如何使用 Playwright 的 APIRequestContext 进行 API 测试：
1. p.request.new_context(): 创建 API 请求上下文
2. request_context.get/post/fetch(): 发送 HTTP 请求
3. response.json/text/status(): 处理响应

核心概念：
- APIRequestContext 允许在不启动浏览器的情况下发送 HTTP 请求
- 支持所有标准 HTTP 方法（GET、POST、PUT、DELETE、PATCH 等）
- 自动处理 cookies、重定向、headers 等
- 可以用于纯 API 测试，无需浏览器开销

APIRequestContext 特性：
- base_url: 设置基础 URL，后续请求可以使用相对路径
- extra_http_headers: 为所有请求添加默认 HTTP 头
- 自动处理 cookies 和存储状态
- 支持请求超时和重试

常用方法：
- get(url, **kwargs): 发送 GET 请求
- post(url, data=None, **kwargs): 发送 POST 请求
- fetch(url, **kwargs): 通用请求方法
- dispose(): 释放资源（或使用 with 语句）

与浏览器 API 的区别：
- APIRequestContext 不启动浏览器，性能更高
- 适合纯后端 API 测试
- 不支持 DOM 操作和页面交互

常见用途：
- 测试 REST API
- 验证后端接口功能
- 模拟 API 调用
- 与页面测试结合，验证数据流
"""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


# 演示用的 API 服务器处理器
class DemoApiHandler(BaseHTTPRequestHandler):
    """处理 GET/POST 请求的演示 API 服务器"""

    def _write_json(self, status: int, payload: dict[str, object]) -> None:
        """写入 JSON 响应"""
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        # 处理 GET 请求，返回路径和自定义 header
        if self.path.startswith("/ping"):
            self._write_json(
                200,
                {
                    "ok": True,
                    "path": self.path,
                    "x_from": self.headers.get("X-From", ""),
                },
            )
            return
        self._write_json(404, {"error": "not found"})

    def do_POST(self) -> None:  # noqa: N802
        # 处理 POST 请求，回显请求体
        if self.path == "/echo":
            raw_len = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(raw_len).decode("utf-8") if raw_len else ""
            self._write_json(
                200,
                {
                    "echo": raw_body,
                    "content_type": self.headers.get("Content-Type", ""),
                },
            )
            return
        self._write_json(404, {"error": "not found"})

    def log_message(self, format: str, *args: object) -> None:
        # 教学示例不输出 server access log，避免干扰阅读
        return


def start_demo_server() -> tuple[ThreadingHTTPServer, threading.Thread]:
    """启动演示 API 服务器，返回 server 和 thread 对象"""
    server = ThreadingHTTPServer(("127.0.0.1", 0), DemoApiHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 启动演示 API 服务器
    server, thread = start_demo_server()
    base_url = f"http://127.0.0.1:{server.server_port}"
    print("demo api base_url ->", base_url)

    try:
        with sync_playwright() as p:
            # === 创建 APIRequestContext ===
            # base_url: 基础 URL，后续请求可以使用相对路径
            # extra_http_headers: 为所有请求添加默认 HTTP 头
            # 使用 with 语句确保资源正确清理
            with p.request.new_context(
                base_url=base_url,
                extra_http_headers={"X-From": "playwright-demo"},
            ) as request_context:
                # === GET 请求 ===
                # 使用相对路径 "/ping"，base_url 会自动添加
                resp_get = request_context.get("/ping")
                print("GET /ping status ->", resp_get.status)
                print("GET /ping json ->", resp_get.json())

                # === POST 请求 ===
                # post() 发送 POST 请求，data 参数为请求体
                resp_post = request_context.post("/echo", data="hello-api")
                print("POST /echo status ->", resp_post.status)
                print("POST /echo json ->", resp_post.json())

                # === FETCH 请求 ===
                # fetch() 是通用方法，可以指定任意 HTTP 方法
                # 这里使用完整 URL（也可以使用相对路径）
                resp_fetch = request_context.fetch(f"{base_url}/ping?via=fetch")
                print("FETCH /ping status ->", resp_fetch.status)
                print("FETCH /ping text ->", resp_fetch.text())

                # request_context 会自动通过 with 语句释放
    finally:
        # 清理演示服务器资源
        server.shutdown()
        server.server_close()
        thread.join(timeout=1)


if __name__ == "__main__":
    main()
