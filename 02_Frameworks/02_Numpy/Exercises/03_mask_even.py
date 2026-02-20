#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：布尔过滤（偶数）。
Author: Lambert

题目：
给定数组，返回其中的偶数元素。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/03_mask_even.py
"""

from __future__ import annotations

import numpy as np


def filter_even(arr: np.ndarray) -> np.ndarray:
    return arr[arr % 2 == 0]


def check(label: str, got: np.ndarray, expected: np.ndarray) -> None:
    ok = np.array_equal(got, expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->", got)
        print("expected ->", expected)


def main() -> None:
    arr = np.array([1, 2, 3, 4, 5, 6])
    result = filter_even(arr)
    expected = np.array([2, 4, 6])
    check("filter_even", result, expected)


if __name__ == "__main__":
    main()