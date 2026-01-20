#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：按列均值（axis=0）。

题目：
给定二维数组，计算每一列的均值。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/05_mean_axis0.py
"""

from __future__ import annotations

import numpy as np


def mean_axis0(mat: np.ndarray) -> np.ndarray:
    return mat.mean(axis=0)


def check(label: str, got: np.ndarray, expected: np.ndarray) -> None:
    ok = np.allclose(got, expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->", got)
        print("expected ->", expected)


def main() -> None:
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    result = mean_axis0(mat)
    expected = np.array([2.5, 3.5, 4.5])
    check("mean_axis0", result, expected)


if __name__ == "__main__":
    main()
