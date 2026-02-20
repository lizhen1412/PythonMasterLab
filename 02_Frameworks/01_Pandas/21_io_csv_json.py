#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 21：CSV/JSON 的 I/O（使用内存字符串）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/21_io_csv_json.py
"""

from __future__ import annotations

from io import StringIO

import pandas as pd


def main() -> None:
    csv_text = """name,score
Alice,88
Bob,75
Cathy,92
"""
    df_csv = pd.read_csv(StringIO(csv_text))
    print("CSV 读入 ->")
    print(df_csv)

    buffer = StringIO()
    df_csv.to_csv(buffer, index=False)
    print("\nCSV 写出（StringIO）->")
    print(buffer.getvalue())

    json_text = '[{"name":"Alice","score":88},{"name":"Bob","score":75}]'
    df_json = pd.read_json(StringIO(json_text))
    print("\nJSON 读入 ->")
    print(df_json)

    json_lines = df_json.to_json(orient="records", lines=True)
    print("\nJSON Lines 写出 ->")
    print(json_lines)

    df_lines = pd.read_json(StringIO(json_lines), lines=True)
    print("\nJSON Lines 读回 ->")
    print(df_lines)


if __name__ == "__main__":
    main()