#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：1..n 求和（for / while）
Author: Lambert

题目：
实现两个函数：
1) `sum_for(n)`：用 for 循环计算 1 + 2 + ... + n
2) `sum_while(n)`：用 while 循环计算 1 + 2 + ... + n

约定：
- n < 0 视为非法：抛 ValueError
- n == 0 返回 0

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/11_Loops/Exercises/02_sum_1_to_n.py
"""

from __future__ import annotations


def sum_for(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    total = 0
    for x in range(1, n + 1):
        total += x
    return total


def sum_while(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    for n, expected in [(0, 0), (1, 1), (10, 55), (100, 5050)]:
        check(f"sum_for({n})", sum_for(n), expected)
        check(f"sum_while({n})", sum_while(n), expected)


if __name__ == "__main__":
    main()
