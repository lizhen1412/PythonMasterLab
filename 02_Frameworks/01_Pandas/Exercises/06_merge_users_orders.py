#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：合并表（merge）。

题目：
给定 users 与 orders 两张表，合并得到含用户姓名的订单表。
要求：以 orders 为主表（left join）。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/06_merge_users_orders.py
"""

from __future__ import annotations

import pandas as pd


def merge_users_orders(users: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(orders, users, on="user_id", how="left")


def check_df(label: str, got: pd.DataFrame, expected: pd.DataFrame) -> None:
    ok = got.equals(expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->")
        print(got)
        print("expected ->")
        print(expected)


def main() -> None:
    users = pd.DataFrame(
        {
            "user_id": [1, 2, 3],
            "name": ["Alice", "Bob", "Cathy"],
        }
    )
    orders = pd.DataFrame(
        {
            "order_id": [101, 102, 103],
            "user_id": [1, 1, 2],
        }
    )
    result = merge_users_orders(users, orders)
    expected = pd.DataFrame(
        {
            "order_id": [101, 102, 103],
            "user_id": [1, 1, 2],
            "name": ["Alice", "Alice", "Bob"],
        }
    )
    check_df("merge_left", result, expected)


if __name__ == "__main__":
    main()
