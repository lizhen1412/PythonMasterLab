#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: Parse bytes with struct.
Author: Lambert

Task:
Implement parse_header(data) -> tuple[int, int].
Format: !HB (unsigned short, unsigned char).

Run:
    python3 01_Basics/26_Collections_Algorithms/Exercises/05_struct_parse_header.py
"""

import struct


def parse_header(data: bytes) -> tuple[int, int]:
    return struct.unpack("!HB", data)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    data = struct.pack("!HB", 513, 7)
    check("parse", parse_header(data), (513, 7))


if __name__ == "__main__":
    main()