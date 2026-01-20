#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：async 生产 + 线程池消费阻塞任务，哨兵退出。
"""

from __future__ import annotations

import asyncio
import concurrent.futures as cf
import time

SENTINEL = object()


async def producer(q: asyncio.Queue[object]) -> None:
    for i in range(5):
        await q.put(i)
        print(f"[producer] put {i}")
        await asyncio.sleep(0.05)
    await q.put(SENTINEL)
    print("[producer] put sentinel")


def blocking_consume(item: int) -> str:
    time.sleep(0.1)
    return f"processed-{item}"


async def consumer(q: asyncio.Queue[object], executor: cf.ThreadPoolExecutor) -> None:
    loop = asyncio.get_running_loop()
    while True:
        item = await q.get()
        if item is SENTINEL:
            print("[consumer] got sentinel, exit")
            break
        result = await loop.run_in_executor(executor, blocking_consume, item)
        print("[consumer] result ->", result)


async def main_async() -> None:
    q: asyncio.Queue[object] = asyncio.Queue()
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        await asyncio.gather(producer(q), consumer(q, executor))


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
