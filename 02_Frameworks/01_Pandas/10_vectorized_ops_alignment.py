#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：向量化运算与索引对齐。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/10_vectorized_ops_alignment.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
    s2 = pd.Series([10, 20, 30], index=["b", "c", "d"])

    print("s1 + s2 (对齐) ->")
    print(s1 + s2)

    print("\nadd(fill_value=0) ->")
    print(s1.add(s2, fill_value=0))

    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=["x", "y"])
    s = pd.Series({"A": 10, "B": 100})
    print("\nDataFrame + Series ->")
    print(df + s)


if __name__ == "__main__":
    main()