#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：类型与转换。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/09_dtypes_and_convert.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "id": ["1", "2", "3"],
            "price": ["10.5", "20", "invalid"],
            "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        }
    )

    print("df.dtypes ->")
    print(df.dtypes)

    df["id"] = df["id"].astype(int)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], errors="raise")

    print("\n转换后 dtypes ->")
    print(df.dtypes)

    print("\nconvert_dtypes ->")
    print(df.convert_dtypes().dtypes)


if __name__ == "__main__":
    main()