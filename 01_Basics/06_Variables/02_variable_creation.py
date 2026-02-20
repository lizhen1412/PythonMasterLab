#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：变量创建（assignment / unpacking / annotations）。
Author: Lambert

核心认知：
- 在 Python 里，“变量”更准确的说法是 **名字（name）绑定对象（object）**。
- “创建变量”通常就是：第一次给名字赋值（绑定到某个对象）。

你会学到：
1) 基本赋值：`x = 1`
2) 多重赋值/交换：`a, b = 1, 2` / `a, b = b, a`
3) 解包：`first, *middle, last = ...`
4) 注解（annotations）：`count: int = 0`（主要给 IDE/类型检查器用）
5) `id()`/`type()`：帮助理解“名字与对象”

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/02_variable_creation.py
"""

from __future__ import annotations


def describe(label: str, value: object) -> None:
    print(f"{label:<18} value={value!r:<20} type={type(value).__name__:<10} id=0x{id(value):x}")


def main() -> None:
    print("1) 基本赋值：第一次绑定名字")
    x = 1
    describe("x", x)

    print("\n2) 同一个名字可以重新绑定到不同对象（动态类型）")
    x = "now a str"
    describe("x", x)
    x = {"k": "v"}
    describe("x", x)

    print("\n3) 多重赋值 / 交换变量")
    a, b = 10, 20
    describe("a", a)
    describe("b", b)
    a, b = b, a
    print("swap 后：")
    describe("a", a)
    describe("b", b)

    print("\n4) 解包（unpacking）")
    first, second = [1, 2]
    describe("first", first)
    describe("second", second)

    first, *middle, last = [1, 2, 3, 4, 5]
    describe("first", first)
    describe("middle", middle)
    describe("last", last)

    print("\n5) 注解（annotations）：不改变运行时行为")
    count: int = 0
    name: str
    name = "Alice"
    describe("count", count)
    describe("name", name)
    print("__annotations__ =", __annotations__)

    print("\n6) 赋值是“名字 -> 对象”的绑定，不是把值塞进盒子")
    m = [1, 2, 3]
    n = m
    describe("m", m)
    describe("n", n)
    print("m is n ->", m is n)


if __name__ == "__main__":
    main()
