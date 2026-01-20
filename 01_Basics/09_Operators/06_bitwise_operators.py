#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：位运算符（Bitwise Operators）

你会学到：
1) `& | ^ ~ << >>` 的基本含义
2) 用二进制格式化观察结果：`format(n, '#010b')`
3) 位运算真值表（0/1）与布尔按位运算
4) 负数右移是“算术右移”（保留符号）
5) 位标志（flags）常见写法：`READ = 1 << 0`，用 `|` 组合、用 `&` 检查

运行（在仓库根目录执行）：
    python3 01_Basics/09_Operators/06_bitwise_operators.py
"""

from __future__ import annotations


def b(n: int, width: int = 10) -> str:
    return format(n, f"#0{width}b")


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 基本位运算：& | ^ ~")
    x = 0b1100
    y = 0b1010
    print("x =", b(x), "y =", b(y))
    print("x & y =", b(x & y))
    print("x | y =", b(x | y))
    print("x ^ y =", b(x ^ y))
    print("~x    =", b(~x), "（Python int 无固定宽度，~ 会得到负数）")

    show("2) 位移：<< >>")
    n = 0b0011
    print("n =", b(n))
    print("n << 2 =", b(n << 2))
    print("n >> 1 =", b(n >> 1))

    show("2.1) 位运算真值表（0/1）")
    pairs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for a, b_ in pairs:
        print(f"{a} & {b_} -> {a & b_} | {a} | {b_} -> {a | b_} | {a} ^ {b_} -> {a ^ b_}")

    show("2.2) 负数右移（算术右移）")
    neg = -5
    print("neg =", neg, "bin=", format(neg, "b"))
    print("neg >> 1 =", neg >> 1, "bin=", format(neg >> 1, "b"))

    show("3) flags：用位表示权限/特性")
    READ = 1 << 0
    WRITE = 1 << 1
    EXEC = 1 << 2
    perms = READ | EXEC
    print("READ =", b(READ), "WRITE =", b(WRITE), "EXEC =", b(EXEC))
    print("perms = READ | EXEC ->", b(perms))
    print("has READ ->", bool(perms & READ))
    print("has WRITE ->", bool(perms & WRITE))
    print("has EXEC ->", bool(perms & EXEC))


if __name__ == "__main__":
    main()
