#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: ProcessPoolExecutor map.

Task:
Implement pool_squares(nums) -> list[int].

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/Exercises/03_process_pool_map.py
"""

from concurrent.futures import ProcessPoolExecutor


def square(n: int) -> int:
    return n * n


def pool_squares(nums: list[int]) -> list[int]:
    with ProcessPoolExecutor(max_workers=2) as executor:
        return list(executor.map(square, nums))


def main() -> None:
    print("pool_squares ->", pool_squares([2, 3, 4]))


if __name__ == "__main__":
    main()
