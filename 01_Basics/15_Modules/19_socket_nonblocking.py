#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 19：非阻塞 Socket 与 I/O 多路复用基础。
Author: Lambert

- 非阻塞模式：setblocking(False)
- select 基础：监控多个套接字的可读/可写状态
- 单线程处理多个连接的基础模式
- 为 selectors 模块做铺垫
"""

from __future__ import annotations

import select
import socket
import threading
import time


def demo_nonblocking_socket() -> None:
    """演示非阻塞套接字的行为。"""
    print("== 非阻塞套接字演示 ==\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # 设置为非阻塞模式
        sock.setblocking(False)

        print("1. 尝试非阻塞连接:")
        try:
            # 非阻塞 connect 会立即返回，连接在后台进行
            result = sock.connect(("127.0.0.1", 18888))
            print(f"   connect() 返回: {result}")
        except BlockingIOError as e:
            print(f"   BlockingIOError: {e}")
            print("   连接正在进行中，需要等待...")

        print("\n2. 尝试非阻塞接收:")
        try:
            data = sock.recv(1024)
            print(f"   收到: {data}")
        except BlockingIOError:
            print("   BlockingIOError: 没有数据可读")

        print("\n3. 使用 select 等待套接字就绪:")
        # select 等待套接字可写（连接完成）
        writable, _, _ = select.select([], [sock], [], 1.0)
        if writable:
            print("   套接字已就绪（连接完成或可写）")

        print("\n4. 再次尝试接收:")
        try:
            data = sock.recv(1024)
            print(f"   收到: {data}")
        except BlockingIOError:
            print("   仍然没有数据可读")


def demo_select_multiple_sockets() -> None:
    """演示使用 select 监控多个套接字。"""
    print("\n== Select 监控多个套接字 ==\n")

    # 创建多个非阻塞 UDP 套接字
    sockets = []
    ports = [18901, 18902, 18903]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", port))
        sock.setblocking(False)
        sockets.append(sock)
        print(f"创建 UDP 套接字，监听端口 {port}")

    print("\n使用 select 等待任一套接字可读（2秒超时）:")

    # select 监控可读的套接字
    readable, _, exceptional = select.select(sockets, [], sockets, 2.0)

    if readable:
        print(f"{len(readable)} 个套接字可读")
    else:
        print("超时：没有套接字可读")

    if exceptional:
        print(f"{len(exceptional)} 个套接字有异常")

    # 清理
    for sock in sockets:
        sock.close()

    print("\n提示：select 有文件描述符数量限制（通常 1024），推荐使用 selectors。")


def demo_echo_server_with_select() -> None:
    """演示使用 select 的单线程 echo 服务器。"""
    print("\n== Select 单线程 Echo 服务器 ==\n")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 18904))
    server_socket.listen(5)
    server_socket.setblocking(False)

    print(f"服务器监听 127.0.0.1:18904")

    # 启动客户端线程
    def run_client():
        time.sleep(0.2)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(("127.0.0.1", 18904))
            client.sendall(b"Hello from client!")
            response = client.recv(1024)
            print(f"[客户端] 收到: {response.decode()}")

    client_thread = threading.Thread(target=run_client, daemon=True)
    client_thread.start()

    # 使用 select 处理连接
    inputs = [server_socket]
    outputs = []
    message_queues = {}  # type: dict[socket, list[bytes]]

    start_time = time.time()
    while time.time() - start_time < 2:  # 运行 2 秒
        # 等待套接字就绪，超时 0.5 秒
        readable, writable, exceptional = select.select(inputs, outputs, inputs, 0.5)

        for sock in readable:
            if sock is server_socket:
                # 新连接
                conn, addr = sock.accept()
                print(f"[服务器] 新连接: {addr}")
                conn.setblocking(False)
                inputs.append(conn)
                message_queues[conn] = []
            else:
                # 已连接的套接字可读
                try:
                    data = sock.recv(1024)
                    if data:
                        print(f"[服务器] 收到: {data.decode()}")
                        message_queues[sock].append(data)
                        if sock not in outputs:
                            outputs.append(sock)
                    else:
                        # 连接关闭
                        print(f"[服务器] 连接关闭")
                        if sock in outputs:
                            outputs.remove(sock)
                        inputs.remove(sock)
                        sock.close()
                        del message_queues[sock]
                except OSError:
                    inputs.remove(sock)
                    if sock in outputs:
                        outputs.remove(sock)
                    sock.close()

        for sock in writable:
            if message_queues[sock]:
                msg = message_queues[sock].pop(0)
                try:
                    sock.sendall(msg)
                    print(f"[服务器] 已回显")
                    if not message_queues[sock]:
                        outputs.remove(sock)
                except OSError:
                    inputs.remove(sock)
                    outputs.remove(sock)
                    sock.close()

        for sock in exceptional:
            inputs.remove(sock)
            if sock in outputs:
                outputs.remove(sock)
            sock.close()
            if sock in message_queues:
                del message_queues[sock]

    # 清理
    server_socket.close()
    client_thread.join(timeout=1)

    print("\n提示：select 是跨平台的，但有 FD 数量限制。")


def main() -> None:
    demo_nonblocking_socket()
    demo_select_multiple_sockets()
    demo_echo_server_with_select()

    print("\n== I/O 多路复用演进 ==\n")
    print("方式          | 平台      | FD 限制 | 说明")
    print("--------------|-----------|---------|-----------------------")
    print("select        | 跨平台    | ~1024   | 最早、兼容性好")
    print("poll          | Linux     | 无限制  | 比 select 高效")
    print("epoll         | Linux     | 无限制  | 性能最好")
    print("kqueue        | BSD/macOS | 无限制  | BSD 系统的 epoll")
    print("selectors     | 跨平台    | 取决于底层 | 自动选择最佳实现")


if __name__ == "__main__":
    main()
