#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 07: collections.abc basics.

Run:
    python3 01_Basics/26_Collections_Algorithms/07_collections_abc_basics.py
"""

from collections.abc import Iterable, Mapping, Sequence


def show(obj: object, label: str) -> None:
    print(
        f"{label:<10} Iterable={isinstance(obj, Iterable)} "
        f"Sequence={isinstance(obj, Sequence)} Mapping={isinstance(obj, Mapping)}"
    )


def main() -> None:
    show([1, 2, 3], "list")
    show("abc", "str")
    show({"a": 1}, "dict")
    show((x for x in range(2)), "gen")


if __name__ == "__main__":
    main()
