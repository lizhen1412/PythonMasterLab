#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: Compiled regex with groups.
Author: Lambert

Run:
    python3 01_Basics/27_Text_Unicode_Regex/05_regex_compiled_groups.py
"""

import re


def main() -> None:
    pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
    text = "date=2024-05-20"

    match = pattern.search(text)
    if not match:
        print("no match")
        return

    print("group(0) ->", match.group(0))
    print("groups ->", match.groups())
    print("groupdict ->", match.groupdict())


if __name__ == "__main__":
    main()