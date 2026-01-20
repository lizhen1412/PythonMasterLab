#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: TypeVar-based generic helper.

Task:
Implement first_or(items, default) -> T.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/Exercises/03_generic_first_or.py
"""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def first_or(items: list[T], default: T) -> T:
    return items[0] if items else default


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("ints", first_or([1, 2], 0), 1)
    check("empty", first_or([], 9), 9)
    check("strings", first_or(["a"], "x"), "a")


if __name__ == "__main__":
    main()
