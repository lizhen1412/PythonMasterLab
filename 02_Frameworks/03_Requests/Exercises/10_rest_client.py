#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：REST API 客户端。
Author: Lambert

题目：
实现一个简单的 REST API 客户端，支持 GET/POST/PUT/DELETE。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/10_rest_client.py
"""

from __future__ import annotations

import requests
from typing import Any


class RESTClient:
    """简单的 REST API 客户端"""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, endpoint: str, params: dict | None = None) -> dict:
        """GET 请求"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict | None = None) -> dict:
        """POST JSON 数据"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict | None = None) -> dict:
        """PUT JSON 数据"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=data, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> dict:
        """DELETE 请求"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        """关闭 Session"""
        self.session.close()


def main() -> None:
    client = RESTClient("https://httpbin.org")

    # GET 测试
    result = client.get("/get", params={"foo": "bar"})
    assert result["args"]["foo"] == "bar"
    print("[OK] GET request")

    # POST 测试
    result = client.post("/post", data={"name": "alice"})
    assert result["json"]["name"] == "alice"
    print("[OK] POST request")

    # PUT 测试
    result = client.put("/put", data={"key": "value"})
    assert result["json"]["key"] == "value"
    print("[OK] PUT request")

    # DELETE 测试
    result = client.delete("/delete")
    assert result["data"] == ""
    print("[OK] DELETE request")

    client.close()
    print("[OK] REST client exercise complete")


if __name__ == "__main__":
    main()