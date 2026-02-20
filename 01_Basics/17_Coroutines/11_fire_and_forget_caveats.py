#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：fire-and-forget 风险，添加回调监控异常。
Author: Lambert
"""

from __future__ import annotations

import asyncio


async def risky_task() -> None:
    await asyncio.sleep(0.05)
    raise RuntimeError("fire-and-forget error")


def safe_fire_and_forget(coro: asyncio.coroutine) -> asyncio.Task:
    """创建任务并添加异常回调，避免静默丢失。"""
    task = asyncio.create_task(coro)

    def _on_done(fut: asyncio.Task) -> None:
        if exc := fut.exception():
            print("[safe_fire_and_forget] caught exception ->", type(exc).__name__, exc)

    task.add_done_callback(_on_done)
    return task


async def main_async() -> None:
    print("== fire-and-forget 不监控 ==")
    asyncio.create_task(risky_task())
    await asyncio.sleep(0.1)
    print("若未监控，异常可能仅在日志中出现（或被忽略）。")

    print("\n== 安全封装 ==")
    safe_fire_and_forget(risky_task())
    await asyncio.sleep(0.1)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()