#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 22：Socket 高级 I/O 操作。
Author: Lambert

本示例演示 socket 库的高级 I/O 操作：

1. **socket.getpeername()** - 获取对端地址信息
2. **socket.makefile()** - 将 socket 包装为文件对象
3. **socket.recv_into(buffer)** - 接收数据到预分配缓冲区（零拷贝）
4. **socket.sendfile(file)** - 高效文件传输（零拷贝优化）
5. **socket.dup()** - 复制 socket
6. **socket.detach()** - 分离文件描述符
7. **socket.fileno()** - 获取文件描述符

这些API提供了更底层、更高效的 socket 操作方式。
"""

from __future__ import annotations

import socket
import io
import os
import threading
import time
from pathlib import Path
from typing import Any


# =============================================================================
# socket.getpeername() - 获取对端地址
# =============================================================================


def demo_getpeername() -> None:
    """示例 01：getpeername() - 获取远程socket地址。"""
    print("== socket.getpeername() - 获取对端地址 ==\n")

    def server() -> None:
        """服务器：接受连接并获取客户端地址。"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(("127.0.0.1", 20001))
            server_sock.listen(1)
            print(f"[服务器] 监听: {server_sock.getsockname()}")

            conn, client_addr = server_sock.accept()
            with conn:
                print(f"[服务器] 客户端地址: {client_addr}")

                # 使用 getpeername 获取对端信息
                peer = conn.getpeername()
                print(f"[服务器] getpeername(): {peer}")
                print(f"[服务器] 对端IP: {peer[0]}")
                print(f"[服务器] 对端端口: {peer[1]}")

                # 对比 getsockname
                local = conn.getsockname()
                print(f"[服务器] getsockname(): {local}")
                print(f"[服务器] 本地IP: {local[0]}")
                print(f"[服务器] 本地端口: {local[1]}")

                # 接收数据
                data = conn.recv(1024)
                print(f"[服务器] 收到: {data.decode()}")

    def client() -> None:
        """客户端：连接并查看服务器信息。"""
        time.sleep(0.1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", 20001))

            # 连接后查看对端地址
            peer = sock.getpeername()
            print(f"[客户端] 连接到服务器: {peer}")

            # 查看本地地址
            local = sock.getsockname()
            print(f"[客户端] 本地绑定地址: {local}")

            # 发送数据
            sock.sendall(b"Hello from client")
            print(f"[客户端] 数据已发送")

    server_thread = threading.Thread(target=server, daemon=True)
    server_thread.start()

    client()
    server_thread.join(timeout=2)

    print("\n提示：getpeername() 只在连接状态下可用，未连接时会抛出 OSError")


# =============================================================================
# socket.makefile() - 创建文件对象
# =============================================================================


def demo_makefile() -> None:
    """示例 02：makefile() - 将socket包装为文件对象。"""
    print("\n\n== socket.makefile() - 文件对象包装 ==\n")

    def server() -> None:
        """服务器：使用文件对象读写。"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(("127.0.0.1", 20002))
            server_sock.listen(1)

            conn, addr = server_sock.accept()
            with conn:
                print(f"[服务器] 连接: {addr}")

                # 将 socket 包装为文件对象
                # mode='rb' 表示二进制读模式
                sock_file = conn.makefile('rb')

                print(f"[服务器] makefile() 类型: {type(sock_file)}")
                print(f"[服务器] 可以像文件一样读取")

                # 使用文件对象的 read() 方法
                # 这会一直读取直到连接关闭
                data = sock_file.read()
                print(f"[服务器] 读取到数据: {data.decode()}")

                # 关闭文件对象（不会关闭底层socket）
                sock_file.close()
                print(f"[服务器] 文件对象已关闭")

    def client() -> None:
        """客户端：发送多行数据。"""
        time.sleep(0.1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", 20002))

            # 发送多行数据
            lines = [
                b"First line\n",
                b"Second line\n",
                b"Third line\n",
            ]
            for line in lines:
                sock.sendall(line)
            print(f"[客户端] 发送了 {len(lines)} 行数据")

            # 半关闭，表示发送完成
            sock.shutdown(socket.SHUT_WR)

    server_thread = threading.Thread(target=server, daemon=True)
    server_thread.start()

    client()
    server_thread.join(timeout=2)

    print("\nmakefile() 优势:")
    print("  - 可以使用文件API（readline(), read(), etc.）")
    print("  - 自动处理缓冲")
    print("  - 与代码库集成（接受文件对象）")

    print("\n注意事项:")
    print("  - makefile() 后，socket和file对象共享缓冲区")
    print("  - 不要同时使用socket和file对象的send/recv")
    print("  - 关闭file对象不会关闭socket")


# =============================================================================
# socket.recv_into() - 接收到缓冲区
# =============================================================================


def demo_recv_into() -> None:
    """示例 03：recv_into() - 零拷贝接收。"""
    print("\n\n== socket.recv_into() - 接收到预分配缓冲区 ==\n")

    def server() -> None:
        """服务器：发送数据。"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(("127.0.0.1", 20003))
            server_sock.listen(1)

            conn, addr = server_sock.accept()
            with conn:
                print(f"[服务器] 连接: {addr}")

                # 发送多次数据
                for i in range(3):
                    message = f"Message-{i}".encode()
                    conn.sendall(message)
                    print(f"[服务器] 发送: {message.decode()}")
                    time.sleep(0.1)

                print(f"[服务器] 发送完成")

    def client() -> None:
        """客户端：使用预分配缓冲区接收。"""
        time.sleep(0.1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", 20003))

            # 预分配缓冲区（bytearray）
            # recv_into 会直接写入这个缓冲区，无需额外的内存拷贝
            buffer = bytearray(1024)

            print(f"[客户端] 预分配缓冲区: {len(buffer)} 字节")

            total_received = 0
            while True:
                # recv_into 返回实际接收的字节数
                n = sock.recv_into(buffer, 1024)
                if n == 0:
                    # 连接关闭
                    break

                total_received += n
                print(f"[客户端] 接收到 {n} 字节")
                print(f"[客户端] 内容: {buffer[:n].decode()}")

                # 清空缓冲区（为下次接收做准备）
                buffer = bytearray(1024)

            print(f"[客户端] 总共接收: {total_received} 字节")

    server_thread = threading.Thread(target=server, daemon=True)
    server_thread.start()

    client()
    server_thread.join(timeout=2)

    print("\nrecv_into() 优势:")
    print("  - 零拷贝：直接写入预分配的缓冲区")
    print("  - 减少内存分配和垃圾回收")
    print("  - 适合高性能场景")

    print("\nvs recv():")
    print("  - recv() 返回新 bytes 对象")
    print("  - recv_into() 写入现有缓冲区")


# =============================================================================
# socket.sendfile() - 高效文件传输
# =============================================================================


def demo_sendfile() -> None:
    """示例 04：sendfile() - 零拷贝文件传输。"""
    print("\n\n== socket.sendfile() - 高效文件传输 ==\n")

    # 创建临时文件
    temp_file = Path("/tmp/sendfile_demo.txt")
    temp_file.write_text("A" * 10000)  # 10KB 数据

    def server() -> None:
        """服务器：接收文件。"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(("127.0.0.1", 20004))
            server_sock.listen(1)

            conn, addr = server_sock.accept()
            with conn:
                print(f"[服务器] 连接: {addr}")

                # 接收数据
                total = 0
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    total += len(data)
                print(f"[服务器] 接收完毕: {total} 字节")

    def client() -> None:
        """客户端：使用 sendfile 发送文件。"""
        time.sleep(0.1)

        # 打开文件
        with open(temp_file, 'rb') as file:
            file_size = temp_file.stat().st_size

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(("127.0.0.1", 20004))
                print(f"[客户端] 连接到服务器")

                # 使用 sendfile 高效传输
                # sendfile 使用零拷贝技术，直接在内核空间传输数据
                start = time.time()
                sent = sock.sendfile(file)
                elapsed = time.time() - start

                print(f"[客户端] 发送文件: {sent} 字节")
                print(f"[客户端] 文件大小: {file_size} 字节")
                print(f"[客户端] 耗时: {elapsed:.6f} 秒")
                print(f"[客户端] 速度: {sent/elapsed/1024:.2f} KB/s")

                # 半关闭
                sock.shutdown(socket.SHUT_WR)

    server_thread = threading.Thread(target=server, daemon=True)
    server_thread.start()

    client()
    server_thread.join(timeout=5)

    # 清理
    temp_file.unlink(missing_ok=True)

    print("\nsendfile() 优势:")
    print("  - 零拷贝：数据直接在内核空间传输")
    print("  - 高性能：避免用户空间和内核空间的数据拷贝")
    print("  - 自动处理：一次系统调用完成整个文件传输")

    print("\n等效的Python代码（较慢）:")
    print("""
    # 传统方式：需要多次拷贝
    with open('file.txt', 'rb') as f:
        data = f.read()        # 文件 -> 用户空间
        sock.sendall(data)     # 用户空间 -> 内核空间

    # sendfile方式：零拷贝
    with open('file.txt', 'rb') as f:
        sock.sendfile(f)       # 直接在内核空间传输
    """)


# =============================================================================
# socket.fileno() - 文件描述符
# =============================================================================


def demo_fileno() -> None:
    """示例 05：fileno() - 获取文件描述符。"""
    print("\n\n== socket.fileno() - 文件描述符 ==\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"Socket 文件描述符: {sock.fileno()}")
    print(f"  - 这是操作系统分配的整数标识符")
    print(f"  - 用于 select/poll/epoll 等系统调用")

    print("\n使用 fileno() 的场景:")

    print("\n1. 与 select 配合:")
    print("""
    import select

    sock = socket.socket(...)
    fd = sock.fileno()

    # 等待socket可读
    readable, _, _ = select.select([fd], [], [])
    if fd in readable:
        data = sock.recv(1024)
    """)

    print("\n2. 与 os.fstat 配合:")
    try:
        stat = os.fstat(sock.fileno())
        print(f"   Socket stat: {stat}")
    except:
        pass

    print("\n3. 设置为非阻塞:")
    print("""
    import fcntl

    sock = socket.socket(...)
    fd = sock.fileno()

    # 设置为非阻塞模式
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
    """)

    sock.close()


# =============================================================================
# socket.dup() - 复制socket
# =============================================================================


def demo_dup() -> None:
    """示例 06：dup() - 复制socket。"""
    print("\n\n== socket.dup() - 复制Socket ==\n")

    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(("127.0.0.1", 0))

    print(f"原始 socket: {sock1.getsockname()}")

    # dup() 创建一个新的socket对象，共享相同的文件描述符
    sock2 = sock1.dup()

    print(f"复制的 socket: {sock2.getsockname()}")
    print(f"两者共享文件描述符: {sock1.fileno()} == {sock2.fileno()}")

    print("\ndup() 特点:")
    print("  - 创建新的socket对象")
    print("  - 共享相同的文件描述符")
    print("  - 可以独立关闭，不影响其他副本")
    print("  - 用于多线程/多进程共享socket")

    sock1.close()
    print(f"\n关闭 sock1 后:")
    print(f"  sock2 仍然可用: {not sock2._closed}")
    print(f"  sock2.fileno(): {sock2.fileno()}")

    sock2.close()


# =============================================================================
# socket.detach() - 分离文件描述符
# =============================================================================


def demo_detach() -> None:
    """示例 07：detach() - 分离文件描述符。"""
    print("\n\n== socket.detach() - 分离文件描述符 ==\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 0))

    fd = sock.fileno()
    print(f"原始 fileno: {fd}")

    # detach() 返回文件描述符，但socket对象不再管理它
    detached_fd = sock.detach()

    print(f"分离后的 fileno: {detached_fd}")
    print(f"socket对象 fileno: {sock.fileno() if not sock._closed else '(已分离)'}")

    print("\ndetach() 用途:")
    print("  - 将socket的控制权转移给其他代码")
    print("  - socket对象不会关闭文件描述符")
    print("  - 需要手动关闭文件描述符: os.close(detached_fd)")

    # 手动关闭
    os.close(detached_fd)


# =============================================================================
# socket.setinheritable() - 继承性设置
# =============================================================================


def demo_setinheritable() -> None:
    """示例 08：setinheritable() - 控制继承性。"""
    print("\n\n== socket.setinheritable() - 继承性设置 ==\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket 继承性:")
    print(f"  默认可继承: {sock.get_inheritable()}")

    # 设置为不可继承
    sock.set_inheritable(False)
    print(f"  设置不可继承: {sock.get_inheritable()}")

    print("\n继承性的意义:")
    print("  - 在 subprocess 中使用")
    print("  - 如果可继承：子进程可以访问这个socket")
    print("  - 如果不可继承：子进程无法访问")

    print("\n示例场景:")
    print("""
    import subprocess

    # 创建socket并设置为不可继承
    sock = socket.socket(...)
    sock.set_inheritable(False)

    # 启动子进程，子进程无法访问这个socket
    subprocess.Popen(['child_program'])
    """)

    sock.close()


# =============================================================================
# 综合示例：高性能文件传输服务器
# =============================================================================


def demo_high_performance_server() -> None:
    """示例 09：综合 - 高性能文件传输服务器。"""
    print("\n\n== 综合示例：高性能文件传输 ==\n")

    # 创建测试文件
    temp_file = Path("/tmp/large_file.dat")
    temp_file.write_bytes(b"X" * 102400)  # 100KB

    def server() -> None:
        """服务器：使用高级API优化性能。"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(("127.0.0.1", 20005))
            server_sock.listen(5)

            print(f"[服务器] 监听端口 20005")

            conn, addr = server_sock.accept()
            with conn:
                print(f"[服务器] 连接: {addr}")

                # 使用 makefile 包装，方便读取
                sock_file = conn.makefile('rb')

                # 读取数据
                total = 0
                for line in sock_file:
                    total += len(line)
                    if total >= 100000:
                        break

                sock_file.close()
                print(f"[服务器] 接收: {total} 字节")

    def client() -> None:
        """客户端：使用 sendfile 高效传输。"""
        time.sleep(0.1)

        with open(temp_file, 'rb') as file:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(("127.0.0.1", 20005))

                start = time.time()
                sent = sock.sendfile(file)
                elapsed = time.time() - start

                print(f"[客户端] 发送: {sent} 字节, 耗时: {elapsed:.6f} 秒")

                # 发送完成信号
                sock.shutdown(socket.SHUT_WR)

    server_thread = threading.Thread(target=server, daemon=True)
    server_thread.start()

    client()
    server_thread.join(timeout=5)

    # 清理
    temp_file.unlink(missing_ok=True)

    print("\n性能优化技巧总结:")
    print("  1. sendfile() - 零拷贝文件传输（最快）")
    print("  2. recv_into() - 减少内存分配")
    print("  3. makefile() - 简化代码，自动缓冲")
    print("  4. SO_REUSEADDR - 避免TIME_WAIT占用")
    print("  5. 设置合适的缓冲区大小")


# =============================================================================
# 主函数
# =============================================================================


def main() -> None:
    """运行所有示例。"""
    demo_getpeername()
    demo_makefile()
    demo_recv_into()
    demo_sendfile()
    demo_fileno()
    demo_dup()
    demo_detach()
    demo_setinheritable()
    demo_high_performance_server()

    print("\n" + "="*60)
    print("Socket 高级 I/O API 速查")
    print("="*60)
    print("\n获取信息:")
    print("  getpeername()    -> (host, port): 获取对端地址")
    print("  getsockname()    -> (host, port): 获取本地地址")
    print("  fileno()         -> int:          获取文件描述符")
    print("\n高级I/O:")
    print("  makefile(mode)   -> 文件对象:     包装为文件")
    print("  recv_into(buf)   -> int:          接收到缓冲区")
    print("  sendfile(file)   -> int:          零拷贝传输")
    print("\n复制/分离:")
    print("  dup()            -> socket:       复制socket")
    print("  detach()         -> int:          分离文件描述符")
    print("\n继承性:")
    print("  get_inheritable() -> bool:        检查是否可继承")
    print("  set_inheritable(bool):            设置继承性")
    print("\n性能建议:")
    print("  ✓ 大文件传输: 使用 sendfile()")
    print("  ✓ 减少拷贝: 使用 recv_into()")
    print("  ✓ 简化代码: 使用 makefile()")
    print("  ✓ 高并发: 设置合适的缓冲区")


if __name__ == "__main__":
    main()
