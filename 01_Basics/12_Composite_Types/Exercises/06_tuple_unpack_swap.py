#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：tuple 解包与交换变量（swap）
Author: Lambert

题目：
1) 实现函数 `swap(a, b)`：用“多重赋值/元组打包解包”的方式交换并返回 (b, a)
2) 在 main() 里演示一次“解包”：x, y = (3, 4)

提示：
- Python 里最常见的交换写法：a, b = b, a

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/06_tuple_unpack_swap.py
"""

from __future__ import annotations

from typing import TypeVar

A = TypeVar("A")
B = TypeVar("B")


def swap(a: A, b: B) -> tuple[B, A]:
    a, b = b, a
    return a, b


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("swap(1,2)", swap(1, 2), (2, 1))
    check("swap(1,'x')", swap(1, "x"), ("x", 1))

    x, y = (3, 4)
    check("unpack (3,4)", (x, y), (3, 4))


if __name__ == "__main__":
    main()
