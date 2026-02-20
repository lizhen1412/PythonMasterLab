#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 21：连接池配置。
Author: Lambert

要点：
- HTTPAdapter 控制 requests 的连接池行为
- pool_connections：连接池数量（对应不同主机）
- pool_maxsize：每个连接池最大连接数
- max_retries：最大重试次数
- 连接复用可以显著提升性能

运行：
    python3 02_Frameworks/03_Requests/21_connection_pool.py
"""

from __future__ import annotations

import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def demo_default_pool() -> None:
    """演示默认连接池配置"""
    print("=== 默认连接池配置 ===")

    # 默认配置
    # pool_connections = 10
    # pool_maxsize = 10
    session = requests.Session()

    print(f"默认连接池大小: 10")
    print(f"默认每池最大连接: 10")


def demo_custom_pool() -> None:
    """演示自定义连接池配置"""
    print("\n=== 自定义连接池配置 ===")

    # 创建自定义 Adapter
    adapter = HTTPAdapter(
        pool_connections=5,  # 最多缓存 5 个主机的连接
        pool_maxsize=20,     # 每个主机最多 20 个连接
        max_retries=3,
    )

    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    print(f"连接池数量: {adapter.pool_connections}")
    print(f"每池最大连接: {adapter.pool_maxsize}")
    print(f"最大重试次数: {adapter.max_retries}")


def demo_connection_reuse() -> None:
    """演示连接复用的性能优势"""
    print("\n=== 连接复用性能对比 ===")

    url = "https://httpbin.org/get"
    count = 5

    # 方式1：不使用 Session（每次创建新连接）
    start = time.time()
    for _ in range(count):
        requests.get(url, timeout=5)
    elapsed_no_session = time.time() - start
    print(f"无 Session (新建连接): {elapsed_no_session:.3f}s")

    # 方式2：使用 Session（复用连接）
    session = requests.Session()
    start = time.time()
    for _ in range(count):
        session.get(url, timeout=5)
    elapsed_with_session = time.time() - start
    print(f"有 Session (复用连接): {elapsed_with_session:.3f}s")

    speedup = elapsed_no_session / elapsed_with_session
    print(f"性能提升: {speedup:.2f}x")


def demo_pool_exhaustion() -> None:
    """演示连接池耗尽场景"""
    import concurrent.futures

    print("\n=== 连接池并发测试 ===")

    def make_request(idx: int) -> tuple[int, int]:
        try:
            resp = requests.get("https://httpbin.org/delay/1", timeout=10)
            return (idx, resp.status_code)
        except Exception as e:
            return (idx, -1)

    # 使用默认连接池（可能有限制）
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(make_request, i) for i in range(20)]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    elapsed = time.time() - start

    success = sum(1 for _, code in results if code == 200)
    print(f"并发请求数: 20")
    print(f"成功: {success}, 失败: {20 - success}")
    print(f"总耗时: {elapsed:.3f}s")


def demo_adapter_for_specific_host() -> None:
    """演示为特定主机配置不同的连接池"""
    print("\n=== 分主机配置连接池 ===")

    # 为不同主机配置不同的 Adapter
    small_pool_adapter = HTTPAdapter(pool_connections=1, pool_maxsize=2)
    large_pool_adapter = HTTPAdapter(pool_connections=10, pool_maxsize=50)

    session = requests.Session()
    session.mount("https://httpbin.org/", small_pool_adapter)
    session.mount("https://api.github.com/", large_pool_adapter)

    print("httpbin.org: 小连接池 (1x2)")
    print("api.github.com: 大连接池 (10x50)")


def demo_retry_with_backoff() -> None:
    """演示带退避的重试策略"""
    print("\n=== 重试策略配置 ===")

    retry_strategy = Retry(
        total=3,  # 最多重试 3 次
        backoff_factor=0.5,  # 指数退避：0.5s, 1s, 2s
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)

    print(f"总重试次数: {retry_strategy.total}")
    print(f"退避因子: {retry_strategy.backoff_factor}")
    print(f"重试状态码: {retry_strategy.status_forcelist}")
    print(f"允许重试的方法: {retry_strategy.allowed_methods}")


def main() -> None:
    print("=== 连接池配置演示 ===\n")
    demo_default_pool()
    demo_custom_pool()
    demo_connection_reuse()
    demo_pool_exhaustion()
    demo_adapter_for_specific_host()
    demo_retry_with_backoff()

    print("\n使用建议:")
    print("  - 默认连接池已足够大多数场景")
    print("  - 高并发场景可增大 pool_maxsize")
    print("  - 务必使用 Session 以复用连接")
    print("  - 不同主机可配置不同的连接池大小")


if __name__ == "__main__":
    main()