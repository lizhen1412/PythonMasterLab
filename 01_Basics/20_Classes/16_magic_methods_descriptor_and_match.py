#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：描述符协议与模式匹配（__get__/__set__/__delete__/__match_args__）。

你会学到：
1) 描述符：把校验逻辑封装在字段上
2) __match_args__ 影响类模式的“位置参数匹配”

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/16_magic_methods_descriptor_and_match.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Positive:
    def __set_name__(self, owner, name: str) -> None:
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value: int) -> None:
        if value <= 0:
            raise ValueError("value must be positive")
        setattr(instance, self.private_name, value)

    def __delete__(self, instance) -> None:
        raise AttributeError("cannot delete managed attribute")


class Account:
    balance = Positive()

    def __init__(self, balance: int) -> None:
        self.balance = balance


class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def main() -> None:
    show("1) 描述符 __get__/__set__/__delete__")
    acc = Account(100)
    print("acc.balance ->", acc.balance)
    try:
        acc.balance = -1
    except ValueError as exc:
        print("ValueError:", exc)
    try:
        del acc.balance
    except AttributeError as exc:
        print("AttributeError:", exc)

    show("2) __match_args__ 的影响")
    p = Point(3, 4)
    match p:
        case Point(0, y):
            print("x=0, y =", y)
        case Point(x, y):
            print("matched by position ->", x, y)

    match p:
        case Point(x=3, y=4):
            print("matched by keyword -> 3,4")
        case _:
            print("no match")


if __name__ == "__main__":
    main()
