#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：竞态反例 + Lock 修复。
"""

from __future__ import annotations

import threading
from typing import Callable

COUNTER = 0
LOCK = threading.Lock()


def add_without_lock(times: int) -> None:
    global COUNTER
    for _ in range(times):
        COUNTER += 1


def add_with_lock(times: int) -> None:
    global COUNTER
    for _ in range(times):
        with LOCK:
            COUNTER += 1


def run_in_threads(fn: Callable[[int], None], threads: int = 4, per_thread: int = 100_000) -> int:
    global COUNTER
    COUNTER = 0
    workers = [threading.Thread(target=fn, args=(per_thread,)) for _ in range(threads)]
    for t in workers:
        t.start()
    for t in workers:
        t.join()
    return COUNTER


def main() -> None:
    expected = 4 * 100_000
    wrong = run_in_threads(add_without_lock)
    print("无锁结果 ->", wrong, "(预期", expected, ")")

    right = run_in_threads(add_with_lock)
    print("加锁结果 ->", right, "(预期", expected, ")")

    print("结论：共享可变状态需要锁/同步原语防止竞态。")


if __name__ == "__main__":
    main()
