#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：Semaphore + to_thread 限制阻塞调用并发。
"""

from __future__ import annotations

import asyncio
import time


def blocking_task(i: int) -> str:
    time.sleep(0.2)
    return f"task-{i}"


async def limited_call(i: int, sem: asyncio.Semaphore) -> str:
    async with sem:
        return await asyncio.to_thread(blocking_task, i)


async def main_async() -> None:
    sem = asyncio.Semaphore(2)  # 限制同时最多 2 个阻塞调用
    tasks = [limited_call(i, sem) for i in range(6)]
    start = time.perf_counter()
    results = await asyncio.gather(*tasks)
    duration = (time.perf_counter() - start) * 1000
    print("results ->", results)
    print("耗时 ms ->", round(duration, 2))
    print("通过 Semaphore 控制 to_thread 并发，避免任务爆炸。")


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
