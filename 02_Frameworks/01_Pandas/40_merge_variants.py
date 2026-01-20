#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 40：merge 细节（left_on/right_on/suffixes/indicator/validate）。

运行：
    python3 02_Frameworks/01_Pandas/40_merge_variants.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    users = pd.DataFrame(
        {
            "user_id": [1, 2, 3],
            "name": ["Alice", "Bob", "Cathy"],
            "city": ["A", "B", "A"],
        }
    )
    orders = pd.DataFrame(
        {
            "uid": [1, 1, 2, 4],
            "amount": [100, 50, 80, 20],
            "city": ["X", "X", "Y", "Z"],
        }
    )

    print("left_on / right_on + suffixes ->")
    merged = pd.merge(
        users,
        orders,
        left_on="user_id",
        right_on="uid",
        how="left",
        suffixes=("_user", "_order"),
    )
    print(merged)

    print("\nindicator=True（outer） ->")
    indicator_df = pd.merge(
        users[["user_id", "name"]],
        orders[["uid", "amount"]],
        left_on="user_id",
        right_on="uid",
        how="outer",
        indicator=True,
    )
    print(indicator_df)

    print("\nvalidate（一对一检查）->")
    scores = pd.DataFrame(
        {
            "user_id": [1, 2, 3],
            "level": ["A", "B", "A"],
        }
    )
    checked = pd.merge(users, scores, on="user_id", validate="one_to_one")
    print(checked)


if __name__ == "__main__":
    main()
