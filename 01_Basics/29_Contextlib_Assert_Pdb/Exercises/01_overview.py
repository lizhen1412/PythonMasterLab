#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: contextlib, assert, and pdb.

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_timer_context.py", "contextmanager timer"),
    ("03_suppress_error.py", "suppress specific error"),
    ("04_exitstack_close.py", "ExitStack closes resources"),
    ("05_assert_positive.py", "assert positive input"),
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
