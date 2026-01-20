#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：封装 to_thread，限流并记录异常。
"""

from __future__ import annotations

import asyncio
import time
from typing import Awaitable, Callable


async def to_thread_limited(func: Callable[..., object], *args: object, sem: asyncio.Semaphore) -> object:
    async with sem:
        return await asyncio.to_thread(func, *args)


def may_fail(x: int) -> str:
    time.sleep(0.05)
    if x == 2:
        raise RuntimeError("bad x")
    return f"ok-{x}"


async def main_async() -> None:
    sem = asyncio.Semaphore(2)
    tasks: list[Awaitable[object]] = []
    for i in range(5):
        tasks.append(to_thread_limited(may_fail, i, sem=sem))
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("results ->", results)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
