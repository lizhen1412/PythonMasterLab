#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：to_thread 包装阻塞函数，验证事件循环未被阻塞。
Author: Lambert
"""

from __future__ import annotations

import asyncio
import time


def blocking_io() -> str:
    time.sleep(0.3)
    return "blocking"


async def ticker() -> None:
    for _ in range(3):
        print("[ticker] tick")
        await asyncio.sleep(0.1)


async def main_async() -> None:
    start = time.perf_counter()
    result = await asyncio.gather(ticker(), asyncio.to_thread(blocking_io))
    duration = (time.perf_counter() - start) * 1000
    print("results ->", result)
    print(f"耗时约 {duration:.2f} ms（ticker 未被阻塞）")


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()