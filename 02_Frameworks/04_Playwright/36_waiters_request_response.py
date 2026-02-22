#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 36：waiter + request/response 监听。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/36_waiters_request_response.py

本示例展示如何等待网络请求和响应：
1. expect_request(): 等待特定的请求
2. expect_response(): 等待特定的响应
3. wait_for_load_state(): 等待加载状态
4. wait_for_url(): 等待 URL 变化

核心概念：
- Playwright 可以等待特定条件的满足
- expect_request/response 用于捕获网络事件
- 返回 Request/Response 对象供进一步操作

Waiter 方法：
- expect_request(url/predicate): 等待匹配的请求
- expect_response(url/predicate): 等待匹配的响应
- wait_for_load_state(state): 等待加载状态
- wait_for_url(url): 等待 URL 匹配
- wait_for_selector(selector): 等待元素出现

Request/Response 对象：
- request.method: 请求方法
- request.url: 请求 URL
- request.post_data: 请求体
- response.status: 响应状态码
- response.json()/text(): 响应内容

使用场景：
- 等待 API 请求完成
- 验证请求参数
- 获取响应数据
- 等待页面导航完成
"""

from __future__ import annotations


HTML = """
<button id="load">Load todo</button>
<a id="jump" href="#done">Jump</a>
<p id="out"></p>
<h2 id="done">Done</h2>
<script>
  document.querySelector('#load').addEventListener('click', async () => {
    const resp = await fetch('https://api.example.local/todo');
    const data = await resp.json();
    document.querySelector('#out').textContent = `${data.id}:${data.title}`;
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import expect, sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()

            # Mock API 响应
            page.route(
                "**/todo",
                lambda route: route.fulfill(
                    status=200,
                    content_type="application/json",
                    body='{"id": 1, "title": "learn"}',
                ),
            )

            page.set_content(HTML)
            page.wait_for_load_state("domcontentloaded")

            # === 等待网络请求和响应 ===
            with page.expect_request("**/todo") as request_info:
                with page.expect_response("**/todo") as response_info:
                    page.click("#load")

            request = request_info.value
            response = response_info.value

            print("request method ->", request.method)
            print("response status ->", response.status)
            print("response json ->", response.json())

            expect(page.locator("#out")).to_have_text("1:learn")

            # === 等待 URL 变化 ===
            page.click("#jump")
            page.wait_for_url("**#done")
            print("current url ->", page.url)
        finally:
            browser.close()


if __name__ == "__main__":
    main()

