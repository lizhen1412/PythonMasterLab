#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: struct pack/unpack basics.

Run:
    python3 01_Basics/26_Collections_Algorithms/05_struct_basics.py
"""

import struct


def main() -> None:
    values = (1, 2, 255)
    packed = struct.pack("!HHB", *values)
    print("packed ->", packed)

    unpacked = struct.unpack("!HHB", packed)
    print("unpacked ->", unpacked)

    little = struct.pack("<I", 1024)
    big = struct.pack(">I", 1024)
    print("little endian ->", little)
    print("big endian ->", big)


if __name__ == "__main__":
    main()
