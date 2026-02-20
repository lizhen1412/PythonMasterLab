#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 30：重塑与编码（pivot/get_dummies/explode/crosstab）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/30_reshape_encoding.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    data = pd.DataFrame(
        {
            "name": ["Alice", "Alice", "Bob", "Bob"],
            "subject": ["math", "math", "math", "english"],
            "score": [88, 90, 75, 81],
        }
    )

    print("pivot（有重复会失败） ->")
    try:
        print(data.pivot(index="name", columns="subject", values="score"))
    except Exception as exc:
        print("pivot error ->", type(exc).__name__)

    print("\npivot_table（可聚合） ->")
    print(data.pivot_table(index="name", columns="subject", values="score", aggfunc="mean"))

    print("\nget_dummies ->")
    df = pd.DataFrame({"color": ["red", "blue", "red", "green"]})
    print(pd.get_dummies(df["color"], prefix="color"))

    print("\nexplode ->")
    df_tags = pd.DataFrame({"name": ["A", "B"], "tags": [["x", "y"], ["y", "z"]]})
    print(df_tags.explode("tags"))

    print("\nwide_to_long ->")
    wide = pd.DataFrame(
        {
            "id": [1, 2],
            "sales_2023": [100, 120],
            "sales_2024": [130, 140],
        }
    )
    long = pd.wide_to_long(wide, stubnames="sales", i="id", j="year", sep="_")
    print(long.reset_index())

    print("\ncrosstab ->")
    print(pd.crosstab(data["name"], data["subject"]))

    print("\nconcat(axis=1, keys=...) ->")
    left = pd.DataFrame({"A": [1, 2]})
    right = pd.DataFrame({"B": [3, 4]})
    print(pd.concat([left, right], axis=1, keys=["left", "right"]))


if __name__ == "__main__":
    main()