#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: System/Debug/Testing index.

Run:
    python3 01_Basics/25_System_Debug_Testing/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_os_sys_basics.py", "os/sys essentials"),
    ("03_shutil_tempfile_basics.py", "shutil + tempfile"),
    ("04_subprocess_basics.py", "subprocess basics"),
    ("05_signal_and_atexit.py", "signal + atexit"),
    ("06_logging_handlers_and_filters.py", "logging handlers/filters"),
    ("07_warnings_and_traceback.py", "warnings + traceback"),
    ("08_unittest_basics.py", "unittest basics"),
    ("09_timeit_and_cprofile.py", "timeit + cProfile"),
    ("10_chapter_summary.py", "Chapter summary"),
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
