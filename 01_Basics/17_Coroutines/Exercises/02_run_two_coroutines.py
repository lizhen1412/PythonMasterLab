#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：并发运行两个 sleep，比较耗时。
"""

from __future__ import annotations

import asyncio
import time


async def sleeper(delay: float) -> None:
    await asyncio.sleep(delay)


async def main_async() -> None:
    start = time.perf_counter()
    await asyncio.gather(sleeper(0.2), sleeper(0.2))
    concurrent_ms = (time.perf_counter() - start) * 1000

    start = time.perf_counter()
    await sleeper(0.2)
    await sleeper(0.2)
    serial_ms = (time.perf_counter() - start) * 1000

    print(f"并发耗时约 {concurrent_ms:.2f} ms，串行耗时约 {serial_ms:.2f} ms")


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
