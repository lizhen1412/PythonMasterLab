#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11：使用 ufunc.outer 计算外积。
Author: Lambert

题目：
使用 np.multiply.outer 计算两个向量的外积。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/11_outer_product.py
"""

from __future__ import annotations

import numpy as np


def outer_product(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """使用 multiply.outer 计算外积"""
    return np.multiply.outer(v1, v2)


def check(label: str, got: np.ndarray, expected: np.ndarray) -> None:
    ok = np.array_equal(got, expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->")
        print(got)
        print("expected ->")
        print(expected)


def main() -> None:
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    result = outer_product(v1, v2)
    expected = np.array([
        [4, 5, 6],
        [8, 10, 12],
        [12, 15, 18]
    ])

    check("outer_product", result, expected)


if __name__ == "__main__":
    main()