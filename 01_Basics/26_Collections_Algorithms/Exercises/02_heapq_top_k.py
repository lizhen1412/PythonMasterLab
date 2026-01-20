#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: Top-k using heapq.

Task:
Implement top_k(nums, k) -> list[int].

Run:
    python3 01_Basics/26_Collections_Algorithms/Exercises/02_heapq_top_k.py
"""

import heapq


def top_k(nums: list[int], k: int) -> list[int]:
    if k <= 0:
        return []
    return heapq.nlargest(k, nums)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("top2", top_k([3, 1, 5, 2, 4], 2), [5, 4])
    check("k=0", top_k([1, 2], 0), [])


if __name__ == "__main__":
    main()
