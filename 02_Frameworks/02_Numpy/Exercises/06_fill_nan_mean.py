#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：NaN 均值填充。

题目：
给定包含 NaN 的数组，用非 NaN 均值填充。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/06_fill_nan_mean.py
"""

from __future__ import annotations

import numpy as np


def fill_nan_with_mean(arr: np.ndarray) -> np.ndarray:
    mean_value = np.nanmean(arr)
    return np.where(np.isnan(arr), mean_value, arr)


def check(label: str, got: np.ndarray, expected: np.ndarray) -> None:
    ok = np.allclose(got, expected, equal_nan=True)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->", got)
        print("expected ->", expected)


def main() -> None:
    arr = np.array([1.0, np.nan, 3.0])
    result = fill_nan_with_mean(arr)
    expected = np.array([1.0, 2.0, 3.0])
    check("fill_nan_mean", result, expected)


if __name__ == "__main__":
    main()
