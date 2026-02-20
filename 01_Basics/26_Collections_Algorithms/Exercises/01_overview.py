#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: Collections and Algorithms.
Author: Lambert

Run:
    python3 01_Basics/26_Collections_Algorithms/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_heapq_top_k.py", "Top-k using heapq"),
    ("03_bisect_insert_sorted.py", "Insert into sorted list"),
    ("04_array_average.py", "Average from array"),
    ("05_struct_parse_header.py", "Parse bytes with struct"),
    ("06_enum_status_parse.py", "Parse enum status"),
    ("07_collections_abc_is_sequence.py", "Sequence check"),
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