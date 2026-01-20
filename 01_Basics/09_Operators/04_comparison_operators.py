#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：比较运算符（Comparison Operators）

你会学到：
1) `== != < <= > >=` 的基本用法
2) 链式比较：`0 < x < 10` 等价于 `0 < x and x < 10`
3) 浮点比较：不要直接 `==`，优先 `math.isclose`
4) 不同类型的“大小比较”在 Python 3 中通常是 TypeError（例如 1 < "2"）

运行（在仓库根目录执行）：
    python3 01_Basics/09_Operators/04_comparison_operators.py
"""

from __future__ import annotations

import math


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 基本比较：== != < <= > >=")
    print("3 == 3 ->", 3 == 3)
    print("3 != 4 ->", 3 != 4)
    print("3 < 4  ->", 3 < 4)
    print("3 <= 3 ->", 3 <= 3)
    print("'a' < 'b' ->", "a" < "b", "（字符串按字典序比较）")

    show("2) 链式比较")
    x = 5
    print("0 < x < 10 ->", 0 < x < 10)
    print("0 < x and x < 10 ->", 0 < x and x < 10)

    show("3) 浮点比较：isclose")
    v = 0.1 + 0.2
    print("0.1 + 0.2 =", v)
    print("v == 0.3 ->", v == 0.3)
    print("math.isclose(v, 0.3) ->", math.isclose(v, 0.3))

    show("4) 不同类型的大小比较通常是 TypeError")
    try:
        _ = 1 < "2"
    except TypeError as exc:
        print("1 < '2' -> TypeError:", exc)


if __name__ == "__main__":
    main()

