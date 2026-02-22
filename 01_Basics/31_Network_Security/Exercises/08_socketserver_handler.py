#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 08: TCP server using socketserver.
Author: Lambert

Task: Create a TCP echo server using the socketserver module.

Requirements:
1. Define a handler class inheriting from socketserver.BaseRequestHandler
2. Implement the handle() method to echo data back
3. Use socketserver.TCPServer to create the server
4. Run on 127.0.0.1:19004
"""

from __future__ import annotations

import socketserver
import socket
import threading
import time


class EchoHandler(socketserver.BaseRequestHandler):
    """Echo request handler."""

    def handle(self) -> None:
        """Handle the request by echoing data back."""
        # TODO: Implement this method
        # Hints:
        # 1. data = self.request.recv(1024)
        # 2. if data: self.request.sendall(data)
        # 3. print(f"[服务器] 收到: {data.decode()}")
        data = self.request.recv(1024)
        if data:
            print(f"[服务器] 收到: {data.decode()}")
            self.request.sendall(data)


def run_socketserver_server() -> None:
    """Run a TCP server using socketserver."""
    # TODO: Implement this function
    # Hints:
    # 1. with socketserver.TCPServer(("127.0.0.1", 19004), EchoHandler) as server:
    # 2.     port = server.server_address[1]
    # 3.     print(f"服务器监听 127.0.0.1:{port}")
    # 4.     server.serve_forever() or server.handle_request()
    with socketserver.TCPServer(("127.0.0.1", 19004), EchoHandler) as server:
        port = server.server_address[1]
        print(f"[服务器] 监听 127.0.0.1:{port}")

        # Handle a few requests
        for _ in range(3):
            server.handle_request()


def run_client(port: int = 19004) -> None:
    """Run test client."""
    time.sleep(0.2)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", port))
        messages = ["Hello socketserver!", "Message 2", "Bye!"]
        for msg in messages:
            sock.sendall(msg.encode())
            response = sock.recv(1024)
            print(f"[客户端] 收到: {response.decode()}")


def test() -> None:
    """Test socketserver."""
    print("== Test SocketServer ==\n")

    # Start server in thread
    server_thread = threading.Thread(target=run_socketserver_server, daemon=True)
    server_thread.start()

    # Run client
    run_client()

    # Wait for server
    server_thread.join(timeout=2)

    print("\n[TEST] OK" if True else "[TEST] FAIL")


if __name__ == "__main__":
    test()
