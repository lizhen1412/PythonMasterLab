#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 27：在 AsyncIO 中使用 requests。
Author: Lambert

要点：
- requests 是同步库，不能直接在 async 函数中使用
- 使用线程池在 asyncio 中运行 requests
- run_in_executor()：将阻塞调用放到线程池执行
- asyncio.gather()：并发执行多个请求
- 对比：同步 vs 异步的性能差异

注意：
- 对于真正的异步 HTTP，建议使用 aiohttp
- 本示例展示如何在现有 asyncio 代码中复用 requests

运行：
    python3 02_Frameworks/03_Requests/27_asyncio_integration.py
"""

from __future__ import annotations

import asyncio
import time
import requests


async def fetch_in_thread(url: str, timeout: int = 5) -> dict:
    """在线程池中执行 requests 请求"""
    loop = asyncio.get_event_loop()

    # 使用 run_in_executor 在线程池中执行同步函数
    future = loop.run_in_executor(None, lambda: requests.get(url, timeout=timeout))
    resp = await future

    return {
        "url": url,
        "status": resp.status_code,
        "elapsed": resp.elapsed.total_seconds(),
    }


async def demo_basic_async_usage() -> None:
    """演示基本的异步用法"""
    print("=== 基本异步用法 ===")

    result = await fetch_in_thread("https://httpbin.org/get")
    print(f"请求结果: {result}")


async def demo_concurrent_requests() -> None:
    """演示并发请求"""
    print("\n=== 并发请求 ===")

    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
    ]

    start = time.time()

    # 并发执行多个请求
    tasks = [fetch_in_thread(url, timeout=10) for url in urls]
    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start

    print(f"并发执行 {len(urls)} 个请求")
    print(f"总耗时: {elapsed:.3f}s")
    print(f"每个请求结果:")
    for r in results:
        print(f"  {r['url']} -> {r['status']}")


async def demo_sync_vs_async() -> None:
    """对比同步和异步的性能"""
    print("\n=== 同步 vs 异步性能对比 ===")

    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
    ]

    # 同步方式
    start = time.time()
    for url in urls:
        requests.get(url, timeout=10)
    sync_elapsed = time.time() - start

    # 异步方式
    start = time.time()
    tasks = [fetch_in_thread(url, timeout=10) for url in urls]
    await asyncio.gather(*tasks)
    async_elapsed = time.time() - start

    print(f"同步方式耗时: {sync_elapsed:.3f}s")
    print(f"异步方式耗时: {async_elapsed:.3f}s")
    print(f"性能提升: {sync_elapsed / async_elapsed:.2f}x")


async def demo_with_session() -> None:
    """演示在异步中使用 Session"""
    print("\n=== 异步中使用 Session ===")

    # 在线程外创建 Session
    session = requests.Session()

    async def fetch_with_session(url: str) -> dict:
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, lambda: session.get(url, timeout=5))
        resp = await future
        return {"url": url, "status": resp.status_code}

    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/headers",
        "https://httpbin.org/json",
    ]

    tasks = [fetch_with_session(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for r in results:
        print(f"  {r['url']} -> {r['status']}")

    # 记得关闭 Session
    session.close()


async def demo_error_handling() -> None:
    """演示异步中的错误处理"""
    print("\n=== 异步错误处理 ===")

    async def safe_fetch(url: str) -> dict | None:
        try:
            return await fetch_in_thread(url, timeout=2)
        except requests.Timeout:
            return {"url": url, "error": "Timeout"}
        except Exception as e:
            return {"url": url, "error": str(e)}

    # 故意使用一个会超时的 URL
    results = await asyncio.gather(
        fetch_in_thread("https://httpbin.org/get", timeout=5),
        safe_fetch("https://httpbin.org/delay/5"),
        return_exceptions=True,
    )

    for r in results:
        if isinstance(r, Exception):
            print(f"  异常: {r}")
        else:
            print(f"  结果: {r}")


async def demo_with_progress() -> None:
    """演示带进度反馈的异步请求"""
    print("\n=== 带进度反馈的异步请求 ===")

    completed = 0
    total = 5

    async def fetch_with_progress(url: str, idx: int) -> dict:
        nonlocal completed
        result = await fetch_in_thread(url, timeout=10)
        completed += 1
        print(f"  [{completed}/{total}] 请求 {idx + 1} 完成")
        return result

    urls = [f"https://httpbin.org/delay/1" for _ in range(total)]
    tasks = [fetch_with_progress(url, i) for i, url in enumerate(urls)]

    await asyncio.gather(*tasks)


def demo_aiohttp_alternative() -> None:
    """演示 aiohttp 作为原生异步替代方案"""
    print("\n=== aiohttp 原生异步示例（仅供参考） ===")
    print("""
如果需要真正的异步 HTTP 客户端，推荐使用 aiohttp:

    import aiohttp
    import asyncio

    async def fetch(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def main():
        urls = ["https://httpbin.org/get"] * 3
        tasks = [fetch(url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

    # aiohttp 优势:
    # - 真正的非阻塞 I/O
    # - 更少的线程开销
    # - 更好的并发性能
    # - 与 asyncio 生态系统无缝集成

安装: pip install aiohttp
    """)


async def main() -> None:
    print("=== AsyncIO 中使用 requests 演示 ===\n")
    await demo_basic_async_usage()
    await demo_concurrent_requests()
    await demo_sync_vs_async()
    await demo_with_session()
    await demo_error_handling()
    await demo_with_progress()
    demo_aiohttp_alternative()

    print("\n使用建议:")
    print("  - requests + asyncio: 适用于已有代码迁移")
    print("  - 新项目优先使用 aiohttp 实现真正的异步")
    print("  - 线程池大小可通过 executor 限制")
    print("  - 注意 Session 不能跨线程共享")


if __name__ == "__main__":
    asyncio.run(main())