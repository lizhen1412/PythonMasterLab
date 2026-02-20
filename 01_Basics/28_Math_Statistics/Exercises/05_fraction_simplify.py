#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: Simplify fraction.
Author: Lambert

Task:
Implement simplify(numer, denom) -> str.

Run:
    python3 01_Basics/28_Math_Statistics/Exercises/05_fraction_simplify.py
"""

from fractions import Fraction


def simplify(numer: int, denom: int) -> str:
    return str(Fraction(numer, denom))


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("2/4", simplify(2, 4), "1/2")
    check("3/9", simplify(3, 9), "1/3")


if __name__ == "__main__":
    main()