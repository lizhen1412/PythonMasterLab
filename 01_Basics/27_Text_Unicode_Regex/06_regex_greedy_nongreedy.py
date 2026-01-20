#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: Greedy vs non-greedy regex.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/06_regex_greedy_nongreedy.py
"""

import re


def main() -> None:
    text = "<b>one</b><b>two</b>"

    greedy = re.findall(r"<b>.*</b>", text)
    nongreedy = re.findall(r"<b>.*?</b>", text)

    print("greedy ->", greedy)
    print("non-greedy ->", nongreedy)


if __name__ == "__main__":
    main()
