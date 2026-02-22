#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 10: socketserver - Socket servers.
Author: Lambert

- socketserver.TCPServer and UDPServer
- BaseRequestHandler for handling requests
- ThreadingMixIn and ForkingMixIn for concurrency
- StreamRequestHandler for easier I/O
- Building echo servers with different patterns
"""

from __future__ import annotations

import socketserver
import socket
import threading
import time
from typing import ClassVar


def demo_tcp_server() -> None:
    """Demonstrate a basic TCP echo server using socketserver."""
    print("== TCP Echo Server (socketserver) ==\n")

    class EchoHandler(socketserver.BaseRequestHandler):
        """Handler for echo requests."""

        def handle(self) -> None:
            """Handle one request."""
            data = self.request.recv(1024)
            print(f"[Server] Received from {self.client_address}: {data.decode()}")
            self.request.sendall(data)  # Echo back

    # Create and start server
    with socketserver.TCPServer(("127.0.0.1", 18906), EchoHandler) as server:
        port = server.server_address[1]
        print(f"Server listening on 127.0.0.1:{port}")

        # Start client in thread
        def run_client():
            time.sleep(0.1)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect(("127.0.0.1", port))
                messages = ["Hello!", "World!", "Bye!"]
                for msg in messages:
                    client.sendall(msg.encode())
                    response = client.recv(1024)
                    print(f"[Client] Received: {response.decode()}")

        client_thread = threading.Thread(target=run_client, daemon=True)
        client_thread.start()

        # Handle one request
        server.handle_request()  # Handle one connection then exit

        client_thread.join(timeout=1)

    print("[Server] Server stopped")


def demo_udp_server() -> None:
    """Demonstrate a UDP echo server using socketserver."""
    print("\n== UDP Echo Server (socketserver) ==\n")

    class UDPEchoHandler(socketserver.BaseRequestHandler):
        """Handler for UDP echo requests."""

        def handle(self) -> None:
            """Handle one UDP request."""
            data, socket = self.request  # type: ignore[misc]
            print(f"[Server] Received from {self.client_address}: {data.decode()}")
            socket.sendto(data, self.client_address)

    # Create and start UDP server
    with socketserver.UDPServer(("127.0.0.1", 18907), UDPEchoHandler) as server:
        port = server.server_address[1]
        print(f"Server listening on 127.0.0.1:{port}")

        # Start client in thread
        def run_client():
            time.sleep(0.1)
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
                messages = ["UDP Hello!", "UDP World!", "UDP Bye!"]
                for msg in messages:
                    client.sendto(msg.encode(), ("127.0.0.1", port))
                    response, _ = client.recvfrom(1024)
                    print(f"[Client] Received: {response.decode()}")
                    time.sleep(0.05)

        client_thread = threading.Thread(target=run_client, daemon=True)
        client_thread.start()

        # Handle requests
        for _ in range(3):
            server.handle_request()

        client_thread.join(timeout=1)

    print("[Server] Server stopped")


def demo_threading_server() -> None:
    """Demonstrate a threaded TCP server."""
    print("\n== Threading TCP Server ==\n")

    class ThreadedEchoHandler(socketserver.BaseRequestHandler):
        """Handler for threaded echo requests."""

        def handle(self) -> None:
            """Handle one request."""
            thread_id = threading.get_ident()
            data = self.request.recv(1024)
            print(f"[Server-{thread_id}] Received: {data.decode()}")
            self.request.sendall(data)

    # ThreadedMixIn allows handling multiple clients concurrently
    class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        """TCP server with threading support."""
        daemon_threads: ClassVar[bool] = True

    with ThreadedTCPServer(("127.0.0.1", 18908), ThreadedEchoHandler) as server:
        port = server.server_address[1]
        print(f"Server listening on 127.0.0.1:{port}")

        # Start multiple clients
        def run_client(client_id: int) -> None:
            time.sleep(0.1)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect(("127.0.0.1", port))
                for i in range(2):
                    msg = f"Client-{client_id} Message-{i}"
                    client.sendall(msg.encode())
                    response = client.recv(1024)
                    print(f"[Client-{client_id}] Received: {response.decode()}")
                    time.sleep(0.05)

        threads = []
        for i in range(3):
            t = threading.Thread(target=run_client, args=(i,), daemon=True)
            t.start()
            threads.append(t)

        # Handle all requests
        for _ in range(6):  # 3 clients x 2 messages
            server.handle_request()

        for t in threads:
            t.join(timeout=1)

    print("[Server] Server stopped")


def demo_stream_handler() -> None:
    """Demonstrate StreamRequestHandler for easier I/O."""
    print("\n== StreamRequestHandler Example ==\n")

    class EchoHandler(socketserver.StreamRequestHandler):
        """Handler using stream I/O."""

        def handle(self) -> None:
            """Handle request using file-like objects."""
            # self.rfile and self.wfile are file-like objects
            print(f"[Server] Connection from {self.client_address}")

            while True:
                # Read a line (like reading from a file)
                line = self.rfile.readline()
                if not line:
                    break

                print(f"[Server] Received: {line.decode().strip()}")
                # Write response
                self.wfile.write(line)

    with socketserver.TCPServer(("127.0.0.1", 18909), EchoHandler) as server:
        port = server.server_address[1]
        print(f"Server listening on 127.0.0.1:{port}")

        def run_client():
            time.sleep(0.1)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect(("127.0.0.1", port))
                messages = ["Line 1\n", "Line 2\n", "Line 3\n"]
                for msg in messages:
                    client.sendall(msg.encode())
                    response = client.recv(1024)
                    print(f"[Client] Received: {response.decode().strip()}")

        client_thread = threading.Thread(target=run_client, daemon=True)
        client_thread.start()

        for _ in range(3):
            server.handle_request()

        client_thread.join(timeout=1)

    print("[Server] Server stopped")


def demo_server_customization() -> None:
    """Demonstrate server customization options."""
    print("\n== Server Customization ==\n")

    class CustomServer(socketserver.TCPServer):
        """Custom server with specific settings."""

        # Server configuration
        allow_reuse_address: ClassVar[bool] = True
        timeout: ClassVar[int] = 1

        def server_bind(self) -> None:
            """Custom bind behavior."""
            print("[Server] Custom binding...")
            super().server_bind()

        def get_request(self) -> tuple[object, str]:
            """Custom request handling."""
            request, client_address = super().get_request()
            print(f"[Server] Connection from {client_address}")
            return request, client_address

    class CustomHandler(socketserver.BaseRequestHandler):
        """Custom handler."""

        def setup(self) -> None:
            """Called before handle()."""
            print(f"[Handler] Setting up for {self.client_address}")
            super().setup()

        def handle(self) -> None:
            """Handle the request."""
            data = self.request.recv(1024)
            print(f"[Handler] Handling: {data.decode()}")
            self.request.sendall(data)

        def finish(self) -> None:
            """Called after handle()."""
            print(f"[Handler] Finishing for {self.client_address}")
            super().finish()

    with CustomServer(("127.0.0.1", 18910), CustomHandler) as server:
        port = server.server_address[1]
        print(f"Custom server on 127.0.0.1:{port}")

        def run_client():
            time.sleep(0.1)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect(("127.0.0.1", port))
                client.sendall(b"Test message")
                response = client.recv(1024)
                print(f"[Client] Received: {response.decode()}")

        client_thread = threading.Thread(target=run_client, daemon=True)
        client_thread.start()

        server.handle_request()
        client_thread.join(timeout=1)

    print("[Server] Server stopped")


def main() -> None:
    demo_tcp_server()
    demo_udp_server()
    demo_threading_server()
    demo_stream_handler()
    demo_server_customization()

    print("\n== socketserver Mixin Classes ==\n")
    print("Mixin               | Concurrency Model | Platform")
    print("---------------------|-------------------|----------")
    print("ThreadingMixIn      | Thread-based      | All")
    print("ForkingMixIn        | Process-based     | Unix only")
    print("ThreadingUDPServer  | Thread-based UDP  | All")
    print("ForkingUDPServer    | Process-based UDP | Unix only")
    print("\nRecommendation: Use ThreadingMixIn for cross-platform concurrency.")


if __name__ == "__main__":
    main()
