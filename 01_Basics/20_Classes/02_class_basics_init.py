#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：class 与 __init__（实例、属性、方法）。
Author: Lambert

你会学到：
1) class 定义与实例化
2) __init__ 初始化实例属性
3) 实例方法与 self 的含义

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/02_class_basics_init.py
"""

from __future__ import annotations


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def birthday(self) -> None:
        self.age += 1

    def profile(self) -> str:
        return f"{self.name}({self.age})"


def main() -> None:
    alice = User("Alice", 20)
    bob = User("Bob", 7)

    print("alice.name ->", alice.name)
    print("bob.profile() ->", bob.profile())

    alice.birthday()
    print("alice after birthday ->", alice.profile())

    print("User.profile(alice) ->", User.profile(alice))


if __name__ == "__main__":
    main()