#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 24：性能与最佳实践（入门版）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/24_performance_tips.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    tips = [
        "优先使用向量化运算，少写逐行 for 循环",
        "对重复字符串使用 category 降内存",
        "read_csv 指定 usecols/dtype/parse_dates 减少开销",
        "避免链式赋值，使用 .loc 精确赋值",
        "必要时先选列再计算，减少中间拷贝",
    ]

    print("性能小贴士：")
    for i, tip in enumerate(tips, start=1):
        print(f"{i}. {tip}")

    df = pd.DataFrame(
        {
            "city": ["A", "A", "B", "B", "A"],
            "qty": [1, 2, 3, 4, 2],
            "price": [10, 12, 11, 9, 8],
        }
    )

    print("\n向量化计算 ->")
    df["total"] = df["qty"] * df["price"]
    print(df)

    print("\ncategory 降内存 ->")
    print("before:")
    print(df[["city"]].memory_usage(deep=True))
    df["city_cat"] = df["city"].astype("category")
    print("after:")
    print(df[["city_cat"]].memory_usage(deep=True))

    print("\nloc 赋值避免链式赋值 ->")
    df.loc[df["qty"] >= 3, "priority"] = "high"
    df["priority"] = df["priority"].fillna("normal")
    print(df[["city", "qty", "priority"]])


if __name__ == "__main__":
    main()