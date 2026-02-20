#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 19：使用 DateTime 组件过滤数据。
Author: Lambert

题目：
给定一个包含日期的 DataFrame，筛选出：
1. 所有周末的数据
2. 所有月末的数据
3. 2023年第一季度的数据

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/19_datetime_filter.py
"""

from __future__ import annotations

import pandas as pd


def filter_weekends(df: pd.DataFrame) -> pd.DataFrame:
    """筛选周末数据（周六周日）"""
    df = df.copy()
    return df[df["date"].dt.dayofweek >= 5]


def filter_month_end(df: pd.DataFrame) -> pd.DataFrame:
    """筛选月末数据"""
    df = df.copy()
    return df[df["date"].dt.is_month_end]


def filter_q1_2023(df: pd.DataFrame) -> pd.DataFrame:
    """筛选2023年Q1数据"""
    df = df.copy()
    return df[(df["date"].dt.year == 2023) & (df["date"].dt.quarter == 1)]


def check(label: str, got: object, expected: object) -> None:
    ok = got.equals(expected) if hasattr(got, "equals") else got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")


def main() -> None:
    df = pd.DataFrame({
        "date": pd.to_datetime([
            "2023-01-15",  # 周日
            "2023-01-31",  # 月末
            "2023-02-28",  # 月末
            "2023-03-15",  # 周三
            "2023-04-01",  # Q2开始
        ]),
        "value": [1, 2, 3, 4, 5]
    })

    check("weekends", filter_weekends(df)["value"].tolist(), [1])
    check("month_end", filter_month_end(df)["value"].tolist(), [2, 3])
    check("q1_2023", filter_q1_2023(df)["value"].tolist(), [1, 2, 3, 4])


if __name__ == "__main__":
    main()