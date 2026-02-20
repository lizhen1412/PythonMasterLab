#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 37：eval/query/pipe 与方法链。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/37_eval_query_pipe.py
"""

from __future__ import annotations

import pandas as pd


def add_grade(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["grade"] = "B"
    df.loc[df["score"] >= 85, "grade"] = "A"
    return df


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy"],
            "qty": [1, 2, 3],
            "price": [10, 12, 8],
            "score": [88, 75, 92],
        }
    )

    print("eval ->")
    df["total"] = df.eval("qty * price")
    print(df[["name", "total"]])

    print("\nquery + 外部变量 ->")
    min_score = 80
    print(df.query("score >= @min_score"))

    print("\npipe 方法链 ->")
    result = (
        df.pipe(add_grade)
        .sort_values("score", ascending=False)
        .reset_index(drop=True)
    )
    print(result)


if __name__ == "__main__":
    main()