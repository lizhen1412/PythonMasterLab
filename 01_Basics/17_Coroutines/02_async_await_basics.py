#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：async/await 基础，asyncio.run、sleep、并发 vs 串行。
Author: Lambert
"""

from __future__ import annotations

import asyncio
import time


async def hello(name: str, delay: float = 0.2) -> str:
    await asyncio.sleep(delay)
    return f"Hello, {name}"


async def run_sequential() -> None:
    start = time.perf_counter()
    a = await hello("Alice", 0.2)
    b = await hello("Bob", 0.2)
    duration = (time.perf_counter() - start) * 1000
    print("串行耗时 ms ->", round(duration, 2), a, b)


async def run_concurrent() -> None:
    start = time.perf_counter()
    task1 = asyncio.create_task(hello("Alice", 0.2))
    task2 = asyncio.create_task(hello("Bob", 0.2))
    a = await task1
    b = await task2
    duration = (time.perf_counter() - start) * 1000
    print("并发耗时 ms ->", round(duration, 2), a, b)


async def main_async() -> None:
    print("== async/await 示例 ==")
    print(await hello("World", 0.1))

    print("\n== 串行 vs 并发 ==")
    await run_sequential()
    await run_concurrent()


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()