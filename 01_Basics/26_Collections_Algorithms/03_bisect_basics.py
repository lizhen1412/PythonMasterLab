#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: bisect and insort.
Author: Lambert

Run:
    python3 01_Basics/26_Collections_Algorithms/03_bisect_basics.py
"""

from bisect import bisect_left, bisect_right, insort


def main() -> None:
    nums = [1, 3, 3, 6, 7]
    print("nums ->", nums)
    print("bisect_left(3) ->", bisect_left(nums, 3))
    print("bisect_right(3) ->", bisect_right(nums, 3))

    insort(nums, 4)
    print("after insort(4) ->", nums)
    insort(nums, 3)
    print("after insort(3) ->", nums)


if __name__ == "__main__":
    main()