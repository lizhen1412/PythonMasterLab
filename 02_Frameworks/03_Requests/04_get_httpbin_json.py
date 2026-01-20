#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：GET + JSON 解析（httpbin.org）。

运行：
    python3 02_Frameworks/03_Requests/04_get_httpbin_json.py
"""

from __future__ import annotations

import json

import requests


def main() -> None:
    resp = requests.get("https://httpbin.org/get", params={"q": "hello", "page": 2}, timeout=5)
    print("状态码 ->", resp.status_code)
    print("Content-Type ->", resp.headers.get("Content-Type"))

    data = resp.json()
    print("JSON 数据 ->", json.dumps(data, ensure_ascii=False))


if __name__ == "__main__":
    main()
