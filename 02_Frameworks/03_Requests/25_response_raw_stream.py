#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 25：Response.raw 底层流访问。
Author: Lambert

要点：
- response.raw：访问 urllib3 的原始响应流
- stream=True 时 raw 可用
- read()、read1()、readinto() 方法
- 与 iter_content() 的区别

运行：
    python3 02_Frameworks/03_Requests/25_response_raw_stream.py
"""

from __future__ import annotations

import requests


def demo_raw_basic() -> None:
    """演示 raw 的基本用法"""
    print("=== Response.raw 基本用法 ===")

    # 必须设置 stream=True
    with requests.get("https://httpbin.org/stream/5", stream=True, timeout=5) as resp:
        print(f"状态码: {resp.status_code}")
        print(f"raw 对象类型: {type(resp.raw)}")
        print(f"raw 是否可读: {resp.raw.readable()}")

        # 读取全部内容
        content = resp.raw.read()
        print(f"raw.read() 读取字节数: {len(content)}")
        print(f"内容预览: {content[:100]}")


def demo_raw_vs_iter_content() -> None:
    """对比 raw 和 iter_content"""
    print("\n=== raw vs iter_content ===")

    url = "https://httpbin.org/stream/3"

    # 方式1：使用 raw（底层 urllib3 流）
    with requests.get(url, stream=True, timeout=5) as resp:
        print("使用 raw.read():")
        chunks = []
        while True:
            chunk = resp.raw.read(16)
            if not chunk:
                break
            chunks.append(chunk)
            print(f"  块大小: {len(chunk)} bytes")

    # 方式2：使用 iter_content（requests 封装）
    with requests.get(url, stream=True, timeout=5) as resp:
        print("\n使用 iter_content():")
        chunks = []
        for chunk in resp.iter_content(chunk_size=16):
            if chunk:
                chunks.append(chunk)
                print(f"  块大小: {len(chunk)} bytes")

    print("\n区别:")
    print("  - raw: 直接访问 urllib3 流，不处理解码/压缩")
    print("  - iter_content: requests 封装，自动处理 gzip/deflate")


def demo_raw_read1() -> None:
    """演示 read1() 方法（非阻塞读取）"""
    print("\n=== raw.read1() 非阻塞读取 ===")

    with requests.get("https://httpbin.org/get", stream=True, timeout=5) as resp:
        # read1() 尽可能读取，但不阻塞
        chunk1 = resp.raw.read1(16)
        chunk2 = resp.raw.read1(16)

        print(f"第一次 read1(16) -> {len(chunk1)} bytes")
        print(f"第二次 read1(16) -> {len(chunk2)} bytes")

    print("\n区别:")
    print("  - read(): 阻塞直到读取指定字节数或 EOF")
    print("  - read1(): 立即返回，可能少于指定字节数")


def demo_raw_readinto() -> None:
    """演示 readinto() 方法（读取到缓冲区）"""
    print("\n=== raw.readinto() 读取到缓冲区 ===")

    # 预分配缓冲区
    buffer = bytearray(100)

    with requests.get("https://httpbin.org/get", stream=True, timeout=5) as resp:
        # 读取到 buffer
        n = resp.raw.readinto(buffer)

        print(f"实际读取字节数: {n}")
        print(f"缓冲区内容: {bytes(buffer[:n])}")


def demo_raw_stream_to_file() -> None:
    """演示直接写入文件（零拷贝）"""
    import tempfile

    print("\n=== raw 流直接写入文件 ===")

    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_file = f.name

    try:
        # 使用 shutil.copyfileobj 进行高效复制
        with requests.get("https://httpbin.org/get", stream=True, timeout=5) as resp:
            with open(temp_file, "wb") as f:
                import shutil
                shutil.copyfileobj(resp.raw, f)

        file_size = __import__("pathlib").Path(temp_file).stat().st_size
        print(f"下载文件大小: {file_size} bytes")

    finally:
        __import__("pathlib").Path(temp_file).unlink(missing_ok=True)


def demo_raw_decompression() -> None:
    """演示 raw 不自动解压"""
    print("\n=== raw 不处理压缩 ===")

    # httpbin 默认返回 gzip 压缩的内容
    with requests.get("https://httpbin.org/get", stream=True, timeout=5) as resp:
        # raw 读取的是压缩后的原始数据
        raw_data = resp.raw.read()
        print(f"raw 读取字节数: {len(raw_data)}")

        # content 是解压后的数据
        content_data = resp.content
        print(f"content 读取字节数: {len(content_data)}")

        # 检查是否被压缩
        content_encoding = resp.headers.get("Content-Encoding", "identity")
        print(f"Content-Encoding: {content_encoding}")

        if content_encoding in ("gzip", "deflate"):
            print("注意: raw 读取的是压缩数据，content 是解压后的数据")


def demo_raw_socket_info() -> None:
    """演示获取底层 socket 信息"""
    print("\n=== 底层 socket 信息 ===")

    with requests.get("https://httpbin.org/get", stream=True, timeout=5) as resp:
        # 访问底层连接
        if hasattr(resp.raw, "_connection"):
            conn = resp.raw._connection
            if conn:
                print(f"连接对象类型: {type(conn)}")


def demo_raw_performance() -> None:
    """演示 raw 的性能优势"""
    import time

    print("\n=== 性能对比 ===")

    url = "https://httpbin.org/get"

    # 方式1：使用 content（全部加载到内存）
    start = time.time()
    resp = requests.get(url, timeout=5)
    _ = resp.content
    elapsed1 = time.time() - start
    print(f"content 方式: {elapsed1:.3f}s")

    # 方式2：使用 raw 流式读取
    start = time.time()
    with requests.get(url, stream=True, timeout=5) as resp:
        _ = resp.raw.read()
    elapsed2 = time.time() - start
    print(f"raw 流式方式: {elapsed2:.3f}s")

    print("\n建议:")
    print("  - 小文件：使用 content 简单方便")
    print("  - 大文件：使用 iter_content() 或 raw 流式处理")


def main() -> None:
    print("=== Response.raw 底层流访问演示 ===\n")
    demo_raw_basic()
    demo_raw_vs_iter_content()
    demo_raw_read1()
    demo_raw_readinto()
    demo_raw_stream_to_file()
    demo_raw_decompression()
    demo_raw_socket_info()
    demo_raw_performance()

    print("\n使用建议:")
    print("  - 大文件下载优先使用 iter_content()，更安全")
    print("  - raw 直接访问底层流，需要处理压缩/编码问题")
    print("  - 零拷贝写入文件使用 shutil.copyfileobj(resp.raw, file)")
    print("  - read1() 适合非阻塞/异步场景")
    print("  - readinto() 适合预分配缓冲区场景")


if __name__ == "__main__":
    main()