#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：Barrier 同步两阶段工作。
"""

from __future__ import annotations

import threading
import time


def two_phase_work(barrier: threading.Barrier, idx: int) -> None:
    print(f"[worker {idx}] phase1")
    time.sleep(0.05 * idx)
    barrier.wait()
    print(f"[worker {idx}] phase2")


def main() -> None:
    barrier = threading.Barrier(3)
    threads = [threading.Thread(target=two_phase_work, args=(barrier, i)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("[main] all done")


if __name__ == "__main__":
    main()
