#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: Multiprocessing and Contextvars index.

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_multiprocessing_process_basics.py", "Process basics"),
    ("03_multiprocessing_queue.py", "Queue for results"),
    ("04_process_pool_executor.py", "ProcessPoolExecutor usage"),
    ("05_manager_shared_dict.py", "Manager shared dict"),
    ("06_contextvars_basics.py", "ContextVar basics"),
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
