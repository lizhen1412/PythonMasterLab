#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：线程池多任务，处理异常与超时。
Author: Lambert
"""

from __future__ import annotations

import concurrent.futures as cf
import time


def task(x: int) -> int:
    if x == 3:
        time.sleep(0.3)
    if x == 5:
        raise ValueError("boom")
    return x * 2


def main() -> None:
    successes: list[int] = []
    failures: list[str] = []
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(task, i): i for i in range(6)}
        for fut in cf.as_completed(futures, timeout=1):
            i = futures[fut]
            try:
                result = fut.result(timeout=0.2)
                successes.append(result)
            except Exception as exc:
                failures.append(f"task {i}: {type(exc).__name__} {exc}")

    print("success ->", successes)
    print("failures ->", failures)


if __name__ == "__main__":
    main()