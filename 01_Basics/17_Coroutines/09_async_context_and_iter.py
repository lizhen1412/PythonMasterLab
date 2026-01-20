#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：async with 与 async for。
"""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator


@asynccontextmanager
async def async_resource(name: str) -> AsyncIterator[str]:
    print(f"[{name}] acquiring")
    await asyncio.sleep(0.05)
    try:
        yield name
    finally:
        print(f"[{name}] releasing")
        await asyncio.sleep(0.05)


class AsyncCounter:
    """一个简单的 async 可迭代对象。"""

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.current = 0

    def __aiter__(self) -> "AsyncCounter":
        return self

    async def __anext__(self) -> int:
        if self.current >= self.limit:
            raise StopAsyncIteration
        await asyncio.sleep(0.02)
        self.current += 1
        return self.current


async def main_async() -> None:
    print("== async with ==")
    async with async_resource("res"):
        print("using resource")

    print("\n== async for ==")
    async for value in AsyncCounter(3):
        print("got", value)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
