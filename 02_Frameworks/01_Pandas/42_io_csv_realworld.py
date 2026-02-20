#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 42：CSV 实战参数（sep/index_col/na_values/parse_dates/na_rep）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/42_io_csv_realworld.py
"""

from __future__ import annotations

from io import StringIO

import pandas as pd


def main() -> None:
    csv_text = """id;name;score;date
1;Alice;88;2024-01-01
2;Bob;NA;2024-01-02
3;Cathy;;2024-01-03
"""
    df = pd.read_csv(
        StringIO(csv_text),
        sep=";",
        dtype={"id": "Int64"},
        parse_dates=["date"],
        na_values=["NA", ""],
        index_col="id",
    )
    print("read_csv 常用参数 ->")
    print(df)

    print("\nindex_col ->", df.index.name)

    print("\nto_csv 自定义输出 ->")
    buffer = StringIO()
    df.reset_index().to_csv(
        buffer,
        index=False,
        na_rep="NULL",
        date_format="%Y-%m-%d",
    )
    print(buffer.getvalue())


if __name__ == "__main__":
    main()