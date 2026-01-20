#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 32：时间序列进阶（shift/diff/tz/merge_asof）。

运行：
    python3 02_Frameworks/01_Pandas/32_time_series_advanced.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    idx = pd.date_range("2024-01-01 09:00", periods=6, freq="H")
    s = pd.Series([10, 12, 11, 15, 14, 16], index=idx, name="value")

    print("shift ->")
    print(s.shift(1))

    print("\ndiff ->")
    print(s.diff())

    print("\npct_change ->")
    print(s.pct_change())

    print("\nbetween_time / at_time ->")
    print(s.between_time("10:00", "12:00"))
    print(s.at_time("11:00"))

    print("\n时区本地化与转换 ->")
    s_tz = s.tz_localize("Asia/Shanghai")
    print(s_tz.head(2))
    print(s_tz.tz_convert("UTC").head(2))

    print("\nPeriodIndex ->")
    period_index = s.index.to_period("D")
    print(period_index)
    print(period_index.to_timestamp()[:2])

    print("\nasof / merge_asof ->")
    s2 = pd.Series([100, 200, 300], index=pd.to_datetime(["2024-01-01 09:30", "2024-01-01 11:30", "2024-01-01 14:00"]))
    print("asof('2024-01-01 10:00') ->", s2.asof("2024-01-01 10:00"))

    left = pd.DataFrame(
        {"time": pd.to_datetime(["2024-01-01 10:00", "2024-01-01 12:00", "2024-01-01 15:00"]), "value": [1, 2, 3]}
    )
    right = pd.DataFrame(
        {"time": pd.to_datetime(["2024-01-01 09:50", "2024-01-01 11:40", "2024-01-01 14:30"]), "price": [10, 20, 30]}
    )
    print(pd.merge_asof(left.sort_values("time"), right.sort_values("time"), on="time"))

    print("\nresample 参数示例 ->")
    df = pd.DataFrame({"value": range(6)}, index=idx)
    print(df.resample("D", label="right", closed="right").sum())


if __name__ == "__main__":
    main()
