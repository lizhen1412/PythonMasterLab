#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：异步上下文管理（__aenter__/__aexit__）。
Author: Lambert

你会学到：
1) async with 调用 __aenter__/__aexit__
2) 异步资源的获取与释放

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/14_magic_methods_async_context.py
"""

from __future__ import annotations

import asyncio
import time


class AsyncTimer:
    def __init__(self) -> None:
        self.start: float | None = None
        self.elapsed: float | None = None

    async def __aenter__(self) -> "AsyncTimer":
        self.start = time.perf_counter()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> bool:
        end = time.perf_counter()
        self.elapsed = end - (self.start or end)
        print(f"async elapsed: {self.elapsed:.6f}s")
        return False


async def main_async() -> None:
    print("== async with ==")
    async with AsyncTimer() as timer:
        await asyncio.sleep(0.05)
        print("inside async with")
    print("timer.elapsed ->", timer.elapsed)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()