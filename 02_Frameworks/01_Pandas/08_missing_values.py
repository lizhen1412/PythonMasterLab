#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：缺失值处理。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/08_missing_values.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", None, "Dan"],
            "age": [20, pd.NA, 19, 22],
            "score": [88, 75, float("nan"), 60],
        }
    )

    print("df ->")
    print(df)

    print("\nisna ->")
    print(df.isna())

    print("\nfillna ->")
    filled = df.fillna({"name": "Unknown", "age": 0, "score": df["score"].mean()})
    print(filled)

    print("\ndropna (any) ->")
    print(df.dropna())

    print("\ncombine_first ->")
    other = pd.DataFrame({"name": ["X", "Y", "Z", "W"]})
    print(df["name"].combine_first(other["name"]))


if __name__ == "__main__":
    main()