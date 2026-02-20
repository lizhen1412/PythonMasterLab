#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 22：Pickle/Excel I/O（Excel 为可选依赖）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/22_io_pickle_excel_optional.py
"""

from __future__ import annotations

from io import BytesIO

import pandas as pd


def main() -> None:
    df = pd.DataFrame({"name": ["Alice", "Bob"], "score": [88, 75]})

    print("Pickle 写入内存 ->")
    buffer = BytesIO()
    df.to_pickle(buffer)
    buffer.seek(0)
    df_pickle = pd.read_pickle(buffer)
    print(df_pickle)

    print("\nExcel 读写（需要 openpyxl/xlsxwriter）:")
    try:
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Sheet1")
        excel_buffer.seek(0)
        df_excel = pd.read_excel(excel_buffer, sheet_name="Sheet1")
        print(df_excel)
    except Exception as exc:
        print("缺少可选依赖或环境不支持 Excel 读写 ->", type(exc).__name__)


if __name__ == "__main__":
    main()