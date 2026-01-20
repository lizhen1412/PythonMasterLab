#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: Protocol and structural typing.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/04_typing_protocols_structural.py
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsLen(Protocol):
    def __len__(self) -> int: ...


def describe_size(obj: SupportsLen) -> str:
    return f"len={len(obj)}"


def main() -> None:
    print(describe_size([1, 2, 3]))
    print(describe_size("hello"))

    print("isinstance(list, SupportsLen) ->", isinstance([], SupportsLen))
    print("isinstance(3, SupportsLen) ->", isinstance(3, SupportsLen))


if __name__ == "__main__":
    main()
