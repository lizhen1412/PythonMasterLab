#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：loc 选择行。

题目：
给定一个以姓名为索引的 DataFrame，
使用 .loc 选择指定的行（保持顺序），并仅返回 score 与 age 两列。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/03_select_rows_loc.py
"""

from __future__ import annotations

import pandas as pd


def select_rows(df: pd.DataFrame, names: list[str]) -> pd.DataFrame:
    return df.loc[names, ["score", "age"]]


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
        {"score": [88, 92, 75], "age": [20, 21, 22]},
        index=["Alice", "Bob", "Cathy"],
    )
    result = select_rows(df, ["Cathy", "Alice"])
    expected = pd.DataFrame(
        {"score": [75, 88], "age": [22, 20]},
        index=["Cathy", "Alice"],
    )
    check_df("select_rows", result, expected)


if __name__ == "__main__":
    main()
