#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 10: Chapter summary.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/10_chapter_summary.py
"""


def main() -> None:
    points = [
        "os/sys provide process and environment details",
        "tempfile + shutil enable safe temporary operations",
        "subprocess.run is the simplest way to call external commands",
        "signal and atexit handle lifecycle hooks",
        "logging handlers/filters control where messages go",
        "warnings and traceback help diagnose issues",
        "unittest provides structured tests",
        "timeit and cProfile give quick performance insight",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()