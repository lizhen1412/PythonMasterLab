#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 07: Sequence check.
Author: Lambert

Task:
Implement is_sequence(obj) -> bool.
Return True for Sequence but exclude str/bytes.

Run:
    python3 01_Basics/26_Collections_Algorithms/Exercises/07_collections_abc_is_sequence.py
"""

from collections.abc import Sequence


def is_sequence(obj: object) -> bool:
    if isinstance(obj, (str, bytes, bytearray)):
        return False
    return isinstance(obj, Sequence)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("list", is_sequence([1, 2]), True)
    check("tuple", is_sequence((1, 2)), True)
    check("str", is_sequence("ab"), False)
    check("dict", is_sequence({"a": 1}), False)


if __name__ == "__main__":
    main()