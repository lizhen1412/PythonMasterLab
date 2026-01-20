#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 38：SettingWithCopy 与安全赋值。

运行：
    python3 02_Frameworks/01_Pandas/38_settingwithcopy.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    pd.options.mode.chained_assignment = "warn"

    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy"],
            "score": [88, 75, 92],
        }
    )

    print("原始 df ->")
    print(df)

    print("\n可能触发 SettingWithCopyWarning ->")
    high = df[df["score"] >= 80]
    high["grade"] = "A"
    print(high)

    print("\n推荐做法：用 loc 赋值 ->")
    df.loc[df["score"] >= 80, "grade"] = "A"
    df.loc[df["score"] < 80, "grade"] = "B"
    print(df)

    print("\n或者显式 copy 再改 ->")
    high_copy = df[df["score"] >= 80].copy()
    high_copy["grade"] = "A"
    print(high_copy)


if __name__ == "__main__":
    main()
