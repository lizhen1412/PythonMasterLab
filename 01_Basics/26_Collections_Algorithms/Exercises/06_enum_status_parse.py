#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 06: Parse enum status.
Author: Lambert

Task:
Implement parse_status(text) -> Status.

Run:
    python3 01_Basics/26_Collections_Algorithms/Exercises/06_enum_status_parse.py
"""

from enum import Enum


class Status(Enum):
    OK = "ok"
    FAIL = "fail"
    UNKNOWN = "unknown"


def parse_status(text: str) -> Status:
    for item in Status:
        if item.value == text:
            return item
    return Status.UNKNOWN


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("ok", parse_status("ok"), Status.OK)
    check("bad", parse_status("bad"), Status.UNKNOWN)


if __name__ == "__main__":
    main()