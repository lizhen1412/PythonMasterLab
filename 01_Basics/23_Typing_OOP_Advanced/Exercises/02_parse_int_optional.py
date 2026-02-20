#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: Optional return for parsing.
Author: Lambert

Task:
Implement parse_int(text) -> int | None.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/Exercises/02_parse_int_optional.py
"""

from __future__ import annotations


def parse_int(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("parse_int('7')", parse_int("7"), 7)
    check("parse_int('x')", parse_int("x"), None)
    check("parse_int('-3')", parse_int("-3"), -3)


if __name__ == "__main__":
    main()