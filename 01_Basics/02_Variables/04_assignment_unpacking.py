#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：赋值与解包（unpacking）。

你会看到：
1) 单个赋值：x = 1
2) 多重赋值：a, b = 1, 2
3) 交换变量：a, b = b, a
4) 解包：a, b, c = [1, 2, 3]
5) 星号解包：first, *middle, last = [1, 2, 3, 4]
6) 常见占位符：用 `_` 表示“我不关心这个值”

运行：
    python3 01_Basics/02_Variables/04_assignment_unpacking.py
"""


def main() -> None:
    x = 1
    print("x =", x)

    a, b = 1, 2
    print("a, b =", a, b)

    a, b = b, a
    print("swap -> a, b =", a, b)

    p = (10, 20, 30)
    i, j, k = p
    print("unpack tuple ->", i, j, k)

    first, *middle, last = [1, 2, 3, 4, 5]
    print("first =", first)
    print("middle=", middle)
    print("last  =", last)

    _, keep, _ = ["drop-left", "keep-me", "drop-right"]
    print("keep =", keep)

    print("\n错误示例（会抛 ValueError，我们捕获它）：")
    try:
        u, v = [1]
    except ValueError as exc:
        print("ValueError:", exc)


if __name__ == "__main__":
    main()

