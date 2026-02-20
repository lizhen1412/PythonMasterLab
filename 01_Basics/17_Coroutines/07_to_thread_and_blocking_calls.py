#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：asyncio.to_thread 调用阻塞函数，避免卡住事件循环。
Author: Lambert
"""

from __future__ import annotations

import asyncio
import time


def blocking_io() -> str:
    """模拟阻塞 I/O（sleep 代表阻塞）。"""
    time.sleep(0.3)
    return "blocking result"


async def main_async() -> None:
    start = time.perf_counter()
    # 不用 to_thread，会直接阻塞事件循环
    result = await asyncio.to_thread(blocking_io)
    duration = (time.perf_counter() - start) * 1000
    print("to_thread result ->", result, "耗时 ms ->", round(duration, 2))

    # 同时演示协程并发 while blocking runs in thread
    async def ticker():
        for _ in range(3):
            print("[ticker] tick")
            await asyncio.sleep(0.1)

    await asyncio.gather(ticker(), asyncio.to_thread(blocking_io))


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()