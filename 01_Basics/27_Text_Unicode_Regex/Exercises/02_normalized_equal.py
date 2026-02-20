#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: Compare after normalization.
Author: Lambert

Task:
Implement normalized_equal(a, b) -> bool using NFC.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/Exercises/02_normalized_equal.py
"""

import unicodedata


def normalized_equal(a: str, b: str) -> bool:
    return unicodedata.normalize("NFC", a) == unicodedata.normalize("NFC", b)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    a = "caf\u00e9"
    b = "cafe\u0301"
    check("normalize", normalized_equal(a, b), True)


if __name__ == "__main__":
    main()