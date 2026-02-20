#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 13：AsyncIO 集成。
Author: Lambert

题目：
实现一个异步 HTTP 客户端，使用 run_in_executor 并发执行多个请求。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/13_async_requests.py
"""

from __future__ import annotations

import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import Any


class AsyncRequestsClient:
    """AsyncIO 兼容的 requests 客户端"""

    def __init__(self, max_workers: int = 5):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    async def get(self, url: str, **kwargs: Any) -> dict:
        """异步 GET 请求"""
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            self.executor,
            lambda: requests.get(url, **kwargs)
        )
        response.raise_for_status()
        return response.json()

    async def post(self, url: str, **kwargs: Any) -> dict:
        """异步 POST 请求"""
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            self.executor,
            lambda: requests.post(url, **kwargs)
        )
        response.raise_for_status()
        return response.json()

    async def close(self) -> None:
        """关闭 executor"""
        self.executor.shutdown(wait=True)


async def fetch_multiple_urls(client: AsyncRequestsClient, urls: list[str]) -> list[dict]:
    """并发获取多个 URL"""
    tasks = [client.get(url, timeout=10) for url in urls]
    return await asyncio.gather(*tasks)


async def main() -> None:
    client = AsyncRequestsClient()

    # 单个请求测试
    result = await client.get("https://httpbin.org/get")
    assert "args" in result
    print("[OK] async GET request")

    # 并发多个请求
    urls = [
        "https://httpbin.org/get?n=1",
        "https://httpbin.org/get?n=2",
        "https://httpbin.org/get?n=3",
    ]

    import time
    start = time.time()
    results = await fetch_multiple_urls(client, urls)
    elapsed = time.time() - start

    assert len(results) == 3
    print(f"[OK] fetched {len(results)} URLs in {elapsed:.2f}s (concurrent)")

    await client.close()
    print("[OK] AsyncIO integration exercise complete")


if __name__ == "__main__":
    asyncio.run(main())