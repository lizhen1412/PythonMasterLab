#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 20：多级索引（MultiIndex）。

运行：
    python3 02_Frameworks/01_Pandas/20_multiindex.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    arrays = [
        ["A", "A", "B", "B"],
        [1, 2, 1, 2],
    ]
    index = pd.MultiIndex.from_arrays(arrays, names=["group", "id"])
    df = pd.DataFrame({"score": [88, 90, 70, 75]}, index=index)

    print("多级索引 DataFrame ->")
    print(df)

    print("\n按层级选择（tuple）:")
    print(df.loc[("A", 1)])

    print("\n只选 group=A（部分索引）:")
    print(df.loc["A"])

    print("\nxs(level) 交叉选择:")
    print(df.xs(1, level="id"))

    print("\nlevel values ->", df.index.get_level_values("group").tolist())

    print("\nswaplevel/sort_index ->")
    swapped = df.swaplevel(0, 1)
    print(swapped)
    print(swapped.sort_index())

    print("\nreset_index 回到普通列:")
    flat = df.reset_index()
    print(flat)

    print("\nset_index 重新构建 MultiIndex:")
    print(flat.set_index(["group", "id"]))


if __name__ == "__main__":
    main()
