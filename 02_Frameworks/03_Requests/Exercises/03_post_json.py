#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：POST JSON 数据。
Author: Lambert

题目：
使用 requests 向 httpbin.org 发送 POST 请求，发送 JSON 数据。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/03_post_json.py
"""

from __future__ import annotations

import requests


def post_json(data: dict) -> dict:
    """发送 POST JSON 数据"""
    url = "https://httpbin.org/post"
    response = requests.post(url, json=data, timeout=10)
    response.raise_for_status()
    return response.json()["json"]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got}")


def main() -> None:
    data = {"username": "alice", "password": "secret123"}
    result = post_json(data)
    check("username", result.get("username"), "alice")
    check("password", result.get("password"), "secret123")
    print("[OK] POST JSON data")


if __name__ == "__main__":
    main()