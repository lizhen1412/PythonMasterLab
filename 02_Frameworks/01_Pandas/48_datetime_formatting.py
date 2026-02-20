#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 48：日期格式化（dt.strftime）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/48_datetime_formatting.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "time": pd.to_datetime(
                [
                    "2024-01-01 09:30",
                    "2024-01-03 14:05",
                    "2024-02-10 08:00",
                ]
            )
        }
    )

    print("原始时间 ->")
    print(df)

    df["date_str"] = df["time"].dt.strftime("%Y-%m-%d")
    df["month"] = df["time"].dt.strftime("%Y-%m")
    df["time_str"] = df["time"].dt.strftime("%Y/%m/%d %H:%M")

    print("\n格式化结果 ->")
    print(df)


if __name__ == "__main__":
    main()