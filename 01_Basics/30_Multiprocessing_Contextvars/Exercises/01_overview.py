#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: Multiprocessing and Contextvars.

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_process_square_sum.py", "Sum of squares with processes"),
    ("03_process_pool_map.py", "ProcessPoolExecutor map"),
    ("04_manager_shared_counter.py", "Shared counter"),
    ("05_contextvar_token.py", "ContextVar set/reset"),
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
