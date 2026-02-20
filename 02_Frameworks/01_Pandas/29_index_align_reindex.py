#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 29：索引对齐与重建（reindex/align/sort_index）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/29_index_align_reindex.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series([1, 2], index=["a", "b"], name="value")
    print("reindex ->")
    print(s.reindex(["b", "c", "a"], fill_value=0))

    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=["x", "y"])
    df2 = pd.DataFrame({"B": [30, 40], "C": [5, 6]}, index=["y", "z"])
    print("\nalign(join='outer') ->")
    left, right = df.align(df2, join="outer")
    print(left)
    print(right)

    print("\nreindex_like ->")
    print(df.reindex_like(left))

    print("\nsort_index ->")
    print(df2.sort_index())

    idx = pd.Index(["b", "a", "c"])
    other = pd.Index(["a", "c", "d"])
    print("\nIndex union/intersection/difference ->")
    print(idx.union(other))
    print(idx.intersection(other))
    print(idx.difference(other))

    print("\ntake / sample ->")
    print(df.take([0]))
    print(df.sample(n=1, random_state=42))


if __name__ == "__main__":
    main()