#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：range（步长与反向遍历）
Author: Lambert

题目：
实现两个函数：
1) `countdown(start)`：返回从 start 到 0 的倒计时列表（包含 0）
2) `even_upto(n)`：返回 [0, 2, 4, ..., <= n] 的偶数列表

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/11_Loops/Exercises/07_range_step_reverse.py
"""

from __future__ import annotations


def countdown(start: int) -> list[int]:
    if start < 0:
        raise ValueError("start must be >= 0")
    return list(range(start, -1, -1))


def even_upto(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n must be >= 0")
    return list(range(0, n + 1, 2))


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("countdown", countdown(5), [5, 4, 3, 2, 1, 0])
    check("even_upto_0", even_upto(0), [0])
    check("even_upto_7", even_upto(7), [0, 2, 4, 6])


if __name__ == "__main__":
    main()
