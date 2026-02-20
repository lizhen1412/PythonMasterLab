#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：反例集合——不要这么做。
Author: Lambert
"""

from __future__ import annotations

import asyncio
import concurrent.futures as cf
import time


def bad_run_asyncio_in_worker() -> None:
    """反例：在线程池 worker 里直接 asyncio.run。"""
    async def coro():
        await asyncio.sleep(0.05)
        return "ok"

    # 这样做会为每个任务创建/关闭事件循环，成本高且可能与外层 loop 冲突
    result = asyncio.run(coro())
    print("[bad] asyncio.run in worker ->", result)


async def uncontrolled_task_creation(n: int = 1000) -> None:
    """反例：不受控地创建大量任务，可能耗尽内存/资源。"""
    tasks = [asyncio.create_task(asyncio.sleep(1)) for _ in range(n)]
    print("[bad] created", len(tasks), "tasks")
    await asyncio.gather(*tasks)


def main() -> None:
    print("== 反例 1：线程池里 asyncio.run ==")
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(bad_run_asyncio_in_worker) for _ in range(2)]
        for fut in futures:
            fut.result()

    print("\n== 反例 2：无限制创建任务（请勿在生产这样做） ==")
    asyncio.run(uncontrolled_task_creation(2000))
    print("提示：使用限流（Semaphore/池大小），避免任务爆炸。")


if __name__ == "__main__":
    main()