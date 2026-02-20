#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 14：使用 ufunc.accumulate。
Author: Lambert

题目：
使用 np.add.accumulate 和 np.multiply.accumulate
计算数组的累加和累乘。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/14_accumulate.py
"""

from __future__ import annotations

import numpy as np


def cumulative_sum_product(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """返回累加和和累乘"""
    cumsum = np.add.accumulate(arr)
    cumprod = np.multiply.accumulate(arr)
    return cumsum, cumprod


def check(label: str, got: np.ndarray, expected: np.ndarray) -> None:
    ok = np.array_equal(got, expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got}")


def main() -> None:
    arr = np.array([1, 2, 3, 4, 5])
    cumsum, cumprod = cumulative_sum_product(arr)

    check("cumsum", cumsum, np.array([1, 3, 6, 10, 15]))
    check("cumprod", cumprod, np.array([1, 2, 6, 24, 120]))


if __name__ == "__main__":
    main()