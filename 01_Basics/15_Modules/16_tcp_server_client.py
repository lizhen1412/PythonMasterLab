#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：TCP 服务器与客户端。
Author: Lambert

- TCP 服务器：bind() -> listen() -> accept() -> recv() -> sendall()
- TCP 客户端：connect() -> sendall() -> recv()
- 演示使用 localhost 避免网络问题
- 使用线程在单进程中同时运行服务器和客户端
"""

from __future__ import annotations

import socket
import threading
import time
from typing import NoReturn


def tcp_server(host: str = "127.0.0.1", port: int = 0) -> int:
    """
    TCP echo 服务器。
    接收客户端连接，回显收到的数据。
    返回实际绑定的端口号。
    """
    # 创建 TCP 套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        # 设置 SO_REUSEADDR 选项，避免 TIME_WAIT 状态导致的地址占用
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定地址和端口（port=0 表示自动分配可用端口）
        server_sock.bind((host, port))
        actual_port = server_sock.getsockname()[1]

        # 开始监听，backlog 指定挂起连接队列的最大长度
        server_sock.listen(1)
        print(f"[服务器] 监听 {host}:{actual_port}")

        # 等待客户端连接
        conn, addr = server_sock.accept()
        with conn:
            print(f"[服务器] 客户端已连接: {addr}")
            while True:
                # 接收数据，缓冲区大小 1024
                data = conn.recv(1024)
                if not data:
                    # 客户端关闭连接
                    print(f"[服务器] 客户端 {addr} 断开连接")
                    break
                print(f"[服务器] 收到: {data.decode()}")
                # 回显数据
                conn.sendall(data)

        return actual_port


def tcp_client(host: str = "127.0.0.1", port: int = 0) -> None:
    """TCP 客户端：发送消息并接收回显。"""
    # 等待服务器启动
    time.sleep(0.1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        print(f"[客户端] 连接到 {host}:{port}")
        # 连接服务器
        client_sock.connect((host, port))

        # 发送消息
        messages = ["Hello, TCP!", "Bye!"]
        for msg in messages:
            client_sock.sendall(msg.encode())
            print(f"[客户端] 已发送: {msg}")

            # 接收回显
            data = client_sock.recv(1024)
            print(f"[客户端] 收到回显: {data.decode()}")

        # 关闭连接（with 语句会自动关闭）


def main() -> None:
    print("== TCP Echo 服务器与客户端演示 ==\n")

    # 先启动服务器（在后台线程）
    server_thread = threading.Thread(
        target=tcp_server,
        kwargs={"host": "127.0.0.1", "port": 0},
        daemon=True
    )
    server_thread.start()

    # 等待服务器绑定完成，获取端口号
    time.sleep(0.2)

    # 由于服务器在单独线程中运行，我们需要一种方式获取端口号
    # 这里简化处理：使用固定端口演示
    print("\n== 使用固定端口重新演示 ==\n")

    # 创建服务器套接字并绑定到固定端口
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind(("127.0.0.1", 18888))
        server_sock.listen(1)
        server_sock.settimeout(2.0)  # 设置超时
        port = server_sock.getsockname()[1]
        print(f"[服务器] 监听 127.0.0.1:{port}")

        # 在线程中运行客户端
        client_thread = threading.Thread(
            target=tcp_client,
            kwargs={"host": "127.0.0.1", "port": port},
            daemon=False
        )
        client_thread.start()

        # 接受连接并处理
        try:
            conn, addr = server_sock.accept()
            with conn:
                print(f"[服务器] 客户端已连接: {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"[服务器] 收到: {data.decode()}")
                    conn.sendall(data)
        except socket.timeout:
            pass

        # 等待客户端完成
        client_thread.join()

    print("\n提示：生产环境需处理异常、并发连接、优雅关闭等。")


if __name__ == "__main__":
    main()
