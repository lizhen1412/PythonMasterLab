#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 12：独热编码（get_dummies）。

题目：
给定颜色列，生成带前缀的独热编码表。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/12_get_dummies_basic.py
"""

from __future__ import annotations

import pandas as pd


def encode_colors(s: pd.Series) -> pd.DataFrame:
    return pd.get_dummies(s, prefix="color", dtype=int)


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
    s = pd.Series(["red", "blue", "red"])
    result = encode_colors(s)
    expected = pd.DataFrame(
        {
            "color_blue": [0, 1, 0],
            "color_red": [1, 0, 1],
        }
    )
    check_df("get_dummies", result, expected)


if __name__ == "__main__":
    main()
