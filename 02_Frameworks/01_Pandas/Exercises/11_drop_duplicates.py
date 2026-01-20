#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11：去重（drop_duplicates）。

题目：
给定订单表，按 user_id 去重，保留最后一条。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/11_drop_duplicates.py
"""

from __future__ import annotations

import pandas as pd


def dedup_users(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset=["user_id"], keep="last").reset_index(drop=True)


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
            "user_id": [1, 1, 2, 3, 2],
            "score": [80, 82, 90, 70, 95],
        }
    )
    result = dedup_users(df)
    expected = pd.DataFrame({"user_id": [1, 3, 2], "score": [82, 70, 95]})
    check_df("drop_duplicates", result, expected)


if __name__ == "__main__":
    main()
