#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：socketserver 生产环境模式 - serve_forever() 和 shutdown()。
Author: Lambert

本示例演示 socketserver 的生产环境级用法：

1. **serve_forever()** - 永久运行服务器（处理多个连接）
2. **shutdown()** - 优雅关闭服务器
3. **server_close()** - 立即关闭服务器
4. 自定义服务器类（重写关键方法）
5. 信号处理和优雅关闭
6. 服务器状态监控

关键概念：
- serve_forever() 会持续处理请求，直到调用 shutdown()
- shutdown() 必须在单独的线程中调用（因为 serve_forever() 会阻塞）
- shutdown() 会等待当前请求处理完成
- 使用 ThreadingMixIn 实现并发处理
"""

from __future__ import annotations

import socketserver
import socket
import threading
import time
import signal
from typing import ClassVar


# =============================================================================
# 基础示例：serve_forever() 对比 handle_request()
# =============================================================================


def demo_serve_forever_vs_handle_request() -> None:
    """示例 01：serve_forever() 与 handle_request() 的对比。"""
    print("== serve_forever() vs handle_request() ==\n")

    class EchoHandler(socketserver.BaseRequestHandler):
        """Echo 处理器。"""

        def handle(self) -> None:
            data = self.request.recv(1024)
            print(f"[服务器] 收到: {data.decode()}")
            self.request.sendall(data)

    # 使用 handle_request()
    print("1. 使用 handle_request() - 处理单个请求:")
    with socketserver.TCPServer(("127.0.0.1", 19101), EchoHandler) as server:
        print(f"   服务器启动: {server.server_address}")
        print(f"   handle_request() 只处理一个连接后退出")

        # 在线程中模拟客户端
        def client():
            time.sleep(0.1)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(("127.0.0.1", 19101))
                sock.sendall(b"Hello 1")
                sock.recv(1024)

        client_thread = threading.Thread(target=client, daemon=True)
        client_thread.start()
        server.handle_request()  # 只处理一个请求
        client_thread.join(timeout=1)

    print(f"   服务器已退出\n")

    # 使用 serve_forever()
    print("2. 使用 serve_forever() - 持续处理请求:")
    with socketserver.TCPServer(("127.0.0.1", 19102), EchoHandler) as server:
        print(f"   服务器启动: {server.server_address}")
        print(f"   serve_forever() 会持续运行直到 shutdown()")

        # 在线程中运行服务器
        def run_server():
            server.serve_forever(timeout=2)  # timeout 参数用于定期检查

        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()

        # 模拟多个客户端
        for i in range(3):
            time.sleep(0.2)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(("127.0.0.1", 19102))
                sock.sendall(f"Hello {i+1}".encode())
                response = sock.recv(1024)
                print(f"   客户端 {i+1} 收到: {response.decode()}")

        # 关闭服务器
        print(f"   调用 shutdown()...")
        server.shutdown()
        server_thread.join(timeout=1)
        print(f"   服务器已停止")


# =============================================================================
# 优雅关闭模式
# =============================================================================


def demo_graceful_shutdown() -> None:
    """示例 02：优雅关闭 - shutdown() 的正确使用。"""
    print("\n\n== 优雅关闭模式 ==\n")

    class CountingHandler(socketserver.BaseRequestHandler):
        """计数处理器。"""
        request_count: ClassVar[int] = 0

        def handle(self) -> None:
            CountingHandler.request_count += 1
            count = CountingHandler.request_count

            data = self.request.recv(1024)
            print(f"[服务器] 处理请求 #{count}: {data.decode()}")

            # 模拟处理时间
            time.sleep(0.3)

            self.request.sendall(f"Response #{count}".encode())
            print(f"[服务器] 完成 #{count}")

    class CustomServer(socketserver.TCPServer):
        """自定义服务器：支持优雅关闭。"""
        allow_reuse_address: ClassVar[bool] = True
        shutdown_flag = False

        def serve_forever(self, poll_interval: float = 0.5) -> None:
            """重写 serve_forever 以支持关闭标志。"""
            print(f"[服务器] 启动 serve_forever()...")
            super().serve_forever(poll_interval)
            print(f"[服务器] serve_forever() 已退出")

        def shutdown(self) -> None:
            """重写 shutdown 以添加日志。"""
            print(f"[服务器] 开始 shutdown()...")
            super().shutdown()
            print(f"[服务器] shutdown() 完成")

    # 创建服务器
    server = CustomServer(("127.0.0.1", 19103), CountingHandler)

    # 在线程中运行服务器
    server_thread = threading.Thread(target=server.serve_forever, daemon=False)
    server_thread.start()

    time.sleep(0.2)

    # 发送多个请求
    print("[客户端] 发送 5 个请求...")
    clients = []
    for i in range(5):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 19103))
        client.sendall(f"Request-{i+1}".encode())
        clients.append(client)
        time.sleep(0.1)  # 错开发送时间

    print("[客户端] 等待响应...")
    for i, client in enumerate(clients, 1):
        response = client.recv(1024)
        print(f"[客户端-{i}] 收到: {response.decode()}")
        client.close()

    # 等待处理完成
    time.sleep(0.5)

    print("\n[主控] 调用 shutdown()...")
    server.shutdown()
    server_thread.join(timeout=2)

    print(f"[主控] 服务器已关闭，总计处理 {CountingHandler.request_count} 个请求")
    server.server_close()


# =============================================================================
# ThreadingMixIn + serve_forever
# =============================================================================


def demo_threading_serve_forever() -> None:
    """示例 03：ThreadingMixIn + serve_forever 并发服务器。"""
    print("\n\n== ThreadingMixIn + serve_forever ==\n")

    class ThreadedEchoHandler(socketserver.BaseRequestHandler):
        """Echo 处理器。"""

        def handle(self) -> None:
            thread_id = threading.get_ident()
            data = self.request.recv(1024)
            print(f"[Thread-{thread_id}] 收到: {data.decode()}")

            # 模拟处理
            time.sleep(0.5)

            self.request.sendall(data)
            print(f"[Thread-{thread_id}] 发送回显")

    class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        """线程化 TCP 服务器。"""
        allow_reuse_address: ClassVar[bool] = True
        daemon_threads: ClassVar[bool] = True

    server = ThreadedTCPServer(("127.0.0.1", 19104), ThreadedEchoHandler)

    # 启动服务器
    server_thread = threading.Thread(target=server.serve_forever, daemon=False)
    server_thread.start()
    print(f"[服务器] 启动: {server.server_address}")

    # 多个并发客户端
    print("\n[客户端] 启动 5 个并发连接...")

    def client_worker(client_id: int) -> None:
        """客户端工作协程。"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", 19104))
            message = f"Client-{client_id}"
            sock.sendall(message.encode())

            start = time.time()
            response = sock.recv(1024)
            elapsed = time.time() - start

            print(f"[Client-{client_id}] 收到: {response.decode()} | 耗时: {elapsed:.2f}s")

    # 启动客户端线程
    client_threads = []
    for i in range(5):
        t = threading.Thread(target=client_worker, args=(i,), daemon=True)
        t.start()
        client_threads.append(t)

    # 等待所有客户端完成
    for t in client_threads:
        t.join(timeout=3)

    # 关闭服务器
    print(f"\n[主控] 关闭服务器...")
    server.shutdown()
    server_thread.join(timeout=2)
    server.server_close()
    print(f"[主控] 服务器已关闭")


# =============================================================================
# 信号处理和优雅关闭
# =============================================================================


def demo_signal_handling() -> None:
    """示例 04：信号处理 - Ctrl+C 优雅关闭。"""
    print("\n\n== 信号处理和优雅关闭 ==\n")

    class GracefulHandler(socketserver.BaseRequestHandler):
        """处理器。"""

        def handle(self) -> None:
            try:
                self.request.settimeout(1.0)  # 设置超时
                data = self.request.recv(1024)
                if data:
                    print(f"[服务器] 处理: {data.decode()}")
                    self.request.sendall(b"OK")
            except socket.timeout:
                pass

    class GracefulServer(socketserver.TCPServer):
        """支持优雅关闭的服务器。"""
        allow_reuse_address: ClassVar[bool] = True

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.shutdown_flag = False

        def shutdown(self) -> None:
            """关闭服务器。"""
            self.shutdown_flag = True
            super().shutdown()

    server = GracefulServer(("127.0.0.1", 19105), GracefulHandler)

    # 信号处理函数
    def signal_handler(signum, frame):
        print(f"\n[信号] 收到信号 {signum}，准备关闭服务器...")
        server.shutdown()

    # 注册信号处理
    signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGTERM, signal_handler)  # Unix only

    # 启动服务器
    server_thread = threading.Thread(target=server.serve_forever, daemon=False)
    server_thread.start()

    print(f"[服务器] 启动: {server.server_address}")
    print(f"[提示] 按 Ctrl+C 测试优雅关闭（或在 2 秒后自动关闭）")

    # 模拟一段时间后关闭
    time.sleep(2)
    if not server.shutdown_flag:
        print(f"\n[主控] 超时，自动关闭...")
        server.shutdown()

    server_thread.join(timeout=2)
    server.server_close()
    print(f"[主控] 服务器已关闭")


# =============================================================================
# 自定义服务器方法
# =============================================================================


def demo_custom_server_methods() -> None:
    """示例 05：自定义服务器方法。"""
    print("\n\n== 自定义服务器方法 ==\n")

    class LoggingHandler(socketserver.BaseRequestHandler):
        """带日志的处理器。"""

        def setup(self) -> None:
            """连接建立时调用。"""
            print(f"[Handler] 连接建立: {self.client_address}")
            super().setup()

        def handle(self) -> None:
            """处理请求。"""
            data = self.request.recv(1024)
            print(f"[Handler] 处理: {data.decode()}")
            self.request.sendall(data)

        def finish(self) -> None:
            """连接关闭时调用。"""
            print(f"[Handler] 连接关闭: {self.client_address}")
            super().finish()

    class CustomServer(socketserver.TCPServer):
        """自定义服务器。"""
        allow_reuse_address: ClassVar[bool] = True

        def __init__(self, *args, **kwargs):
            self.request_count = 0
            super().__init__(*args, **kwargs)

        def server_bind(self) -> None:
            """重写绑定行为。"""
            print(f"[服务器] 绑定地址: {self.server_address}")
            super().server_bind()

        def server_activate(self) -> None:
            """重写激活行为。"""
            print(f"[服务器] 激活服务器")
            super().server_activate()

        def get_request(self) -> tuple[object, str]:
            """重写请求获取。"""
            request, client_address = super().get_request()
            self.request_count += 1
            print(f"[服务器] 接受请求 #{self.request_count}: {client_address}")
            return request, client_address

    server = CustomServer(("127.0.0.1", 19106), LoggingHandler)

    # 启动服务器
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    # 测试连接
    time.sleep(0.1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", 19106))
        sock.sendall(b"Test")
        sock.recv(1024)

    time.sleep(0.1)

    # 关闭
    server.shutdown()
    server_thread.join(timeout=1)
    server.server_close()
    print(f"\n[主控] 总计处理 {server.request_count} 个请求")


# =============================================================================
# 服务器状态监控
# =============================================================================


def demo_server_monitoring() -> None:
    """示例 06：服务器状态监控。"""
    print("\n\n== 服务器状态监控 ==\n")

    class MonitoringHandler(socketserver.BaseRequestHandler):
        """处理器。"""
        active_connections: ClassVar[int] = 0

        def setup(self) -> None:
            MonitoringHandler.active_connections += 1
            print(f"[监控] 活跃连接: {MonitoringHandler.active_connections}")
            super().setup()

        def handle(self) -> None:
            self.request.sendall(b"Ping")
            time.sleep(0.5)  # 模拟处理

        def finish(self) -> None:
            MonitoringHandler.active_connections -= 1
            print(f"[监控] 活跃连接: {MonitoringHandler.active_connections}")
            super().finish()

    class MonitoredServer(socketserver.TCPServer):
        """被监控的服务器。"""
        allow_reuse_address: ClassVar[bool] = True

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.requests_handled = 0

        def get_request(self) -> tuple[object, str]:
            """统计请求数。"""
            request, client_address = super().get_request()
            self.requests_handled += 1
            print(f"[监控] 总请求: {self.requests_handled}")
            return request, client_address

    server = MonitoredServer(("127.0.0.1", 19107), MonitoringHandler)

    # 启动服务器
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    # 监控线程
    def monitor_thread():
        for i in range(3):
            time.sleep(0.3)
            print(f"[监控] 快照 - 请求: {server.requests_handled}, 活跃: {MonitoringHandler.active_connections}")

    monitor = threading.Thread(target=monitor_thread, daemon=True)
    monitor.start()

    # 发起多个连接
    clients = []
    for i in range(3):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 19107))
        client.recv(1024)
        clients.append(client)

    time.sleep(0.3)
    for client in clients:
        client.close()

    monitor.join(timeout=2)

    # 关闭
    server.shutdown()
    server_thread.join(timeout=1)
    server.server_close()

    print(f"\n[统计] 总请求: {server.requests_handled}")


# =============================================================================
# 最佳实践总结
# =============================================================================


def demo_best_practices() -> None:
    """示例 07：生产环境最佳实践。"""
    print("\n\n== 生产环境最佳实践 ==\n")

    print("1. 使用 ThreadingMixIn 实现并发:")
    print("   class ThreadedServer(ThreadingMixIn, TCPServer): ...")

    print("\n2. 设置 daemon_threads = True:")
    print("   daemon_threads = True  # 允许主线程退出时自动终止")

    print("\n3. 设置 allow_reuse_address = True:")
    print("   allow_reuse_address = True  # 避免 TIME_WAIT 问题")

    print("\n4. shutdown() 必须在单独线程调用:")
    print("   server_thread = Thread(target=server.serve_forever)")
    print("   server_thread.start()")
    print("   # ...")
    print("   server.shutdown()  # 在主线程或其他线程")
    print("   server_thread.join()")

    print("\n5. 实现信号处理:")
    print("   signal.signal(signal.SIGINT, handler)")
    print("   def handler(signum, frame):")
    print("       server.shutdown()")

    print("\n6. 添加超时和日志:")
    print("   def serve_forever(self, poll_interval=0.5):")
    print("       # 添加监控逻辑")


def main() -> None:
    """运行所有示例。"""
    demo_serve_forever_vs_handle_request()
    demo_graceful_shutdown()
    demo_threading_serve_forever()
    demo_signal_handling()
    demo_custom_server_methods()
    demo_server_monitoring()
    demo_best_practices()

    print("\n" + "="*60)
    print("socketserver 核心方法速查")
    print("="*60)
    print("\n服务器生命周期:")
    print("  server_bind()         绑定地址")
    print("  server_activate()     开始监听")
    print("  serve_forever()       持续处理请求（阻塞）")
    print("  handle_request()      处理单个请求")
    print("  shutdown()            优雅关闭（停止 serve_forever）")
    print("  server_close()        关闭套接字")
    print("\n处理器生命周期:")
    print("  __init__()            创建处理器实例")
    print("  setup()               连接建立时调用")
    print("  handle()              处理请求")
    print("  finish()              连接关闭时调用")
    print("\nThreadingMixIn:")
    print("  daemon_threads        True = 主线程退出时终止工作线程")
    print("\n重要提示:")
    print("  - shutdown() 必须在单独线程调用")
    print("  - shutdown() 会等待当前请求完成")
    print("  - ThreadingMixIn 自动为每个请求创建新线程")


if __name__ == "__main__":
    main()
