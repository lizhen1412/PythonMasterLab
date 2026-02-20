#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：Queue 任务 + 哨兵退出。
Author: Lambert
"""

from __future__ import annotations

import queue
import threading
import time

SENTINEL = object()


def producer(q: queue.Queue[object]) -> None:
    for i in range(3):
        q.put(i)
        print(f"[producer] put {i}")
    q.put(SENTINEL)
    print("[producer] put sentinel")


def consumer(q: queue.Queue[object]) -> None:
    while True:
        item = q.get()
        if item is SENTINEL:
            print("[consumer] got sentinel, exit")
            q.task_done()
            break
        print(f"[consumer] got {item}")
        time.sleep(0.05)
        q.task_done()


def main() -> None:
    q: queue.Queue[object] = queue.Queue()
    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()
    q.join()
    t1.join()
    t2.join()
    print("[main] done")


if __name__ == "__main__":
    main()