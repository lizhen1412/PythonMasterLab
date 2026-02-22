#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：UDP 客户端。
Author: Lambert

任务：创建一个 UDP 客户端，向本地服务器发送消息并接收响应。
要求：
1. 使用 socket.socket() 创建 UDP 套接字（SOCK_DGRAM）
2. 使用 sendto() 发送消息到 127.0.0.1:19002
3. 使用 recvfrom() 接收响应
4. 打印接收到的响应
"""

from __future__ import annotations

import socket
import threading
import time


def run_server() -> None:
    """运行简单的 UDP 服务器用于测试。"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", 19002))
        sock.settimeout(2.0)
        print("[服务器] UDP 监听 127.0.0.1:19002")

        try:
            while True:
                data, addr = sock.recvfrom(1024)
                if data:
                    print(f"[服务器] 收到来自 {addr}: {data.decode()}")
                    sock.sendto(b"Echo: " + data, addr)
        except socket.timeout:
            print("[服务器] 超时退出")


def run_client() -> None:
    """运行 UDP 客户端。"""
    # TODO: 实现这个函数
    # 提示：
    # 1. with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # 2. for msg in messages:
    # 3.     sock.sendto(msg.encode(), ("127.0.0.1", 19002))
    # 4.     data, _ = sock.recvfrom(1024)
    # 5.     print(f"收到: {data.decode()}")
    time.sleep(0.1)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        messages = ["UDP Hello", "UDP World", "UDP Bye"]
        for msg in messages:
            sock.sendto(msg.encode(), ("127.0.0.1", 19002))
            data, _ = sock.recvfrom(1024)
            print(f"[客户端] 收到: {data.decode()}")


def test() -> None:
    """测试 UDP 客户端。"""
    print("== 测试 UDP 客户端 ==\n")

    # 启动服务器线程
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # 运行客户端
    run_client()

    # 等待服务器完成
    server_thread.join(timeout=3)

    print("\n[测试] OK" if True else "[测试] FAIL")


if __name__ == "__main__":
    test()
