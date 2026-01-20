#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：数字类型（int / float / complex）以及常见精度问题。

你会学到：
1) int：任意精度整数（不会溢出，只会更大）
2) float：双精度浮点，存在“二进制表示误差”
3) complex：复数（a + bj），常用于科学计算
4) 精度方案：math.isclose / Decimal / Fraction

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/04_numbers_int_float_complex.py
"""

from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
import math


def main() -> None:
    print("1) int：任意精度")
    big = 2**100
    print("2**100 =", big)
    print("len(str(2**100)) =", len(str(big)))

    print("\n2) 常见运算符：")
    a, b = 7, 3
    print("a+b =", a + b)
    print("a-b =", a - b)
    print("a*b =", a * b)
    print("a/b  =", a / b)
    print("a//b =", a // b, "(floor division)")
    print("a%b  =", a % b)
    print("divmod(a,b) =", divmod(a, b))
    print("a**b =", a**b)

    print("\n3) float 精度问题：")
    x = 0.1 + 0.2
    print("0.1 + 0.2 =", x)
    print("x == 0.3 ->", x == 0.3)
    print("math.isclose(x, 0.3) ->", math.isclose(x, 0.3))

    print("\n4) Decimal：十进制精确表示（常用于金额）")
    d = Decimal("0.1") + Decimal("0.2")
    print("Decimal('0.1') + Decimal('0.2') =", d)
    print("d == Decimal('0.3') ->", d == Decimal("0.3"))

    print("\n5) Fraction：有理数精确表示（分数）")
    f = Fraction(1, 10) + Fraction(1, 5)
    print("1/10 + 1/5 =", f, "as float =", float(f))

    print("\n6) complex：复数")
    z = 3 + 4j
    print("z =", z)
    print("z.real =", z.real)
    print("z.imag =", z.imag)
    print("|z| =", abs(z))
    print("z.conjugate() =", z.conjugate())


if __name__ == "__main__":
    main()

