#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: Network and Security basics index.

Run:
    python3 01_Basics/31_Network_Security/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_urllib_parse_basics.py", "URL parsing and encoding"),
    ("03_urllib_request_build.py", "Build Request objects"),
    ("04_hashlib_basics.py", "Hashing basics"),
    ("05_hmac_basics.py", "HMAC basics"),
    ("06_ssl_context_basics.py", "SSL context basics"),
    ("07_chapter_summary.py", "Chapter summary"),
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
