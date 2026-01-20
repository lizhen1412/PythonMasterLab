#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：对比线程池处理 CPU vs I/O 耗时。
"""

from __future__ import annotations

import concurrent.futures as cf
import time
from typing import Callable


def measure(fn: Callable[[], None], label: str) -> float:
    start = time.perf_counter()
    fn()
    duration = (time.perf_counter() - start) * 1000
    print(f"{label} -> {duration:.2f} ms")
    return duration


def cpu_task(n: int = 50_000_00) -> None:
    total = 0
    for i in range(n):
        total += i % 7


def io_task(delay: float = 0.05) -> None:
    time.sleep(delay)


def main() -> None:
    measure(cpu_task, "CPU 单线程")
    with cf.ThreadPoolExecutor(max_workers=4) as executor:
        measure(lambda: list(executor.map(cpu_task, [10_000_00] * 4)), "CPU 线程池")

    measure(lambda: [io_task() for _ in range(4)], "I/O 单线程")
    with cf.ThreadPoolExecutor(max_workers=4) as executor:
        measure(lambda: list(executor.map(io_task, [0.05] * 8)), "I/O 线程池")


if __name__ == "__main__":
    main()
