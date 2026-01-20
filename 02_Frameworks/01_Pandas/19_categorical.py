#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 19：类别数据（category）。

运行：
    python3 02_Frameworks/01_Pandas/19_categorical.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series(["low", "medium", "low", "high"])
    cat = s.astype("category")
    print("category dtype ->", cat.dtype)
    print("categories ->", cat.cat.categories.tolist())
    print("codes ->", cat.cat.codes.tolist())

    cat = cat.cat.add_categories(["very high"])
    print("add categories ->", cat.cat.categories.tolist())

    cat = cat.cat.remove_unused_categories()
    print("remove unused ->", cat.cat.categories.tolist())


if __name__ == "__main__":
    main()
