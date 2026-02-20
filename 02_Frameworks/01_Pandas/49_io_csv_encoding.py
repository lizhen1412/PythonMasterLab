#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 49：CSV 编码与中文（encoding）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/49_io_csv_encoding.py
"""

from __future__ import annotations

from io import BytesIO

import pandas as pd


def main() -> None:
    csv_text = """id,name,city
1,张三,Beijing
2,李四,Shanghai
"""
    csv_bytes = csv_text.encode("utf-8")
    df = pd.read_csv(BytesIO(csv_bytes), encoding="utf-8")
    print("read_csv(encoding='utf-8') ->")
    print(df)

    buffer = BytesIO()
    df.to_csv(buffer, index=False, encoding="utf-8")
    out_bytes = buffer.getvalue()
    out_text = out_bytes.decode("utf-8")
    print("\nto_csv(encoding='utf-8') ->")
    print(out_text)

    print("utf-8 字节长度 ->", len(out_bytes))


if __name__ == "__main__":
    main()