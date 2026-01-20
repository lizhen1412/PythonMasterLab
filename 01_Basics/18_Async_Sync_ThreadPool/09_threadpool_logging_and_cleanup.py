#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：线程名日志，shutdown(cancel_futures) 行为与清理。
"""

from __future__ import annotations

import concurrent.futures as cf
import logging
import time


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)s] %(message)s",
    )


def work(x: int) -> str:
    try:
        time.sleep(0.2)
        return f"done-{x}"
    finally:
        logging.info("cleanup for %s", x)


def main() -> None:
    configure_logging()
    executor = cf.ThreadPoolExecutor(max_workers=2, thread_name_prefix="worker")
    futures = [executor.submit(work, i) for i in range(4)]

    # 提前关闭，取消未开始的任务
    executor.shutdown(wait=False, cancel_futures=True)
    logging.info("shutdown called (cancel_futures=True)")

    for fut in futures:
        if fut.cancelled():
            logging.info("future cancelled")
        else:
            try:
                logging.info("result -> %s", fut.result(timeout=1))
            except Exception as exc:
                logging.info("caught -> %s %s", type(exc).__name__, exc)


if __name__ == "__main__":
    main()
