#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 26：DNS 与连接复用原理。
Author: Lambert

要点：
- requests 默认使用 urllib3 的连接池
- Session 复用 TCP 连接，避免重复握手
- DNS 解析在首次请求时进行
- 连接复用显著提升性能
- 长连接 vs 短连接

运行：
    python3 02_Frameworks/03_Requests/26_dns_and_connection_reuse.py
"""

from __future__ import annotations

import time
import requests


def demo_connection_reuse_benefit() -> None:
    """演示连接复用的性能优势"""
    print("=== 连接复用性能对比 ===")

    url = "https://httpbin.org/get"
    count = 10

    # 无 Session：每次新建连接
    start = time.time()
    for _ in range(count):
        requests.get(url, timeout=5)
    elapsed_no_session = time.time() - start

    # 有 Session：复用连接
    session = requests.Session()
    start = time.time()
    for _ in range(count):
        session.get(url, timeout=5)
    elapsed_with_session = time.time() - start

    print(f"无 Session (10次请求): {elapsed_no_session:.3f}s")
    print(f"有 Session (10次请求): {elapsed_with_session:.3f}s")
    print(f"性能提升: {elapsed_no_session / elapsed_with_session:.2f}x")


def demo_dns_caching() -> None:
    """演示 DNS 缓存行为"""
    print("\n=== DNS 解析 ===")

    # requests 本身不缓存 DNS，但操作系统的 DNS 缓存会生效
    # urllib3 的连接池会保持已建立的连接

    session = requests.Session()

    # 首次请求：DNS 解析 + TCP 握手 + TLS 握手
    start = time.time()
    session.get("https://httpbin.org/get", timeout=5)
    first_elapsed = time.time() - start

    # 后续请求：复用已建立的连接
    start = time.time()
    session.get("https://httpbin.org/get", timeout=5)
    second_elapsed = time.time() - start

    print(f"首次请求 (含DNS+握手): {first_elapsed:.3f}s")
    print(f"后续请求 (复用连接): {second_elapsed:.3f}s")


def demo_connection_pool_state() -> None:
    """演示连接池状态"""
    print("\n=== 连接池状态 ===")

    session = requests.Session()

    # 查看默认连接池配置
    print("默认连接池:")
    print(f"  HTTPAdapter 数量: {len(session.adapters)}")

    # 访问底层连接池（内部实现）
    for key, adapter in session.adapters.items():
        print(f"\nAdapter for {key}:")
        print(f"  pool_connections: {adapter.pool_connections}")
        print(f"  pool_maxsize: {adapter.pool_maxsize}")


def demo_keep_alive() -> None:
    """演示 Keep-Alive 长连接"""
    print("\n=== Keep-Alive 长连接 ===")

    session = requests.Session()

    # 发送多个请求到同一主机
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/headers",
        "https://httpbin.org/json",
    ]

    for url in urls:
        start = time.time()
        resp = session.get(url, timeout=5)
        elapsed = time.time() - start

        # 检查连接是否复用（通过响应头）
        connection = resp.headers.get("Connection", "未指定")
        print(f"{url} -> {resp.status_code} ({elapsed:.3f}s), Connection: {connection}")


def demo_connection_to_different_hosts() -> None:
    """演示不同主机的连接管理"""
    print("\n=== 多主机连接管理 ===")

    session = requests.Session()

    hosts = [
        "https://httpbin.org",
        "https://www.google.com",
        "https://www.github.com",
    ]

    for host in hosts:
        try:
            start = time.time()
            resp = session.get(f"{host}/", timeout=5)
            elapsed = time.time() - start
            print(f"{host} -> {resp.status_code} ({elapsed:.3f}s)")
        except Exception as e:
            print(f"{host} -> 错误: {e}")


def demo_connection_close() -> None:
    """演示连接关闭"""
    print("\n=== 连接关闭 ===")

    session = requests.Session()

    # 正常请求
    resp1 = session.get("https://httpbin.org/get", timeout=5)
    print(f"第一次请求状态码: {resp1.status_code}")

    # 关闭所有连接
    session.close()
    print("已调用 session.close()，所有连接已关闭")

    # 重新请求会建立新连接
    start = time.time()
    resp2 = session.get("https://httpbin.org/get", timeout=5)
    elapsed = time.time() - start
    print(f"关闭后重新请求: {resp2.status_code} ({elapsed:.3f}s)")


def demo_context_manager() -> None:
    """演示使用上下文管理器"""
    print("\n=== 使用上下文管理器 ===")

    # with 语句会自动关闭连接
    with requests.Session() as session:
        resp = session.get("https://httpbin.org/get", timeout=5)
        print(f"状态码: {resp.status_code}")

    print("退出 with 块后，连接已自动关闭")


def demo_connection_headers() -> None:
    """演示连接相关的响应头"""
    print("\n=== 连接相关响应头 ===")

    resp = requests.get("https://httpbin.org/get", timeout=5)

    print("响应头中的连接信息:")
    for key, value in resp.headers.items():
        if "connection" in key.lower() or "keep" in key.lower():
            print(f"  {key}: {value}")


def main() -> None:
    print("=== DNS 与连接复用原理演示 ===\n")
    demo_connection_reuse_benefit()
    demo_dns_caching()
    demo_connection_pool_state()
    demo_keep_alive()
    demo_connection_to_different_hosts()
    demo_connection_close()
    demo_context_manager()
    demo_connection_headers()

    print("\n使用建议:")
    print("  - 务必使用 Session 复用连接，性能提升显著")
    print("  - 请求同一主机的多个接口时，Session 尤其重要")
    print("  - 使用完毕后调用 session.close() 或使用 with 语句")
    print("  - 连接会保持一段时间，超时后会被服务端关闭")
    print("  - 高并发场景可调整连接池大小（HTTPAdapter）")


if __name__ == "__main__":
    main()