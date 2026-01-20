#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: Compute sha256.

Task:
Implement sha256_hex(text) -> str.

Run:
    python3 01_Basics/31_Network_Security/Exercises/04_hash_password.py
"""

import hashlib


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check(label: str, got: str, expected_len: int) -> None:
    ok = len(got) == expected_len
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: len={len(got)} expected={expected_len}")


def main() -> None:
    check("sha", sha256_hex("hello"), 64)


if __name__ == "__main__":
    main()
