#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 09: timeit and cProfile basics.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/09_timeit_and_cprofile.py
"""

import cProfile
import io
import pstats
import timeit


def work() -> int:
    total = 0
    for i in range(1000):
        total += i * i
    return total


def main() -> None:
    t = timeit.timeit("work()", globals=globals(), number=1000)
    print("timeit (1000 runs) ->", f"{t:.4f}s")

    prof = cProfile.Profile()
    prof.runcall(work)
    stream = io.StringIO()
    stats = pstats.Stats(prof, stream=stream).sort_stats("cumulative")
    stats.print_stats(5)
    print("profile top ->")
    print(stream.getvalue().strip())


if __name__ == "__main__":
    main()