#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：错误处理和状态码检查。
Author: Lambert

题目：
实现一个函数，处理各种 HTTP 错误（404, 500, 超时等）。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/05_error_handling.py
"""

from __future__ import annotations

import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError


def safe_get(url: str, timeout: int = 10) -> dict | None:
    """
    安全的 GET 请求，处理各种错误
    返回 JSON 数据或 None（如果出错）
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Timeout:
        print(f"[ERROR] Timeout accessing {url}")
        return None
    except ConnectionError:
        print(f"[ERROR] Connection error accessing {url}")
        return None
    except HTTPError as e:
        print(f"[ERROR] HTTP error: {e.response.status_code}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return None


def main() -> None:
    # 测试成功请求
    result = safe_get("https://httpbin.org/get")
    assert result is not None
    print("[OK] successful request")

    # 测试 404
    result = safe_get("https://httpbin.org/status/404")
    assert result is None
    print("[OK] 404 error handled")

    # 测试超时（使用很小的延迟模拟）
    result = safe_get("https://httpbin.org/delay/10", timeout=1)
    assert result is None
    print("[OK] timeout handled")

    print("[OK] error handling exercise complete")


if __name__ == "__main__":
    main()