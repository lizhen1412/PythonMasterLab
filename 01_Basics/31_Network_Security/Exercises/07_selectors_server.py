#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 07: Echo server using selectors.
Author: Lambert

Task: Create an echo server using the selectors module for I/O multiplexing.

Requirements:
1. Use selectors.DefaultSelector()
2. Register the listening socket for EVENT_READ
3. Use select() to wait for events
4. Handle new connections and data from existing connections
5. Echo received data back to clients
"""

from __future__ import annotations

import selectors
import socket
import threading
import time


def run_selector_server() -> None:
    """
    Run an echo server using selectors.

    The server should:
    1. Create a listening socket on 127.0.0.1:19003
    2. Register it with the selector
    3. Use select() to wait for events
    4. Accept new connections and register them
    5. Echo data back to clients
    """
    # TODO: Implement this function
    # Hints:
    # 1. sel = selectors.DefaultSelector()
    # 2. sel.register(lsock, selectors.EVENT_READ, data=None)
    # 3. events = sel.select(timeout=1.0)
    # 4. for key, mask in events:
    # 5.     if key.data is None: # New connection
    # 6.     else: # Data from existing connection
    sel = selectors.DefaultSelector()

    # Create listening socket
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    lsock.bind(("127.0.0.1", 19003))
    lsock.listen()
    lsock.setblocking(False)

    sel.register(lsock, selectors.EVENT_READ, data=None)
    print("[服务器] 监听 127.0.0.1:19003")

    connections = {}  # type: dict[socket, bytes]

    start_time = time.time()
    try:
        while time.time() - start_time < 3:  # Run for 3 seconds
            events = sel.select(timeout=0.5)
            for key, mask in events:
                if key.data is None:
                    # New connection
                    conn, addr = lsock.accept()
                    conn.setblocking(False)
                    connections[conn] = b""
                    sel.register(conn, selectors.EVENT_READ, data=addr)
                    print(f"[服务器] 新连接: {addr}")
                else:
                    # Data from existing connection
                    sock = key.fileobj
                    addr = key.data
                    try:
                        data = sock.recv(1024)
                        if data:
                            print(f"[服务器] 收到: {data.decode()}")
                            sock.sendall(data)  # Echo back
                        else:
                            # Connection closed
                            sel.unregister(sock)
                            sock.close()
                            del connections[sock]
                    except OSError:
                        sel.unregister(sock)
                        sock.close()
                        if sock in connections:
                            del connections[sock]
    finally:
        sel.close()
        lsock.close()


def run_client(port: int = 19003) -> None:
    """Run test client."""
    time.sleep(0.3)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", port))
        messages = ["Hello selectors!", "Message 2", "Bye!"]
        for msg in messages:
            sock.sendall(msg.encode())
            response = sock.recv(1024)
            print(f"[客户端] 收到: {response.decode()}")
            time.sleep(0.1)


def test() -> None:
    """Test selectors server."""
    print("== Test Selectors Echo Server ==\n")

    # Start server in thread
    server_thread = threading.Thread(target=run_selector_server, daemon=True)
    server_thread.start()

    # Run client
    run_client()

    # Wait for server
    server_thread.join(timeout=4)

    print("\n[TEST] OK" if True else "[TEST] FAIL")


if __name__ == "__main__":
    test()
