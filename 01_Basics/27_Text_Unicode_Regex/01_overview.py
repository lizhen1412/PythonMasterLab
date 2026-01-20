#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: Text, Unicode, and Regex index.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_unicode_normalization.py", "unicodedata normalization"),
    ("03_encoding_errors.py", "encoding/decoding error strategies"),
    ("04_locale_basics.py", "locale basics"),
    ("05_regex_compiled_groups.py", "compiled regex with groups"),
    ("06_regex_greedy_nongreedy.py", "greedy vs non-greedy"),
    ("07_regex_verbose_flags.py", "verbose patterns and flags"),
    ("08_chapter_summary.py", "Chapter summary"),
    ("Exercises/01_overview.py", "Exercises index"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"Directory: {here}")
    print("Lesson files:")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
