#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 19：扩展认证方式（Digest Auth、Bearer Token、API Key）。
Author: Lambert

要点：
- Digest Auth：比 Basic 更安全的摘要认证
- Bearer Token：OAuth 2.0 常用的 Token 认证
- API Key：通过 Header 或 Query 参数传递 API 密钥
- 自定义 Header 认证

运行：
    python3 02_Frameworks/03_Requests/19_auth_extended.py
"""

from __future__ import annotations

import requests
from requests.auth import HTTPDigestAuth


def demo_digest_auth() -> None:
    """演示 Digest 认证"""
    resp = requests.get(
        "https://httpbin.org/digest-auth/auth/user/pass",
        auth=HTTPDigestAuth("user", "pass"),
        timeout=5,
    )
    print(f"Digest 认证（正确凭据）状态码 -> {resp.status_code}")
    print(f"Digest 认证返回 -> {resp.json()}")

    # 错误凭据
    bad_resp = requests.get(
        "https://httpbin.org/digest-auth/auth/user/pass",
        auth=HTTPDigestAuth("user", "wrong"),
        timeout=5,
    )
    print(f"Digest 认证（错误凭据）状态码 -> {bad_resp.status_code}")


def demo_bearer_token() -> None:
    """演示 Bearer Token 认证"""
    # Bearer Token 通常放在 Authorization Header 中
    token = "your_bearer_token_here"
    headers = {
        "Authorization": f"Bearer {token}",
    }

    resp = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=5,
    )
    print(f"\nBearer Token 状态码 -> {resp.status_code}")
    print(f"服务器看到的 Authorization 头 -> {resp.json()['headers']['Authorization']}")


def demo_api_key_header() -> None:
    """演示 API Key 通过 Header 传递"""
    # 方式1：使用 X-API-Key 头（常见）
    headers = {
        "X-API-Key": "sk-1234567890abcdef",
    }

    resp = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=5,
    )
    print(f"\nAPI Key (Header) 状态码 -> {resp.status_code}")
    print(f"服务器看到的 X-API-Key -> {resp.json()['headers'].get('X-API-Key')}")

    # 方式2：自定义 Header 名称
    headers_custom = {
        "Authorization": f"Apikey sk-1234567890abcdef",
    }
    resp_custom = requests.get(
        "https://httpbin.org/headers",
        headers=headers_custom,
        timeout=5,
    )
    print(f"自定义 Authorization -> {resp_custom.json()['headers']['Authorization']}")


def demo_api_key_query() -> None:
    """演示 API Key 通过 Query 参数传递"""
    api_key = "sk-1234567890abcdef"

    # 方式1：直接拼接到 URL（不推荐，易泄露）
    resp = requests.get(
        f"https://httpbin.org/get?api_key={api_key}",
        timeout=5,
    )
    print(f"\nAPI Key (Query - 直接拼接) 状态码 -> {resp.status_code}")
    print(f"URL 中的 api_key -> {resp.json()['args']}")

    # 方式2：使用 params 参数（推荐，自动编码）
    resp2 = requests.get(
        "https://httpbin.org/get",
        params={"api_key": api_key, "format": "json"},
        timeout=5,
    )
    print(f"API Key (Query - params) 状态码 -> {resp2.status_code}")
    print(f"URL 中的参数 -> {resp2.json()['args']}")


def demo_session_with_auth() -> None:
    """演示 Session 级别的认证配置"""
    session = requests.Session()

    # Session 级别设置默认认证头
    session.headers.update({
        "Authorization": "Bearer default_token_here",
        "X-API-Key": "default_api_key_here",
    })

    resp = session.get("https://httpbin.org/headers", timeout=5)
    print(f"\nSession 认证状态码 -> {resp.status_code}")
    print(f"Session 默认 Authorization -> {resp.json()['headers']['Authorization']}")
    print(f"Session 默认 X-API-Key -> {resp.json()['headers']['X-API-Key']}")


def demo_basic_auth_review() -> None:
    """回顾 Basic Auth（与 Digest 对比）"""
    from requests.auth import HTTPBasicAuth

    resp = requests.get(
        "https://httpbin.org/basic-auth/user/pass",
        auth=HTTPBasicAuth("user", "pass"),
        timeout=5,
    )
    print(f"\nBasic Auth 状态码 -> {resp.status_code}")

    # 简写方式
    resp2 = requests.get(
        "https://httpbin.org/basic-auth/user/pass",
        auth=("user", "pass"),
        timeout=5,
    )
    print(f"Basic Auth（简写）状态码 -> {resp2.status_code}")


def demo_auth_comparison() -> None:
    """对比不同认证方式"""
    print("\n=== 认证方式对比 ===")
    print("""
认证方式              | 安全性 | 使用场景
---------------------|--------|--------------------------
Basic Auth           | 低     | 简单场景，HTTPS 下使用
Digest Auth          | 中     | 比 Basic 安全，但不常用
Bearer Token (JWT)   | 高     | OAuth 2.0，现代 API
API Key (Header)     | 中     | 简单 API 密钥认证
API Key (Query)      | 低     | 不推荐（URL 易泄露）
客户端证书 (mTLS)    | 最高   | 金融、支付等高安全场景
    """)


def main() -> None:
    print("=== 扩展认证方式演示 ===\n")
    demo_digest_auth()
    demo_bearer_token()
    demo_api_key_header()
    demo_api_key_query()
    demo_session_with_auth()
    demo_basic_auth_review()
    demo_auth_comparison()

    print("\n使用建议：")
    print("  - 现代云 API 优先使用 Bearer Token (OAuth 2.0)")
    print("  - API Key 放在 Header 中，不要放在 URL 里")
    print("  - 生产环境使用 HTTPS")
    print("  - Token/密钥应通过环境变量或配置文件管理，不要硬编码")


if __name__ == "__main__":
    main()