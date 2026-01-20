#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：Condition 与 Barrier。
"""

from __future__ import annotations

import threading
import time


def demo_condition() -> None:
    """
    生产者准备数据后通知消费者。
    Condition 内部带锁：wait 会释放锁、被 notify 唤醒后再重新获得。
    """
    condition = threading.Condition()
    shared: dict[str, int] = {}

    def producer() -> None:
        with condition:
            print("[condition] producer preparing data")
            shared["value"] = 42
            time.sleep(0.1)
            print("[condition] producer notify")
            condition.notify()

    def consumer() -> None:
        with condition:
            print("[condition] consumer waiting")
            condition.wait()
            print("[condition] consumer got", shared.get("value"))

    t1 = threading.Thread(target=consumer)
    t2 = threading.Thread(target=producer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def demo_barrier(parties: int = 3) -> None:
    """Barrier：所有线程到齐后再继续下一阶段。"""
    barrier = threading.Barrier(parties)

    def worker(idx: int) -> None:
        print(f"[barrier] worker {idx} waiting")
        barrier.wait()
        print(f"[barrier] worker {idx} passed barrier")

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(parties)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def main() -> None:
    print("== Condition ==")
    demo_condition()

    print("\n== Barrier ==")
    demo_barrier()


if __name__ == "__main__":
    main()
