#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：GIL 与性能：I/O vs CPU。
"""

from __future__ import annotations

import threading
import time
from typing import Callable


def measure(fn: Callable[[], None], label: str) -> None:
    start = time.perf_counter()
    fn()
    duration = (time.perf_counter() - start) * 1000
    print(f"{label} -> {duration:.2f} ms")


def io_bound_simulation(count: int = 5, delay: float = 0.05) -> None:
    """sleep 模拟 I/O，线程可并行等待。"""
    def task() -> None:
        time.sleep(delay)

    threads = [threading.Thread(target=task) for _ in range(count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def cpu_bound_simulation(count: int = 2, n: int = 50_000_00) -> None:
    """CPU 密集：简单循环累加，不会因线程显著提速。"""
    def task() -> None:
        total = 0
        for i in range(n):
            total += i % 7

    threads = [threading.Thread(target=task) for _ in range(count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def single_cpu_task(n: int = 50_000_00) -> None:
    total = 0
    for i in range(n):
        total += i % 7


def main() -> None:
    print("== I/O 模拟（sleep） ==")
    measure(lambda: io_bound_simulation(), "多线程等待 I/O")

    print("\n== CPU 密集 ==")
    measure(single_cpu_task, "单线程 CPU 任务")
    measure(lambda: cpu_bound_simulation(), "多线程 CPU 任务")
    print("提示：CPU 密集不建议用线程提速，可考虑 multiprocessing 或 C 扩展。")


if __name__ == "__main__":
    main()
