#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：wait_for 包装 to_thread，超时后清理。
"""

from __future__ import annotations

import asyncio
import time


def blocking() -> str:
    try:
        time.sleep(1.0)
        return "done"
    finally:
        print("[blocking] cleanup")


async def main_async() -> None:
    try:
        await asyncio.wait_for(asyncio.to_thread(blocking), timeout=0.2)
    except asyncio.TimeoutError:
        print("timeout -> blocking still running (不可被强杀)")


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
