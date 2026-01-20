#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：时间与时间差。

运行：
    python3 02_Frameworks/01_Pandas/13_datetime_timedelta.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    dates = pd.to_datetime(["2024-01-01", "2024-01-03", "2024-01-05"])
    s = pd.Series(dates)
    print("dt.year ->", s.dt.year.tolist())
    print("dt.day_name ->", s.dt.day_name().tolist())

    delta = pd.Timedelta(days=2, hours=3)
    print("Timedelta ->", delta)

    rng = pd.date_range("2024-01-01", periods=5, freq="D")
    print("date_range ->", rng)


if __name__ == "__main__":
    main()
