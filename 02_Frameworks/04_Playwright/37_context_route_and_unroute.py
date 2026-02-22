#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 37：context.route / unroute / clear_cookies。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/37_context_route_and_unroute.py

本示例展示 context 级别的路由和 cookie 操作：
1. context.route(): 在 context 级别设置路由
2. context.unroute(): 移除 context 级别的路由
3. context.clear_cookies(): 清空 cookies

核心概念：
- context 级别的路由会应用到所有页面
- page 级别的路由优先级高于 context 级别
- unroute 可以移除指定的路由处理器

Context 路由：
- context.route(url, handler): 设置全局路由
- context.unroute(url, handler): 移除指定路由
- 适用于需要多个页面共享 mock 的场景

Cookie 操作：
- add_cookies(): 添加 cookies
- clear_cookies(): 清空所有 cookies
- cookies(): 获取所有 cookies

路由优先级：
1. 页面路由（page.route）优先
2. context 路由次之
3. 后注册的路由优先级更高
"""

from __future__ import annotations

import json


HTML = """
<button id="load">Load user</button>
<p id="out"></p>
<script>
  document.querySelector('#load').addEventListener('click', async () => {
    const resp = await fetch('https://api.example.local/user');
    const data = await resp.json();
    document.querySelector('#out').textContent = `${data.name}|${data.from}`;
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
        context = browser.new_context(extra_http_headers={"X-From": "context-demo"})

        # === Cookie 操作 ===
        context.add_cookies([{"name": "k", "value": "v", "domain": "example.local", "path": "/"}])
        print("cookies before clear ->", len(context.cookies()))
        context.clear_cookies()
        print("cookies after clear ->", len(context.cookies()))

        # === Context 级别路由 ===
        def context_handler(route) -> None:  # type: ignore[no-untyped-def]
            """Context 级别的路由处理器"""
            body = json.dumps(
                {
                    "name": "context",
                    "from": route.request.headers.get("x-from", ""),
                }
            )
            route.fulfill(status=200, content_type="application/json", body=body)

        context.route("**/user", context_handler)

        page = context.new_page()
        page.set_content(HTML)
        page.click("#load")
        expect(page.locator("#out")).to_have_text("context|context-demo")

        # === 移除 context 路由，使用 page 路由 ===
        context.unroute("**/user", context_handler)
        page.route(
            "**/user",
            lambda route: route.fulfill(
                status=200,
                content_type="application/json",
                body='{"name":"page","from":"page-route"}',
            ),
        )

        page.click("#load")
        expect(page.locator("#out")).to_have_text("page|page-route")

        print("[OK] context.route/unroute 已验证")

        context.close()
        browser.close()


if __name__ == "__main__":
    main()

