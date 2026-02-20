#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：GET 请求带查询参数。
Author: Lambert

题目：
使用 requests 向 httpbin.org 发送 GET 请求，带查询参数 name 和 age。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/02_get_with_params.py
"""

from __future__ import annotations

import requests


def get_with_params(name: str, age: int) -> dict:
    """发送 GET 请求带查询参数"""
    url = "https://httpbin.org/get"
    params = {"name": name, "age": age}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()["args"]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got}")


def main() -> None:
    result = get_with_params("Alice", 25)
    check("name", result.get("name"), "Alice")
    check("age", result.get("age"), "25")
    print("[OK] GET request with params")


if __name__ == "__main__":
    main()