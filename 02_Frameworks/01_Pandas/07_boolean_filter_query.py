#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：条件过滤与 query。

运行：
    python3 02_Frameworks/01_Pandas/07_boolean_filter_query.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy", "Dan"],
            "age": [20, 21, 19, 22],
            "score": [88, 75, 92, 60],
        }
    )

    print("df ->")
    print(df)

    print("\n条件过滤 ->")
    print(df[df["score"] >= 80])

    print("\nquery ->")
    print(df.query("age >= 20 and score < 90"))

    print("\nisin/between ->")
    print(df[df["name"].isin(["Alice", "Dan"])])
    print(df[df["age"].between(20, 21)])

    print("\nfilter columns ->")
    print(df.filter(["name", "score"]))


if __name__ == "__main__":
    main()
