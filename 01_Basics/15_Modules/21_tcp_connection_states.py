#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 21：TCP 连接状态详解 - 三次握手与四次挥手。
Author: Lambert

本示例详细演示 TCP 连接的完整生命周期，包括：

1. **三次握手（Three-Way Handshake）**
   - SYN: 客户端发送连接请求
   - SYN-ACK: 服务器确认并请求连接
   - ACK: 客户端确认连接建立

2. **四次挥手（Four-Way Wave）**
   - FIN: 主动方请求关闭
   - ACK: 被动方确认
   - FIN: 被动方也请求关闭
   - ACK: 主动方确认

3. **TCP 状态机**
   - LISTEN: 服务器监听状态
   - SYN_SENT: 客户端发送SYN后的状态
   - SYN_RCVD: 服务器收到SYN后的状态
   - ESTABLISHED: 连接建立状态
   - FIN_WAIT_1: 主动关闭方发送FIN后的状态
   - FIN_WAIT_2: 主动关闭方收到ACK后的状态
   - CLOSE_WAIT: 被动关闭方收到FIN后的状态
   - LAST_ACK: 被动关闭方发送FIN后的状态
   - TIME_WAIT: 主动关闭方收到最终FIN后的状态
   - CLOSED: 连接关闭状态

注意：Python的socket API封装了底层TCP细节，我们通过socket选项和日志来推断和展示这些状态。
"""

from __future__ import annotations

import socket
import struct
import threading
import time
from typing import NoReturn


# =============================================================================
# TCP 选项常量
# =============================================================================


# TCP 状态（在 /proc/net/tcp 中可见）
TCP_STATES = {
    '01': 'ESTABLISHED',
    '02': 'SYN_SENT',
    '03': 'SYN_RECV',
    '04': 'FIN_WAIT1',
    '05': 'FIN_WAIT2',
    '06': 'TIME_WAIT',
    '07': 'CLOSE',
    '08': 'CLOSE_WAIT',
    '09': 'LAST_ACK',
    '0A': 'LISTEN',
    '0B': 'CLOSING',
}


def print_separator(title: str = "") -> None:
    """打印分隔线。"""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}")
    else:
        print(f"{'-'*60}")


def get_tcp_state_name(state_int: int) -> str:
    """将TCP状态整数转换为名称。"""
    state_hex = f"{state_int:02X}"
    return TCP_STATES.get(state_hex, f"UNKNOWN({state_int})")


# =============================================================================
# 三次握手详解
# =============================================================================


def demo_three_way_handshake() -> None:
    """示例 01：TCP三次握手详细演示。"""
    print_separator("TCP 三次握手演示")

    print("""
    TCP三次握手是建立TCP连接的过程：

    客户端                              服务器
       |                                   |
       |  1. SYN                          |  (LISTEN -> SYN_RCVD)
       | --------------------------------> |
       |                                   |
       |  2. SYN-ACK                       |  (SYN_RCVD -> ESTABLISHED)
       | <------------------------------- |
       |                                   |
       |  3. ACK                          |  (SYN_SENT -> ESTABLISHED)
       | --------------------------------> |
       |                                   |
       |        连接建立 (ESTABLISHED)        |

    实际观察：
    - 客户端调用 connect() 时，内核发送SYN包
    - 服务器调用 accept() 返回时，表示三次握手完成
    - 我们通过socket状态和日志来观察这个过程
    """)

    def server() -> None:
        """服务器端：监听并接受连接。"""
        print("\n[服务器] 创建TCP套接字...")
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设置SO_REUSEADDR避免TIME_WAIT占用
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print(f"[服务器] 绑定地址 127.0.0.1:19999")
        server_sock.bind(("127.0.0.1", 19999))

        print(f"[服务器] 状态: LISTEN (等待连接...)")
        server_sock.listen(1)

        # 尝试获取socket状态
        print(f"[服务器] Socket fileno: {server_sock.fileno()}")
        print(f"[服务器] Socket family: {server_sock.family}")
        print(f"[服务器] Socket type: {server_sock.type}")

        # 等待连接（这里会阻塞直到三次握手完成）
        print(f"[服务器] 等待连接（阻塞在accept()）...")
        print(f"[服务器]     内核: 收到SYN包 -> 状态: LISTEN -> SYN_RCVD")
        print(f"[服务器]     内核: 发送SYN-ACK包")

        conn, client_addr = server_sock.accept()

        print(f"[服务器] ✓ 三次握手完成！")
        print(f"[服务器] 状态: ESTABLISHED")
        print(f"[服务器] 客户端地址: {client_addr}")
        print(f"[服务器] 本地地址: {conn.getsockname()}")
        print(f"[服务器] 对端地址: {conn.getpeername()}")

        # 保持连接一会儿
        time.sleep(1)

        # 关闭连接
        conn.close()
        server_sock.close()
        print(f"[服务器] 连接关闭")

    def client() -> None:
        """客户端：发起连接。"""
        time.sleep(0.2)  # 等待服务器启动

        print("\n[客户端] 创建TCP套接字...")
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"[客户端] 调用 connect('127.0.0.1', 19999)...")
        print(f"[客户端]     内核: 发送SYN包 -> 状态: CLOSED -> SYN_SENT")
        print(f"[客户端]     内核: 收到SYN-ACK包 -> 状态: SYN_SENT -> ESTABLISHED")
        print(f"[客户端]     内核: 发送ACK包")

        # connect()会在三次握手完成后返回
        client_sock.connect(("127.0.0.1", 19999))

        print(f"[客户端] ✓ 三次握手完成！")
        print(f"[客户端] 状态: ESTABLISHED")
        print(f"[客户端] 本地地址: {client_sock.getsockname()}")
        print(f"[客户端] 对端地址: {client_sock.getpeername()}")

        # 获取socket选项
        print(f"[客户端] Socket选项:")

        # 获取SO_ERROR（检查是否有待处理的错误）
        try:
            error = client_sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
            print(f"   SO_ERROR: {error} (0=无错误)")
        except:
            pass

        # 获取TCP_INFO（如果平台支持）
        try:
            tcp_info = client_sock.getsockopt(socket.IPPROTO_TCP, socket.TCP_INFO, 92)
            # TCP_INFO结构解析（简化）
            state = struct.unpack('I', tcp_info[4:8])[0]
            print(f"   TCP_STATE: {get_tcp_state_name(state)}")
        except:
            print(f"   TCP_INFO: (平台不支持)")

        time.sleep(0.5)
        client_sock.close()
        print(f"[客户端] 连接关闭")

    # 启动服务器和客户端
    server_thread = threading.Thread(target=server, daemon=False)
    server_thread.start()

    client()
    server_thread.join(timeout=5)


# =============================================================================
# 四次挥手详解
# =============================================================================


def demo_four_way_wave() -> None:
    """示例 02：TCP四次挥手详细演示。"""
    print_separator("TCP 四次挥手演示")

    print("""
    TCP四次挥手是断开TCP连接的过程：

    情况A：主动关闭方先关闭（常见情况）

    主动方                            被动方
       |                                   |
       |  1. FIN                         |  (ESTABLISHED -> FIN_WAIT_1)
       | --------------------------------> |
       |                                   |  (ESTABLISHED -> CLOSE_WAIT)
       |  2. ACK                         |
       | <------------------------------- |  (FIN_WAIT_1 -> FIN_WAIT_2)
       |                                   |
       |  3. FIN                         |  (CLOSE_WAIT -> LAST_ACK)
       | <------------------------------- |
       |                                   |
       |  4. ACK                         |  (LAST_ACK -> CLOSED)
       | --------------------------------> |  (FIN_WAIT_2 -> TIME_WAIT -> CLOSED)
       |                                   |
       |        连接关闭                        |

    重要细节：
    - ACK和FIN可能合并（如果应用层同时关闭）
    - 主动关闭方需要经历TIME_WAIT状态（2*MSL，通常60秒）
    - 被动关闭方关闭后直接进入CLOSED状态

    shutdown() vs close():
    - shutdown(SHUT_WR): 发送FIN，但还能接收数据（半关闭）
    - close(): 既发送FIN，又不再接收数据
    """)

    def server() -> None:
        """服务器：被动关闭方。"""
        print("\n[服务器] 启动...")
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind(("127.0.0.1", 19998))
        server_sock.listen(1)
        print(f"[服务器] 状态: LISTEN")

        # 接受连接
        conn, addr = server_sock.accept()
        print(f"[服务器] 连接建立: {addr}")
        print(f"[服务器] 状态: ESTABLISHED")

        # 接收数据
        data = conn.recv(1024)
        print(f"[服务器] 收到: {data.decode()}")

        # 模拟处理
        time.sleep(0.3)

        # 发送响应
        conn.sendall(b"Goodbye from server")
        print(f"[服务器] 发送响应")

        # 等待客户端关闭
        print(f"[服务器] 等待客户端关闭...")
        try:
            # 设置接收超时
            conn.settimeout(2.0)
            more_data = conn.recv(1024)
            if not more_data:
                print(f"[服务器] 收到FIN包")
                print(f"[服务器] 状态: ESTABLISHED -> CLOSE_WAIT")
                print(f"[服务器] 发送ACK包")
        except socket.timeout:
            print(f"[服务器] 超时（客户端已关闭）")

        # 服务器也关闭
        print(f"[服务器] 调用 close()...")
        print(f"[服务器]     内核: 发送FIN包 -> 状态: CLOSE_WAIT -> LAST_ACK")
        conn.close()
        print(f"[服务器] 状态: LAST_ACK -> CLOSED")

        server_sock.close()

    def client() -> None:
        """客户端：主动关闭方。"""
        time.sleep(0.2)

        print("\n[客户端] 创建套接字...")
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 连接
        client_sock.connect(("127.0.0.1", 19998))
        print(f"[客户端] 连接建立")
        print(f"[客户端] 状态: ESTABLISHED")

        # 发送数据
        client_sock.sendall(b"Hello from client")
        print(f"[客户端] 发送数据")

        # 接收响应
        data = client_sock.recv(1024)
        print(f"[客户端] 收到: {data.decode()}")

        # 主动关闭（四次挥手开始）
        print(f"\n[客户端] 主动关闭连接...")
        print(f"[客户端] 调用 close()...")
        print(f"[客户端]     内核: 发送FIN包 -> 状态: ESTABLISHED -> FIN_WAIT_1")

        client_sock.close()

        print(f"[客户端] 状态: FIN_WAIT_1 -> FIN_WAIT_2 (收到服务器的ACK)")

        # 等待服务器的FIN
        time.sleep(0.2)
        print(f"[客户端] 收到服务器的FIN包")
        print(f"[客户端] 发送ACK包")
        print(f"[客户端] 状态: FIN_WAIT_2 -> TIME_WAIT")
        print(f"[客户端]     (等待2*MSL时间，通常60秒)")
        print(f"[客户端] 状态: TIME_WAIT -> CLOSED")

    # 启动服务器和客户端
    server_thread = threading.Thread(target=server, daemon=False)
    server_thread.start()

    client()
    server_thread.join(timeout=5)


# =============================================================================
# 半关闭演示
# =============================================================================


def demo_half_close() -> None:
    """示例 03：半关闭（Half-Close）- shutdown()的详细过程。"""
    print_separator("TCP 半关闭演示")

    print("""
    半关闭是指一方停止发送数据，但仍能接收数据。

    这是通过 shutdown(SHUT_WR) 实现的：

    发送方                            接收方
       |                                   |
       |  数据                            |
       | --------------------------------> |
       |  shutdown(SHUT_WR)               |
       |     内核: 发送FIN                 |  (ESTABLISHED -> CLOSE_WAIT)
       | --------------------------------> |
       |                                   |
       |  ACK                             |  (FIN_WAIT_1 -> FIN_WAIT_2)
       | <------------------------------- |
       |                                   |
       |  还能接收数据...                    |
       | <------------------------------- |
       |                                   |
       |  数据/关闭                        |
       | <------------------------------- |  (CLOSE_WAIT -> LAST_ACK)
       |                                   |
       |  ACK                             |  (FIN_WAIT_2 -> TIME_WAIT)
       | --------------------------------> |  (LAST_ACK -> CLOSED)
       |                                   |

    应用场景：
    - HTTP客户端：发送完请求后shutdown，但仍接收响应
    - 文件传输：发送方发送完文件后shutdown，等待确认
    """)

    def server() -> None:
        """服务器：接收数据后继续发送。"""
        print("\n[服务器] 启动...")
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind(("127.0.0.1", 19997))
        server_sock.listen(1)

        conn, addr = server_sock.accept()
        print(f"[服务器] 连接建立: {addr}")

        # 接收数据
        print(f"[服务器] 接收请求...")
        data = conn.recv(1024)
        print(f"[服务器] 收到: {data.decode()}")

        # 此时客户端已经shutdown写端
        # 检查连接状态
        try:
            # 尝试设置非阻塞来检查是否有更多数据
            conn.setblocking(False)
            more = conn.recv(1024)
            if not more:
                print(f"[服务器] 检测到: 客户端已关闭写端（收到FIN）")
                print(f"[服务器] 状态: ESTABLISHED -> CLOSE_WAIT")
        except BlockingIOError:
            print(f"[服务器] 客户端仍可写")

        conn.setblocking(True)

        # 继续发送响应（客户端仍能接收）
        print(f"[服务器] 发送响应...")
        conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, Client!")
        print(f"[服务器] 响应已发送")

        time.sleep(0.2)

        # 关闭连接
        conn.close()
        print(f"[服务器] 连接关闭")

    def client() -> None:
        """客户端：发送完请求后shutdown写端。"""
        time.sleep(0.2)

        print("\n[客户端] 创建套接字...")
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(("127.0.0.1", 19997))
        print(f"[客户端] 连接建立")

        # 发送请求
        print(f"[客户端] 发送HTTP请求...")
        client_sock.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        print(f"[客户端] 请求已发送")

        # 关闭写端（半关闭）
        print(f"\n[客户端] 调用 shutdown(SHUT_WR)...")
        print(f"[客户端]     内核: 发送FIN包 -> 状态: ESTABLISHED -> FIN_WAIT_1")
        client_sock.shutdown(socket.SHUT_WR)
        print(f"[客户端] 状态: FIN_WAIT_1 -> FIN_WAIT_2 (收到服务器的ACK)")
        print(f"[客户端] 写端已关闭，但仍可读取")

        # 接收响应
        print(f"[客户端] 接收响应...")
        response = client_sock.recv(1024)
        print(f"[客户端] 收到: {response.decode()[:50]}...")

        time.sleep(0.2)

        # 完全关闭
        print(f"\n[客户端] 调用 close()...")
        client_sock.close()
        print(f"[客户端] 连接关闭")

    # 启动服务器和客户端
    server_thread = threading.Thread(target=server, daemon=False)
    server_thread.start()

    client()
    server_thread.join(timeout=5)


# =============================================================================
# 连接状态监控
# =============================================================================


def demo_connection_state_monitoring() -> None:
    """示例 04：监控连接状态变化。"""
    print_separator("连接状态监控")

    print("""
    通过socket选项和系统调用监控TCP连接状态：

    关键方法：
    - getsockname(): 获取本地地址和端口
    - getpeername(): 获取远程地址和端口
    - getsockopt(): 获取socket选项
    - fileno(): 获取文件描述符

    TCP状态转换路径：

    主动连接方:
    CLOSED -> SYN_SENT -> ESTABLISHED -> FIN_WAIT_1 -> FIN_WAIT_2 -> TIME_WAIT -> CLOSED

    被动连接方:
    LISTEN -> SYN_RCVD -> ESTABLISHED -> CLOSE_WAIT -> LAST_ACK -> CLOSED
    """)

    def monitor_socket(sock: socket.socket, name: str) -> None:
        """监控socket状态。"""
        print(f"\n[{name}] Socket状态监控:")
        print(f"  文件描述符: {sock.fileno()}")
        print(f"  地址族: {sock.family} (AF_INET={socket.AF_INET})")
        print(f"  类型: {sock.type} (SOCK_STREAM={socket.SOCK_STREAM})")
        print(f"  协议: {sock.proto} (IPPROTO_TCP={socket.IPPROTO_TCP})")

        try:
            print(f"  本地地址: {sock.getsockname()}")
        except OSError:
            print(f"  本地地址: (未绑定)")

        try:
            print(f"  远程地址: {sock.getpeername()}")
        except OSError:
            print(f"  远程地址: (未连接)")

        # 获取SO_ERROR
        try:
            error = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
            if error == 0:
                print(f"  Socket错误: 无")
            else:
                print(f"  Socket错误: {error}")
        except:
            pass

        # 获取发送/接收缓冲区大小
        try:
            recv_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
            send_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
            print(f"  接收缓冲区: {recv_buf} 字节")
            print(f"  发送缓冲区: {send_buf} 字节")
        except:
            pass

    def server() -> None:
        """服务器：监控连接状态。"""
        print("\n[服务器] 启动...")
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind(("127.0.0.1", 19996))

        monitor_socket(server_sock, "服务器(监听)")

        server_sock.listen(1)
        print(f"\n[服务器] 状态: LISTEN")
        print(f"[服务器] 等待连接...")

        conn, addr = server_sock.accept()
        print(f"\n[服务器] ✓ 连接建立: {addr}")
        print(f"[服务器] 状态: SYN_RCVD -> ESTABLISHED")

        monitor_socket(conn, "服务器(连接)")

        # 数据交换
        data = conn.recv(1024)
        print(f"\n[服务器] 收到: {data.decode()}")

        conn.sendall(b"ACK")
        print(f"[服务器] 发送: ACK")

        time.sleep(0.3)
        conn.close()
        print(f"\n[服务器] 连接关闭")
        server_sock.close()

    def client() -> None:
        """客户端：监控连接状态。"""
        time.sleep(0.3)

        print("\n[客户端] 创建套接字...")
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        monitor_socket(client_sock, "客户端(创建)")

        print(f"\n[客户端] 调用 connect()...")
        print(f"[客户端] 状态: CLOSED -> SYN_SENT")

        client_sock.connect(("127.0.0.1", 19996))

        print(f"\n[客户端] ✓ 三次握手完成")
        print(f"[客户端] 状态: SYN_SENT -> ESTABLISHED")

        monitor_socket(client_sock, "客户端(已连接)")

        # 数据交换
        client_sock.sendall(b"Hello")
        print(f"\n[客户端] 发送: Hello")

        data = client_sock.recv(1024)
        print(f"[客户端] 收到: {data.decode()}")

        time.sleep(0.2)

        print(f"\n[客户端] 关闭连接...")
        client_sock.close()
        print(f"[客户端] 状态: ESTABLISHED -> FIN_WAIT_1 -> FIN_WAIT_2")

    # 启动服务器和客户端
    server_thread = threading.Thread(target=server, daemon=False)
    server_thread.start()

    client()
    server_thread.join(timeout=5)


# =============================================================================
# TIME_WAIT 状态演示
# =============================================================================


def demo_time_wait_state() -> None:
    """示例 05：TIME_WAIT状态演示。"""
    print_separator("TIME_WAIT 状态演示")

    print("""
    TIME_WAIT是TCP连接关闭后的一个重要状态：

    为什么需要TIME_WAIT？
    1. 确保最终的ACK到达对方（如果丢失，对方会重发FIN）
    2. 确保当前连接的所有包都从网络中消失

    TIME_WAIT的特点：
    - 持续时间：2*MSL（Maximum Segment Lifetime，通常60秒）
    - 只有主动关闭方会进入TIME_WAIT
    - 占用源端口，可能导致端口耗尽

    影响：
    - 高并发服务器如果频繁关闭连接，可能积累大量TIME_WAIT连接
    - 解决方案：SO_REUSEADDR（允许地址复用）
    """)

    def server() -> None:
        """服务器：快速关闭连接以产生TIME_WAIT。"""
        print("\n[服务器] 启动...")
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind(("127.0.0.1", 19995))
        server_sock.listen(5)

        for i in range(3):
            print(f"\n[服务器] 等待连接 #{i+1}...")
            conn, addr = server_sock.accept()
            print(f"[服务器] 连接 #{i+1} 建立: {addr}")

            # 快速处理
            conn.sendall(b"Quick response")
            conn.recv(1024)

            # 立即关闭
            conn.close()
            print(f"[服务器] 连接 #{i+1} 已关闭")

        server_sock.close()
        print(f"\n[服务器] 服务器关闭")

    def client() -> None:
        """客户端：发起多个连接，观察TIME_WAIT。"""
        time.sleep(0.2)

        print("\n[客户端] 创建多个连接...")
        for i in range(3):
            print(f"\n[客户端] 连接 #{i+1}...")
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_sock.connect(("127.0.0.1", 19995))

            # 接收响应
            data = client_sock.recv(1024)
            print(f"[客户端] 收到: {data.decode()}")

            # 关闭
            client_sock.close()
            print(f"[客户端] 连接 #{i+1} 关闭")
            print(f"[客户端]     -> 将进入TIME_WAIT状态（持续2*MSL）")

            time.sleep(0.1)

        print(f"\n[客户端] 检查系统TIME_WAIT连接:")
        print(f"[客户端] 在Linux上可以执行: netstat -an | grep TIME_WAIT")
        print(f"[客户端] 或: ss -tan | grep TIME_WAIT")
        print(f"[客户端] 应该能看到多个19995端口的TIME_WAIT连接")

    # 启动服务器和客户端
    server_thread = threading.Thread(target=server, daemon=False)
    server_thread.start()

    client()
    server_thread.join(timeout=5)


# =============================================================================
# SO_LINGER 选项演示
# =============================================================================


def demo_so_linger() -> None:
    """示例 06：SO_LINGER选项 - 控制关闭行为。"""
    print_separator("SO_LINGER 选项演示")

    print("""
    SO_LINGER选项控制close()的行为：

    struct linger {
        int l_onoff;    // 是否启用
        int l_linger;   // 拖延时间（秒）
    };

    三种模式：
    1. l_onoff=0: 关闭SO_LINGER（默认）
       - close()立即返回
       - 内核发送剩余数据
       - 主动方进入TIME_WAIT

    2. l_onoff=1, l_linger=0: 启用但等待时间为0
       - 丢弃发送缓冲区数据
       - 发送RST（复位）而不是FIN
       - 不进入TIME_WAIT
       - 可能导致对方数据丢失

    3. l_onoff=1, l_linger>0: 等待指定时间
       - 等待数据发送和ACK接收
       - 超时后强制关闭
       - 不进入TIME_WAIT
    """)

    def demo_no_linger() -> None:
        """默认行为：无SO_LINGER。"""
        print("\n[演示] 默认行为（无SO_LINGER）:")
        print("  close()立即返回，内核继续发送数据")
        print("  进入TIME_WAIT状态")

    def demo_linger_zero() -> None:
        """l_linger=0：强制关闭。"""
        print("\n[演示] SO_LINGER with l_linger=0:")
        print("  发送RST而不是FIN")
        print("  不进入TIME_WAIT")
        print("  对方收到'Connection reset by peer'")

    def demo_linger_positive() -> None:
        """l_linger>0：等待指定时间。"""
        print("\n[演示] SO_LINGER with l_linger=2:")
        print("  等待2秒让数据发送和ACK接收")
        print("  超时后强制关闭")
        print("  不进入TIME_WAIT")

    # 展示代码结构（不实际运行，因为需要更复杂的设置）
    print("\n[代码示例]")
    print("""
    import socket
    import struct

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置SO_LINGER (l_onoff=1, l_linger=0)
    linger_data = struct.pack('ii', 1, 0)  # l_onoff=1, l_linger=0
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, linger_data)

    # 连接和通信...
    # ...

    # 关闭时会发送RST
    sock.close()
    """)

    demo_no_linger()
    demo_linger_zero()
    demo_linger_positive()


# =============================================================================
# 主函数
# =============================================================================


def main() -> None:
    """运行所有演示。"""
    demo_three_way_handshake()
    demo_four_way_wave()
    demo_half_close()
    demo_connection_state_monitoring()
    demo_time_wait_state()
    demo_so_linger()

    print_separator("总结")
    print("""
    TCP连接状态要点：

    1. 三次握手：
       - SYN -> SYN-ACK -> ACK
       - connect()和accept()在握手完成后返回
       - 状态: SYN_SENT <-> SYN_RCVD -> ESTABLISHED

    2. 四次挥手：
       - FIN -> ACK -> FIN -> ACK
       - 主动关闭方经历FIN_WAIT状态
       - 被动关闭方经历CLOSE_WAIT状态

    3. 半关闭：
       - shutdown(SHUT_WR)关闭写端，保留读端
       - 允许单向数据传输
       - HTTP常用模式

    4. TIME_WAIT：
       - 持续2*MSL（通常60秒）
       - 只有主动关闭方进入
       - SO_REUSEADDR允许地址复用

    5. 监控方法：
       - getsockname(): 本地地址
       - getpeername(): 远程地址
       - getsockopt(): 读取socket选项
       - fileno(): 文件描述符

    推荐工具：
    - netstat -an: 查看所有TCP连接
    - ss -tan: 查看TCP连接状态
    - tcpdump/wireshark: 抓包分析
    - /proc/net/tcp: Linux内核TCP状态
    """)


if __name__ == "__main__":
    main()
