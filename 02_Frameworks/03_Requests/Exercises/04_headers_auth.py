#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：自定义头和 Basic Auth。
Author: Lambert

题目：
使用 requests 向 httpbin.org 发送请求，包含自定义 User-Agent 头和 Basic Auth。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/04_headers_auth.py
"""

from __future__ import annotations

import requests


def get_with_auth() -> dict:
    """发送请求带自定义头和 Basic Auth"""
    url = "https://httpbin.org/headers"
    headers = {"User-Agent": "MyPythonApp/1.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()["headers"]


def get_basic_auth(username: str, password: str) -> dict:
    """发送 Basic Auth 认证请求"""
    url = "https://httpbin.org/basic-auth/{}/{self}"
    response = requests.get(
        url.format(username=username, password=password),
        auth=(username, password),
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    headers = get_with_auth()
    user_agent = headers.get("User-Agent", "")
    print(f"User-Agent: {user_agent}")
    assert "MyPythonApp" in user_agent
    print("[OK] custom headers")

    result = get_basic_auth("alice", "password")
    check = result.get("authenticated", False)
    assert check is True
    print("[OK] Basic Auth")


if __name__ == "__main__":
    main()