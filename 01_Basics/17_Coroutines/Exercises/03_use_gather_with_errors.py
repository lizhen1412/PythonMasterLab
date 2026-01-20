#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：gather 处理异常（return_exceptions 对比）。
"""

from __future__ import annotations

import asyncio


async def may_fail(x: int) -> int:
    await asyncio.sleep(0.05)
    if x == 2:
        raise ValueError("x=2 bad")
    return x * 2


async def main_async() -> None:
    tasks = [may_fail(i) for i in range(4)]
    try:
        await asyncio.gather(*tasks)
    except Exception as exc:
        print("gather raised ->", type(exc).__name__, exc)

    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("gather return_exceptions ->", results)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
