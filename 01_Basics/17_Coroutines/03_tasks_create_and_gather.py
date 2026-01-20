#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：任务创建与 gather/as_completed。
"""

from __future__ import annotations

import asyncio
import random
from typing import Any


async def work(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    if name == "fail":
        raise RuntimeError("boom")
    return f"{name} done in {delay:.2f}s"


async def demo_gather() -> None:
    tasks = [
        work("A", 0.2),
        work("B", 0.1),
        work("fail", 0.15),
    ]
    try:
        results = await asyncio.gather(*tasks)
        print("gather results ->", results)
    except Exception as exc:
        print("gather raised ->", type(exc).__name__, exc)

    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("gather return_exceptions ->", results)


async def demo_as_completed() -> None:
    tasks = [asyncio.create_task(work(f"T{i}", random.uniform(0.05, 0.2))) for i in range(3)]
    for coro in asyncio.as_completed(tasks):
        try:
            result = await coro
            print("as_completed result ->", result)
        except Exception as exc:
            print("as_completed caught ->", exc)


async def main_async() -> None:
    print("== gather ==")
    await demo_gather()

    print("\n== as_completed ==")
    await demo_as_completed()


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
