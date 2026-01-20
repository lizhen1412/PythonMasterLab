#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：变量类型（运行时 type/isinstance + 动态类型）。

你会学到：
1) `type(obj)`：对象的“实际类型”
2) `isinstance(obj, T)`：推荐的类型判断方式（支持继承/抽象基类）
3) 动态类型：同一个名字可以绑定不同类型对象
4) 一个常见细节：bool 是 int 的子类（`isinstance(True, int)` 为 True）

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/05_variable_types_runtime.py
"""

from __future__ import annotations


class User:
    def __init__(self, name: str) -> None:
        self.name = name


def describe(value: object) -> None:
    print(f"value={value!r:<22} type={type(value).__name__:<10}")


def main() -> None:
    print("1) type()：")
    for v in [1, 3.14, True, "hi", None, [1], {"k": "v"}, (1, 2)]:
        describe(v)

    print("\n2) isinstance()：")
    x: object = 123
    print("x =", x)
    print("isinstance(x, int) ->", isinstance(x, int))
    print("isinstance(x, (int, str)) ->", isinstance(x, (int, str)))

    print("\n3) 动态类型（同一个名字绑定不同对象）：")
    x = "now a str"
    print("x =", x, "type =", type(x).__name__)
    x = User("Alice")
    print("x =", x, "type =", type(x).__name__)
    print("isinstance(x, User) ->", isinstance(x, User))

    print("\n4) bool 是 int 的子类（重要细节）：")
    print("isinstance(True, bool) ->", isinstance(True, bool))
    print("isinstance(True, int)  ->", isinstance(True, int))
    print("True + 1 ->", True + 1)


if __name__ == "__main__":
    main()

