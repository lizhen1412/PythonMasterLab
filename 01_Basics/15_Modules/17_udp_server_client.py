#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：UDP 服务器与客户端。
Author: Lambert

- UDP 服务器：bind() -> recvfrom() -> sendto()
- UDP 客户端：sendto() -> recvfrom()
- UDP 无连接、不可靠但高效
- 演示数据报（datagram）通信模式
"""

from __future__ import annotations

import socket
import threading
import time


def udp_server(host: str = "127.0.0.1", port: int = 18899) -> None:
    """UDP echo 服务器：接收数据报并回显。"""
    # 创建 UDP 套接字（SOCK_DGRAM）
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((host, port))
        server_sock.settimeout(2.0)  # 设置超时

        print(f"[服务器] UDP 监听 {host}:{port}")

        while True:
            try:
                # recvfrom 返回 (data, address)
                data, addr = server_sock.recvfrom(1024)
                if not data:
                    break
                print(f"[服务器] 收到来自 {addr}: {data.decode()}")
                # 回显到同一地址
                server_sock.sendto(data, addr)
            except socket.timeout:
                # 超时退出
                break

        print("[服务器] 超时退出")


def udp_client(host: str = "127.0.0.1", port: int = 18899) -> None:
    """UDP 客户端：发送数据报并接收回显。"""
    time.sleep(0.1)  # 等待服务器启动

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
        messages = ["Hello, UDP!", "Datagram 2", "Bye!"]

        for msg in messages:
            # UDP 无需连接，直接 sendto
            client_sock.sendto(msg.encode(), (host, port))
            print(f"[客户端] 已发送: {msg}")

            # 接收回显
            data, _ = client_sock.recvfrom(1024)
            print(f"[客户端] 收到回显: {data.decode()}")

        print("[客户端] 完成")


def main() -> None:
    print("== UDP Echo 服务器与客户端演示 ==\n")

    # 启动服务器线程
    server_thread = threading.Thread(
        target=udp_server,
        kwargs={"host": "127.0.0.1", "port": 18899},
        daemon=True
    )
    server_thread.start()

    # 启动客户端
    udp_client(host="127.0.0.1", port=18899)

    # 等待服务器完成
    server_thread.join(timeout=3)

    print("\n提示：UDP 无连接、不可靠但高效，适用于实时场景。")
    print("注意：UDP 不保证顺序和送达，生产环境需实现重传和校验。")


if __name__ == "__main__":
    main()
