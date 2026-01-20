#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：异步生成器基础。

你会学到：
1) async def + yield 定义异步生成器
2) 只能用 async for 消费
3) 适合 I/O 等待型流式处理

运行：
    python3 01_Basics/21_Iterators_Generators/12_async_generator_basics.py
"""

import asyncio


async def ticker(delay: float, count: int):
    for i in range(count):
        await asyncio.sleep(delay)
        yield i


async def run() -> None:
    async for value in ticker(0.05, 3):
        print("tick ->", value)


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
