#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 45：数值列选择与 numeric_only。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/45_select_dtypes_numeric_only.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy"],
            "score": [88, 75, 92],
            "bonus": ["10", "5", "not"],
            "city": ["A", "B", "A"],
        }
    )

    print("原始 df ->")
    print(df)
    print("\n原始 dtypes ->")
    print(df.dtypes)

    print("\nselect_dtypes(include='number') ->")
    num_df = df.select_dtypes(include="number")
    print(num_df)

    print("\nmean(numeric_only=True) ->")
    print(df.mean(numeric_only=True))

    print("\n把 bonus 转成数值 ->")
    df["bonus_num"] = pd.to_numeric(df["bonus"], errors="coerce")
    print(df[["bonus", "bonus_num"]])

    print("\n数值列均值 ->")
    print(df[["score", "bonus_num"]].mean())


if __name__ == "__main__":
    main()