#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 28：统计概览与对比。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/28_stats_summary.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy", "Dan"],
            "age": [20, 21, 19, 22],
            "score": [88, 75, 92, 60],
            "city": ["A", "B", "A", None],
        }
    )

    print("describe(include='all') ->")
    print(df.describe(include="all"))

    print("\nvalue_counts(dropna=False) ->")
    print(df["city"].value_counts(dropna=False))

    print("\nunique / nunique ->")
    print("unique:", df["city"].unique())
    print("nunique(dropna=False):", df["city"].nunique(dropna=False))

    print("\nquantile ->")
    print(df["score"].quantile([0.25, 0.5, 0.75]))

    print("\ncorr/cov ->")
    print(df[["age", "score"]].corr())
    print(df[["age", "score"]].cov())

    print("\nDataFrame.compare ->")
    df2 = df.copy()
    df2.loc[1, "score"] = 80
    print(df.compare(df2))


if __name__ == "__main__":
    main()