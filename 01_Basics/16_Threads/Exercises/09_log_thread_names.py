#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：logging 打印线程名。
Author: Lambert
"""

from __future__ import annotations

import logging
import threading
import time


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)s] %(message)s",
    )


def worker(idx: int) -> None:
    logging.info("hello from worker %s", idx)
    time.sleep(0.05)
    logging.info("bye from worker %s", idx)


def main() -> None:
    configure_logging()
    threads = [threading.Thread(target=worker, name=f"worker-{i}", args=(i,)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    logging.info("main done")


if __name__ == "__main__":
    main()