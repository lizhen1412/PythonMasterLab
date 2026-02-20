#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: Serialization/Config/SQLite index.
Author: Lambert

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_json_dumps_loads.py", "JSON dumps/loads basics"),
    ("03_json_file_like_custom_encoder.py", "File-like JSON + custom encoder"),
    ("04_pickle_roundtrip.py", "Pickle roundtrip and warning"),
    ("05_configparser_basics.py", "ConfigParser basics"),
    ("06_tomllib_basics.py", "TOML parsing with tomllib"),
    ("07_sqlite_in_memory_basics.py", "sqlite3 in-memory usage"),
    ("08_sqlite_row_factory_and_params.py", "Row factory + parameterized queries"),
    ("09_chapter_summary.py", "Chapter summary"),
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