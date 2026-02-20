#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: contextlib, assert, and pdb index.
Author: Lambert

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_contextmanager_basics.py", "contextmanager basics"),
    ("03_exitstack_basics.py", "ExitStack usage"),
    ("04_contextlib_helpers.py", "suppress and redirect_stdout"),
    ("05_assert_and_debug.py", "assert and __debug__"),
    ("06_breakpoint_safe.py", "safe breakpoint usage"),
    ("07_chapter_summary.py", "Chapter summary"),
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