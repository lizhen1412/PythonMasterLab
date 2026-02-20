#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: Encoding/decoding error strategies.
Author: Lambert

Run:
    python3 01_Basics/27_Text_Unicode_Regex/03_encoding_errors.py
"""


def main() -> None:
    text = "caf\u00e9"
    print("text ->", text)

    try:
        text.encode("ascii")
    except UnicodeEncodeError as exc:
        print("encode error ->", exc.__class__.__name__)

    print("encode replace ->", text.encode("ascii", errors="replace"))
    print("encode ignore ->", text.encode("ascii", errors="ignore"))

    data = b"caf\xe9"
    print("decode strict ->", data.decode("latin1"))
    print("decode replace ->", data.decode("utf-8", errors="replace"))
    print("decode backslashreplace ->", data.decode("utf-8", errors="backslashreplace"))


if __name__ == "__main__":
    main()