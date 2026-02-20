#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：CPU 密集 vs I/O 模拟 —— 线程池收益对比。
Author: Lambert
"""

from __future__ import annotations

import concurrent.futures as cf
import time
from typing import Callable


def measure(fn: Callable[[], None], label: str) -> None:
    start = time.perf_counter()
    fn()
    duration = (time.perf_counter() - start) * 1000
    print(f"{label} -> {duration:.2f} ms")


def cpu_bound(n: int = 50_000_00) -> int:
    total = 0
    for i in range(n):
        total += i % 7
    return total


def io_like(delay: float = 0.05) -> None:
    time.sleep(delay)


def run_cpu_threadpool(workers: int = 4) -> None:
    with cf.ThreadPoolExecutor(max_workers=workers) as executor:
        list(executor.map(cpu_bound, [10_000_00] * workers))


def run_io_threadpool(tasks: int = 10) -> None:
    with cf.ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(io_like, [0.05] * tasks))


def main() -> None:
    print("== CPU 密集 ==")
    measure(cpu_bound, "单线程 CPU")
    measure(run_cpu_threadpool, "线程池 CPU（无明显收益）")

    print("\n== I/O 模拟 ==")
    measure(lambda: [io_like() for _ in range(4)], "单线程 I/O")
    measure(run_io_threadpool, "线程池 I/O（可并发等待）")
    print("结论：线程池适合阻塞 I/O，不适合 CPU 密集求加速。")


if __name__ == "__main__":
    main()