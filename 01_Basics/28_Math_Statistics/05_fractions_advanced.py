#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: fractions advanced usage.
Author: Lambert

Run:
    python3 01_Basics/28_Math_Statistics/05_fractions_advanced.py
"""

from fractions import Fraction


def main() -> None:
    f = Fraction(2, 4)
    print("2/4 simplified ->", f)

    approx = Fraction.from_float(0.1).limit_denominator()
    print("0.1 as fraction ->", approx)

    ratio = Fraction(22, 7)
    print("22/7 as float ->", float(ratio))


if __name__ == "__main__":
    main()