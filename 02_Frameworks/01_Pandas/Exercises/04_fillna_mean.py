#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：缺失值填充（用均值）。
Author: Lambert

题目：
给定一个包含缺失值的 Series，用均值填充 NaN。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/04_fillna_mean.py
"""

from __future__ import annotations

import pandas as pd


def fillna_with_mean(s: pd.Series) -> pd.Series:
    mean_value = s.mean()
    return s.fillna(mean_value)


def check_series(label: str, got: pd.Series, expected: pd.Series) -> None:
    ok = got.equals(expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->")
        print(got)
        print("expected ->")
        print(expected)


def main() -> None:
    s = pd.Series([1.0, None, 3.0, None])
    expected = pd.Series([1.0, 2.0, 3.0, 2.0])
    result = fillna_with_mean(s)
    check_series("fillna_mean", result, expected)


if __name__ == "__main__":
    main()