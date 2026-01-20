#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: Assert positive input.

Task:
Implement assert_positive(x) -> None.

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/Exercises/05_assert_positive.py
"""


def assert_positive(x: int) -> None:
    assert x > 0, "x must be positive"


def check_raises() -> bool:
    try:
        assert_positive(-1)
    except AssertionError:
        return True
    return False


def main() -> None:
    print("raises ->", check_raises())


if __name__ == "__main__":
    main()
