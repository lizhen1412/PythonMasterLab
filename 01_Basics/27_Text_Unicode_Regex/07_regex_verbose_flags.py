#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 07: Verbose regex and flags.
Author: Lambert

Run:
    python3 01_Basics/27_Text_Unicode_Regex/07_regex_verbose_flags.py
"""

import re


def main() -> None:
    pattern = re.compile(
        r"""
        ^\s*            # leading spaces
        (?P<user>[a-z]+) # user
        @
        (?P<host>[a-z]+) # host
        \.com\s*$       # suffix
        """,
        re.IGNORECASE | re.VERBOSE,
    )

    text = "  Alice@Example.com  "
    match = pattern.match(text)
    print("match ->", bool(match))
    if match:
        print("groups ->", match.groupdict())


if __name__ == "__main__":
    main()