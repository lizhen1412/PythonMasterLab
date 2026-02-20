#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 34：其他格式与 SQL（可选依赖）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/34_io_other_formats_sql_optional.py
"""

from __future__ import annotations

from io import BytesIO, StringIO
import sqlite3
import tempfile

import pandas as pd


def main() -> None:
    df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})

    print("SQL (sqlite3 内存库) ->")
    with sqlite3.connect(":memory:") as conn:
        df.to_sql("users", conn, index=False, if_exists="replace")
        out = pd.read_sql("SELECT * FROM users", conn)
    print(out)

    print("\nParquet (需 pyarrow/fastparquet) ->")
    try:
        buffer = BytesIO()
        df.to_parquet(buffer, index=False)
        buffer.seek(0)
        print(pd.read_parquet(buffer))
    except Exception as exc:
        print("Parquet 依赖缺失 ->", type(exc).__name__)

    print("\nFeather (需 pyarrow) ->")
    try:
        with tempfile.NamedTemporaryFile(suffix=".feather") as tmp:
            df.to_feather(tmp.name)
            print(pd.read_feather(tmp.name))
    except Exception as exc:
        print("Feather 依赖缺失 ->", type(exc).__name__)

    print("\nHDF (需 tables) ->")
    try:
        with tempfile.NamedTemporaryFile(suffix=".h5") as tmp:
            df.to_hdf(tmp.name, key="data", mode="w")
            print(pd.read_hdf(tmp.name, key="data"))
    except Exception as exc:
        print("HDF 依赖缺失 ->", type(exc).__name__)

    print("\nread_html (需 lxml/bs4) ->")
    html = """<table><tr><th>id</th><th>name</th></tr>
<tr><td>1</td><td>Alice</td></tr>
<tr><td>2</td><td>Bob</td></tr></table>"""
    try:
        tables = pd.read_html(StringIO(html))
        print(tables[0])
    except Exception as exc:
        print("read_html 依赖缺失 ->", type(exc).__name__)

    print("\nread_clipboard (需系统剪贴板) ->")
    try:
        print(pd.read_clipboard())
    except Exception as exc:
        print("read_clipboard 不可用 ->", type(exc).__name__)


if __name__ == "__main__":
    main()