#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：阶乘递归 vs 迭代。
Author: Lambert

要求：
- 写两个实现：递归与迭代
- 讨论递归深度限制：尝试一个较大的 n，捕获 RecursionError
"""

from __future__ import annotations


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main() -> None:
    print("递归 factorial(6) ->", factorial_recursive(6))
    print("迭代 factorial(6) ->", factorial_iterative(6))

    try:
        # 故意用较大值，展示递归的深度限制（根据环境可能抛出 RecursionError）
        factorial_recursive(2000)
    except RecursionError as exc:
        print("RecursionError 捕获 ->", exc)


if __name__ == "__main__":
    main()