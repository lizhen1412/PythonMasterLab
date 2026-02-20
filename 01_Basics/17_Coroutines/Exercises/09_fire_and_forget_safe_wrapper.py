#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：封装 create_task，记录异常/结果。
Author: Lambert
"""

from __future__ import annotations

import asyncio
from typing import Awaitable


def fire_and_report(coro: Awaitable[object]) -> asyncio.Task[object]:
    task = asyncio.create_task(coro)

    def _on_done(fut: asyncio.Task[object]) -> None:
        if fut.cancelled():
            print("[fire_and_report] task cancelled")
        elif exc := fut.exception():
            print("[fire_and_report] exception ->", type(exc).__name__, exc)
        else:
            print("[fire_and_report] result ->", fut.result())

    task.add_done_callback(_on_done)
    return task


async def may_fail(flag: bool) -> str:
    await asyncio.sleep(0.05)
    if flag:
        raise RuntimeError("failed")
    return "ok"


async def main_async() -> None:
    fire_and_report(may_fail(False))
    fire_and_report(may_fail(True))
    await asyncio.sleep(0.2)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()