#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 13：datetime64 运算。
Author: Lambert

题目：
给定两个 datetime64 日期数组，计算它们之间的天数差。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/13_datetime_diff.py
"""

from __future__ import annotations

import numpy as np


def days_between(dates1: np.ndarray, dates2: np.ndarray) -> np.ndarray:
    """计算两个日期数组之间的天数差"""
    return (dates2 - dates1).astype("timedelta64[D]").astype(int)


def check(label: str, got: np.ndarray, expected: np.ndarray) -> None:
    ok = np.array_equal(got, expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got}")


def main() -> None:
    dates1 = np.array(["2023-01-01", "2023-02-01", "2023-03-01"], dtype="datetime64[D]")
    dates2 = np.array(["2023-01-15", "2023-02-15", "2023-03-15"], dtype="datetime64[D]")

    result = days_between(dates1, dates2)
    expected = np.array([14, 14, 14])

    check("days_between", result, expected)


if __name__ == "__main__":
    main()