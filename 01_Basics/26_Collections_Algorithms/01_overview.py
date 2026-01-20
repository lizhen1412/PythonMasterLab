#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: Collections and Algorithms index.

Run:
    python3 01_Basics/26_Collections_Algorithms/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_heapq_basics.py", "heapq basics and priority queue"),
    ("03_bisect_basics.py", "bisect and insort"),
    ("04_array_basics.py", "array module basics"),
    ("05_struct_basics.py", "struct pack/unpack"),
    ("06_enum_basics.py", "Enum, IntEnum, Flag"),
    ("07_collections_abc_basics.py", "collections.abc checks"),
    ("08_chapter_summary.py", "Chapter summary"),
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
