#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: array module basics.

Run:
    python3 01_Basics/26_Collections_Algorithms/04_array_basics.py
"""

from array import array


def main() -> None:
    nums = array("i", [1, 2, 3])
    nums.append(4)
    nums.extend([5, 6])

    print("array ->", nums)
    print("tolist ->", nums.tolist())
    print("itemsize ->", nums.itemsize)
    print("buffer_info ->", nums.buffer_info())


if __name__ == "__main__":
    main()
