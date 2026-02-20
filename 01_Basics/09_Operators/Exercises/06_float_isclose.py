#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：用 math.isclose 做浮点相等判断
Author: Lambert

题目：
实现 `float_equal(a, b, rel_tol=..., abs_tol=...)`，内部用 `math.isclose`。

提示：
- 浮点数往往无法精确表示十进制小数：0.1 + 0.2 != 0.3

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/09_Operators/Exercises/06_float_isclose.py
"""

from __future__ import annotations

import math


def float_equal(a: float, b: float, *, rel_tol: float = 1e-09, abs_tol: float = 0.0) -> bool:
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    v = 0.1 + 0.2
    check("raw_eq", v == 0.3, False)
    check("isclose", float_equal(v, 0.3), True)
    check("far", float_equal(1.0, 1.1), False)


if __name__ == "__main__":
    main()
