#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 07: Chapter summary.
Author: Lambert

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/07_chapter_summary.py
"""


def main() -> None:
    points = [
        "multiprocessing uses separate processes and needs __main__ guard",
        "Queue and Manager allow data exchange across processes",
        "ProcessPoolExecutor provides a high-level API",
        "ContextVar isolates context values across tasks",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()