#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：修复计数竞态，使用 Lock。
"""

from __future__ import annotations

import threading

COUNTER = 0
LOCK = threading.Lock()


def worker(times: int, use_lock: bool) -> None:
    global COUNTER
    for _ in range(times):
        if use_lock:
            with LOCK:
                COUNTER += 1
        else:
            COUNTER += 1


def run(use_lock: bool) -> int:
    global COUNTER
    COUNTER = 0
    threads = [threading.Thread(target=worker, args=(100_000, use_lock)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return COUNTER


def main() -> None:
    expected = 4 * 100_000
    no_lock = run(use_lock=False)
    print("无锁结果 ->", no_lock, "(预期", expected, ")")

    locked = run(use_lock=True)
    print("加锁结果 ->", locked, "(预期", expected, ")")


if __name__ == "__main__":
    main()
