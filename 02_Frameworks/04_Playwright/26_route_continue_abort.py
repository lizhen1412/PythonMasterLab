#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 26：route 的 continue / abort / fulfill。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/26_route_continue_abort.py

本示例展示网络路由的三种处理方式：
1. route.continue_(): 继续发送原始请求
2. route.abort(): 中止请求
3. route.fulfill(): 返回自定义响应

核心概念：
- page.route() 可以拦截网络请求
- 根据请求 URL 或内容选择不同的处理方式
- 实现 mock API、阻止请求、修改响应等功能

路由处理方法：
- route.continue_(): 继续原始请求（可修改请求参数）
- route.abort(): 中止请求，抛出网络错误
- route.fulfill(): 返回自定义响应，无需真实网络请求

使用场景：
- continue_: 监控请求、添加自定义 headers
- abort: 阻止特定请求（如追踪脚本、广告）
- fulfill: Mock API 响应、离线测试

路由匹配：
- page.route(pattern, handler): pattern 可以是 URL、glob 或正则
- "**/*" 匹配所有请求
- "**/*.js" 匹配所有 JS 文件
- "https://example.com/api/**" 匹配特定路径

路由顺序：
- 多个路由时，后注册的优先级更高
- 可以使用 route.fallback() 回退到下一个匹配的路由
"""

from __future__ import annotations


# 模拟包含多种网络请求的页面
HTML = """
<button id="run">run</button>
<pre id="out"></pre>
<script>
  document.querySelector('#run').addEventListener('click', async () => {
    // 这个请求会被 mock
    const ok = await fetch('https://api.example.local/mock').then(r => r.text());
    // 这个请求会被中止
    let blocked = 'not-called';
    try {
      await fetch('https://api.example.local/blocked');
      blocked = 'unexpected';
    } catch (e) {
      blocked = 'aborted';
    }
    document.querySelector('#out').textContent = ok + '|' + blocked;
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()

            # === 路由处理器 ===
            # 根据请求 URL 选择不同的处理方式
            def handler(route) -> None:  # type: ignore[no-untyped-def]
                """路由处理器：根据 URL 决定如何处理请求"""
                url = route.request.url

                # 中止请求：阻止特定 URL 的请求
                if url.endswith('/blocked'):
                    route.abort()
                    return

                # Mock 响应：返回自定义响应，无需真实网络请求
                if url.endswith('/mock'):
                    route.fulfill(status=200, body='mock-ok')
                    return

                # 继续请求：让请求正常发送到服务器
                route.continue_()

            # 注册路由处理器，匹配所有请求
            page.route("**/*", handler)

            # 设置页面内容并触发请求
            page.set_content(HTML)
            page.click("#run")
            # 等待结果显示
            page.wait_for_function("() => document.querySelector('#out').textContent.length > 0")
            print("out ->", page.locator("#out").inner_text())
        finally:
            browser.close()


if __name__ == "__main__":
    main()
