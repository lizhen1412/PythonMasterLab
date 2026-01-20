#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：超时与取消（wait_for / asyncio.timeout / task.cancel）。
"""

from __future__ import annotations

import asyncio


async def slow_task() -> str:
    try:
        await asyncio.sleep(1.0)
        return "done"
    except asyncio.CancelledError:
        print("[slow_task] cancelled, cleaning up")
        raise


async def demo_wait_for() -> None:
    try:
        await asyncio.wait_for(slow_task(), timeout=0.2)
    except asyncio.TimeoutError:
        print("wait_for timeout")


async def demo_timeout_ctx() -> None:
    try:
        async with asyncio.timeout(0.2):
            await slow_task()
    except asyncio.TimeoutError:
        print("asyncio.timeout context -> timeout")


async def demo_cancel() -> None:
    task = asyncio.create_task(slow_task())
    await asyncio.sleep(0.1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("task cancelled caught in caller")


async def main_async() -> None:
    print("== wait_for 超时 ==")
    await demo_wait_for()

    print("\n== asyncio.timeout 上下文 ==")
    await demo_timeout_ctx()

    print("\n== task.cancel ==")
    await demo_cancel()


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
