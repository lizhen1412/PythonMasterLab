#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: Parse query params.

Task:
Implement parse_query(query) -> dict[str, list[str]].

Run:
    python3 01_Basics/31_Network_Security/Exercises/02_parse_query_params.py
"""

from urllib.parse import parse_qs


def parse_query(query: str) -> dict[str, list[str]]:
    return parse_qs(query, keep_blank_values=True)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    query = "a=1&b=2&b=3"
    expected = {"a": ["1"], "b": ["2", "3"]}
    check("parse", parse_query(query), expected)


if __name__ == "__main__":
    main()
