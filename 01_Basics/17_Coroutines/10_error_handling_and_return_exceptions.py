#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：错误处理与 return_exceptions，后台任务异常监控。
Author: Lambert
"""

from __future__ import annotations

import asyncio


async def may_fail(x: int) -> int:
    await asyncio.sleep(0.05)
    if x == 2:
        raise ValueError("bad x=2")
    return x * 2


async def demo_gather_errors() -> None:
    tasks = [may_fail(i) for i in range(4)]
    try:
        await asyncio.gather(*tasks)
    except Exception as exc:
        print("gather raised ->", type(exc).__name__, exc)

    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("gather return_exceptions ->", results)


async def monitor_task(task: asyncio.Task) -> None:
    try:
        await task
    except Exception as exc:
        print("[monitor] task error ->", type(exc).__name__, exc)


async def demo_background_task() -> None:
    task = asyncio.create_task(may_fail(2))
    asyncio.create_task(monitor_task(task))  # 监控异常
    await asyncio.sleep(0.2)


async def main_async() -> None:
    print("== gather 错误处理 ==")
    await demo_gather_errors()

    print("\n== 背景任务异常监控 ==")
    await demo_background_task()


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()