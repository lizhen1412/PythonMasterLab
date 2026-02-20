#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: TypeVar and generics.
Author: Lambert

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/03_typing_typevar_generics.py
"""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    if not items:
        raise ValueError("items must not be empty")
    return items[0]


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value


def main() -> None:
    print("first([10, 20]) ->", first([10, 20]))
    print("first(['a', 'b']) ->", first(["a", "b"]))

    int_box = Box(123)
    str_box = Box("hello")
    print("Box[int] ->", int_box.get())
    print("Box[str] ->", str_box.get())


if __name__ == "__main__":
    main()