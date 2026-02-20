#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：CSV 读写（StringIO）。
Author: Lambert

题目：
实现两个函数：
1) read_users_from_csv(text) -> DataFrame
2) to_csv_text(df) -> str（不包含索引）

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/10_io_csv_stringio.py
"""

from __future__ import annotations

from io import StringIO

import pandas as pd


def read_users_from_csv(text: str) -> pd.DataFrame:
    return pd.read_csv(StringIO(text))


def to_csv_text(df: pd.DataFrame) -> str:
    buffer = StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue()


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
    csv_text = """name,age
Alice,20
Bob,21
"""
    df = read_users_from_csv(csv_text)
    out_text = to_csv_text(df)
    df_roundtrip = read_users_from_csv(out_text)
    check_df("csv_roundtrip", df_roundtrip, df)


if __name__ == "__main__":
    main()