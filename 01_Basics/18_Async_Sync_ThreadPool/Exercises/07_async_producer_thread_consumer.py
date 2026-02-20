#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：asyncio.Queue 生产、线程池消费（阻塞），哨兵退出。
Author: Lambert
"""

from __future__ import annotations

import asyncio
import concurrent.futures as cf
import time

SENTINEL = object()


async def producer(q: asyncio.Queue[object]) -> None:
    for i in range(4):
        await q.put(i)
        print(f"[producer] put {i}")
    await q.put(SENTINEL)
    print("[producer] sentinel")


def consume_blocking(x: int) -> str:
    time.sleep(0.1)
    return f"c-{x}"


async def consumer(q: asyncio.Queue[object], executor: cf.ThreadPoolExecutor) -> None:
    loop = asyncio.get_running_loop()
    while True:
        item = await q.get()
        if item is SENTINEL:
            print("[consumer] exit")
            break
        res = await loop.run_in_executor(executor, consume_blocking, item)
        print("[consumer] got", res)


async def main_async() -> None:
    q: asyncio.Queue[object] = asyncio.Queue()
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        await asyncio.gather(producer(q), consumer(q, executor))


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()