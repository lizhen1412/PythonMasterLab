#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 41：时间序列切片与时间窗口。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/41_time_series_slicing.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    idx = pd.date_range("2024-01-30 06:00", periods=8, freq="6H")
    s = pd.Series(range(8), index=idx, name="value")

    print("原始时间序列 ->")
    print(s)

    print("\n按天切片 ->")
    print(s.loc["2024-01-31"])

    print("\n按月切片 ->")
    print(s.loc["2024-01"])
    print(s.loc["2024-02"])

    print("\nbetween_time ->")
    print(s.between_time("06:00", "18:00"))

    print("\n时间窗口 rolling('12H').mean ->")
    print(s.rolling("12H").mean())

    print("\nresample(on='time') ->")
    df = pd.DataFrame({"time": idx, "value": range(8)})
    print(df.resample("D", on="time")["value"].sum())


if __name__ == "__main__":
    main()