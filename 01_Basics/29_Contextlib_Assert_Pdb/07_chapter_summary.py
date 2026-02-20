#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 07: Chapter summary.
Author: Lambert

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/07_chapter_summary.py
"""


def main() -> None:
    points = [
        "contextmanager builds lightweight context managers",
        "ExitStack handles dynamic cleanup",
        "suppress and redirect_stdout are handy helpers",
        "assert is for internal checks; __debug__ indicates optimization",
        "breakpoint can be disabled via PYTHONBREAKPOINT=0",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()