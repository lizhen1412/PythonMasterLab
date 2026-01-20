#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: Insert into sorted list.

Task:
Implement insert_sorted(nums, value) -> list[int].

Run:
    python3 01_Basics/26_Collections_Algorithms/Exercises/03_bisect_insert_sorted.py
"""

from bisect import insort


def insert_sorted(nums: list[int], value: int) -> list[int]:
    result = list(nums)
    insort(result, value)
    return result


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("insert 4", insert_sorted([1, 3, 5], 4), [1, 3, 4, 5])
    check("insert 3", insert_sorted([1, 3, 3, 5], 3), [1, 3, 3, 3, 5])


if __name__ == "__main__":
    main()
