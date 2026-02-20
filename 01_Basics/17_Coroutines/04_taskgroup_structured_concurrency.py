#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：TaskGroup（3.11+）结构化并发与异常传播。
Author: Lambert
"""

from __future__ import annotations

import asyncio


async def child(name: str, delay: float, fail: bool = False) -> str:
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(f"{name} failed")
    return f"{name} ok"


async def run_group() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(child("task1", 0.2))
            tg.create_task(child("task2", 0.1, fail=True))
            tg.create_task(child("task3", 0.15))
    except* Exception as eg:
        print("TaskGroup 捕获异常组 ->", eg)


async def main_async() -> None:
    print("== TaskGroup 示例 ==")
    await run_group()
    print("TaskGroup 会等待并取消其他子任务，异常以 ExceptionGroup 抛出。")


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()