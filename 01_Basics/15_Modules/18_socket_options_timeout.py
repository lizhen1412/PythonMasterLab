#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 18：Socket 选项与超时设置。
Author: Lambert

- 套接字选项：SO_REUSEADDR, SO_KEEPALIVE, TCP_NODELAY
- 超时设置：settimeout(), gettimeout()
- 非阻塞模式
- 获取套接字状态信息
"""

from __future__ import annotations

import socket
import time


def demo_socket_options() -> None:
    """演示常用套接字选项。"""
    print("== 套接字选项演示 ==\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("1. SO_REUSEADDR（地址复用）:")
        # 允许在 TIME_WAIT 状态下复用地址
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        value = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        print(f"   SO_REUSEADDR = {value}")

        print("\n2. SO_KEEPALIVE（保持连接）:")
        # 启用 TCP keepalive
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        value = sock.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)
        print(f"   SO_KEEPALIVE = {value}")

        print("\n3. TCP_NODELAY（禁用 Nagle 算法）:")
        # 立即发送数据，不等待缓冲区填满
        try:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            value = sock.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)
            print(f"   TCP_NODELAY = {value}")
        except (OSError, AttributeError) as e:
            print(f"   TCP_NODELAY 不可用: {e}")

        print("\n4. SO_RCVBUF / SO_SNDBUF（缓冲区大小）:")
        # 获取接收缓冲区大小
        recv_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        # 获取发送缓冲区大小
        send_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        print(f"   接收缓冲区: {recv_buf} 字节")
        print(f"   发送缓冲区: {send_buf} 字节")

        # 设置缓冲区大小（需要谨慎）
        sock.setsockopt(socket.SOL_SOCKET, SO_RCVBUF:=getattr(socket, "SO_RCVBUF", 8), 8192)
        print(f"   设置接收缓冲区为 8192 字节")


def demo_socket_timeout() -> None:
    """演示套接字超时设置。"""
    print("\n== 套接字超时演示 ==\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("1. 设置超时:")
        # 设置超时为 1 秒
        sock.settimeout(1.0)
        timeout = sock.gettimeout()
        print(f"   超时时间: {timeout} 秒")

        print("\n2. 尝试连接到不可达地址（会超时）:")
        start = time.time()
        try:
            # 连接到一个不太可能开放的端口
            sock.connect(("127.0.0.1", 9999))
        except socket.timeout:
            elapsed = time.time() - start
            print(f"   连接超时！耗时: {elapsed:.2f} 秒")
        except ConnectionRefusedError:
            elapsed = time.time() - start
            print(f"   连接被拒绝（服务未运行），耗时: {elapsed:.2f} 秒")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("\n3. 设置为阻塞模式（默认）:")
        sock.setblocking(True)
        print(f"   阻塞模式: {sock.getblocking()}")

        print("\n4. 设置为非阻塞模式:")
        sock.setblocking(False)
        print(f"   阻塞模式: {sock.getblocking()}")

        print("\n5. 尝试非阻塞接收（会立即返回）:")
        # 在非阻塞模式下，未连接的套接字调用 recv 会抛出异常
        try:
            # 尝试绑定但不连接，然后 recv 会立即返回错误
            test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            test_sock.setblocking(False)
            data = test_sock.recv(1024)
        except (BlockingIOError, OSError):
            # macOS 抛出 OSError，Linux 可能抛出 BlockingIOError
            print("   立即返回错误：没有连接或数据可读（非阻塞）")
        finally:
            try:
                test_sock.close()
            except:
                pass


def demo_socket_info() -> None:
    """演示获取套接字信息。"""
    print("\n== 套接字信息演示 ==\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))  # 绑定到随机端口
        port = sock.getsockname()[1]

        print("1. 套接字名称（本地地址）:")
        print(f"   本地地址: {sock.getsockname()}")

        print("\n2. 套接字类型:")
        sock_type = sock.getsockopt(socket.SOL_SOCKET, socket.SO_TYPE)
        type_name = "SOCK_STREAM" if sock_type == socket.SOCK_STREAM else "SOCK_DGRAM"
        print(f"   类型: {type_name} ({sock_type})")

        print("\n3. 套接字族:")
        family = sock.family
        family_name = "AF_INET" if family == socket.AF_INET else "AF_INET6"
        print(f"   族: {family_name} ({family})")


def main() -> None:
    demo_socket_options()
    demo_socket_timeout()
    demo_socket_info()

    print("\n== 常用套接字选项速查 ==\n")
    print("选项                       | 说明")
    print("----------------------------|-------------------------------------")
    print("SO_REUSEADDR              | 允许地址复用（避免 TIME_WAIT 问题）")
    print("SO_KEEPALIVE              | 启用 TCP keepalive")
    print("TCP_NODELAY               | 禁用 Nagle 算法（降低延迟）")
    print("SO_RCVBUF / SO_SNDBUF     | 接收/发送缓冲区大小")
    print("SO_BROADCAST              | 允许广播")
    print("IP_MULTICAST_TTL          | 组播 TTL")
    print("\n提示：不同操作系统可能支持不同的选项。")


if __name__ == "__main__":
    main()
