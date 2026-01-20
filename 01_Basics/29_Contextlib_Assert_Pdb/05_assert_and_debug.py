#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: assert and __debug__.

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/05_assert_and_debug.py
"""


def check_positive(x: int) -> None:
    assert x > 0, "x must be positive"


def main() -> None:
    print("__debug__ ->", __debug__)

    try:
        check_positive(-1)
    except AssertionError as exc:
        print("assert failed ->", exc)


if __name__ == "__main__":
    main()
