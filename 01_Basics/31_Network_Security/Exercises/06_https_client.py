#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 06: HTTPS client with SSL.
Author: Lambert

Task: Create a simple HTTPS client that connects to www.example.com and
retrieves the homepage.

Requirements:
1. Create a socket and connect to www.example.com:443
2. Create an SSL context with ssl.create_default_context()
3. Wrap the socket with SSL
4. Send a simple HTTP GET request
5. Receive and print the response status line
"""

from __future__ import annotations

import socket
import ssl


def fetch_https() -> str:
    """
    Fetch www.example.com using HTTPS.

    Returns:
        The HTTP status line from the response.
    """
    # TODO: Implement this function
    # Hints:
    # 1. Create socket: socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. Create SSL context: ssl.create_default_context()
    # 3. Wrap socket: context.wrap_socket(sock, server_hostname="www.example.com")
    # 4. Connect: ssl_sock.connect(("www.example.com", 443))
    # 5. Send request: ssl_sock.sendall(b"GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n")
    # 6. Receive response: ssl_sock.recv(4096)
    # 7. Parse and return status line

    host = "www.example.com"
    port = 443

    # Create socket and SSL context
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context()

    try:
        # Wrap socket with SSL and connect
        ssl_sock = context.wrap_socket(sock, server_hostname=host)
        ssl_sock.connect((host, port))

        # Send HTTP request
        request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        ssl_sock.sendall(request.encode())

        # Receive response
        response = b""
        while True:
            data = ssl_sock.recv(4096)
            if not data:
                break
            response += data

        # Extract status line
        status_line = response.split(b"\r\n")[0].decode()
        return status_line

    finally:
        sock.close()


def test() -> None:
    """Test HTTPS client."""
    print("== Test HTTPS Client ==\n")

    try:
        status = fetch_https()
        print(f"Status: {status}")

        if "200" in status or "HTTP" in status:
            print("\n[TEST] OK")
        else:
            print("\n[TEST] FAIL: Unexpected status")
    except Exception as e:
        print(f"\n[TEST] FAIL: {e}")


if __name__ == "__main__":
    test()
