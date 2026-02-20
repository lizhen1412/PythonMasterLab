#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：赋值运算符（Assignment Operators）
Author: Lambert

你会学到：
1) `=`：名字绑定对象；支持多重赋值与解包
2) 交换变量：`a, b = b, a`
3) 增强赋值：`+= -= *= /= //= %= **= &= |= ^= <<= >>= @=` 等
   - 对可变对象（如 list）可能是“原地修改”，会影响别名
4) 赋值表达式 `:=`（海象运算符）：在表达式内部绑定名字

运行（在仓库根目录执行）：
    python3 01_Basics/09_Operators/03_assignment_operators.py
"""

from __future__ import annotations

from collections.abc import Iterable


def sum_numbers_until_blank(lines: Iterable[str]) -> int:
    total = 0
    for raw in lines:
        if not (s := raw.strip()):
            break
        total += int(s)
    return total


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
    show("1) = 与解包")
    x = 10
    y = x
    print("x =", x, "y =", y, "x is y ->", x is y)

    a, b = 1, 2
    print("a, b =", a, b)
    a, b = b, a
    print("swap -> a, b =", a, b)

    first, *middle, last = [10, 20, 30, 40]
    print("unpack ->", first, middle, last)

    show("2) 增强赋值（+=）与别名")
    items = [1, 2]
    alias = items
    items += [3]
    print("items += [3] -> items =", items, "alias =", alias, "items is alias ->", items is alias)

    items2 = [1, 2]
    alias2 = items2
    items2 = items2 + [3]
    print("items = items + [3] -> items2 =", items2, "alias2 =", alias2, "items2 is alias2 ->", items2 is alias2)

    show("2.1) @=（矩阵乘法的增强赋值）")
    m1 = Matrix2x2(1, 0, 0, 1)
    m2 = Matrix2x2(2, 3, 4, 5)
    print("m1 ->", m1)
    m1 @= m2
    print("m1 @= m2 ->", m1)

    show("3) :=（海象运算符）")
    total = sum_numbers_until_blank(["10\n", "20\n", "  \n", "999\n"])
    print("sum_numbers_until_blank ->", total)


if __name__ == "__main__":
    main()