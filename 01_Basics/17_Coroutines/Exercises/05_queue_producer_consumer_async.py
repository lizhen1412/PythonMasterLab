#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：asyncio.Queue 生产消费，哨兵退出。
"""

from __future__ import annotations

import asyncio

SENTINEL = object()


async def producer(q: asyncio.Queue[object]) -> None:
    for i in range(3):
        await q.put(i)
        print(f"[producer] put {i}")
    await q.put(SENTINEL)
    print("[producer] put sentinel")


async def consumer(q: asyncio.Queue[object]) -> None:
    while True:
        item = await q.get()
        if item is SENTINEL:
            print("[consumer] exit")
            break
        print(f"[consumer] got {item}")
        await asyncio.sleep(0.05)


async def main_async() -> None:
    q: asyncio.Queue[object] = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
