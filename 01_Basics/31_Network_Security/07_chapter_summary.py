#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 07: Chapter summary.

Run:
    python3 01_Basics/31_Network_Security/07_chapter_summary.py
"""


def main() -> None:
    points = [
        "urllib.parse handles URL parsing and encoding",
        "Request objects can be built without sending",
        "hashlib provides standard digests",
        "hmac.compare_digest avoids timing leaks",
        "ssl.create_default_context configures TLS defaults",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()
