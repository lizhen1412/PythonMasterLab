#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: Chapter summary.
Author: Lambert

Run:
    python3 01_Basics/28_Math_Statistics/06_chapter_summary.py
"""


def main() -> None:
    points = [
        "math provides common numeric functions and constants",
        "statistics offers mean/median and standard deviation",
        "decimal context controls precision and rounding",
        "fractions keep exact rational values",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()