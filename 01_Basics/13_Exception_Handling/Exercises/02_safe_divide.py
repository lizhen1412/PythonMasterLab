#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：安全除法（safe divide）
Author: Lambert

题目：
实现函数 `safe_divide(a, b, default=None)`：
- 当 a/b 成功时返回结果
- 当发生 ZeroDivisionError 或 TypeError 时，返回 default

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/02_safe_divide.py
"""

from __future__ import annotations


def safe_divide(a: float, b: float, default: float | None = None) -> float | None:
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return default


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("safe_divide(10, 2)", safe_divide(10, 2), 5.0)
    check("safe_divide(10, 0)", safe_divide(10, 0), None)
    check("safe_divide(10, 0, -1)", safe_divide(10, 0, -1), -1)
    check("safe_divide('x', 2)", safe_divide("x", 2, 0), 0)  # type: ignore[arg-type]


if __name__ == "__main__":
    main()
