#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：SSL 服务器上下文 - 创建 HTTPS 服务器。
Author: Lambert

本示例演示如何使用 ssl 模块创建 HTTPS 服务器：

1. **SSLContext(protocol)** - 创建自定义 SSL 上下文
2. **load_cert_chain()** - 加载服务器证书和私钥
3. **load_verify_locations()** - 加载 CA 证书（客户端认证）
4. **PROTOCOL_TLS_SERVER** - 服务器端 TLS 协议
5. **verify_mode** - 客户端证书验证模式
6. **check_hostname** - 主机名验证

前置条件：
- 需要生成自签名证书或使用真实证书
- 本示例使用自签名证书进行演示

证书生成（仅供参考，不自动执行）:
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
"""

from __future__ import annotations

import ssl
import socket
import threading
import time
from pathlib import Path
from typing import NoReturn


# =============================================================================
# 生成自签名证书（演示用）
# =============================================================================


def generate_self_signed_cert() -> tuple[bytes, bytes]:
    """生成自签名证书和私钥（演示用，实际应使用 openssl）。

    Returns:
        (cert_pem, key_pem): 证书和私钥的 PEM 格式
    """
    # 注意：这是演示用的伪证书，实际环境应使用 openssl 生成真实证书
    cert_pem = b"""-----BEGIN CERTIFICATE-----
MIIC9jCCAd4CCQD2rKXxBHxLjDANBgkqhkiG9w0BAQsFADA9MQswCQYDVQQGEwJV
UzELMAkGA1UECAwCQ0ExFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xDTALBgNVBAoM
BERlbW8wHhcNMjQwMTAxMDAwMDAwWhcNMjUwMTAxMDAwMDAwWjA9MQswCQYDVQQG
EwJVUzELMAkGA1UECAwCQ0ExFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xDTALBgNV
BAoMBERlbW8wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDNFPzH8ZK
-----END CERTIFICATE-----
"""

    key_pem = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDNFPzH8ZKH8QxN
-----END PRIVATE KEY-----
"""

    # 实际使用时应该：
    # 1. 使用 openssl 生成真实的证书和私钥
    # 2. 或者使用 let's encrypt 等服务获取证书
    # 3. 将证书保存到文件，在程序中加载

    return cert_pem, key_pem


def create_cert_files(temp_dir: Path) -> tuple[Path, Path]:
    """创建临时证书文件（用于演示）。

    在实际生产环境中，你应该：
    1. 使用 openssl 生成真实证书
    2. 或者从证书颁发机构获取证书
    3. 将证书和私钥安全地保存在文件中
    """
    cert_file = temp_dir / "cert.pem"
    key_file = temp_dir / "key.pem"

    # 创建临时目录
    temp_dir.mkdir(parents=True, exist_ok=True)

    # 生成自签名证书（简化版，仅用于演示）
    # 实际环境请使用：openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

    # 为了演示，创建假的证书文件
    # 真实场景需要有效的证书
    cert_file.write_text("# Demo certificate file\n# Use: openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes\n")
    key_file.write_text("# Demo key file\n")

    return cert_file, key_file


# =============================================================================
# SSLContext 基础
# =============================================================================


def demo_ssl_context_creation() -> None:
    """示例 01：创建不同类型的 SSLContext。"""
    print("== 创建 SSLContext ==\n")

    print("1. 创建默认上下文（客户端）:")
    client_ctx = ssl.create_default_context()
    print(f"   ssl.create_default_context()")
    print(f"   check_hostname: {client_ctx.check_hostname}")
    print(f"   verify_mode: {client_ctx.verify_mode}")
    print(f"   minimum_version: {client_ctx.minimum_version}")

    print("\n2. 创建服务器上下文:")
    server_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    print(f"   ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)")
    print(f"   check_hostname: {server_ctx.check_hostname}")
    print(f"   verify_mode: {server_ctx.verify_mode}")

    print("\n3. 创建客户端上下文:")
    client_ctx2 = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    print(f"   ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)")
    print(f"   check_hostname: {client_ctx2.check_hostname}")
    print(f"   verify_mode: {client_ctx2.verify_mode}")

    print("\n4. 旧式上下文（不推荐）:")
    old_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
    print(f"   ssl.SSLContext(ssl.PROTOCOL_TLS)")
    print(f"   需要手动设置 check_hostname 和 verify_mode")

    print("\n协议版本对比:")
    print(f"  PROTOCOL_TLS_CLIENT: 客户端专用，自动设置安全选项")
    print(f"  PROTOCOL_TLS_SERVER: 服务器专用，不验证客户端（默认）")
    print(f"  PROTOCOL_TLS:        通用协议，需手动配置")


def demo_context_options() -> None:
    """示例 02：配置 SSL 上下文选项。"""
    print("\n\n== 配置 SSL 上下文选项 ==\n")

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    print("1. 设置最低 TLS 版本:")
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    print(f"   minimum_version = TLSVersion.TLSv1_2")
    print(f"   当前值: {ctx.minimum_version}")

    print("\n2. 设置最高 TLS 版本:")
    ctx.maximum_version = ssl.TLSVersion.TLSv1_3
    print(f"   maximum_version = TLSVersion.TLSv1_3")
    print(f"   当前值: {ctx.maximum_version}")

    print("\n3. 设置密码套件:")
    # 设置只使用安全的密码套件
    ctx.set_ciphers('ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256')
    print(f"   set_ciphers(...)")
    print(f"   当前密码套件: {ctx.get_ciphers()[:2]}...")  # 只显示前两个

    print("\n4. 启用/禁用选项:")
    print(f"   默认选项: {ctx.options:#x}")
    # 可以使用 | 或 & 运算符修改选项
    # ctx.options |= ssl.OP_NO_SSLv2  # 禁用 SSLv2
    # ctx.options |= ssl.OP_NO_SSLv3  # 禁用 SSLv3
    # ctx.options |= ssl.OP_NO_TLSv1  # 禁用 TLSv1
    # ctx.options |= ssl.OP_NO_TLSv1_1  # 禁用 TLSv1.1


# =============================================================================
# 加载证书链
# =============================================================================


def demo_load_cert_chain() -> None:
    """示例 03：加载服务器证书链。"""
    print("\n\n== 加载服务器证书链 ==\n")

    # 创建服务器上下文
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    # 方法 1: 从文件加载（推荐用于生产）
    print("1. 从文件加载证书:")
    print("   ctx.load_cert_chain(certfile='server.crt', keyfile='server.key')")
    print("   # certfile: 服务器证书文件")
    print("   # keyfile: 私钥文件")
    print("   # password: 私钥密码（如果有的话）")

    # 方法 2: 加载证书链（中间证书）
    print("\n2. 加载证书链（包含中间证书）:")
    print("   ctx.load_cert_chain(certfile='server.crt', keyfile='server.key')")
    print("   # 如果 server.crt 包含完整证书链，会自动加载")
    print("   # 也可以将中间证书追加到服务器证书文件")

    # 演示创建临时文件
    temp_dir = Path("/tmp/ssl_demo")
    cert_file, key_file = create_cert_files(temp_dir)

    print(f"\n3. 临时演示文件:")
    print(f"   证书文件: {cert_file}")
    print(f"   私钥文件: {key_file}")

    # 注意：由于是演示文件，实际 load 会失败
    # 在真实环境中，这样使用：
    try:
        # ctx.load_cert_chain(str(cert_file), str(key_file))
        print("   # 证书加载成功（真实环境中）")
    except Exception as e:
        print(f"   # 证书加载失败（预期，演示文件）: {type(e).__name__}")

    print("\n4. 使用密码保护的私钥:")
    print("   ctx.load_cert_chain(certfile='server.crt', keyfile='server.key', password='secret')")


# =============================================================================
# 客户端证书验证
# =============================================================================


def demo_client_cert_verification() -> None:
    """示例 04：客户端证书验证（双向认证）。"""
    print("\n\n== 客户端证书验证（双向认证）==\n")

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    print("1. 启用客户端证书验证:")
    # 设置验证模式为要求客户端证书
    ctx.verify_mode = ssl.CERT_REQUIRED
    print(f"   ctx.verify_mode = ssl.CERT_REQUIRED")
    print(f"   验证模式: {ctx.verify_mode}")

    print("\n2. 加载 CA 证书（用于验证客户端）:")
    print("   ctx.load_verify_locations(cafile='ca.crt')")
    print("   # cafile: CA 证书文件")
    print("   # capath: CA 证书目录")
    print("   # cadata: PEM 编码的 CA 证书（字符串）")

    print("\n3. 验证模式对比:")
    print(f"   CERT_NONE:       {ssl.CERT_NONE} - 不验证客户端")
    print(f"   CERT_OPTIONAL:   {ssl.CERT_OPTIONAL} - 可选验证")
    print(f"   CERT_REQUIRED:   {ssl.CERT_REQUIRED} - 必须验证")

    print("\n4. 设置 CA 证书路径:")
    print("   方法 1: 指定 CA 文件")
    print("   ctx.load_verify_locations(cafile='/path/to/ca.crt')")
    print("\n   方法 2: 指定 CA 目录")
    print("   ctx.load_verify_locations(capath='/etc/ssl/certs')")
    print("\n   方法 3: 直接传入 CA 证书内容")
    print("   with open('ca.crt') as f:")
    print("       ctx.load_verify_locations(cadata=f.read())")


# =============================================================================
# HTTPS 服务器示例
# =============================================================================


def demo_https_server_basic() -> None:
    """示例 05：基础 HTTPS 服务器框架。"""
    print("\n\n== 基础 HTTPS 服务器框架 ==\n")

    print("注意：此示例展示 HTTPS 服务器的基本结构。")
    print("实际运行需要有效的证书文件。\n")

    print("第一步：生成自签名证书（使用命令行）:")
    print("  $ openssl req -x509 -newkey rsa:2048 -keyout key.pem \\")
    print("      -out cert.pem -days 365 -nodes")
    print("      # 或指定主题信息:")
    print("      -subj '/C=CN/ST=Beijing/L=Beijing/O=Demo/CN=localhost'")

    print("\n第二步：HTTPS 服务器代码结构:")
    print("""
    # https_server.py
    import ssl
    import socket
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class HTTPSRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Hello, HTTPS!</h1>')

    def main():
        # 创建 SSL 上下文
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

        # 创建 HTTP 服务器
        server = HTTPServer(('0.0.0.0', 4443), HTTPSRequestHandler)

        # 包装套接字为 SSL
        server.socket = context.wrap_socket(server.socket, server_side=True)

        print('HTTPS server running on https://localhost:4443')
        server.serve_forever()

    if __name__ == '__main__':
        main()
    """)

    print("\n第三步：运行服务器和测试:")
    print("  $ python3 https_server.py")
    print("  $ curl -k https://localhost:4443")
    print("  # 或浏览器访问: https://localhost:4443")

    print("\n提示：-k 参数表示跳过证书验证（仅用于自签名证书）")


def demo_https_server_custom() -> None:
    """示例 06：自定义 HTTPS 服务器。"""
    print("\n\n== 自定义 HTTPS 服务器 ==\n")

    print("完整 HTTPS 服务器示例:")
    print("""
    import ssl
    import socketserver
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class HTTPSRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, HTTPS!')

    class HTTPSServer(HTTPServer):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            self.context.load_cert_chain(certfile='server.crt', keyfile='server.key')

        def get_request(self):
            conn, addr = super().get_request()
            # 包装为 SSL 连接
            ssl_conn = self.context.wrap_socket(conn, server_side=True)
            return ssl_conn, addr

    # 启动服务器
    server = HTTPSServer(('0.0.0.0', 443), HTTPSRequestHandler)
    server.serve_forever()
    """)


# =============================================================================
# SSL 会话和性能
# =============================================================================


def demo_ssl_session_settings() -> None:
    """示例 07：SSL 会话和性能设置。"""
    print("\n\n== SSL 会话和性能设置 ==\n")

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    print("1. 会话复用（提高性能）:")
    print("   # 启用会话票据")
    print("   # 默认已启用，减少握手开销")

    print("\n2. 设置会话超时:")
    print("   # Python SSL 模块使用系统默认值")
    print("   # 可通过 OpenSSL 配置调整")

    print("\n3. 性能优化选项:")
    print("   # 设置合适的密码套件")
    ctx.set_ciphers('ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256')
    print("   # 使用 ECDHE 密码交换（前向保密）")
    print("   # 使用 AES-GCM（更快）")

    print("\n4. 检查会话统计:")
    print("   stats = ctx.session_stats()")
    print("   # 返回: {'accept': 0, 'accept_good': 0, 'accept_renegotiate': 0, ...}")


# =============================================================================
# 证书验证和主机名检查
# =============================================================================


def demo_hostname_verification() -> None:
    """示例 08：主机名验证。"""
    print("\n\n== 主机名验证 ==\n")

    print("1. 客户端主机名验证:")
    client_ctx = ssl.create_default_context()
    print(f"   默认: check_hostname = {client_ctx.check_hostname}")

    print("\n2. 禁用主机名验证（仅用于测试）:")
    client_ctx.check_hostname = False
    client_ctx.verify_mode = ssl.CERT_NONE
    print(f"   测试模式: check_hostname = {client_ctx.check_hostname}")
    print(f"   测试模式: verify_mode = {client_ctx.verify_mode}")

    print("\n3. 手动验证主机名:")
    print("   import ssl")
    print("   cert = sock.getpeercert()")
    print("   ssl.match_hostname(cert, 'example.com')")

    print("\n4. SNI (Server Name Indication):")
    print("   # 客户端发送 SNI")
    print("   context.wrap_socket(sock, server_hostname='example.com')")
    print("   # 服务器根据 SNI 选择证书")


# =============================================================================
# 完整示例：HTTPS 服务器
# =============================================================================


def demo_complete_https_example() -> None:
    """示例 09：完整的 HTTPS 服务器框架。"""
    print("\n\n== 完整 HTTPS 服务器框架 ==\n")

    print("""
    #!/usr/bin/env python3
    import ssl
    import socket
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class MyHTTPSHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Hello, HTTPS!</h1>')

    def create_https_context(certfile, keyfile):
        '''创建 HTTPS 服务器上下文'''
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

        # 加载证书和私钥
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)

        # 设置最低 TLS 版本
        context.minimum_version = ssl.TLSVersion.TLSv1_2

        # 设置安全的密码套件
        context.set_ciphers(
            'ECDHE-ECDSA-AES128-GCM-SHA256:'
            'ECDHE-RSA-AES128-GCM-SHA256:'
            'ECDHE-ECDSA-AES256-GCM-SHA384:'
            'ECDHE-RSA-AES256-GCM-SHA384'
        )

        return context

    def main():
        # 创建服务器
        server = HTTPServer(('0.0.0.0', 443), MyHTTPSHandler)

        # 创建 SSL 上下文
        context = create_https_context('server.crt', 'server.key')

        # 包装服务器套接字
        server.socket = context.wrap_socket(server.socket, server_side=True)

        print('HTTPS server running on https://localhost:443')
        server.serve_forever()

    if __name__ == '__main__':
        main()
    """)


# =============================================================================
# 最佳实践
# =============================================================================


def demo_ssl_best_practices() -> None:
    """示例 10：SSL/TLS 最佳实践。"""
    print("\n\n== SSL/TLS 最佳实践 ==\n")

    print("1. 证书管理:")
    print("   ✓ 使用受信任的 CA 签发的证书（生产环境）")
    print("   ✓ 定期更新证书（监控过期时间）")
    print("   ✓ 使用强密钥（RSA 2048+ 或 ECC 256+）")
    print("   ✓ 安全存储私钥（权限 600）")

    print("\n2. 协议配置:")
    print("   ✓ 使用 PROTOCOL_TLS_SERVER/CLIENT（Python 3.6+）")
    print("   ✓ 设置 minimum_version = TLSv1_2")
    print("   ✓ 禁用旧协议（SSLv3, TLSv1, TLSv1.1）")

    print("\n3. 密码套件:")
    print("   ✓ 优先使用 ECDHE（前向保密）")
    print("   ✓ 使用 AES-GCM 或 ChaCha20-Poly1305")
    print("   ✓ 避免不安全的套件（RC4, SHA1, DES 等）")

    print("\n4. 验证设置:")
    print("   ✓ 客户端：使用 create_default_context()")
    print("   ✓ 服务器：启用 CERT_REQUIRED（双向认证）")
    print("   ✓ 始终检查主机名（客户端）")

    print("\n5. 性能优化:")
    print("   ✓ 启用会话复用")
    print("   ✓ 使用 HTTP/2（减少连接数）")
    print("   ✓ 启用 OCSP Stapling")

    print("\n6. 测试:")
    print("   ✓ 使用 openssl s_client 测试连接")
    print("   ✓ 使用 SSL Labs 检查配置")
    print("   ✓ 定期检查漏洞（CVE）")


def main() -> None:
    """运行所有示例。"""
    demo_ssl_context_creation()
    demo_context_options()
    demo_load_cert_chain()
    demo_client_cert_verification()
    demo_https_server_basic()
    demo_https_server_custom()
    demo_ssl_session_settings()
    demo_hostname_verification()
    demo_complete_https_example()
    demo_ssl_best_practices()

    print("\n" + "="*60)
    print("SSL 服务器核心 API 速查")
    print("="*60)
    print("\n创建上下文:")
    print("  ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)")
    print("  ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)")
    print("\n加载证书:")
    print("  ctx.load_cert_chain(certfile, keyfile, password=None)")
    print("\n加载 CA 证书:")
    print("  ctx.load_verify_locations(cafile, capath, cadata)")
    print("\n验证模式:")
    print("  ctx.verify_mode = ssl.CERT_NONE / CERT_OPTIONAL / CERT_REQUIRED")
    print("\n协议版本:")
    print("  ctx.minimum_version = ssl.TLSVersion.TLSv1_2")
    print("  ctx.maximum_version = ssl.TLSVersion.TLSv1_3")
    print("\n密码套件:")
    print("  ctx.set_ciphers('cipher:list')")
    print("  ctx.get_ciphers()")
    print("\n包装套接字:")
    print("  secure_sock = ctx.wrap_socket(sock, server_side=True)")
    print("\n证书生成（命令行）:")
    print("  openssl req -x509 -newkey rsa:2048 -keyout key.pem \\\\ ")
    print("    -out cert.pem -days 365 -nodes")


if __name__ == "__main__":
    main()
