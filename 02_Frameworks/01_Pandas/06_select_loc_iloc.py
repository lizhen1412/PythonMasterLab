#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：loc/iloc/at/iat 选择。

运行：
    python3 02_Frameworks/01_Pandas/06_select_loc_iloc.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy"],
            "age": [20, 21, 19],
            "score": [88, 75, 92],
        },
        index=["a", "b", "c"],
    )

    print("df ->")
    print(df)

    print("\nloc 行列 ->")
    print(df.loc["a", "score"])
    print(df.loc["a":"b", ["name", "score"]])

    print("\niloc 行列 ->")
    print(df.iloc[0, 2])
    print(df.iloc[0:2, 0:2])

    print("\nat/iat 标量 ->")
    print(df.at["b", "age"])
    print(df.iat[2, 1])


if __name__ == "__main__":
    main()
