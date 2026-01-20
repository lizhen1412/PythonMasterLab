#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 35：与 NumPy/字典互操作 + 可空类型。

运行：
    python3 02_Frameworks/01_Pandas/35_interop_nullable.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "id": [1, None, 3],
            "flag": [True, None, False],
            "name": ["Alice", None, "Cathy"],
        }
    )
    print("原始 dtypes ->")
    print(df.dtypes)

    print("\nconvert_dtypes ->")
    df2 = df.convert_dtypes()
    print(df2.dtypes)

    print("\n显式可空类型 ->")
    df3 = df.copy()
    df3["id"] = df3["id"].astype("Int64")
    df3["flag"] = df3["flag"].astype("boolean")
    df3["name"] = df3["name"].astype("string")
    print(df3.dtypes)

    print("\nto_numpy ->")
    print(df2.to_numpy())

    print("\nto_dict(records) ->")
    print(df2.to_dict(orient="records"))

    print("\nto_records ->")
    print(df2.to_records(index=False))


if __name__ == "__main__":
    main()
