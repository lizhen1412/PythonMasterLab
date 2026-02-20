#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：apply / map / replace。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/11_apply_map_replace.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series(["a", "bb", "ccc"])
    print("map ->", s.map(len).tolist())

    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    print("\napply(axis=0) ->")
    print(df.apply(sum, axis=0))

    print("\napply(axis=1) ->")
    print(df.apply(sum, axis=1))

    print("\nDataFrame.map (元素级) ->")
    print(df.map(lambda x: x * 10))

    print("\nreplace ->")
    print(df.replace({1: 100, 4: 400}))


if __name__ == "__main__":
    main()