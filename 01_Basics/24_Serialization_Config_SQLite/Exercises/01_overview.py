#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: Serialization/Config/SQLite.
Author: Lambert

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_json_compact_line.py", "Compact JSON line"),
    ("03_pickle_roundtrip.py", "Pickle roundtrip"),
    ("04_configparser_get.py", "Read config with fallback"),
    ("05_tomllib_parse.py", "Parse TOML string"),
    ("06_sqlite_insert_count.py", "Insert and count rows"),
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