#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: Capture warnings.

Task:
Implement count_warnings(func) -> int using warnings.catch_warnings.

Run:
    python3 01_Basics/25_System_Debug_Testing/Exercises/04_warning_capture.py
"""

import warnings


def count_warnings(func) -> int:
    with warnings.catch_warnings(record=True) as records:
        warnings.simplefilter("always")
        func()
        return len(records)


def emit_two() -> None:
    warnings.warn("first", RuntimeWarning)
    warnings.warn("second", RuntimeWarning)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("two warnings", count_warnings(emit_two), 2)


if __name__ == "__main__":
    main()
