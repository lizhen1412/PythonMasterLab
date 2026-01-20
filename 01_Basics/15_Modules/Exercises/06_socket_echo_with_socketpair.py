#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：用 socketpair 做本地 echo。

要求：
- 使用 socket.socketpair 创建一对套接字
- 一端发送消息，另一端收到后回显
"""

from __future__ import annotations

import socket


def echo_once(message: bytes) -> bytes:
    s1, s2 = socket.socketpair()
    with s1, s2:
        s1.sendall(message)
        received = s2.recv(1024)
        s2.sendall(received.upper())
        return s1.recv(1024)


def main() -> None:
    reply = echo_once(b"hello")
    print("echo reply ->", reply)


if __name__ == "__main__":
    main()
