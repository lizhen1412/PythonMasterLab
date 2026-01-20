#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：asyncio 同步原语与 Queue。
"""

from __future__ import annotations

import asyncio

SENTINEL = object()


async def producer(q: asyncio.Queue[object]) -> None:
    for i in range(3):
        await q.put(i)
        print(f"[producer] put {i}")
        await asyncio.sleep(0.05)
    await q.put(SENTINEL)
    print("[producer] put sentinel")


async def consumer(q: asyncio.Queue[object]) -> None:
    while True:
        item = await q.get()
        if item is SENTINEL:
            print("[consumer] got sentinel, exit")
            break
        print(f"[consumer] got {item}")
        await asyncio.sleep(0.1)


async def demo_lock() -> None:
    lock = asyncio.Lock()
    value = 0

    async def add():
        nonlocal value
        async with lock:
            tmp = value
            await asyncio.sleep(0)
            value = tmp + 1

    await asyncio.gather(*(add() for _ in range(5)))
    print("[lock] value ->", value)


async def demo_semaphore() -> None:
    sem = asyncio.Semaphore(2)

    async def task(i: int):
        async with sem:
            print(f"[sem] task {i} start")
            await asyncio.sleep(0.1)
            print(f"[sem] task {i} end")

    await asyncio.gather(*(task(i) for i in range(5)))


async def main_async() -> None:
    print("== asyncio.Queue ==")
    q: asyncio.Queue[object] = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

    print("\n== Lock ==")
    await demo_lock()

    print("\n== Semaphore ==")
    await demo_semaphore()


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
