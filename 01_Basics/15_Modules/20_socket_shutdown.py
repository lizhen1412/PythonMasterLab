#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 20：Socket 优雅关闭 - shutdown() 方法。
Author: Lambert

- socket.shutdown() 的三种模式：SHUT_RD、SHUT_WR、SHUT_RDWR
- shutdown() 与 close() 的区别
- 半关闭场景：关闭写但保持读
- 优雅关闭流程的最佳实践
- TCP FIN 包的发送与接收
"""

from __future__ import annotations

import socket
import threading
import time
from typing import NoReturn


def demo_shutdown_modes() -> None:
    """演示 shutdown() 的三种模式。"""
    print("== Socket Shutdown 模式演示 ==\n")

    print("1. shutdown() 的三种模式:")
    print(f"   SHUT_RD ({socket.SHUT_RD}):  关闭读取端，不再接收数据")
    print(f"   SHUT_WR ({socket.SHUT_WR}):  关闭写入端，不再发送数据（发送 FIN）")
    print(f"   SHUT_RDWR ({socket.SHUT_RDWR}): 关闭读写两端")

    print("\n2. shutdown() 与 close() 的区别:")
    print("   shutdown():")
    print("     - 立即发送 TCP FIN 包，通知对端关闭连接")
    print("     - 可以选择只关闭读或写（半关闭）")
    print("     - 可以多次调用不同模式")
    print("   close():")
    print("     - 完全关闭套接字，释放资源")
    print("     - 相当于 shutdown(SHUT_RDWR) + 清理")
    print("     - 只能调用一次")

    print("\n3. 半关闭（Half-Close）场景:")
    print("   客户端 shutdown(SHUT_WR) -> 发送 FIN ->")
    print("   服务器仍可向客户端发送数据 ->")
    print("   服务器关闭 -> 客户端接收 FIN -> 连接结束")


def demo_shutdown_write_only() -> None:
    """演示关闭写端但保持读（常见于 HTTP 请求）。"""
    print("\n== 关闭写端，保持读（SHUT_WR）==\n")

    def server() -> None:
        """服务器：接收请求后发送响应。"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(("127.0.0.1", 19001))
            server_sock.listen(1)
            print(f"[服务器] 监听 127.0.0.1:19001")

            conn, addr = server_sock.accept()
            with conn:
                print(f"[服务器] 客户端已连接: {addr}")

                # 接收客户端数据
                data = conn.recv(1024)
                if data:
                    print(f"[服务器] 收到请求: {data.decode()}")

                    # 客户端关闭写端后，服务器仍可发送响应
                    response = b"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, Client!"
                    conn.sendall(response)
                    print(f"[服务器] 已发送响应")

                # 检测到客户端关闭（recv 返回空）
                more_data = conn.recv(1024)
                if not more_data:
                    print(f"[服务器] 检测到客户端关闭写端")

    def client() -> None:
        """客户端：发送请求后关闭写端，等待响应。"""
        time.sleep(0.1)  # 等待服务器启动

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", 19001))
            print(f"[客户端] 已连接到服务器")

            # 发送请求
            request = b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
            sock.sendall(request)
            print(f"[客户端] 已发送请求")

            # 关闭写端（发送 FIN），但保持读
            # 这告诉服务器："我发送完了，但你还可以继续发"
            sock.shutdown(socket.SHUT_WR)
            print(f"[客户端] 已关闭写端（SHUT_WR）")

            # 仍然可以接收服务器响应
            response = sock.recv(1024)
            if response:
                print(f"[客户端] 收到响应: {response.decode()[:50]}...")

            # 最终关闭读端
            print(f"[客户端] 通信结束")

    # 启动服务器和客户端
    server_thread = threading.Thread(target=server, daemon=True)
    server_thread.start()

    client()
    server_thread.join(timeout=2)


def demo_shutdown_read_only() -> None:
    """演示关闭读端（较少使用）。"""
    print("\n== 关闭读端（SHUT_RD）==\n")

    def server() -> None:
        """服务器：持续发送数据。"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(("127.0.0.1", 19002))
            server_sock.listen(1)

            conn, addr = server_sock.accept()
            with conn:
                print(f"[服务器] 客户端已连接: {addr}")

                # 尝试发送多条消息
                for i in range(3):
                    try:
                        msg = f"Message {i}".encode()
                        conn.sendall(msg)
                        print(f"[服务器] 发送: Message {i}")
                        time.sleep(0.1)
                    except OSError as e:
                        print(f"[服务器] 发送失败: {e}")
                        break

                # 检测客户端是否关闭读端
                try:
                    conn.send(b"Final check")
                except OSError:
                    print(f"[服务器] 客户端已关闭读端")

    def client() -> None:
        """客户端：接收部分数据后关闭读端。"""
        time.sleep(0.1)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", 19002))
            print(f"[客户端] 已连接")

            # 接收一条消息
            data = sock.recv(1024)
            print(f"[客户端] 收到: {data.decode()}")

            # 关闭读端（不再接收，但仍可发送）
            sock.shutdown(socket.SHUT_RD)
            print(f"[客户端] 已关闭读端（SHUT_RD）")

            # 服务器后续发送的数据会被丢弃（TCP 栈自动回复 ACK）
            time.sleep(0.3)

            # 仍可发送数据
            sock.sendall(b"Client message")
            print(f"[客户端] 仍可发送数据")

    server_thread = threading.Thread(target=server, daemon=True)
    server_thread.start()

    client()
    server_thread.join(timeout=2)


def demo_graceful_shutdown() -> None:
    """演示优雅关闭流程（生产环境最佳实践）。"""
    print("\n== 优雅关闭流程（生产环境）==\n")

    def echo_server() -> None:
        """Echo 服务器：支持优雅关闭。"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("127.0.0.1", 19003))
        server_socket.listen(5)
        server_socket.settimeout(1.0)  # 允许定期检查

        print(f"[服务器] 监听 127.0.0.1:19003")

        running = True
        connections = []

        try:
            while running:
                try:
                    conn, addr = server_socket.accept()
                    print(f"[服务器] 新连接: {addr}")
                    connections.append(conn)
                except socket.timeout:
                    continue

                # 处理所有连接
                for conn in connections[:]:
                    try:
                        conn.settimeout(0.1)
                        data = conn.recv(1024)
                        if data:
                            print(f"[服务器] 收到: {data.decode()}")
                            conn.sendall(data)  # Echo
                        else:
                            # 客户端关闭连接
                            print(f"[服务器] 客户端断开")
                            connections.remove(conn)
                            conn.close()
                    except socket.timeout:
                        continue
                    except OSError:
                        connections.remove(conn)
                        conn.close()

        finally:
            # 优雅关闭：先关闭所有连接
            print(f"[服务器] 正在优雅关闭...")
            for conn in connections:
                try:
                    # 发送关闭通知
                    conn.sendall(b"Server shutting down...")
                    conn.shutdown(socket.SHUT_WR)
                    conn.close()
                except OSError:
                    conn.close()

            server_socket.close()
            print(f"[服务器] 已关闭")

    def graceful_client() -> None:
        """客户端：演示优雅关闭流程。"""
        time.sleep(0.1)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", 19003))

            # 发送消息
            sock.sendall(b"Hello!")
            response = sock.recv(1024)
            print(f"[客户端] 收到: {response.decode()}")

            # 优雅关闭：先 shutdown 写端，等待响应完成
            sock.shutdown(socket.SHUT_WR)
            print(f"[客户端] 已关闭写端")

            # 等待服务器可能的最后消息
            time.sleep(0.2)
            final = sock.recv(1024)
            if final:
                print(f"[客户端] 收到: {final.decode()}")

    server_thread = threading.Thread(target=echo_server, daemon=True)
    server_thread.start()

    graceful_client()
    time.sleep(0.5)


def demo_bidirectional_shutdown() -> None:
    """演示双向关闭（完整关闭流程）。"""
    print("\n== 双向关闭（SHUT_RDWR）==\n")

    def server() -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(("127.0.0.1", 19004))
            server_sock.listen(1)

            conn, addr = server_sock.accept()
            with conn:
                print(f"[服务器] 客户端已连接: {addr}")

                data = conn.recv(1024)
                print(f"[服务器] 收到: {data.decode()}")

                # 发送响应后立即关闭
                conn.sendall(b"Response")
                # shutdown(SHUT_RDWR) 立即发送 FIN
                conn.shutdown(socket.SHUT_RDWR)
                print(f"[服务器] 已执行 shutdown(SHUT_RDWR)")

    def client() -> None:
        time.sleep(0.1)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", 19004))
            print(f"[客户端] 已连接")

            sock.sendall(b"Request")
            print(f"[客户端] 已发送请求")

            # 接收响应
            response = sock.recv(1024)
            print(f"[客户端] 收到: {response.decode()}")

            # 检测到服务器关闭（recv 返回空）
            data = sock.recv(1024)
            if not data:
                print(f"[客户端] 检测到服务器已关闭（收到 FIN）")

    server_thread = threading.Thread(target=server, daemon=True)
    server_thread.start()

    client()
    server_thread.join(timeout=2)


def main() -> None:
    demo_shutdown_modes()
    demo_shutdown_write_only()
    demo_shutdown_read_only()
    demo_graceful_shutdown()
    demo_bidirectional_shutdown()

    print("\n== Socket Shutdown 最佳实践 ==\n")
    print("场景                    | 推荐方式")
    print("------------------------|-------------------------------------")
    print("HTTP 客户端            | 发送请求后 shutdown(SHUT_WR)")
    print("HTTP 服务器            | 发送响应后 close()")
    print("长连接服务器            | 先 shutdown(SHUT_WR)，再 close()")
    print("客户端主动关闭          | shutdown(SHUT_WR) -> 等待响应 -> close()")
    print("服务器主动关闭          | 发送关闭通知 -> shutdown(SHUT_RDWR) -> close()")
    print("\n提示：shutdown() 后，套接字仍需调用 close() 释放资源！")


if __name__ == "__main__":
    main()
