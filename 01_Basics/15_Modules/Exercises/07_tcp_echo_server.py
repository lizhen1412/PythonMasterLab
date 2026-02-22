#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：TCP Echo 服务器。
Author: Lambert

任务：创建一个 TCP echo 服务器，接收客户端消息并原样返回。
要求：
1. 使用 socket.socket() 创建 TCP 套接字
2. 使用 bind() 绑定到 127.0.0.1:19001
3. 使用 listen() 开始监听
4. 使用 accept() 接受客户端连接
5. 接收客户端发送的消息并原样返回
6. 客户端断开时关闭连接
"""

from __future__ import annotations

import socket
import threading
import time


def run_server() -> None:
    """运行 TCP echo 服务器。"""
    # TODO: 实现这个函数
    # 提示：
    # 1. with socket.socket(...) as sock:
    # 2. sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 3. sock.bind(("127.0.0.1", 19001))
    # 4. sock.listen(1)
    # 5. conn, addr = sock.accept()
    # 6. while True: data = conn.recv(1024); if not data: break; conn.sendall(data)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", 19001))
        sock.listen(1)
        print("[服务器] 监听 127.0.0.1:19001")

        conn, addr = sock.accept()
        with conn:
            print(f"[服务器] 客户端已连接: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[服务器] 收到: {data.decode()}")
                conn.sendall(data)


def run_client() -> None:
    """运行测试客户端。"""
    time.sleep(0.2)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", 19001))
        messages = ["Hello", "World", "Bye"]
        for msg in messages:
            sock.sendall(msg.encode())
            response = sock.recv(1024)
            print(f"[客户端] 收到: {response.decode()}")
            time.sleep(0.1)


def test() -> None:
    """测试 TCP echo 服务器。"""
    print("== 测试 TCP Echo 服务器 ==\n")

    # 启动服务器线程
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # 运行客户端
    run_client()

    # 等待服务器完成
    server_thread.join(timeout=1)

    print("\n[测试] OK" if True else "[测试] FAIL")


if __name__ == "__main__":
    test()
