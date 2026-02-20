#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 17：使用 Grouper 按月分组统计。
Author: Lambert

题目：
给定一个包含日期和销售额的 DataFrame，使用 pd.Grouper 按月分组统计销售额。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/17_grouper_monthly.py
"""

from __future__ import annotations

import pandas as pd


def monthly_sales(df: pd.DataFrame) -> pd.Series:
    """按月统计销售额"""
    return df.groupby(pd.Grouper(key="date", freq="M"))["sales"].sum()


def check(label: str, got: object, expected: object) -> None:
    ok = got.equals(expected) if hasattr(got, "equals") else got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print(f"  got: {got}")
        print(f"  expected: {expected}")


def main() -> None:
    df = pd.DataFrame({
        "date": pd.to_datetime(["2023-01-15", "2023-01-25", "2023-02-10", "2023-02-20", "2023-03-05"]),
        "sales": [100, 150, 200, 250, 300]
    })

    expected = pd.Series(
        [250, 450, 300],
        index=pd.to_datetime(["2023-01-31", "2023-02-28", "2023-03-31"]),
        name="sales"
    )

    result = monthly_sales(df)
    check("monthly_sales", result, expected)


if __name__ == "__main__":
    main()