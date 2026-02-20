#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: System/Debug/Testing.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_get_env_default.py", "getenv with default"),
    ("03_subprocess_capture.py", "run Python and capture output"),
    ("04_warning_capture.py", "capture warnings"),
    ("05_traceback_last_line.py", "extract last traceback line"),
    ("06_unittest_small.py", "small unittest example"),
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