#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：属性访问与 __slots__。
Author: Lambert

你会学到：
1) __getattr__：找不到属性时的兜底逻辑
2) __setattr__：写入属性时做校验
3) __delattr__：拦截删除属性
4) __slots__：限制可创建的属性

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/09_magic_methods_attribute_and_slots.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class User:
    __slots__ = ("first", "last")

    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    def __setattr__(self, name: str, value: object) -> None:
        if name in {"first", "last"}:
            if not isinstance(value, str) or not value.strip():
                raise ValueError("first/last must be non-empty str")
        super().__setattr__(name, value)

    def __getattr__(self, name: str) -> str:
        if name == "full_name":
            return f"{self.first} {self.last}"
        raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")

    def __delattr__(self, name: str) -> None:
        raise AttributeError("deleting attributes is not allowed")


def main() -> None:
    show("1) __getattr__ 计算属性")
    u = User("Alice", "Zhao")
    print("full_name ->", u.full_name)
    print("has __dict__ ->", hasattr(u, "__dict__"))

    show("2) __setattr__ 校验写入")
    try:
        u.first = ""
    except ValueError as exc:
        print("ValueError:", exc)

    show("3) __slots__ 限制新属性")
    try:
        u.nickname = "Al"
    except AttributeError as exc:
        print("AttributeError:", exc)

    show("4) __delattr__ 阻止删除")
    try:
        del u.first
    except AttributeError as exc:
        print("AttributeError:", exc)


if __name__ == "__main__":
    main()