#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：RLock 与 Semaphore。
"""

from __future__ import annotations

import threading
import time


def demo_rlock() -> None:
    """同一线程可重复获取 RLock；普通 Lock 会死锁。"""
    lock = threading.RLock()

    def nested() -> None:
        with lock:
            print("[RLock] outer acquired")
            with lock:
                print("[RLock] inner acquired")

    t = threading.Thread(target=nested, name="rlock-thread")
    t.start()
    t.join()


def demo_semaphore(max_workers: int = 3) -> None:
    """Semaphore 限制同时进入的线程数。"""
    sem = threading.Semaphore(max_workers)

    def worker(i: int) -> None:
        with sem:
            print(f"[sem] worker {i} start")
            time.sleep(0.2)
            print(f"[sem] worker {i} end")

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def main() -> None:
    print("== RLock ==")
    demo_rlock()

    print("\n== Semaphore 限流 ==")
    demo_semaphore()


if __name__ == "__main__":
    main()
