#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: Extract last traceback line.
Author: Lambert

Task:
Implement last_traceback_line(func) -> str.

Run:
    python3 01_Basics/25_System_Debug_Testing/Exercises/05_traceback_last_line.py
"""

import traceback


def last_traceback_line(func) -> str:
    try:
        func()
    except Exception:
        return traceback.format_exc().strip().splitlines()[-1]
    return ""


def boom() -> None:
    int("x")


def check(label: str, got: object, expected_contains: str) -> None:
    ok = expected_contains in str(got)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected~={expected_contains!r}")


def main() -> None:
    check("boom", last_traceback_line(boom), "ValueError")


if __name__ == "__main__":
    main()