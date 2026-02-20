#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：构建 GET/参数/头，不发送。
Author: Lambert

要点：
- 使用 requests.Request 构建请求，再用 Session.prepare_request 生成 PreparedRequest
- 查看最终 URL（含查询参数编码）与头
- 适合“先看看最终会发什么”，再决定是否发送

运行：
    python3 02_Frameworks/03_Requests/03_prepare_get_and_params.py
"""

from __future__ import annotations

import requests


def main() -> None:
    req = requests.Request(
        method="GET",
        url="https://example.com/search",
        params={"q": "测试 空格", "page": 2},
        headers={"X-Demo": "abc"},
    )
    session = requests.Session()
    prepared = session.prepare_request(req)

    print("最终 URL:", prepared.url)
    print("最终方法:", prepared.method)
    print("最终头部:")
    for k, v in prepared.headers.items():
        print(f"  {k}: {v}")

    print("\n提示：PreparedRequest 只构建，不会发送；可根据需要再 session.send()。")


if __name__ == "__main__":
    main()