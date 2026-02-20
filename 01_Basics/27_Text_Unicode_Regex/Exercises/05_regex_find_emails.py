#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: Find emails.
Author: Lambert

Task:
Implement find_emails(text) -> list[str].

Run:
    python3 01_Basics/27_Text_Unicode_Regex/Exercises/05_regex_find_emails.py
"""

import re


def find_emails(text: str) -> list[str]:
    pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    return pattern.findall(text)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    text = "Contact a@b.com or test.user@example.org"
    check("emails", find_emails(text), ["a@b.com", "test.user@example.org"])


if __name__ == "__main__":
    main()