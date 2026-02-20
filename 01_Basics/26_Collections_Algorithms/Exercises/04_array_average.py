#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: Average from array.
Author: Lambert

Task:
Implement average(nums) -> float using array('d').

Run:
    python3 01_Basics/26_Collections_Algorithms/Exercises/04_array_average.py
"""

from array import array


def average(nums: list[float]) -> float:
    if not nums:
        return 0.0
    arr = array("d", nums)
    return sum(arr) / len(arr)


def check(label: str, got: object, expected: object) -> None:
    ok = abs(got - expected) < 1e-9
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("avg", average([1.0, 2.0, 3.0]), 2.0)
    check("empty", average([]), 0.0)


if __name__ == "__main__":
    main()