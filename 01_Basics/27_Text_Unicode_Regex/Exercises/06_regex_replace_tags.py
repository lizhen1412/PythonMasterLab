#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 06: Replace tags with non-greedy regex.

Task:
Implement strip_b_tags(text) -> str to remove <b>...</b>.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/Exercises/06_regex_replace_tags.py
"""

import re


def strip_b_tags(text: str) -> str:
    return re.sub(r"<b>(.*?)</b>", r"\1", text)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    text = "<b>one</b><b>two</b>"
    check("strip", strip_b_tags(text), "onetwo")


if __name__ == "__main__":
    main()
