#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 16：json_normalize。
Author: Lambert

题目：
将嵌套 JSON 展开为扁平表。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/16_json_normalize_basic.py
"""

from __future__ import annotations

import pandas as pd


def normalize_orders(data: list[dict]) -> pd.DataFrame:
    return pd.json_normalize(data, record_path="items", meta=[["user", "id"], ["user", "name"]])


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
    data = [
        {
            "user": {"id": 1, "name": "Alice"},
            "items": [{"product": "P1", "qty": 2}],
        },
        {
            "user": {"id": 2, "name": "Bob"},
            "items": [{"product": "P2", "qty": 1}, {"product": "P3", "qty": 2}],
        },
    ]
    result = normalize_orders(data)
    expected = pd.DataFrame(
        {
            "product": ["P1", "P2", "P3"],
            "qty": [2, 1, 2],
            "user.id": [1, 2, 2],
            "user.name": ["Alice", "Bob", "Bob"],
        }
    )
    check_df("json_normalize", result, expected)


if __name__ == "__main__":
    main()