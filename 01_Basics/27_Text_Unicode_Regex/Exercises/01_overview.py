#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: Text, Unicode, and Regex.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_normalized_equal.py", "Compare after normalization"),
    ("03_safe_decode.py", "Decode with error handling"),
    ("04_regex_extract_dates.py", "Extract dates with regex"),
    ("05_regex_find_emails.py", "Find emails"),
    ("06_regex_replace_tags.py", "Replace tags with non-greedy"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"Directory: {here}")
    print("Exercise files:")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
