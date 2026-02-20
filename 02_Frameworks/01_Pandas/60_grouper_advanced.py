#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 60：Grouper 高级操作。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/60_grouper_advanced.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    # 创建示例数据
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(
                [
                    "2023-01-15",
                    "2023-01-20",
                    "2023-02-10",
                    "2023-02-25",
                    "2023-03-05",
                ]
            ),
            "category": ["A", "B", "A", "B", "A"],
            "subcategory": ["X", "Y", "X", "Y", "X"],
            "value": [10, 20, 30, 40, 50],
        }
    )

    print("原始数据 ->")
    print(df)

    # 1. 按 Grouper 分组 - 时间序列按月分组
    print("\n按月分组 (freq='M') ->")
    monthly = df.groupby(pd.Grouper(key="date", freq="M"))["value"].sum()
    print(monthly)

    # 2. 按 Grouper 分组 - 按季度分组
    print("\n按季度分组 (freq='Q') ->")
    quarterly = df.groupby(pd.Grouper(key="date", freq="Q"))["value"].sum()
    print(quarterly)

    # 3. 按 Grouper 分组 - 按周分组
    print("\n按周分组 (freq='W') ->")
    weekly = df.groupby(pd.Grouper(key="date", freq="W"))["value"].sum()
    print(weekly)

    # 4. 多级分组 - Grouper + 列名
    print("\n多级分组 (date按月 + category) ->")
    multi = df.groupby(
        [pd.Grouper(key="date", freq="M"), "category"]
    )["value"].sum()
    print(multi)

    # 5. 多级分组 - 两个 Grouper
    print("\n多级分组 (两个列都按月) ->")
    df["date2"] = df["date"] + pd.Timedelta(days=15)
    multi_grouper = df.groupby(
        [pd.Grouper(key="date", freq="M"), pd.Grouper(key="date2", freq="M")]
    )["value"].sum()
    print(multi_grouper)

    # 6. Grouper with level - 用于 MultiIndex
    print("\nGrouper with level ->")
    df_indexed = df.set_index("date")
    by_level = df_indexed.groupby(pd.Grouper(freq="M"))["value"].sum()
    print(by_level)

    # 7. Grouper + sort 参数
    print("\nGrouper with sort=False ->")
    unsorted = df.sort_values("value", ascending=False)
    grouped_unsorted = unsorted.groupby(
        pd.Grouper(key="date", freq="M", sort=False)
    )["value"].sum()
    print(grouped_unsorted)

    # 8. Grouper + dropna
    df_with_na = df.copy()
    df_with_na.loc[1, "date"] = pd.NaT
    print("\nGrouper with dropna=False ->")
    grouped_na = df_with_na.groupby(
        pd.Grouper(key="date", freq="M", dropna=False)
    )["value"].sum()
    print(grouped_na)

    # 9. Grouper 用于时间窗口
    print("\n按5天时间窗口分组 ->")
    window = df.groupby(pd.Grouper(key="date", freq="5D"))["value"].sum()
    print(window)

    # 10. 多个 Grouper 组合
    print("\n多个 Grouper (月+category) agg 多种统计 ->")
    result = df.groupby(
        [pd.Grouper(key="date", freq="M"), "category"]
    ).agg(
        total=("value", "sum"),
        mean=("value", "mean"),
        count=("value", "count"),
    )
    print(result)


if __name__ == "__main__":
    main()