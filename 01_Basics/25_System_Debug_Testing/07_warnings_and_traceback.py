#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 07: warnings and traceback.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/07_warnings_and_traceback.py
"""

import traceback
import warnings


def risky_divide(a: int, b: int) -> float:
    if b == 0:
        warnings.warn("b is zero; defaulting to 1", RuntimeWarning)
        b = 1
    return a / b


def main() -> None:
    with warnings.catch_warnings(record=True) as records:
        warnings.simplefilter("always")
        print("result ->", risky_divide(10, 0))
        print("warnings ->", len(records))
        if records:
            print("warning message ->", records[0].message)

    try:
        int("x")
    except ValueError:
        line = traceback.format_exc().strip().splitlines()[-1]
        print("traceback last line ->", line)


if __name__ == "__main__":
    main()