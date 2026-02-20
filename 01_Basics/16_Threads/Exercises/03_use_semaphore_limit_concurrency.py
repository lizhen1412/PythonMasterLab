#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：Semaphore 限制并发任务数。
Author: Lambert
"""

from __future__ import annotations

import threading
import time


def run_with_semaphore(max_concurrent: int = 2, tasks: int = 5) -> None:
    sem = threading.Semaphore(max_concurrent)

    def task(i: int) -> None:
        with sem:
            print(f"[task {i}] start")
            time.sleep(0.1)
            print(f"[task {i}] end")

    threads = [threading.Thread(target=task, args=(i,)) for i in range(tasks)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def main() -> None:
    run_with_semaphore()


if __name__ == "__main__":
    main()