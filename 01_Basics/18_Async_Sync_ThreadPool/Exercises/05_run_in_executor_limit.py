#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：自建线程池 + run_in_executor 提交多任务，限制并发。
Author: Lambert
"""

from __future__ import annotations

import asyncio
import concurrent.futures as cf
import time


def blocking_job(x: int) -> str:
    time.sleep(0.1)
    return f"job-{x}"


async def main_async() -> None:
    loop = asyncio.get_running_loop()
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        futs = [loop.run_in_executor(executor, blocking_job, i) for i in range(6)]
        results = await asyncio.gather(*futs)
    print("results ->", results)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()