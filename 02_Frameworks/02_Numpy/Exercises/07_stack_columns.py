#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：列拼接。

题目：
给定两个一维数组，将它们拼成二维列向量。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/07_stack_columns.py
"""

from __future__ import annotations

import numpy as np


def stack_columns(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.column_stack((a, b))


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
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])
    result = stack_columns(a, b)
    expected = np.array([[1, 10], [2, 20], [3, 30]])
    check("stack_columns", result, expected)


if __name__ == "__main__":
    main()
