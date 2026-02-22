#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 18：asyncio Streams 高级API。
Author: Lambert

本示例演示 asyncio.StreamReader 和 StreamWriter 的高级用法：

1. **StreamReader 高级方法**：
   - read(n) - 读取指定字节数
   - readuntil(separator) - 读取直到分隔符
   - readline() - 读取一行
   - readexactly(n) - 精确读取n字节（否则异常）
   - read() - 读取直到EOF

2. **StreamWriter 高级方法**：
   - write(data) - 写入数据
   - writelines(lines) - 写入多行
   - can_write_eof() - 是否可发送EOF
   - write_eof() - 发送EOF
   - transport - 访问传输层
   - is_closing() - 是否正在关闭

3. **Streams 创建**：
   - asyncio.open_connection() - 打开TCP连接
   - asyncio.start_server() - 启动TCP服务器
   - asyncio.open_unix_connection() - Unix域socket
   - asyncio.start_unix_server() - Unix域socket服务器

4. **底层 Protocol/Transport**（简要介绍）
"""

from __future__ import annotations

import asyncio
from typing import Any


# =============================================================================
# StreamReader 高级方法
# =============================================================================


async def demo_stream_reader_advanced() -> None:
    """示例 01：StreamReader 高级方法。"""
    print("== StreamReader 高级方法 ==\n")

    # 创建一个模拟的stream reader
    reader = asyncio.StreamReader()

    # 模拟数据
    data = b"Line 1\nLine 2\nLine 3\nEnd"

    def feed_data():
        """模拟数据到达。"""
        reader.feed_data(data)
        reader.feed_eof()

    feed_data()

    print("1. read(n) - 读取指定字节数:")
    chunk = await reader.read(5)
    print(f"   read(5): {chunk}")

    print("\n2. readuntil(separator) - 读取直到分隔符:")
    line = await reader.readuntil(b'\n')
    print(f"   readuntil(b'\\n'): {line}")

    print("\n3. readline() - 读取一行:")
    line = await reader.readline()
    print(f"   readline(): {line}")

    print("\n4. readexactly(n) - 精确读取n字节:")
    try:
        exact = await reader.readexactly(5)
        print(f"   readexactly(5): {exact}")
    except asyncio.IncompleteReadError as e:
        print(f"   readexactly(5) 失败: {e}")

    print("\n5. read() - 读取直到EOF:")
    remaining = await reader.read()
    print(f"   read(): {remaining}")


# =============================================================================
# StreamWriter 高级方法
# =============================================================================


async def demo_stream_writer_advanced() -> None:
    """示例 02：StreamWriter 高级方法。"""
    print("\n\n== StreamWriter 高级方法 ==\n")

    # 创建一对读写stream
    reader = asyncio.StreamReader()
    writer = asyncio.StreamWriter(
        protocol=None,
        reader=None,
        transport=asyncio.Transport(asyncio.AbstractEventLoop()),
    )

    # 注意：这只是一个演示框架
    # 实际使用时，streamreader/writer 通过 open_connection 获取

    print("StreamWriter 关键属性:")
    print("  transport.can_write_eof() - 检查是否可发送EOF")
    print("  write_eof() - 发送EOF（半关闭）")
    print("  is_closing() - 检查是否正在关闭")
    print("  transport - 访问底层传输对象")

    print("\n实际使用示例:")
    print("""
    # 打开连接
    reader, writer = await asyncio.open_connection('host', port)

    # 写入数据
    writer.write(b'Hello')
    await writer.drain()  # 等待发送完成

    # 发送EOF（半关闭）
    writer.write_eof()
    writer.can_write_eof()  # 检查是否支持

    # 读取响应
    data = await reader.read(100)

    # 关闭连接
    writer.close()
    await writer.wait_closed()
    """)


# =============================================================================
# 完整的Echo服务器和客户端
# =============================================================================


async def echo_server(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    """Echo服务器处理函数。"""
    print(f"[服务器] 新连接: {writer.get_extra_info('peername')}")

    try:
        while True:
            # 读取数据（使用 readexactly 确保读取到数据）
            try:
                data = await reader.read(1024)
                if not data:
                    # EOF
                    break

                print(f"[服务器] 收到: {data.decode()}")
                writer.write(data)
                await writer.drain()
                print(f"[服务器] 已回显")

            except ConnectionError:
                break

    finally:
        print(f"[服务器] 连接关闭")
        writer.close()
        await writer.wait_closed()


async def demo_echo_client() -> None:
    """示例 03：Echo客户端 - 演示完整的stream交互。"""
    print("\n\n== Echo 客户端示例 ==\n")

    # 启动服务器
    server = await asyncio.start_server(echo_server, '127.0.0.1', 20010)

    print(f"Echo服务器启动: 127.0.0.1:20010")

    # 创建任务运行服务器
    async def run_server():
        await server.serve_forever()

    server_task = asyncio.create_task(run_server())

    # 连接到服务器
    reader, writer = await asyncio.open_connection('127.0.0.1', 20010)

    print(f"[客户端] 已连接")

    # 发送多行消息
    messages = [b"Hello 1", b"Hello 2", b"Hello 3"]
    for msg in messages:
        writer.write(msg)
        await writer.drain()
        print(f"[客户端] 发送: {msg.decode()}")

        # 接收回显
        echo = await reader.read(1024)
        print(f"[客户端] 收到: {echo.decode()}")

    # 关闭写端
    print(f"[客户端] 关闭写端")
    writer.write_eof()
    writer.close()

    # 停止服务器
    server.close()
    await server.wait_closed()

    try:
        await asyncio.wait_for(server_task, timeout=1.0)
    except asyncio.TimeoutError:
        pass


# =============================================================================
# 分隔符协议
# =============================================================================


async def demo_delimiter_protocol() -> None:
    """示例 04：基于分隔符的协议。"""
    print("\n\n== 分隔符协议示例 ==\n")

    class DelimiterProtocol:
        """基于分隔符的协议处理器。"""

        def __init__(self) -> None:
            self.reader = asyncio.StreamReader()
            self.messages: list[str] = []

        def data_received(self, data: bytes) -> None:
            """数据到达回调。"""
            self.reader.feed_data(data)

        def eof_received(self) -> bool:
            """EOF到达回调。"""
            self.reader.feed_eof()
            return False  # False = 关闭连接

        async def read_messages(self) -> None:
            """读取所有消息（每行一个）。"""
            while True:
                try:
                    # 读取一行
                    line = await self.reader.readline()
                    if not line:
                        break

                    message = line.decode().strip()
                    if message:
                        self.messages.append(message)
                        print(f"  收到消息: {message}")

                except asyncio.IncompleteReadError:
                    break

    # 模拟数据
    protocol = DelimiterProtocol()

    data = b"Message 1\nMessage 2\nMessage 3\n"
    protocol.data_received(data)
    protocol.eof_received()

    print("读取消息:")
    await protocol.read_messages()


# =============================================================================
# 固定长度协议
# =============================================================================


async def demo_fixed_length_protocol() -> None:
    """示例 05：固定长度协议。"""
    print("\n\n== 固定长度协议 ==\n")

    async def read_fixed_length(reader: asyncio.StreamReader, length: int) -> bytes:
        """读取固定长度的数据。"""
        try:
            data = await reader.readexactly(length)
            return data
        except asyncio.IncompleteReadError as e:
            print(f"读取不完整: 期望{e.expected}字节，实际{e.partial}字节")
            return e.partial

    # 创建reader并模拟数据
    reader = asyncio.StreamReader()

    # 模拟固定长度的消息
    messages = [
        b"MSG1",  # 4字节
        b"MSG2",  # 4字节
        b"MSG3",  # 4字节
    ]

    for msg in messages:
        reader.feed_data(msg)

    reader.feed_eof()

    # 读取固定长度消息
    for i in range(3):
        data = await read_fixed_length(reader, 4)
        print(f"  消息 {i+1}: {data.decode()}")


# =============================================================================
# 长度前缀协议
# =============================================================================


async def demo_length_prefix_protocol() -> None:
    """示例 06：长度前缀协议。"""
    print("\n\n== 长度前缀协议 ==\n")

    async def send_message(writer: asyncio.StreamWriter, message: bytes) -> None:
        """发送带长度前缀的消息。"""
        # 4字节长度前缀（大端序）
        length = len(message)
        prefix = length.to_bytes(4, 'big')

        writer.write(prefix + message)
        await writer.drain()

    async def recv_message(reader: asyncio.StreamReader) -> bytes | None:
        """接收带长度前缀的消息。"""
        try:
            # 读取4字节长度前缀
            prefix = await reader.readexactly(4)
            length = int.from_bytes(prefix, 'big')

            # 读取消息体
            data = await reader.readexactly(length)
            return data

        except asyncio.IncompleteReadError:
            return None

    # 模拟通信
    reader = asyncio.StreamReader()

    # 构造消息：长度前缀 + 消息体
    messages = [b"Hello", b"World", b"Test"]
    for msg in messages:
        # 长度前缀
        length = len(msg)
        prefix = length.to_bytes(4, 'big')
        reader.feed_data(prefix + msg)

    reader.feed_eof()

    # 读取消息
    print("读取消息:")
    for i in range(3):
        msg = await recv_message(reader)
        if msg:
            print(f"  消息 {i+1}: {msg.decode()} (长度: {len(msg)})")


# =============================================================================
# 超时和取消
# =============================================================================


async def demo_stream_timeout() -> None:
    """示例 07：Stream超时和取消。"""
    print("\n\n== Stream 超时处理 ==\n")

    reader = asyncio.StreamReader()

    async def read_with_timeout(reader: asyncio.StreamReader) -> bytes:
        """带超时的读取。"""
        try:
            # 使用 wait_for 设置超时
            data = await asyncio.wait_for(reader.read(1024), timeout=0.5)
            return data
        except asyncio.TimeoutError:
            print(f"  超时！")
            return b''

    # 先不提供数据
    try:
        data = await read_with_timeout(reader)
    except:
        pass

    print("超时处理方式:")
    print("  1. asyncio.wait_for(reader.read(), timeout)")
    print("  2. asyncio.timeout(1.0) 上下文管理器")
    print("  3. 在Protocol中实现超时")


# =============================================================================
# 主函数
# =============================================================================


async def main() -> None:
    """运行所有示例。"""
    print("="*60)
    print("asyncio Streams 高级API")
    print("="*60)

    demo_stream_reader_advanced()
    await demo_stream_reader_advanced()

    demo_stream_writer_advanced()

    await demo_echo_client()

    demo_delimiter_protocol()
    await demo_delimiter_protocol()

    demo_fixed_length_protocol()
    await demo_fixed_length_protocol()

    demo_length_prefix_protocol()
    await demo_length_prefix_protocol()

    demo_stream_timeout()
    await demo_stream_timeout()

    print("\n" + "="*60)
    print("StreamReader/Writer API 速查")
    print("="*60)
    print("\nStreamReader:")
    print("  read(n=-1)              读取直到EOF或n字节")
    print("  readuntil(separator)    读取直到分隔符")
    print("  readline()              读取一行")
    print("  readexactly(n)          精确读取n字节")
    print("  at_eof()                检查是否EOF")
    print("\nStreamWriter:")
    print("  write(data)             写入数据")
    print("  writelines(lines)       写入多行")
    print("  drain()                 等待发送完成")
    print("  write_eof()             发送EOF")
    print("  can_write_eof()         检查是否支持EOF")
    print("  is_closing()            检查是否关闭")
    print("  close()                 关闭连接")
    print("  wait_closed()           等待关闭完成")
    print("\n创建连接:")
    print("  open_connection(host, port)   打开TCP连接")
    print("  start_server(handler)        启动TCP服务器")
    print("  open_unix_connection(path)   打开Unix socket")
    print("  start_unix_server(handler)  启动Unix socket服务器")


if __name__ == "__main__":
    asyncio.run(main())
