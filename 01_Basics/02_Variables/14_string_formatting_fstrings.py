#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：格式化输出（更专业地打印变量）。

你会学到：
1) `str(x)` vs `repr(x)`：面向用户 vs 面向开发者
2) f-string：`f\"{name}\"`、调试用 `f\"{var=}\"`
3) `!r`：强制用 repr；`!s`：强制用 str
4) 常见格式化规格：小数位、千分位、百分比、对齐

运行：
    python3 01_Basics/02_Variables/14_string_formatting_fstrings.py
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    score: int


def main() -> None:
    u = User(name="Alice", score=98)
    pi = 3.1415926
    n = 1234567
    ratio = 0.375

    print("1) str vs repr：")
    print("str(u) =", str(u))
    print("repr(u)=", repr(u))

    print("\n2) f-string 基础：")
    print(f"Hello, {u.name}!")
    print(f"{u=}")  # 调试友好：打印变量名和值

    print("\n3) !r / !s：")
    text = "hi\n"
    print(f"text as repr -> {text!r}")
    print(f"text as str  -> {text!s}")

    print("\n4) 数值格式化：")
    print(f"pi rounded   = {pi:.2f}")
    print(f"n with comma = {n:,}")
    print(f"ratio        = {ratio:.1%}")

    print("\n5) 对齐：")
    rows = [
        ("Alice", 98),
        ("Bob", 7),
        ("Charlie", 100),
    ]
    for name, score in rows:
        print(f"{name:<10} | {score:>3}")


if __name__ == "__main__":
    main()

