#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 07: TypeGuard and Self.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/07_typing_typeguard_self.py
"""

from __future__ import annotations

from typing import Self, TypeGuard


def is_str_list(items: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(item, str) for item in items)


class Builder:
    def __init__(self) -> None:
        self.name = ""
        self.tags: list[str] = []

    def set_name(self, name: str) -> Self:
        self.name = name
        return self

    def add_tag(self, tag: str) -> Self:
        self.tags.append(tag)
        return self


def main() -> None:
    items: list[object] = ["a", "b", "c"]
    if is_str_list(items):
        print("all strings ->", ",".join(items))

    b = Builder().set_name("demo").add_tag("x").add_tag("y")
    print("builder ->", b.name, b.tags)


if __name__ == "__main__":
    main()
