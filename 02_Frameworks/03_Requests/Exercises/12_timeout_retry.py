#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 12：超时和重试进阶。
Author: Lambert

题目：
实现一个函数，支持连接超时、读取超时和智能重试。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/12_timeout_retry.py
"""

from __future__ import annotations

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Any


class SmartHTTPClient:
    """支持超时和重试的 HTTP 客户端"""

    def __init__(
        self,
        connect_timeout: int = 5,
        read_timeout: int = 30,
        max_retries: int = 3,
        backoff_factor: float = 0.5
    ):
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.session = requests.Session()

        # 配置重试策略
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE", "POST"],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get(self, url: str, **kwargs: Any) -> requests.Response:
        """GET 请求，带超时"""
        timeout = (self.connect_timeout, self.read_timeout)
        kwargs.setdefault("timeout", timeout)
        response = self.session.get(url, **kwargs)
        response.raise_for_status()
        return response

    def post(self, url: str, **kwargs: Any) -> requests.Response:
        """POST 请求，带超时"""
        timeout = (self.connect_timeout, self.read_timeout)
        kwargs.setdefault("timeout", timeout)
        response = self.session.post(url, **kwargs)
        response.raise_for_status()
        return response

    def close(self) -> None:
        """关闭 Session"""
        self.session.close()


def main() -> None:
    # 创建客户端
    client = SmartHTTPClient(connect_timeout=3, read_timeout=10, max_retries=2)

    # 测试正常请求
    response = client.get("https://httpbin.org/get")
    assert response.status_code == 200
    print("[OK] normal request")

    # 测试连接超时（使用无效地址）
    try:
        client.get("http://10.255.255.1/", timeout=1)
    except requests.exceptions.ConnectTimeout:
        print("[OK] connect timeout handled")
    except requests.exceptions.Timeout:
        print("[OK] timeout handled")
    except Exception as e:
        print(f"[INFO] Other exception (expected): {type(e).__name__}")

    # 测试读取超时
    try:
        # httpbin 的 delay endpoint 会延迟响应
        client.get("https://httpbin.org/delay/10")
    except requests.exceptions.ReadTimeout:
        print("[OK] read timeout handled")
    except requests.exceptions.Timeout:
        print("[OK] timeout handled")

    client.close()
    print("[OK] timeout and retry exercise complete")


if __name__ == "__main__":
    main()