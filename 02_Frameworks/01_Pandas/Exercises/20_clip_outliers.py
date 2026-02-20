#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 20：使用 clip 处理异常值。
Author: Lambert

题目：
给定一个包含数值的 Series，使用 clip 将超出 1.5倍 IQR 范围的值裁剪到边界值。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/20_clip_outliers.py
"""

from __future__ import annotations

import pandas as pd


def clip_outliers(s: pd.Series) -> pd.Series:
    """使用 IQR 方法裁剪异常值"""
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return s.clip(lower, upper)


def check(label: str, got: object, expected: object) -> None:
    ok = got.equals(expected) if hasattr(got, "equals") else got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print(f"  got: {got.tolist()}")
        print(f"  expected: {expected.tolist()}")


def main() -> None:
    s = pd.Series([10, 12, 15, 14, 13, 100, 11])  # 100 是异常值
    result = clip_outliers(s)
    # Q1=11, Q3=15, IQR=4, lower=5, upper=21
    # 100 应该被裁剪到 21
    expected = pd.Series([10, 12, 15, 14, 13, 21, 11])
    check("clip_outliers", result, expected)


if __name__ == "__main__":
    main()