#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：Queue 生产者-消费者，哨兵退出。
"""

from __future__ import annotations

import queue
import threading
import time

SENTINEL = object()


def producer(q: queue.Queue[object], items: int = 5) -> None:
    for i in range(items):
        print(f"[producer] put {i}")
        q.put(i)
        time.sleep(0.05)
    print("[producer] put sentinel")
    q.put(SENTINEL)


def consumer(q: queue.Queue[object]) -> None:
    while True:
        item = q.get()
        if item is SENTINEL:
            print("[consumer] got sentinel, exit")
            q.task_done()
            break
        print(f"[consumer] got {item}")
        time.sleep(0.1)
        q.task_done()


def main() -> None:
    q: queue.Queue[object] = queue.Queue()
    t_prod = threading.Thread(target=producer, args=(q,))
    t_cons = threading.Thread(target=consumer, args=(q,))
    t_prod.start()
    t_cons.start()
    q.join()  # 等待所有 task_done
    t_prod.join()
    t_cons.join()
    print("[main] all done")


if __name__ == "__main__":
    main()
