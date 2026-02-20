#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：socket 基础。
Author: Lambert

- 地址族与类型：AF_INET（IPv4）/ SOCK_STREAM（TCP）
- 用 socket.socketpair() 在本地进程内演示收发（无需网络）
"""

from __future__ import annotations

import socket
from typing import Tuple


def show_constants() -> None:
    """列出常见地址族与类型。"""
    print("AF_INET (IPv4) ->", socket.AF_INET)
    print("AF_INET6 (IPv6) ->", socket.AF_INET6)
    print("SOCK_STREAM (TCP) ->", socket.SOCK_STREAM)
    print("SOCK_DGRAM (UDP) ->", socket.SOCK_DGRAM)


def demo_socketpair() -> None:
    """使用 socketpair 在同一进程收发。"""
    s1, s2 = socket.socketpair()
    with s1, s2:
        message = b"hello socket"
        s1.sendall(message)
        data = s2.recv(1024)
        print("s2 收到 ->", data)

        s2.sendall(b"pong")
        reply = s1.recv(1024)
        print("s1 收到 ->", reply)


def main() -> None:
    print("== 常见常量 ==")
    show_constants()

    print("\n== socketpair 本地收发 ==")
    demo_socketpair()

    print("\n提示：实际网络通信需绑定地址/端口，注意防火墙与权限。")


if __name__ == "__main__":
    main()