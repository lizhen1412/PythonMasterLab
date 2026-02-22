#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 53：Request 和 Response API 详细分析。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/53_request_response_details.py

本示例展示 Request 和 Response 对象的所有 API，用于网络调试和分析。

覆盖的 API：
Request: url, method, headers, all_headers, header_value, post_data, post_data_json,
          post_data_buffer, sizes, response, is_navigation_request, redirected_from,
          redirected_to, failure, timing, resource_type, frame, service_worker

Response: url, ok, status, status_text, headers, all_headers, headers_array,
          header_value, header_values, body, text, json, server_addr, security_details,
          finished, from_service_worker, request
"""

from __future__ import annotations

from typing import Any


def demo_request_basic_properties() -> None:
    """示例 01：Request 基础属性"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <head><title>Request Test</title></head>
    <body>
        <form id="form" method="post" action="/submit">
            <input name="username" value="testuser">
            <input name="email" value="test@example.com">
        </form>
        <a href="/navigate">Navigation Link</a>
        <img src="/image.jpg" alt="Test Image">
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(base_url="https://example.com")
        page = context.new_page()

        # 收集所有请求
        requests = []

        def on_request(request: Any) -> None:
            requests.append(request)

        page.on("request", on_request)
        page.set_content(HTML)

        print("=" * 60)
        print("Request 基础属性")
        print("=" * 60)

        for req in requests:
            print(f"\n请求: {req.url}")
            print(f"  方法: {req.method}")
            print(f"  资源类型: {req.resource_type}")
            print(f"  是否导航请求: {req.is_navigation_request()}")

            # headers 属性（字典形式）
            print(f"  请求头 (headers):")
            for key, value in dict(req.headers).items():
                print(f"    {key}: {value}")

        browser.close()


def demo_request_post_data() -> None:
    """示例 02：Request POST 数据"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <form id="json-form" method="post" action="/api/data">
            <input name="name" value="Alice">
            <input name="age" value="25" type="number">
        </form>
        <button onclick="sendJson()">Send JSON</button>
        <script>
        function sendJson() {
            fetch('/api/json', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({user: 'Bob', score: 100})
            });
        }
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 拦截请求
        post_requests = []

        def handle_route(route: Any) -> None:
            req = route.request
            if req.method == "POST":
                post_requests.append(req)
            route.abort()

        page.route("**/*", handle_route)
        page.set_content(HTML)

        print("\n" + "=" * 60)
        print("Request POST 数据")
        print("=" * 60)

        # 提交表单
        page.locator("#json-form").evaluate("form => form.submit()")

        # 发送 JSON
        page.locator("button").click()

        for req in post_requests:
            print(f"\nPOST 请求: {req.url}")

            # post_data - 原始字符串
            if req.post_data:
                print(f"  post_data (字符串): {req.post_data}")

            # post_data_buffer - 原始字节
            if req.post_data_buffer:
                print(f"  post_data_buffer (字节长度): {len(req.post_data_buffer)}")

            # post_data_json - 自动解析为对象
            try:
                json_data = req.post_data_json
                if json_data:
                    print(f"  post_data_json (解析后): {json_data}")
            except Exception as e:
                print(f"  post_data_json: 无法解析 - {e}")

        browser.close()


def demo_request_sizes() -> None:
    """示例 03：Request 大小分析"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>body { background: url('/large-bg.jpg'); }</style>
    </head>
    <body>
        <h1>Page with Large Resources</h1>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        sizes_data = []

        def handle_route(route: Any) -> None:
            req = route.request
            route.fulfill(status=200, body=b"OK")
            # 获取请求大小信息
            if req.resource_type in ["stylesheet", "image", "script"]:
                try:
                    sizes = req.sizes()
                    sizes_data.append({"url": req.url, "sizes": sizes})
                except Exception:
                    pass

        page.route("**/*", handle_route)
        page.set_content(HTML)

        print("\n" + "=" * 60)
        print("Request 大小分析 (sizes)")
        print("=" * 60)

        for data in sizes_data:
            url = data["url"].split("/")[-1]
            sizes = data["sizes"]
            print(f"\n资源: {url}")
            print(f"  请求体大小: {sizes['body']}")
            print(f"  请求头大小: {sizes['headers']}")
            print(f"  总大小: {sizes['body'] + sizes['headers']}")

        browser.close()


def demo_request_headers() -> None:
    """示例 04：Request 头部 API"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        headers_info = []

        def handle_route(route: Any) -> None:
            req = route.request

            # 1. headers - 属性访问（字典）
            headers_dict = dict(req.headers)

            # 2. all_headers() - 获取所有头部（包含额外信息）
            all_headers = req.all_headers()

            # 3. header_value() - 获取单个头部值
            user_agent = req.header_value("user-agent")

            # 4. headers_array() - 获取头部数组
            headers_array = req.headers_array()

            headers_info.append({
                "url": req.url,
                "headers": headers_dict,
                "all_headers": all_headers,
                "user_agent": user_agent,
                "headers_array": headers_array,
            })

            route.abort()

        page.route("**/*", handle_route)
        page.goto("https://example.com")

        print("\n" + "=" * 60)
        print("Request 头部 API")
        print("=" * 60)

        for info in headers_info[:1]:  # 只打印第一个
            print(f"\n请求: {info['url']}")
            print(f"\n1. headers (属性):")
            for k, v in list(info["headers"].items())[:3]:
                print(f"   {k}: {v}")
            print(f"\n2. all_headers():")
            for k, v in list(info["all_headers"].items())[:3]:
                print(f"   {k}: {v}")
            print(f"\n3. header_value('user-agent'):")
            print(f"   {info['user_agent']}")
            print(f"\n4. headers_array():")
            for h in info["headers_array"][:3]:
                print(f"   {h['name']}: {h['value']}")

        browser.close()


def demo_request_redirect_chain() -> None:
    """示例 05：请求重定向链"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        def handle_route(route: Any) -> None:
            req = route.request
            url = req.url

            # 模拟重定向链
            # /page1 -> /page2 -> /page3 -> /final
            if url.endswith("/page1"):
                route.fulfill(
                    status=301,
                    headers={"Location": "/page2"},
                    body=""
                )
            elif url.endswith("/page2"):
                route.fulfill(
                    status=302,
                    headers={"Location": "/page3"},
                    body=""
                )
            elif url.endswith("/page3"):
                route.fulfill(
                    status=307,
                    headers={"Location": "/final"},
                    body=""
                )
            else:
                route.fulfill(
                    status=200,
                    body="Final Destination"
                )

        page.route("**/*", handle_route)

        print("\n" + "=" * 60)
        print("请求重定向链")
        print("=" * 60)

        # 导航到会重定向的 URL
        page.goto("https://example.com/page1")

        # 获取最终请求
        final_req = page.request
        print(f"\n最终请求: {final_req.url}")

        # 追踪重定向链（向后）
        print("\n重定向链（向后追踪）:")
        current = final_req.redirected_from
        while current:
            print(f"  <- {current.url}")
            current = current.redirected_from

        # 追踪重定向链（向前）
        print("\n重定向链（向前追踪）:")
        current = final_req.redirected_from
        while current:
            if current.redirected_to:
                print(f"  {current.url} -> {current.redirected_to.url}")
            current = current.redirected_from

        browser.close()


def demo_request_timing() -> None:
    """示例 06：Request 时机分析"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        timing_info = []

        def handle_route(route: Any) -> None:
            req = route.request
            route.fulfill(status=200, body="Response")

            # 获取时机信息
            timing = req.timing
            timing_info.append({
                "url": req.url,
                "timing": timing
            })

        page.route("**/*", handle_route)
        page.goto("https://example.com")

        print("\n" + "=" * 60)
        print("Request Resource Timing")
        print("=" * 60)

        for info in timing_info[:1]:
            timing = info["timing"]
            print(f"\nURL: {info['url']}")
            print(f"  startTime: {timing['startTime']}")
            print(f"  domainLookupStart: {timing['domainLookupStart']}")
            print(f"  domainLookupEnd: {timing['domainLookupEnd']}")
            print(f"  connectStart: {timing['connectStart']}")
            print(f"  connectEnd: {timing['connectEnd']}")
            print(f"  requestStart: {timing['requestStart']}")
            print(f"  responseStart: {timing['responseStart']}")
            print(f"  responseEnd: {timing['responseEnd']}")

            # 计算各阶段耗时
            if timing['domainLookupEnd'] > 0:
                dns_time = timing['domainLookupEnd'] - timing['domainLookupStart']
                print(f"\n  DNS 查询耗时: {dns_time}ms")

            if timing['connectEnd'] > 0:
                connect_time = timing['connectEnd'] - timing['connectStart']
                print(f"  连接建立耗时: {connect_time}ms")

            if timing['responseEnd'] > 0:
                total_time = timing['responseEnd'] - timing['startTime']
                print(f"  总耗时: {total_time}ms")

        browser.close()


def demo_response_basic_properties() -> None:
    """示例 07：Response 基础属性"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        responses = []

        def on_response(response: Any) -> None:
            responses.append(response)

        page.on("response", on_response)

        def handle_route(route: Any) -> None:
            # 返回不同状态码
            url = route.request.url
            if "ok" in url:
                route.fulfill(status=200, status_text="OK", body="Success")
            elif "notfound" in url:
                route.fulfill(status=404, status_text="Not Found", body="Missing")
            elif "error" in url:
                route.fulfill(status=500, status_text="Server Error", body="Error")
            else:
                route.continue_()

        page.route("**/*", handle_route)

        # 触发不同请求
        page.goto("https://example.com/ok")
        page.goto("https://example.com/notfound")
        page.goto("https://example.com/error")

        print("\n" + "=" * 60)
        print("Response 基础属性")
        print("=" * 60)

        for resp in responses:
            print(f"\n响应: {resp.url}")
            print(f"  状态码 (status): {resp.status}")
            print(f"  状态文本 (status_text): {resp.status_text}")
            print(f"  是否成功 (ok): {resp.ok}")
            print(f"  来自 Service Worker: {resp.from_service_worker}")

        browser.close()


def demo_response_headers() -> None:
    """示例 08：Response 头部 API"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        def handle_route(route: Any) -> None:
            route.fulfill(
                status=200,
                headers={
                    "Content-Type": "application/json",
                    "Cache-Control": "max-age=3600",
                    "X-Custom-Header": "Custom-Value",
                    "Set-Cookie": "session=abc123"
                },
                body='{"data": "value"}'
            )

        page.route("**/*", handle_route)
        page.goto("https://example.com")

        # 获取响应
        response = page.request.response()

        print("\n" + "=" * 60)
        print("Response 头部 API")
        print("=" * 60)

        print(f"\n响应: {response.url}")

        # 1. headers - 属性访问
        print(f"\n1. headers (属性):")
        for k, v in dict(response.headers).items():
            print(f"   {k}: {v}")

        # 2. all_headers()
        print(f"\n2. all_headers():")
        all_headers = response.all_headers()
        for k, v in all_headers.items():
            print(f"   {k}: {v}")

        # 3. headers_array()
        print(f"\n3. headers_array():")
        headers_array = response.headers_array()
        for h in headers_array:
            print(f"   {h['name']}: {h['value']}")

        # 4. header_value()
        print(f"\n4. header_value('content-type'):")
        ct = response.header_value("content-type")
        print(f"   {ct}")

        # 5. header_values() - 获取多值头部的所有值
        print(f"\n5. header_values('set-cookie'):")
        values = response.header_values("set-cookie")
        for v in values:
            print(f"   {v}")

        browser.close()


def demo_response_body() -> None:
    """示例 09：Response 正文处理"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        def handle_route(route: Any) -> None:
            url = route.request.url

            if "json" in url:
                route.fulfill(
                    status=200,
                    headers={"Content-Type": "application/json"},
                    body='{"user": "Alice", "age": 30, "active": true}'
                )
            elif "text" in url:
                route.fulfill(
                    status=200,
                    headers={"Content-Type": "text/plain"},
                    body="Hello, World!"
                )
            elif "binary" in url:
                route.fulfill(
                    status=200,
                    headers={"Content-Type": "application/octet-stream"},
                    body=b"\x00\x01\x02\x03"
                )
            else:
                route.continue_()

        page.route("**/*", handle_route)

        print("\n" + "=" * 60)
        print("Response 正文 API")
        print("=" * 60)

        # JSON 响应
        page.goto("https://example.com/api/json")
        json_resp = page.request.response()
        print(f"\nJSON 响应: {json_resp.url}")

        # body() - 获取原始字节
        body_bytes = json_resp.body()
        print(f"  body() (字节): {body_bytes}")

        # text() - 获取解码后的文本
        text = json_resp.text()
        print(f"  text(): {text}")

        # json() - 解析为对象
        json_obj = json_resp.json()
        print(f"  json(): {json_obj}")

        # 文本响应
        page.goto("https://example.com/api/text")
        text_resp = page.request.response()
        print(f"\n文本响应: {text_resp.url}")
        print(f"  text(): {text_resp.text()}")

        # 二进制响应
        page.goto("https://example.com/api/binary")
        binary_resp = page.request.response()
        print(f"\n二进制响应: {binary_resp.url}")
        print(f"  body(): {binary_resp.body()}")

        browser.close()


def demo_response_server_info() -> None:
    """示例 10：Response 服务器信息"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        def handle_route(route: Any) -> None:
            # 对于 HTTPS 请求，返回模拟的安全信息
            # 注意：实际安全信息来自真实 SSL 连接
            route.fulfill(status=200, body="Secure Response")

        page.route("**/*", handle_route)

        # 使用真实网站获取实际的服务器信息
        page.goto("https://example.com")

        response = page.request.response()

        print("\n" + "=" * 60)
        print("Response 服务器信息")
        print("=" * 60)

        print(f"\n响应: {response.url}")

        # server_addr() - 获取服务器地址
        server_addr = response.server_addr()
        if server_addr:
            print(f"\nserver_addr():")
            print(f"  IP 地址: {server_addr.get('ipAddress')}")
            print(f"  端口: {server_addr.get('port')}")

        # security_details() - 获取安全详情（仅 HTTPS）
        security = response.security_details()
        if security:
            print(f"\nsecurity_details():")
            print(f"  协议: {security.get('protocol')}")
            print(f"  主体名称: {security.get('subjectName')}")
            print(f"  颁发者: {security.get('issuer')}")
            print(f"  有效期: {security.get('validFrom')} - {security.get('validTo')}")
        else:
            print("\nsecurity_details(): 不可用（非 HTTPS）")

        browser.close()


def demo_response_finished() -> None:
    """示例 11：Response 完成等待"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    import time

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("\n" + "=" * 60)
        print("Response finished() 等待")
        print("=" * 60)

        def handle_route(route: Any) -> None:
            # 模拟慢速响应
            time.sleep(0.1)
            route.fulfill(status=200, body="Slow Response")

        page.route("**/*", handle_route)

        start = time.time()
        page.goto("https://example.com")
        response = page.request.response()

        # 等待响应完全完成
        response.finished()
        elapsed = time.time() - start

        print(f"\n响应完全完成耗时: {elapsed:.3f} 秒")
        print("  finished() 确保响应体完全下载并处理完成")

        browser.close()


def demo_request_response_together() -> None:
    """示例 12：Request 和 Response 配合使用"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        request_response_pairs = []

        def on_request(request: Any) -> None:
            # 记录请求
            request_response_pairs.append({"request": request, "response": None})

        def on_response(response: Any) -> None:
            # 关联请求和响应
            for pair in request_response_pairs:
                if pair["request"] == response.request:
                    pair["response"] = response
                    break

        page.on("request", on_request)
        page.on("response", on_response)

        def handle_route(route: Any) -> None:
            req = route.request
            # 返回基于请求的响应
            body = f"Response to {req.method} {req.url}"
            route.fulfill(
                status=200,
                headers={"X-Request-Method": req.method},
                body=body
            )

        page.route("**/*", handle_route)
        page.goto("https://example.com")

        print("\n" + "=" * 60)
        print("Request 和 Response 配合使用")
        print("=" * 60)

        for pair in request_response_pairs:
            req = pair["request"]
            resp = pair["response"]

            print(f"\n请求-响应对:")
            print(f"  请求 URL: {req.url}")
            print(f"  请求方法: {req.method}")
            print(f"  请求头: {dict(req.headers).get('user-agent', 'N/A')}")
            if resp:
                print(f"  响应状态: {resp.status}")
                print(f"  响应头: {dict(resp.headers).get('content-type', 'N/A')}")

        browser.close()


def main() -> None:
    """运行所有示例"""
    print("Playwright Request 和 Response API 详细分析")
    print("=" * 60)

    demo_request_basic_properties()
    demo_request_post_data()
    demo_request_sizes()
    demo_request_headers()
    demo_request_redirect_chain()
    demo_request_timing()
    demo_response_basic_properties()
    demo_response_headers()
    demo_response_body()
    demo_response_server_info()
    demo_response_finished()
    demo_request_response_together()

    print("\n" + "=" * 60)
    print("API 速查表")
    print("=" * 60)
    print("\nRequest 属性和方法:")
    print("  url                请求 URL")
    print("  method             HTTP 方法")
    print("  headers            请求头（字典）")
    print("  all_headers()      所有请求头（异步）")
    print("  headers_array()    请求头数组（异步）")
    print("  header_value()     获取单个头部值")
    print("  post_data          POST 数据（字符串）")
    print("  post_data_json     POST 数据（JSON）")
    print("  post_data_buffer   POST 数据（字节）")
    print("  sizes()            请求大小信息")
    print("  response()         获取响应对象")
    print("  is_navigation_request()  是否为导航请求")
    print("  redirected_from    重定向来源")
    print("  redirected_to      重定向目标")
    print("  failure            失败原因")
    print("  timing             资源时机")
    print("  resource_type      资源类型")
    print("  frame              所属 Frame")
    print("  service_worker     所属 Service Worker")

    print("\nResponse 属性和方法:")
    print("  url                响应 URL")
    print("  ok                 是否成功 (2xx)")
    print("  status             状态码")
    print("  status_text        状态文本")
    print("  headers            响应头（字典）")
    print("  all_headers()      所有响应头（异步）")
    print("  headers_array()    响应头数组（异步）")
    print("  header_value()     获取单个头部值")
    print("  header_values()    获取多值头部")
    print("  body()             响应体（字节）")
    print("  text()             响应体（文本）")
    print("  json()             响应体（JSON）")
    print("  server_addr()      服务器地址")
    print("  security_details() SSL/TLS 详情")
    print("  finished()         等待响应完成")
    print("  from_service_worker  来自 SW")
    print("  request            对应的 Request")


if __name__ == "__main__":
    main()
