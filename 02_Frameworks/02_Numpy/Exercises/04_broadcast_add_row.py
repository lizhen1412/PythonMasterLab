#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：广播相加。

题目：
给定 2D 数组和 1D 行向量，返回相加结果。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/04_broadcast_add_row.py
"""

from __future__ import annotations

import numpy as np


def add_row(mat: np.ndarray, row: np.ndarray) -> np.ndarray:
    return mat + row


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
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    row = np.array([10, 20, 30])
    result = add_row(mat, row)
    expected = np.array([[11, 22, 33], [14, 25, 36]])
    check("broadcast_add", result, expected)


if __name__ == "__main__":
    main()
