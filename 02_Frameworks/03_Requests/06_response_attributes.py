#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：响应属性（status_code/headers/text/content/json/encoding）。

运行：
    python3 02_Frameworks/03_Requests/06_response_attributes.py
"""

from __future__ import annotations

import requests


def main() -> None:
    resp = requests.get("https://httpbin.org/json", timeout=5)
    print("状态码 ->", resp.status_code)
    print("Headers 示例 ->")
    for k, v in list(resp.headers.items())[:4]:
        print(f"  {k}: {v}")

    print("\n编码 ->", resp.encoding)
    print("text 前 80 字符 ->", resp.text[:80].replace("\n", " "))
    print("content 字节长度 ->", len(resp.content))

    data = resp.json()
    print("json() 返回类型 ->", type(data))
    print("json() keys ->", list(data.keys()))


if __name__ == "__main__":
    main()
