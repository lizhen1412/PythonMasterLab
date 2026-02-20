#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: ProcessPoolExecutor usage.
Author: Lambert

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/04_process_pool_executor.py
"""

from concurrent.futures import ProcessPoolExecutor


def cube(n: int) -> int:
    return n * n * n


def main() -> None:
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(cube, [1, 2, 3, 4]))
    print("results ->", results)


if __name__ == "__main__":
    main()