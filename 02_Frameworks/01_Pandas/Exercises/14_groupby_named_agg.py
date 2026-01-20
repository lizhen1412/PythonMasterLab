#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 14：命名聚合（groupby.agg）。

题目：
按部门分组，计算总分 total 与平均分 avg。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/14_groupby_named_agg.py
"""

from __future__ import annotations

import pandas as pd


def groupby_named_agg(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("dept").agg(total=("score", "sum"), avg=("score", "mean"))


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
            "dept": ["A", "A", "B"],
            "score": [80, 90, 70],
        }
    )
    result = groupby_named_agg(df)
    expected = pd.DataFrame({"total": [170, 70], "avg": [85.0, 70.0]}, index=["A", "B"])
    expected.index.name = "dept"
    check_df("named_agg", result, expected)


if __name__ == "__main__":
    main()
