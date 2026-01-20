#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 44：小项目——从 CSV 到报表。

运行：
    python3 02_Frameworks/01_Pandas/44_mini_project_sales.py
"""

from __future__ import annotations

from io import StringIO

import pandas as pd


def main() -> None:
    users_csv = """user_id,name,city
1, Alice ,Beijing
2,Bob,Shanghai
3,Cathy,Beijing
"""
    orders_csv = """order_id,user_id,qty,price,order_time
1001,1,2,10.5,2024-01-01 10:00
1002,1,1,20,2024-01-03 09:00
1003,2,3,5,2024-02-01 15:30
1004,3,1,30,2024-02-02 10:00
"""

    users = pd.read_csv(StringIO(users_csv))
    orders = pd.read_csv(StringIO(orders_csv))

    print("原始 users ->")
    print(users)
    print("\n原始 orders ->")
    print(orders)

    users["name"] = users["name"].str.strip()
    users["city"] = users["city"].str.strip()
    orders["order_time"] = pd.to_datetime(orders["order_time"])
    orders["total"] = orders["qty"] * orders["price"]

    print("\n清洗后的 users ->")
    print(users)
    print("\n订单加总额 ->")
    print(orders[["order_id", "user_id", "total", "order_time"]])

    merged = orders.merge(users, on="user_id", how="left")
    merged["month"] = merged["order_time"].dt.to_period("M").astype(str)

    summary = (
        merged.groupby(["name", "month"])["total"]
        .sum()
        .reset_index()
        .sort_values(["name", "month"])
    )
    print("\n汇总明细 ->")
    print(summary)

    report = summary.pivot_table(
        index="name",
        columns="month",
        values="total",
        aggfunc="sum",
        fill_value=0,
    )
    print("\n报表（name x month）->")
    print(report)

    buffer = StringIO()
    summary.to_csv(buffer, index=False)
    print("\n导出 CSV 文本 ->")
    print(buffer.getvalue())


if __name__ == "__main__":
    main()
