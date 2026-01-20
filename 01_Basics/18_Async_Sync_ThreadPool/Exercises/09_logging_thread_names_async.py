#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：logging 打印线程名与 async 上下文，运行混合任务。
"""

from __future__ import annotations

import asyncio
import concurrent.futures as cf
import logging
import time


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)s] %(message)s",
    )


def blocking_job() -> None:
    logging.info("blocking job start")
    time.sleep(0.1)
    logging.info("blocking job end")


async def async_job() -> None:
    logging.info("async job start")
    await asyncio.sleep(0.05)
    logging.info("async job end")


async def main_async() -> None:
    configure_logging()
    loop = asyncio.get_running_loop()
    with cf.ThreadPoolExecutor(max_workers=2, thread_name_prefix="pool") as executor:
        await asyncio.gather(
            async_job(),
            loop.run_in_executor(executor, blocking_job),
            loop.run_in_executor(executor, blocking_job),
        )


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
