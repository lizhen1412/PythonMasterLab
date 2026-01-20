#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: Parse TOML string.

Task:
Implement get_title(text) -> str using tomllib.loads.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/Exercises/05_tomllib_parse.py
"""

import tomllib


def get_title(text: str) -> str:
    data = tomllib.loads(text)
    return data["title"]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    text = "title = \"Demo\""
    check("title", get_title(text), "Demo")


if __name__ == "__main__":
    main()
