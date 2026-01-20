#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: multiprocessing.Queue for results.

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/03_multiprocessing_queue.py
"""

import multiprocessing as mp


def square(n: int, q: mp.Queue) -> None:
    q.put(n * n)


def main() -> None:
    q: mp.Queue = mp.Queue()
    procs = [mp.Process(target=square, args=(n, q)) for n in (2, 3, 4)]

    for p in procs:
        p.start()
    results = [q.get() for _ in procs]
    for p in procs:
        p.join()

    print("results ->", sorted(results))


if __name__ == "__main__":
    main()
