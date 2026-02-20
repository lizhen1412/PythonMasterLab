#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：TaskGroup 并发，失败任务打印日志。
Author: Lambert
"""

from __future__ import annotations

import asyncio


async def task(name: str, fail: bool = False) -> str:
    await asyncio.sleep(0.05)
    if fail:
        raise RuntimeError(f"{name} failed")
    return f"{name} ok"


async def main_async() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(task("t1"))
            tg.create_task(task("t2", fail=True))
            tg.create_task(task("t3"))
    except* Exception as eg:
        print("TaskGroup 捕获 ->", eg)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()