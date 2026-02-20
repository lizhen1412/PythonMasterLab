#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: Shared counter.
Author: Lambert

Task:
Implement shared_count(workers, times) -> int using Manager.

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/Exercises/04_manager_shared_counter.py
"""

import multiprocessing as mp


def inc(shared, lock: mp.Lock, times: int) -> None:
    for _ in range(times):
        with lock:
            shared["count"] += 1


def shared_count(workers: int, times: int) -> int:
    with mp.Manager() as manager:
        shared = manager.dict()
        shared["count"] = 0
        lock = manager.Lock()
        procs = [mp.Process(target=inc, args=(shared, lock, times)) for _ in range(workers)]
        for p in procs:
            p.start()
        for p in procs:
            p.join()
        return int(shared["count"])


def main() -> None:
    print("count ->", shared_count(2, 5))


if __name__ == "__main__":
    main()