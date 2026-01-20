#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：loop.run_in_executor（兼容旧代码，自建线程池）。
"""

from __future__ import annotations

import asyncio
import concurrent.futures as cf
import time


def blocking_task(x: int) -> str:
    time.sleep(0.1)
    return f"blk-{x}"


async def main_async() -> None:
    loop = asyncio.get_running_loop()
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        futs = [
            loop.run_in_executor(executor, blocking_task, i)
            for i in range(4)
        ]
        results = await asyncio.gather(*futs)
        print("run_in_executor results ->", results)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
