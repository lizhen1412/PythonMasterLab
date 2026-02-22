#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 08: SSL wrapped sockets.
Author: Lambert

- Creating SSL context with custom settings
- Wrapping a socket with SSL
- SSL certificate verification modes
- Creating a simple HTTPS client
"""

from __future__ import annotations

import socket
import ssl
from typing import Tuple


def demo_ssl_context_modes() -> None:
    """Demonstrate different SSL context verification modes."""
    print("== SSL Context Verification Modes ==\n")

    # Default context (with certificate verification)
    default_ctx = ssl.create_default_context()
    print("1. Default Context:")
    print(f"   check_hostname: {default_ctx.check_hostname}")
    print(f"   verify_mode: {default_ctx.verify_mode}")
    print(f"   CERT_REQUIRED: {ssl.CERT_REQUIRED}")

    # Unverified context (for testing)
    unverified_ctx = ssl.create_default_context()
    unverified_ctx.check_hostname = False
    unverified_ctx.verify_mode = ssl.CERT_NONE
    print("\n2. Unverified Context (for testing):")
    print(f"   check_hostname: {unverified_ctx.check_hostname}")
    print(f"   verify_mode: {unverified_ctx.verify_mode}")
    print(f"   CERT_NONE: {ssl.CERT_NONE}")

    # Optional context
    optional_ctx = ssl.create_default_context()
    optional_ctx.check_hostname = False
    optional_ctx.verify_mode = ssl.CERT_OPTIONAL
    print("\n3. Optional Context:")
    print(f"   check_hostname: {optional_ctx.check_hostname}")
    print(f"   verify_mode: {optional_ctx.verify_mode}")
    print(f"   CERT_OPTIONAL: {ssl.CERT_OPTIONAL}")


def demo_ssl_wrap_socket() -> None:
    """Demonstrate wrapping a socket with SSL."""
    print("\n== SSL Socket Wrapping ==\n")

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5.0)

    # Wrap with SSL
    context = ssl.create_default_context()
    ssl_sock = context.wrap_socket(sock, server_hostname="www.example.com")

    print("1. Wrapped socket attributes:")
    print(f"   Socket type: {ssl_sock.type}")
    print(f"   Cipher: {ssl_sock.cipher()}")
    print(f"   Version: {ssl_sock.version()}")

    # Connect using SSL socket
    print("\n2. Connecting to www.example.com:443...")
    try:
        ssl_sock.connect(("www.example.com", 443))
        print(f"   Connected!")
        print(f"   Peer certificate: {ssl_sock.getpeercert()}")
        print(f"   Server hostname: {ssl_sock.server_hostname}")
    except (socket.timeout, ConnectionError, ssl.SSLError) as e:
        print(f"   Connection failed: {e}")
    finally:
        ssl_sock.close()


def demo_https_client() -> None:
    """Demonstrate a simple HTTPS client."""
    print("\n== Simple HTTPS Client ==\n")

    host = "www.example.com"
    port = 443
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

    # Create SSL context
    context = ssl.create_default_context()

    # Create socket, wrap with SSL, connect
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssl_sock:
            # Send HTTP request
            ssl_sock.sendall(request.encode())
            print("1. Sent HTTP request")

            # Receive response
            response = b""
            while True:
                data = ssl_sock.recv(4096)
                if not data:
                    break
                response += data

            # Parse response
            headers, _, body = response.partition(b"\r\n\r\n")
            print("2. Received response:")
            status_line = headers.split(b'\r\n')[0].decode()
            print(f"   Status line: {status_line}")
            print(f"   Total bytes: {len(response)}")


def demo_ssl_socket_methods() -> None:
    """Demonstrate SSL socket specific methods."""
    print("\n== SSL Socket Specific Methods ==\n")

    context = ssl.create_default_context()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with context.wrap_socket(sock, server_hostname="www.example.com") as ssl_sock:
            try:
                ssl_sock.connect(("www.example.com", 443))

                print("1. SSL session info:")
                print(f"   Cipher: {ssl_sock.cipher()}")
                print(f"   TLS version: {ssl_sock.version()}")
                print(f"   Server hostname: {ssl_sock.server_hostname}")

                print("\n2. Certificate info:")
                cert = ssl_sock.getpeercert()
                if cert:
                    print(f"   Subject: {cert.get('subject')}")
                    print(f"   Issuer: {cert.get('issuer')}")
                    print(f"   Not after: {cert.get('notAfter')}")

                print("\n3. PEM encoded certificate:")
                pem_cert = ssl_sock.getpeercert(binary_form=True)
                if pem_cert:
                    # Show first few lines
                    pem_str = ssl.DER_cert_to_PEM_cert(pem_cert)
                    lines = pem_str.split('\n')[:5]
                    print("   " + "\n   ".join(lines))

            except (socket.timeout, ConnectionError, ssl.SSLError) as e:
                print(f"   Connection failed: {e}")


def main() -> None:
    demo_ssl_context_modes()
    demo_ssl_wrap_socket()
    demo_https_client()
    demo_ssl_socket_methods()

    print("\n== SSL Security Best Practices ==\n")
    print("- Always use verify_mode=CERT_REQUIRED for production")
    print("- Use create_default_context() for secure defaults")
    print("- Check hostname to prevent MITM attacks")
    print("- Keep certificates updated")
    print("- Consider certificate pinning for high-security apps")


if __name__ == "__main__":
    main()
