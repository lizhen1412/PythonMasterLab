#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 23：时间序列重采样（resample）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/23_time_series_resample.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    idx = pd.date_range("2024-01-01", periods=12, freq="6H")
    s = pd.Series(range(12), index=idx, name="value")

    print("原始时间序列 ->")
    print(s.head())

    print("\n按天汇总（sum）->")
    print(s.resample("D").sum())

    print("\n按 12 小时重采样（mean）->")
    print(s.resample("12H").mean())

    print("\nasfreq 生成规则频率（会出现 NaN）->")
    daily = s.resample("D").asfreq()
    print(daily)

    print("\nffill 填充缺失 ->")
    print(daily.ffill())

    print("\n分组 + 时间频率（Grouper）->")
    df = pd.DataFrame(
        {
            "time": idx,
            "city": ["A", "A", "B", "B"] * 3,
            "value": [10, 11, 8, 9, 12, 13, 6, 7, 14, 15, 5, 6],
        }
    )
    grouped = (
        df.groupby(["city", pd.Grouper(key="time", freq="D")])["value"].sum()
    )
    print(grouped)


if __name__ == "__main__":
    main()