#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：代理（Proxies）配置。

要点：
- 使用 proxies 参数设置 HTTP/HTTPS 代理
- 支持带认证的代理（user:pass@host:port）
- 可通过环境变量 HTTP_PROXY/HTTPS_PROXY 设置全局代理
- 企业网络、爬虫场景常用

注意：
- 本示例演示代理配置语法，实际运行需要有效的代理服务器
- httpbin.org/ip 用于查看请求来源 IP

运行：
    python3 02_Frameworks/03_Requests/17_proxies.py
"""

from __future__ import annotations

import requests


def demo_proxy_config() -> None:
    """演示代理配置语法"""
    # 基本代理配置（需要替换为实际可用的代理地址）
    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }

    print("代理配置示例：")
    print(f"  HTTP 代理 -> {proxies['http']}")
    print(f"  HTTPS 代理 -> {proxies['https']}")

    # 实际请求（注释掉，因为没有真实代理）
    # resp = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=5)
    # print(f"通过代理的请求 IP -> {resp.json()['origin']}")


def demo_proxy_with_auth() -> None:
    """演示带认证的代理"""
    # 代理需要用户名密码认证
    proxies = {
        "http": "http://user:pass@10.10.1.10:3128",
        "https": "http://user:pass@10.10.1.10:1080",
    }

    print("\n带认证的代理配置示例：")
    print(f"  HTTP 代理 -> {proxies['http']}")
    print(f"  HTTPS 代理 -> {proxies['https']}")

    # 实际请求（注释掉，因为没有真实代理）
    # resp = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=5)


def demo_proxy_with_session() -> None:
    """演示 Session 级别的代理配置"""
    session = requests.Session()

    # Session 设置默认代理
    session.proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }

    print("\nSession 代理配置示例：")
    print(f"  Session 默认代理 -> {session.proxies}")

    # 所有通过该 Session 的请求都会使用代理
    # resp = session.get("https://httpbin.org/ip", timeout=5)


def demo_no_proxy() -> None:
    """演示不使用代理的情况"""
    # 显式设置不使用代理
    resp = requests.get("https://httpbin.org/ip", timeout=5)
    print(f"\n不使用代理的请求 IP -> {resp.json()['origin']}")


def demo_environment_variables() -> None:
    """演示通过环境变量设置代理"""
    import os

    print("\n环境变量代理配置：")
    print(f"  HTTP_PROXY -> {os.environ.get('HTTP_PROXY', '未设置')}")
    print(f"  HTTPS_PROXY -> {os.environ.get('HTTPS_PROXY', '未设置')}")
    print(f"  NO_PROXY -> {os.environ.get('NO_PROXY', '未设置')}")

    # 设置环境变量后，requests 会自动使用
    # export HTTP_PROXY=http://10.10.1.10:3128
    # export HTTPS_PROXY=http://10.10.1.10:1080


def main() -> None:
    print("=== 代理配置演示 ===\n")
    demo_proxy_config()
    demo_proxy_with_auth()
    demo_proxy_with_session()
    demo_no_proxy()
    demo_environment_variables()

    print("\n注意：")
    print("  - 本示例仅展示代理配置语法")
    print("  - 实际使用需要有效的代理服务器地址")
    print("  - 企业网络可联系网络管理员获取代理地址")
    print("  - 常见代理软件：Clash、V2Ray、TinyProxy、Squid")


if __name__ == "__main__":
    main()
