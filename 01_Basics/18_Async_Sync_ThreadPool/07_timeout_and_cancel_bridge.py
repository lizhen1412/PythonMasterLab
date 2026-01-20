#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：wait_for/asyncio.timeout + to_thread，取消与清理。
"""

from __future__ import annotations

import asyncio
import time


def blocking_long() -> str:
    try:
        time.sleep(1.0)
        return "done"
    finally:
        print("[blocking_long] cleanup")


async def demo_wait_for() -> None:
    try:
        await asyncio.wait_for(asyncio.to_thread(blocking_long), timeout=0.2)
    except asyncio.TimeoutError:
        print("wait_for timeout -> blocking task likely still running")


async def demo_timeout_ctx() -> None:
    try:
        async with asyncio.timeout(0.2):
            await asyncio.to_thread(blocking_long)
    except asyncio.TimeoutError:
        print("asyncio.timeout context -> timeout")


async def main_async() -> None:
    print("== wait_for + to_thread ==")
    await demo_wait_for()

    print("\n== asyncio.timeout + to_thread ==")
    await demo_timeout_ctx()
    print("提示：to_thread 里的阻塞调用不会被强制杀死；需自行设计可终止的阻塞操作。")


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
