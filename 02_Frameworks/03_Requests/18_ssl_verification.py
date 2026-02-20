#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 18：SSL/TLS 证书验证控制。
Author: Lambert

要点：
- verify=True（默认）：验证 SSL 证书，推荐生产环境使用
- verify=False：关闭验证，仅测试环境使用（会报 InsecureRequestWarning）
- verify 指定自定义 CA bundle 证书文件路径
- cert 参数：客户端证书（.pem 或 .cert + .key 组合）

注意：
- 关闭证书验证会带来安全风险（中间人攻击）
- 使用 verify=False 时需要禁用警告

运行：
    python3 02_Frameworks/03_Requests/18_ssl_verification.py
"""

from __future__ import annotations

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def demo_default_verification() -> None:
    """演示默认的证书验证行为"""
    resp = requests.get("https://httpbin.org/get", timeout=5)
    print(f"默认验证状态码 -> {resp.status_code}")
    print(f"验证有效证书 -> {resp.ok}")


def demo_disable_verification() -> None:
    """演示关闭证书验证（不推荐！）"""
    import warnings

    # 禁用 InsecureRequestWarning 警告
    warnings.filterwarnings("ignore", category=InsecureRequestWarning)

    resp = requests.get("https://httpbin.org/get", verify=False, timeout=5)
    print(f"\n关闭验证状态码 -> {resp.status_code}")
    print("警告：关闭证书验证会导致安全风险！")


def demo_custom_ca_bundle() -> None:
    """演示使用自定义 CA bundle"""
    # 指定自定义 CA 证书文件
    # ca_bundle_path = "/path/to/custom-ca-bundle.pem"
    # resp = requests.get("https://example.com", verify=ca_bundle_path, timeout=5)

    print("\n自定义 CA bundle 示例：")
    print("  verify = '/path/to/custom-ca-bundle.pem'")
    print("  resp = requests.get('https://example.com', verify=ca_bundle_path)")
    print("\n使用场景：")
    print("  - 企业内部自签名证书")
    print("  - 特定 CA 颁发的证书")


def demo_client_certificate() -> None:
    """演示客户端证书认证"""
    # 方式1：单个文件包含证书和私钥
    # cert = "/path/to/client.pem"

    # 方式2：证书和私钥分开
    # cert = ("/path/to/client.cert", "/path/to/client.key")

    print("\n客户端证书认证示例：")
    print("  # 单文件格式（.pem）")
    print("  cert = '/path/to/client.pem'")
    print("  resp = requests.get('https://example.com', cert=cert)")
    print("\n  # 证书+私钥分开")
    print("  cert = ('/path/to/client.cert', '/path/to/client.key')")
    print("  resp = requests.get('https://example.com', cert=cert)")
    print("\n使用场景：")
    print("  - 双向 TLS 认证（mTLS）")
    print("  - 金融、支付等高安全场景")


def demo_session_ssl_config() -> None:
    """演示 Session 级别的 SSL 配置"""
    session = requests.Session()

    # Session 级别关闭验证（仅示例）
    # session.verify = False

    # Session 级别指定 CA bundle
    # session.verify = "/path/to/ca-bundle.pem"

    # Session 级别设置客户端证书
    # session.cert = ("/path/to/client.cert", "/path/to/client.key")

    print("\nSession SSL 配置示例：")
    print("  session = requests.Session()")
    print("  session.verify = '/path/to/ca-bundle.pem'")
    print("  session.cert = ('/path/to/client.cert', '/path/to/client.key')")


def demo_get_cert_info() -> None:
    """演示获取服务器的证书信息"""
    resp = requests.get("https://httpbin.org/get", timeout=5)

    print("\n服务器证书信息：")
    print(f"  URL -> {resp.url}")
    print(f"  是否 HTTPS -> {resp.url.startswith('https')}")

    # 获取原始连接的证书信息（需要访问底层 socket）
    if hasattr(resp.raw, "_connection"):
        try:
            import ssl

            # 注意：这部分实现较复杂，需要访问底层连接
            print("  证书详细信息 -> 需要访问底层连接（略）")
        except Exception:
            pass


def main() -> None:
    print("=== SSL/TLS 证书验证演示 ===\n")
    demo_default_verification()
    demo_disable_verification()
    demo_custom_ca_bundle()
    demo_client_certificate()
    demo_session_ssl_config()
    demo_get_cert_info()

    print("\n安全提示：")
    print("  - 生产环境务必使用 verify=True")
    print("  - 关闭验证仅用于测试/开发环境")
    print("  - 自签名证书应配置正确的 CA bundle")
    print("  - 客户端证书需妥善保管私钥文件")


if __name__ == "__main__":
    main()