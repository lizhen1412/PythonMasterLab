#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: Math and Statistics index.

Run:
    python3 01_Basics/28_Math_Statistics/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_math_basics.py", "math module basics"),
    ("03_statistics_basics.py", "statistics module basics"),
    ("04_decimal_context.py", "decimal context and rounding"),
    ("05_fractions_advanced.py", "fractions advanced usage"),
    ("06_chapter_summary.py", "Chapter summary"),
    ("Exercises/01_overview.py", "Exercises index"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"Directory: {here}")
    print("Lesson files:")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
