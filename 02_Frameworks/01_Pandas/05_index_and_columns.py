#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：Index 与列名管理。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/05_index_and_columns.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "id": [101, 102, 103],
            "name": ["Alice", "Bob", "Cathy"],
            "score": [88, 75, 92],
        }
    )

    print("原始 df ->")
    print(df)

    df2 = df.set_index("id")
    print("\nset_index('id') ->")
    print(df2)

    df3 = df2.reset_index()
    print("\nreset_index ->")
    print(df3)

    df4 = df.rename(columns={"score": "final_score"})
    print("\nrename columns ->")
    print(df4)

    df5 = df.rename_axis("row_id")
    print("\nrename_axis ->", df5.index.name)


if __name__ == "__main__":
    main()