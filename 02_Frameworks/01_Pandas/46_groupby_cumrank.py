#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 46：分组累计与排名（cumsum/cumcount/rank）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/46_groupby_cumrank.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "dept": ["A", "A", "B", "A", "B", "B"],
            "month": [1, 2, 1, 3, 2, 3],
            "sales": [100, 80, 90, 60, 120, 110],
        }
    ).sort_values(["dept", "month"]).reset_index(drop=True)

    print("原始 df（已按 dept, month 排序）->")
    print(df)

    df["dept_cumsum"] = df.groupby("dept")["sales"].cumsum()
    df["dept_order"] = df.groupby("dept").cumcount() + 1
    df["dept_rank"] = df.groupby("dept")["sales"].rank(ascending=False, method="dense")

    print("\n分组累计与排名 ->")
    print(df)


if __name__ == "__main__":
    main()