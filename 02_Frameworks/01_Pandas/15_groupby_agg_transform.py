#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：分组聚合与转换。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/15_groupby_agg_transform.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "dept": ["A", "A", "B", "B", "B"],
            "name": ["Alice", "Bob", "Cathy", "Dan", "Eve"],
            "score": [88, 75, 92, 60, 85],
        }
    )

    print("groupby mean ->")
    print(df.groupby("dept")["score"].mean())

    print("\nagg 多指标 ->")
    print(df.groupby("dept")["score"].agg(["count", "mean", "max"]))

    print("\ntransform ->")
    df["dept_mean"] = df.groupby("dept")["score"].transform("mean")
    print(df)

    print("\nvalue_counts ->")
    print(df["dept"].value_counts())


if __name__ == "__main__":
    main()