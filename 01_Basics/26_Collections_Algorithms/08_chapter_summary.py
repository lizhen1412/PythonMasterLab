#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 08: Chapter summary.
Author: Lambert

Run:
    python3 01_Basics/26_Collections_Algorithms/08_chapter_summary.py
"""


def main() -> None:
    points = [
        "heapq provides min-heap operations and top-k helpers",
        "bisect keeps sorted lists efficient without full re-sort",
        "array stores typed numeric data compactly",
        "struct packs/unpacks binary data with format strings",
        "enum provides named constants and bit flags",
        "collections.abc offers protocol-style checks",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()