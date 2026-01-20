#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: Build Request objects without sending.

Run:
    python3 01_Basics/31_Network_Security/03_urllib_request_build.py
"""

from urllib.parse import urlencode
from urllib.request import Request


def main() -> None:
    data = urlencode({"name": "alice", "age": 20}).encode("utf-8")
    req = Request(
        "https://example.com/api",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )

    print("method ->", req.method)
    print("url ->", req.full_url)
    print("headers ->", dict(req.header_items()))
    print("data ->", req.data)


if __name__ == "__main__":
    main()
