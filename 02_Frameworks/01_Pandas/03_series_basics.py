#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：Series 基础。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/03_series_basics.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s1 = pd.Series([10, 20, 30], index=["a", "b", "c"], name="score")
    print("s1 ->")
    print(s1)
    print("name ->", s1.name)
    print("index ->", s1.index.tolist())
    print("dtype ->", s1.dtype)

    s2 = pd.Series({"alice": 90, "bob": 75, "cathy": 88}, name="grade")
    print("\ns2 ->")
    print(s2)

    print("\n访问元素:")
    print("s1['b'] ->", s1["b"])
    print("s1.loc['a'] ->", s1.loc["a"])
    print("s1.iloc[1] ->", s1.iloc[1])

    print("\n切片:")
    print(s1.loc["a":"b"])  # label slice includes end


if __name__ == "__main__":
    main()