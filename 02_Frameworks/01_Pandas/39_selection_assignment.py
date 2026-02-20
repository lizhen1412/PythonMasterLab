#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 39：选择与赋值（[]/loc/assign/where）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/39_selection_assignment.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy", "Dan"],
            "qty": [1, 2, 1, 3],
            "price": [10, 12, 8, 7],
            "score": [88, 75, 92, 60],
        }
    )

    print("原始 df ->")
    print(df)

    print("\n选择单列（Series）->")
    print(df["score"])

    print("\n选择多列（DataFrame）->")
    print(df[["name", "score"]])

    print("\nloc 条件选择 ->")
    print(df.loc[df["score"] >= 80, ["name", "score"]])

    print("\n新增列（直接赋值）->")
    df["total"] = df["qty"] * df["price"]
    print(df)

    print("\n条件赋值（用 loc）->")
    df.loc[df["score"] >= 85, "grade"] = "A"
    df.loc[df["score"] < 85, "grade"] = "B"
    print(df)

    print("\nassign 返回新表 ->")
    df2 = df.assign(score_min80=lambda x: x["score"].where(x["score"] >= 80, 0))
    print(df2)


if __name__ == "__main__":
    main()