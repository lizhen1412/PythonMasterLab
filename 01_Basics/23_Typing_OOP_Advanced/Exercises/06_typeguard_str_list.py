#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 06: TypeGuard for list[str].

Task:
Implement is_str_list(items) -> TypeGuard[list[str]].

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/Exercises/06_typeguard_str_list.py
"""

from __future__ import annotations

from typing import TypeGuard


def is_str_list(items: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(item, str) for item in items)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("all str", is_str_list(["a", "b"]), True)
    check("mixed", is_str_list(["a", 1]), False)
    check("empty", is_str_list([]), True)


if __name__ == "__main__":
    main()
