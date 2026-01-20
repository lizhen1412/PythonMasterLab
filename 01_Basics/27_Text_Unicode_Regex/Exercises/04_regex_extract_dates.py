#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: Extract dates with regex.

Task:
Implement extract_dates(text) -> list[str] for YYYY-MM-DD.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/Exercises/04_regex_extract_dates.py
"""

import re


def extract_dates(text: str) -> list[str]:
    pattern = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
    return pattern.findall(text)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    text = "a=2024-05-20 b=1999-01-01 x=202-1-1"
    check("dates", extract_dates(text), ["2024-05-20", "1999-01-01"])


if __name__ == "__main__":
    main()
