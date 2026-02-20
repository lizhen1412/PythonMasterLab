#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11：代理配置。
Author: Lambert

题目：
实现一个函数，配置 HTTP/HTTPS 代理。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/11_proxy_config.py
"""

from __future__ import annotations

import requests
from typing import Any


def fetch_with_proxy(
    url: str,
    proxy_config: dict[str, str] | None = None,
    timeout: int = 10
) -> dict:
    """
    使用代理发起请求
    proxy_config 格式: {"http": "...", "https": "..."}
    """
    response = requests.get(
        url,
        proxies=proxy_config,
        timeout=timeout
    )
    response.raise_for_status()
    return response.json()


def get_env_proxies() -> dict[str, str]:
    """从环境变量获取代理配置"""
    import os
    proxies = {}
    if http_proxy := os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy"):
        proxies["http"] = http_proxy
    if https_proxy := os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy"):
        proxies["https"] = https_proxy
    return proxies


def main() -> None:
    # 不使用代理的请求
    url = "https://httpbin.org/ip"
    result = fetch_with_proxy(url)
    print(f"直接访问 IP: {result.get('origin')}")
    print("[OK] request without proxy")

    # 测试环境变量代理（如果有的话）
    env_proxies = get_env_proxies()
    if env_proxies:
        print(f"检测到环境变量代理: {env_proxies}")
        result = fetch_with_proxy(url, env_proxies)
        print(f"通过代理访问 IP: {result.get('origin')}")
        print("[OK] request with env proxy")
    else:
        print("未检测到环境变量代理，跳过代理测试")

    # 演示代理配置（不实际连接）
    proxy_config = {
        "http": "http://proxy.example.com:8080",
        "https": "https://proxy.example.com:8080",
    }
    print(f"\n代理配置示例: {proxy_config}")

    print("[OK] proxy configuration exercise complete")


if __name__ == "__main__":
    main()