#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: Protocol with __len__.
Author: Lambert

Task:
Implement total_size(items) -> int for a list of sized objects.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/Exercises/04_protocol_total_size.py
"""

from __future__ import annotations

from typing import Protocol


class Sized(Protocol):
    def __len__(self) -> int: ...


def total_size(items: list[Sized]) -> int:
    return sum(len(item) for item in items)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    data = ["ab", [1, 2, 3], {"x": 1, "y": 2}]
    check("total_size", total_size(data), 2 + 3 + 2)
    check("empty", total_size([]), 0)


if __name__ == "__main__":
    main()