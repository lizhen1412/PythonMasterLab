#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: URL parsing and encoding.
Author: Lambert

Run:
    python3 01_Basics/31_Network_Security/02_urllib_parse_basics.py
"""

from urllib.parse import parse_qs, urlencode, urlparse


def main() -> None:
    url = "https://example.com/search?q=python&lang=en"
    parsed = urlparse(url)
    print("scheme ->", parsed.scheme)
    print("netloc ->", parsed.netloc)
    print("path ->", parsed.path)
    print("query ->", parsed.query)

    params = parse_qs(parsed.query)
    print("params ->", params)

    new_query = urlencode({"q": "py3", "page": 2})
    print("encoded ->", new_query)


if __name__ == "__main__":
    main()