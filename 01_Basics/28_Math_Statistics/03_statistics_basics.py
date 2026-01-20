#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: statistics module basics.

Run:
    python3 01_Basics/28_Math_Statistics/03_statistics_basics.py
"""

import statistics as stats


def main() -> None:
    data = [1, 2, 3, 4, 5]
    print("mean ->", stats.mean(data))
    print("median ->", stats.median(data))
    print("pstdev ->", stats.pstdev(data))


if __name__ == "__main__":
    main()
