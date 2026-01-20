#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：排序与排名。

运行：
    python3 02_Frameworks/01_Pandas/14_sort_rank.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame({"name": ["A", "B", "C", "D"], "score": [88, 75, 92, 75]})

    print("sort_values(score) ->")
    print(df.sort_values("score"))

    print("\nrank ->")
    df["rank"] = df["score"].rank(ascending=False, method="dense")
    print(df)

    print("\nnlargest(2) ->")
    print(df.nlargest(2, "score"))


if __name__ == "__main__":
    main()
