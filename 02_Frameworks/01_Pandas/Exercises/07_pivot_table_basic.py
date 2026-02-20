#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：透视表（pivot_table）。
Author: Lambert

题目：
给定订单明细（user, product, amount），
生成以 user 为行、product 为列的金额透视表（sum）。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/07_pivot_table_basic.py
"""

from __future__ import annotations

import pandas as pd


def build_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(df, index="user", columns="product", values="amount", aggfunc="sum")


def check_df(label: str, got: pd.DataFrame, expected: pd.DataFrame) -> None:
    ok = got.equals(expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->")
        print(got)
        print("expected ->")
        print(expected)


def main() -> None:
    df = pd.DataFrame(
        {
            "user": ["Alice", "Alice", "Bob", "Bob"],
            "product": ["A", "B", "A", "B"],
            "amount": [10, 20, 5, 7],
        }
    )
    result = build_pivot_table(df)
    expected = pd.DataFrame(
        {"A": [10, 5], "B": [20, 7]},
        index=["Alice", "Bob"],
    )
    expected.index.name = "user"
    expected.columns.name = "product"
    check_df("pivot_table", result, expected)


if __name__ == "__main__":
    main()