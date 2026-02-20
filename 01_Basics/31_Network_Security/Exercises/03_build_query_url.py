#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: Build URL with query.
Author: Lambert

Task:
Implement build_url(base, params) -> str.

Run:
    python3 01_Basics/31_Network_Security/Exercises/03_build_query_url.py
"""

from urllib.parse import urlencode


def build_url(base: str, params: dict[str, str]) -> str:
    query = urlencode(params)
    return f"{base}?{query}" if query else base


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    url = build_url("https://example.com", {"q": "py", "p": "1"})
    check("url", url, "https://example.com?q=py&p=1")


if __name__ == "__main__":
    main()