#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：合并 / 连接 / 拼接。

运行：
    python3 02_Frameworks/01_Pandas/17_merge_join_concat.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    users = pd.DataFrame({"user_id": [1, 2], "name": ["Alice", "Bob"]})
    orders = pd.DataFrame({"user_id": [1, 1, 3], "amount": [100, 50, 200]})

    print("merge (inner) ->")
    print(users.merge(orders, on="user_id", how="inner"))

    print("\nmerge (left) ->")
    print(users.merge(orders, on="user_id", how="left"))

    users = users.set_index("user_id")
    orders = orders.set_index("user_id")
    print("\njoin ->")
    print(users.join(orders, how="left"))

    print("\nconcat ->")
    df1 = pd.DataFrame({"A": [1, 2]})
    df2 = pd.DataFrame({"A": [3, 4]})
    print(pd.concat([df1, df2], ignore_index=True))


if __name__ == "__main__":
    main()
