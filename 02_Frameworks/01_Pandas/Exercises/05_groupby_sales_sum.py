#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：分组汇总（groupby + sum）。

题目：
给定一张销售表（store, amount），按 store 分组求和。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/05_groupby_sales_sum.py
"""

from __future__ import annotations

import pandas as pd


def sum_sales_by_store(df: pd.DataFrame) -> pd.Series:
    return df.groupby("store")["amount"].sum()


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
    df = pd.DataFrame(
        {
            "store": ["A", "A", "B", "B"],
            "amount": [100, 50, 80, 20],
        }
    )
    result = sum_sales_by_store(df)
    expected = pd.Series([150, 100], index=pd.Index(["A", "B"], name="store"), name="amount")
    check_series("groupby_sum", result, expected)


if __name__ == "__main__":
    main()
