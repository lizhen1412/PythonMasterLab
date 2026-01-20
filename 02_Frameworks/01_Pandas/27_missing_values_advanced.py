#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 27：缺失值处理（进阶）。

运行：
    python3 02_Frameworks/01_Pandas/27_missing_values_advanced.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series([1.0, None, None, 4.0, None])
    print("原始 Series ->")
    print(s)

    print("\nffill/bfill ->")
    print(s.ffill())
    print(s.bfill())

    print("\nfillna(limit=1) ->")
    print(s.fillna(0, limit=1))

    print("\ninterpolate(linear) ->")
    print(s.interpolate())

    df = pd.DataFrame(
        {
            "name": ["Alice", None, "Cathy", None],
            "age": [20, None, None, 22],
            "score": [88, 75, None, None],
        }
    )
    print("\n原始 df ->")
    print(df)

    print("\ndropna(how='any') ->")
    print(df.dropna(how="any"))

    print("\ndropna(how='all') ->")
    print(df.dropna(how="all"))

    print("\ndropna(subset=['name', 'age']) ->")
    print(df.dropna(subset=["name", "age"]))

    print("\ndropna(thresh=2) ->")
    print(df.dropna(thresh=2))


if __name__ == "__main__":
    main()
