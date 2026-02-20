#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：算术运算符（Arithmetic Operators）
Author: Lambert

你会学到：
1) `+ - * / // % **` 的基本行为（含一元 + / -）
2) `/` 永远返回 float；`//` 是“向下取整”（floor）
3) `%` 与 `//` 的恒等式：a == (a // b) * b + (a % b)
4) `divmod(a, b)` 等价于 `(a // b, a % b)`
5) `@`：矩阵乘法（需要对象实现 __matmul__）
6) 序列的 `+` 与 `*`：字符串/列表拼接与重复

运行（在仓库根目录执行）：
    python3 01_Basics/09_Operators/02_arithmetic_operators.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Matrix2x2:
    def __init__(self, a11: int, a12: int, a21: int, a22: int) -> None:
        self.rows = [[a11, a12], [a21, a22]]

    def __matmul__(self, other: object) -> "Matrix2x2":
        if not isinstance(other, Matrix2x2):
            return NotImplemented
        a = self.rows
        b = other.rows
        return Matrix2x2(
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        )

    def __imatmul__(self, other: object) -> "Matrix2x2":
        result = self @ other
        self.rows = result.rows
        return self

    def __repr__(self) -> str:
        return f"Matrix2x2({self.rows[0]}, {self.rows[1]})"


def main() -> None:
    show("1) 基本算术：+ - * /")
    a, b = 7, 3
    print("a, b =", a, b)
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b, "(type:", type(a / b).__name__, ")")

    show("1.1) 一元 + 与 -")
    n = 3
    print("+n =", +n)
    print("-n =", -n)

    show("2) // 与 %（注意负数）")
    x, y = -7, 3
    print("x, y =", x, y)
    print("x // y =", x // y)
    print("x % y  =", x % y)
    print("恒等式 x == (x//y)*y + (x%y) ->", x == (x // y) * y + (x % y))
    print("divmod(x, y) ->", divmod(x, y))

    show("3) 幂运算 **（右结合）")
    print("2 ** 3 =", 2**3)
    print("2 ** 3 ** 2 =", 2**3**2, "（等价于 2 ** (3 ** 2)）")

    show("4) 结合内置函数（常用搭配）")
    print("abs(-3) =", abs(-3))
    print("round(1.23456, 2) =", round(1.23456, 2))
    print("pow(2, 10) =", pow(2, 10))
    print("pow(2, 10, 1000) =", pow(2, 10, 1000), "（带模幂，常见于算法）")

    show("5) 矩阵乘法 @")
    m1 = Matrix2x2(1, 2, 3, 4)
    m2 = Matrix2x2(5, 6, 7, 8)
    print("m1 @ m2 ->", m1 @ m2)
    m1 @= m2
    print("m1 @= m2 ->", m1)

    show("6) 序列的 + 与 *（不是数值运算，但很常用）")
    print("'ab' + 'cd' =", "ab" + "cd")
    print("'ha' * 3 =", "ha" * 3)
    print("[1, 2] + [3] =", [1, 2] + [3])
    print("[0] * 3 =", [0] * 3)


if __name__ == "__main__":
    main()