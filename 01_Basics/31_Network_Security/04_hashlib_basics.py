#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: hashlib basics.

Run:
    python3 01_Basics/31_Network_Security/04_hashlib_basics.py
"""

import hashlib


def main() -> None:
    text = "hello"
    h = hashlib.sha256(text.encode("utf-8"))
    print("hexdigest ->", h.hexdigest())
    print("digest length ->", len(h.digest()))


if __name__ == "__main__":
    main()
