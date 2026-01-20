#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：时间序列重采样（日汇总）。

题目：
给定带时间索引的 Series，按天 resample 并求和。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/08_resample_daily.py
"""

from __future__ import annotations

import pandas as pd


def resample_daily_sum(s: pd.Series) -> pd.Series:
    return s.resample("D").sum()


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
    idx = pd.to_datetime(
        [
            "2024-01-01 10:00",
            "2024-01-01 12:00",
            "2024-01-02 09:00",
        ]
    )
    s = pd.Series([10, 5, 7], index=idx, name="sales")
    result = resample_daily_sum(s)
    expected = pd.Series(
        [15, 7],
        index=pd.to_datetime(["2024-01-01", "2024-01-02"]),
        name="sales",
    )
    check_series("resample_daily", result, expected)


if __name__ == "__main__":
    main()
