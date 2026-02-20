#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: Suppress specific error.
Author: Lambert

Task:
Implement safe_pop(d, key) -> tuple[bool, object].
Return (True, value) if key exists, otherwise (False, None).

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/Exercises/03_suppress_error.py
"""

from contextlib import suppress


def safe_pop(d: dict, key: object) -> tuple[bool, object | None]:
    with suppress(KeyError):
        return True, d.pop(key)
    return False, None


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    d = {"a": 1}
    check("exists", safe_pop(d, "a"), (True, 1))
    check("missing", safe_pop(d, "b"), (False, None))


if __name__ == "__main__":
    main()