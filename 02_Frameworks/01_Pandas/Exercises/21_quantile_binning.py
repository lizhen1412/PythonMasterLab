#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 21：使用 quantile 进行分箱。
Author: Lambert

题目：
给定一个数值 Series，使用 qcut 按四分位数分箱，并返回每个值所在的分位数区间标签。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/21_quantile_binning.py
"""

from __future__ import annotations

import pandas as pd


def quartile_bins(s: pd.Series) -> pd.Series:
    """按四分位数分箱，返回标签 Q1-Q4"""
    return pd.qcut(s, q=4, labels=["Q1", "Q2", "Q3", "Q4"])


def check(label: str, got: object, expected: object) -> None:
    ok = got.equals(expected) if hasattr(got, "equals") else got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print(f"  got: {got.tolist()}")
        print(f"  expected: {expected.tolist()}")


def main() -> None:
    s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
    result = quartile_bins(s)
    # 1-2: Q1, 3-4: Q2, 5-6: Q3, 7-8: Q4
    expected = pd.Series(["Q1", "Q1", "Q2", "Q2", "Q3", "Q3", "Q4", "Q4"])
    check("quartile_bins", result, expected)


if __name__ == "__main__":
    main()