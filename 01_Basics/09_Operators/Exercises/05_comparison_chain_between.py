#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：用链式比较实现 is_between
Author: Lambert

题目：
实现 `is_between(x, low, high, inclusive=True)`，要求：
- inclusive=True  时返回 `low <= x <= high`
- inclusive=False 时返回 `low < x < high`

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/09_Operators/Exercises/05_comparison_chain_between.py
"""

from __future__ import annotations


def is_between(x: int, low: int, high: int, *, inclusive: bool = True) -> bool:
    if inclusive:
        return low <= x <= high
    return low < x < high


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("inclusive_mid", is_between(5, 0, 10), True)
    check("inclusive_edge", is_between(0, 0, 10), True)
    check("exclusive_edge", is_between(0, 0, 10, inclusive=False), False)
    check("exclusive_mid", is_between(5, 0, 10, inclusive=False), True)
    check("out", is_between(11, 0, 10), False)


if __name__ == "__main__":
    main()
