#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: Math and Statistics.

Run:
    python3 01_Basics/28_Math_Statistics/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_math_hypot.py", "Distance using math.hypot"),
    ("03_statistics_mean.py", "Mean of list"),
    ("04_decimal_quantize.py", "Decimal rounding"),
    ("05_fraction_simplify.py", "Simplify fraction"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"Directory: {here}")
    print("Exercise files:")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
