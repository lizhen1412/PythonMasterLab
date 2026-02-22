#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 09: selectors - High-level I/O multiplexing.
Author: Lambert

- selectors.BaseSelector and DefaultSelector
- Registering file descriptors for monitoring
- select() for waiting for events
- Building an echo server with selectors
- Cross-platform abstraction (select/poll/epoll/kqueue)
"""

from __future__ import annotations

import selectors
import socket
import threading
import time
from typing import NoReturn


def demo_selector_types() -> None:
    """Demonstrate different selector types."""
    print("== Selector Types ==\n")

    # Get the default selector for the platform
    sel = selectors.DefaultSelector()
    print(f"1. Default selector: {type(sel).__name__}")

    # Check available selector types
    print("\n2. Available selector types:")
    selector_names = [
        "SelectSelector",
        "PollSelector",
        "EpollSelector",
        "KqueueSelector",
        "DevpollSelector",
    ]

    for name in selector_names:
        if hasattr(selectors, name):
            print(f"   {name}: Available on this platform")
        else:
            print(f"   {name}: Not available on this platform")

    print("\n3. Platform-specific optimal selector:")
    if hasattr(selectors, 'EpollSelector'):
        print("   Linux: epoll (best performance, unlimited FDs)")
    elif hasattr(selectors, 'KqueueSelector'):
        print("   BSD/macOS: kqueue (best performance, unlimited FDs)")
    elif hasattr(selectors, 'PollSelector'):
        print("   Linux (old): poll (unlimited FDs)")
    else:
        print("   Other: select (limited to ~1024 FDs)")


def demo_selector_basics() -> None:
    """Demonstrate basic selector operations."""
    print("\n== Selector Basics ==\n")

    # Create a selector
    sel = selectors.DefaultSelector()

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 0))
    sock.listen(1)
    sock.setblocking(False)

    port = sock.getsockname()[1]
    print(f"1. Created listening socket on port {port}")

    # Register the socket for read events
    key = sel.register(sock, selectors.EVENT_READ, data=f"server-{port}")
    print(f"2. Registered socket for EVENT_READ")
    print(f"   SelectorKey: {key}")
    print(f"   FileObj: {key.fileobj}")
    print(f"   Fd: {key.fd}")
    print(f"   Events: {key.events}")
    print(f"   Data: {key.data}")

    # Check registered sockets
    print(f"\n3. Registered sockets count: {len(sel.get_map())}")

    # Unregister
    sel.unregister(sock)
    print(f"4. Unregistered socket, count: {len(sel.get_map())}")

    sock.close()
    sel.close()


def demo_echo_server_with_selectors() -> None:
    """Demonstrate an echo server using selectors."""
    print("\n== Echo Server with Selectors ==\n")

    sel = selectors.DefaultSelector()

    # Create listening socket
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    lsock.bind(("127.0.0.1", 18905))
    lsock.listen()
    lsock.setblocking(False)

    sel.register(lsock, selectors.EVENT_READ, data=None)

    print(f"Server listening on 127.0.0.1:18905")

    # Start client thread
    def run_client():
        time.sleep(0.2)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(("127.0.0.1", 18905))
            messages = ["Hello from client!", "Second message", "Bye!"]
            for msg in messages:
                client.sendall(msg.encode())
                response = client.recv(1024)
                print(f"[Client] Received: {response.decode()}")
                time.sleep(0.1)

    client_thread = threading.Thread(target=run_client, daemon=True)
    client_thread.start()

    # Event loop
    start_time = time.time()
    connections = {}  # type: dict[socket, bytes]

    try:
        while time.time() - start_time < 3:  # Run for 3 seconds
            # Wait for events (timeout 0.5s)
            events = sel.select(timeout=0.5)
            if not events:
                continue

            for key, mask in events:
                if key.data is None:
                    # New connection
                    conn, addr = lsock.accept()
                    print(f"[Server] Accepted connection from {addr}")
                    conn.setblocking(False)
                    connections[conn] = b""
                    sel.register(conn, selectors.EVENT_READ, data=addr)
                else:
                    # Data from existing connection
                    sock = key.fileobj
                    addr = key.data
                    try:
                        data = sock.recv(1024)
                        if data:
                            print(f"[Server] Received from {addr}: {data.decode()}")
                            sock.sendall(data)  # Echo back
                        else:
                            # Connection closed
                            print(f"[Server] Connection closed: {addr}")
                            sel.unregister(sock)
                            sock.close()
                            del connections[sock]
                    except OSError:
                        sel.unregister(sock)
                        sock.close()
                        del connections[sock]

    finally:
        sel.close()
        lsock.close()
        client_thread.join(timeout=1)

    print("[Server] Server stopped")


def demo_selector_event_types() -> None:
    """Demonstrate different event types."""
    print("\n== Selector Event Types ==\n")

    print("1. Event types:")
    print(f"   EVENT_READ: {selectors.EVENT_READ:#x} (readable)")
    print(f"   EVENT_WRITE: {selectors.EVENT_WRITE:#x} (writable)")

    print("\n2. Combined events:")
    combined = selectors.EVENT_READ | selectors.EVENT_WRITE
    print(f"   EVENT_READ | EVENT_WRITE: {combined:#x}")

    print("\n3. Event mask checking:")
    mask = selectors.EVENT_READ | selectors.EVENT_WRITE
    print(f"   Has EVENT_READ: {bool(mask & selectors.EVENT_READ)}")
    print(f"   Has EVENT_WRITE: {bool(mask & selectors.EVENT_WRITE)}")


def main() -> None:
    demo_selector_types()
    demo_selector_basics()
    demo_selector_event_types()
    demo_echo_server_with_selectors()

    print("\n== Selectors vs Low-Level APIs ==\n")
    print("API           | FD Limit | Platform   | Performance")
    print("--------------|----------|------------|-------------")
    print("select()      | ~1024    | All        | Slow for many FDs")
    print("poll()        | None     | Linux      | O(n) per call")
    print("epoll()       | None     | Linux      | O(1) - best")
    print("kqueue()      | None     | BSD/macOS  | O(1) - best")
    print("selectors     | Depends  | All        | Auto-selects best")
    print("\nRecommendation: Always use selectors for new code!")


if __name__ == "__main__":
    main()
