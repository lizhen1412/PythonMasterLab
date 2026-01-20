#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: locale basics.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/04_locale_basics.py
"""

import locale


def main() -> None:
    try:
        current = locale.setlocale(locale.LC_ALL, "")
    except locale.Error:
        current = locale.setlocale(locale.LC_ALL, None)

    print("locale ->", current)
    conv = locale.localeconv()
    print("decimal_point ->", conv.get("decimal_point"))
    print("thousands_sep ->", conv.get("thousands_sep"))

    value = 12345.67
    formatted = locale.format_string("%.2f", value, grouping=True)
    print("formatted ->", formatted)


if __name__ == "__main__":
    main()
