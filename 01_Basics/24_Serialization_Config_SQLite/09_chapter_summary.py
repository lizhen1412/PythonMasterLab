#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 09: Chapter summary.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/09_chapter_summary.py
"""


def main() -> None:
    points = [
        "JSON is text-based; use dumps/loads and control formatting",
        "Custom JSON encoding uses default= for non-serializable objects",
        "Pickle is binary and unsafe for untrusted input",
        "ConfigParser handles INI-style configs with types",
        "tomllib parses TOML strings/files (3.11+)",
        "sqlite3 supports in-memory DBs for quick demos/tests",
        "Always use parameterized queries to avoid injection",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()
