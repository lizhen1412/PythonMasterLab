#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 26：数据清洗与列操作。

运行：
    python3 02_Frameworks/01_Pandas/26_data_cleaning_columns.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy", "Bob"],
            "qty": [1, 2, 3, 2],
            "price": [10, 12, 8, 12],
            "temp": ["x", "y", "z", "y"],
        }
    )
    print("原始 df ->")
    print(df)

    print("\ndrop 列 ->")
    print(df.drop(columns=["temp"]))

    print("\nassign 新列 ->")
    df_assigned = df.assign(total=lambda x: x["qty"] * x["price"])
    print(df_assigned)

    print("\ninsert 列 ->")
    df_insert = df.copy()
    df_insert.insert(1, "city", ["A", "B", "A", "B"])
    print(df_insert)

    print("\npop 列 ->")
    removed = df_insert.pop("city")
    print("pop 出来的列 ->", removed.tolist())
    print(df_insert)

    print("\n重复行检测 ->")
    print(df.duplicated(subset=["name", "qty"]))
    print("drop_duplicates(keep='last') ->")
    print(df.drop_duplicates(subset=["name", "qty"], keep="last"))

    print("\nwhere/mask/clip ->")
    scores = pd.DataFrame({"score": [120, 80, -5, 95]})
    print("clip 到 0~100 ->")
    print(scores.clip(lower=0, upper=100))
    print("where(score>=0, 0) ->")
    print(scores.where(scores["score"] >= 0, 0))
    print("mask(score>100, 100) ->")
    print(scores.mask(scores["score"] > 100, 100))

    print("\n正则替换 ->")
    phones = pd.DataFrame({"phone": ["138-0000", "138 1111", "138_2222"]})
    phones["phone_clean"] = phones["phone"].str.replace(r"\D", "", regex=True)
    print(phones)


if __name__ == "__main__":
    main()
