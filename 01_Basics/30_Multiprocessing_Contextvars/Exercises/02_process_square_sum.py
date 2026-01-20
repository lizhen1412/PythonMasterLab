#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: Sum of squares with processes.

Task:
Implement sum_squares(nums) -> int using multiprocessing.Queue.

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/Exercises/02_process_square_sum.py
"""

import multiprocessing as mp


def square_worker(n: int, q: mp.Queue) -> None:
    q.put(n * n)


def sum_squares(nums: list[int]) -> int:
    q: mp.Queue = mp.Queue()
    procs = [mp.Process(target=square_worker, args=(n, q)) for n in nums]
    for p in procs:
        p.start()
    total = 0
    for _ in procs:
        total += q.get()
    for p in procs:
        p.join()
    return total


def main() -> None:
    print("sum_squares ->", sum_squares([1, 2, 3]))


if __name__ == "__main__":
    main()
