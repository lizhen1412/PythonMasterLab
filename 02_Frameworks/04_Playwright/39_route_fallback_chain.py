#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 39：route.fallback 链式处理。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/39_route_fallback_chain.py

本示例展示路由的链式处理（fallback）：
1. route.fallback(): 将请求传递给下一个路由处理器
2. 多个路由可以组成处理链
3. 后注册的路由优先执行

核心概念：
- 多个路由可以匹配同一个 URL
- 后注册的路由优先级更高
- fallback() 将请求传递给下一个匹配的路由
- 适合实现日志、监控等功能

路由处理流程：
1. 按注册顺序的倒序查找匹配的路由
2. 找到第一个匹配的路由并执行
3. 如果路由调用 fallback()，继续查找下一个
4. 直到有路由 fulfill/abort/continue，或没有更多路由

使用场景：
- 日志记录：先记录请求，再传递给下一个处理器
- 条件 mock：根据条件决定是否 mock
- 监控统计：统计请求，再正常处理
"""

from __future__ import annotations


HTML = """
<button id="load">Load</button>
<p id="out"></p>
<script>
  document.querySelector('#load').addEventListener('click', async () => {
    const resp = await fetch('https://api.example.local/level');
    const data = await resp.json();
    document.querySelector('#out').textContent = data.level;
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import expect, sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 记录路由执行顺序
    hits: list[str] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # === 基础处理器 ===
        def base_handler(route) -> None:  # type: ignore[no-untyped-def]
            """基础处理器：返回 mock 响应"""
            hits.append("base")
            route.fulfill(
                status=200,
                content_type="application/json",
                body='{"level":"base"}',
            )

        # === 日志处理器 ===
        def log_handler(route) -> None:  # type: ignore[no-untyped-def]
            """日志处理器：记录请求并传递给下一个处理器"""
            hits.append("log")
            # fallback() 将请求传递给下一个匹配的路由
            route.fallback()

        # 注册路由（后注册的优先）
        page.route("**/level", base_handler)
        page.route("**/level", log_handler)

        page.set_content(HTML)
        page.click("#load")
        expect(page.locator("#out")).to_have_text("base")

        print("route hit order ->", hits)

        browser.close()


if __name__ == "__main__":
    main()

