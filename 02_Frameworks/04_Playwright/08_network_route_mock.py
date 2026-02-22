#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：route 拦截与 mock 接口。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/08_network_route_mock.py

本示例展示如何拦截和 mock 网络请求：
1. route(): 注册路由拦截器
2. route.fulfill(): 返回 mock 响应
3. wait_for_function(): 等待异步操作完成

核心概念：
- route() 可以拦截匹配 URL 模式的所有网络请求
- 使用通配符 "**/user" 匹配任何包含 "/user" 的 URL
- fulfill() 可以返回自定义的响应状态码、头部和内容
- 这对于测试非常有用：可以避免依赖真实后端 API

常见用途：
- Mock API 响应，避免依赖真实服务器
- 修改请求/响应内容
- 阻止某些请求（如埋点、广告）
- 模拟网络错误场景
"""

from __future__ import annotations


# 模拟一个会发起网络请求的页面
HTML = """
<button id="btn">Load</button>
<pre id="out"></pre>
<script>
  document.querySelector('#btn').addEventListener('click', async () => {
    // 发起一个网络请求
    const resp = await fetch('https://api.example.local/user');
    const data = await resp.json();
    document.querySelector('#out').textContent = `${data.name}:${data.level}`;
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

            # === 定义 mock 函数 ===
            # route 参数是 Route 对象，表示被拦截的路由
            # type: ignore 用于忽略类型检查（route 参数类型较复杂）
            def mock_user(route) -> None:  # type: ignore[no-untyped-def]
                # fulfill() 返回一个 mock 响应
                # status: HTTP 状态码
                # content_type: 响应的 Content-Type 头
                # body: 响应体内容（字符串）
                route.fulfill(
                    status=200,
                    content_type="application/json",
                    body='{"name":"lizhen","level":"gold"}',
                )

            # === 注册路由拦截 ===
            # "**/user" 是 URL 匹配模式
            # ** 表示匹配任意字符（包括路径分隔符）
            # 这会匹配任何包含 "/user" 的 URL
            page.route("**/user", mock_user)

            # 设置页面内容
            page.set_content(HTML)

            # 点击按钮触发网络请求
            page.click("#btn")

            # 等待输出内容出现
            # 等待直到输出元素的文本长度大于 0
            page.wait_for_function(
                "() => document.querySelector('#out').textContent.length > 0"
            )

            # 获取并验证结果
            out = page.locator("#out").inner_text()
            print("mock result ->", out)
            assert out == "lizhen:gold", f"期望 'lizhen:gold'，实际得到 '{out}'"

            print("Mock 测试通过！")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
