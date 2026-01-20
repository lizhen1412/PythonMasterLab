#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: Distance using math.hypot.

Task:
Implement distance(x, y) -> float.

Run:
    python3 01_Basics/28_Math_Statistics/Exercises/02_math_hypot.py
"""

import math


def distance(x: float, y: float) -> float:
    return math.hypot(x, y)


def check(label: str, got: object, expected: object) -> None:
    ok = abs(got - expected) < 1e-9
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("(3,4)", distance(3, 4), 5.0)
    check("(0,0)", distance(0, 0), 0.0)


if __name__ == "__main__":
    main()
