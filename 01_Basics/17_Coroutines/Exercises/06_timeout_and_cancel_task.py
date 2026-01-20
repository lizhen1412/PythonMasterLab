#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：wait_for 超时取消，捕获 CancelledError。
"""

from __future__ import annotations

import asyncio


async def slow() -> str:
    await asyncio.sleep(1.0)
    return "done"


async def main_async() -> None:
    try:
        await asyncio.wait_for(slow(), timeout=0.2)
    except asyncio.TimeoutError:
        print("timeout -> cancelled slow()")

    task = asyncio.create_task(slow())
    await asyncio.sleep(0.1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("caught CancelledError from task")


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
