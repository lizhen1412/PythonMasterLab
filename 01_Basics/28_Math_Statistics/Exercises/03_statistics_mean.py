#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: Mean of list.

Task:
Implement mean_value(nums) -> float.

Run:
    python3 01_Basics/28_Math_Statistics/Exercises/03_statistics_mean.py
"""

import statistics as stats


def mean_value(nums: list[float]) -> float:
    return stats.mean(nums) if nums else 0.0


def check(label: str, got: object, expected: object) -> None:
    ok = abs(got - expected) < 1e-9
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("mean", mean_value([1, 2, 3]), 2.0)
    check("empty", mean_value([]), 0.0)


if __name__ == "__main__":
    main()
