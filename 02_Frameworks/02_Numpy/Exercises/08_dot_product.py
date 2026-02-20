#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：向量点积。
Author: Lambert

题目：
给定两个向量，计算点积。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/08_dot_product.py
"""

from __future__ import annotations

import numpy as np


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b))


def check(label: str, got: float, expected: float) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = dot_product(a, b)
    check("dot_product", result, 32.0)


if __name__ == "__main__":
    main()