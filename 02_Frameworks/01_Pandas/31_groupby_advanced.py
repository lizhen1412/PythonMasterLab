#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 31：groupby 进阶。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/31_groupby_advanced.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "dept": ["A", "A", "B", None, "B"],
            "city": ["X", "Y", "X", "Y", "X"],
            "name": ["Alice", "Bob", "Cathy", "Dan", "Eve"],
            "score": [88, 75, 92, 60, 85],
        }
    )

    print("多键分组 ->")
    print(df.groupby(["dept", "city"])["score"].mean())

    print("\nas_index=False ->")
    print(df.groupby("dept", as_index=False)["score"].sum())

    print("\ndropna=False ->")
    print(df.groupby("dept", dropna=False)["score"].mean())

    print("\nobserved=True（类别分组） ->")
    df_cat = df.copy()
    df_cat["dept"] = df_cat["dept"].astype("category")
    print(df_cat.groupby("dept", observed=True)["score"].mean())

    print("\n命名聚合 ->")
    print(df.groupby("dept").agg(total=("score", "sum"), avg=("score", "mean")))

    print("\nsize vs count ->")
    print(df.groupby("dept").size())
    print(df.groupby("dept")["score"].count())

    print("\napply vs transform ->")
    def top_one(g: pd.DataFrame) -> pd.DataFrame:
        return g.nlargest(1, "score")

    print(df.groupby("dept").apply(top_one))
    df["score_centered"] = df.groupby("dept")["score"].transform(lambda s: s - s.mean())
    print(df)


if __name__ == "__main__":
    main()