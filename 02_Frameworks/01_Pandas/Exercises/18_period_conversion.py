#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 18：Period 转换。
Author: Lambert

题目：
给定一个 DatetimeIndex，将其转换为 PeriodIndex（按月），然后再转换回 DatetimeIndex。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/18_period_conversion.py
"""

from __future__ import annotations

import pandas as pd


def convert_to_period_and_back(dates: pd.DatetimeIndex) -> pd.DatetimeIndex:
    """将日期转为月度 Period 后再转回 DatetimeIndex（月末）"""
    period_idx = dates.to_period("M")
    return period_idx.to_timestamp()


def check(label: str, got: object, expected: object) -> None:
    ok = got.equals(expected) if hasattr(got, "equals") else got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print(f"  got: {got}")
        print(f"  expected: {expected}")


def main() -> None:
    dates = pd.DatetimeIndex(["2023-01-15", "2023-02-10", "2023-03-05"])
    expected = pd.DatetimeIndex(["2023-01-31", "2023-02-28", "2023-03-31"])

    result = convert_to_period_and_back(dates)
    check("period_conversion", result, expected)


if __name__ == "__main__":
    main()