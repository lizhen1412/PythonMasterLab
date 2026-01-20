#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：DataFrame 基础。

运行：
    python3 02_Frameworks/01_Pandas/04_dataframe_basics.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    data = [
        {"name": "Alice", "age": 20, "score": 88},
        {"name": "Bob", "age": 21, "score": 75},
        {"name": "Cathy", "age": 19, "score": 92},
    ]
    df = pd.DataFrame(data)
    print("df ->")
    print(df)

    print("\nshape ->", df.shape)
    print("columns ->", df.columns.tolist())
    print("dtypes ->")
    print(df.dtypes)

    print("\nhead(2) ->")
    print(df.head(2))
    print("\ntail(2) ->")
    print(df.tail(2))

    print("\ninfo ->")
    df.info()


if __name__ == "__main__":
    main()
