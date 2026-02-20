#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：Session 和重试策略。
Author: Lambert

题目：
创建一个带重试策略的 Session，访问 httpbin.org 多次。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/06_session_retry.py
"""

from __future__ import annotations

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_retry_session(retries: int = 3) -> requests.Session:
    """创建带重试策略的 Session"""
    session = requests.Session()

    retry_strategy = Retry(
        total=retries,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def main() -> None:
    session = create_retry_session()

    # 测试基本请求
    response = session.get("https://httpbin.org/get", timeout=10)
    assert response.status_code == 200
    print("[OK] session request")

    # 测试 Cookie 持久化
    session.get("https://httpbin.org/cookies/set?mycookie=hello")
    response = session.get("https://httpbin.org/cookies")
    cookies = response.json()["cookies"]
    assert cookies.get("mycookie") == "hello"
    print("[OK] cookie persistence")

    session.close()
    print("[OK] session and retry exercise complete")


if __name__ == "__main__":
    main()