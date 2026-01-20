#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 33：I/O 进阶（read_csv 参数、chunksize、json_normalize、Excel 多表）。

运行：
    python3 02_Frameworks/01_Pandas/33_io_csv_json_excel_advanced.py
"""

from __future__ import annotations

from io import BytesIO, StringIO
import gzip

import pandas as pd


def main() -> None:
    csv_text = """id,name,score,date
1,Alice,88,2024-01-01
2,Bob,NA,2024-01-02
3,Cathy,92,2024-01-03
"""
    df = pd.read_csv(
        StringIO(csv_text),
        dtype={"id": "Int64"},
        parse_dates=["date"],
        usecols=["id", "name", "score", "date"],
        na_values=["NA", ""],
    )
    print("read_csv 参数示例 ->")
    print(df)

    print("\nchunksize ->")
    total = 0
    for chunk in pd.read_csv(StringIO(csv_text), chunksize=2):
        total += chunk["id"].sum()
    print("chunksize sum(id) ->", total)

    print("\ncompression=gzip ->")
    gz_buffer = BytesIO()
    with gzip.GzipFile(fileobj=gz_buffer, mode="wb") as f:
        f.write(csv_text.encode("utf-8"))
    gz_buffer.seek(0)
    print(pd.read_csv(gz_buffer, compression="gzip").head(2))

    print("\njson_normalize ->")
    data = [
        {
            "user": {"id": 1, "name": "Alice"},
            "items": [{"product": "P1", "qty": 2}, {"product": "P2", "qty": 1}],
        },
        {
            "user": {"id": 2, "name": "Bob"},
            "items": [{"product": "P1", "qty": 3}],
        },
    ]
    normalized = pd.json_normalize(
        data,
        record_path="items",
        meta=[["user", "id"], ["user", "name"]],
    )
    print(normalized)

    print("\nExcel 多表（可选依赖 openpyxl） ->")
    try:
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Sheet1")
            df["id"].to_frame("id").to_excel(writer, index=False, sheet_name="Sheet2")
        buffer.seek(0)
        sheets = pd.read_excel(buffer, sheet_name=["Sheet1", "Sheet2"])
        print("Sheet1 ->")
        print(sheets["Sheet1"].head(2))
        print("Sheet2 ->")
        print(sheets["Sheet2"].head(2))
    except Exception as exc:
        print("Excel 读写需要 openpyxl/xlsxwriter ->", type(exc).__name__)


if __name__ == "__main__":
    main()
