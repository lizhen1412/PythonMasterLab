#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 08: Chapter summary.
Author: Lambert

Run:
    python3 01_Basics/27_Text_Unicode_Regex/08_chapter_summary.py
"""


def main() -> None:
    points = [
        "Normalize Unicode before comparison (NFC/NFD)",
        "Choose explicit error strategies for encode/decode",
        "Locale affects formatting and separators",
        "Regex compiled patterns are reusable and faster",
        "Non-greedy patterns stop at the nearest match",
        "Verbose mode improves readability of complex regex",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()