#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: Decode with error handling.
Author: Lambert

Task:
Implement safe_decode(data) -> str using utf-8 and errors='replace'.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/Exercises/03_safe_decode.py
"""


def safe_decode(data: bytes) -> str:
    return data.decode("utf-8", errors="replace")


def check(label: str, got: object, expected_contains: str) -> None:
    ok = expected_contains in str(got)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected~={expected_contains!r}")


def main() -> None:
    data = b"caf\xe9"
    result = safe_decode(data)
    check("replace", result, "caf")


if __name__ == "__main__":
    main()