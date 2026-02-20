#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 43：字符串解析（split/extract）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/43_string_parse.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series(
        ["order_2024-01-01_A", "order_2024-01-02_B", None],
        name="raw",
    ).astype("string")

    print("原始 ->")
    print(s)

    print("\nsplit(expand=True) ->")
    print(s.str.split("_", expand=True))

    print("\nextract 正则分组 ->")
    extracted = s.str.extract(r"order_(\d{4}-\d{2}-\d{2})_([A-Z])")
    extracted.columns = ["date", "code"]
    print(extracted)

    print("\n转换日期 ->")
    print(pd.to_datetime(extracted["date"], errors="coerce"))

    print("\n包含 A 码 ->")
    print(s.str.contains("_A", na=False))


if __name__ == "__main__":
    main()