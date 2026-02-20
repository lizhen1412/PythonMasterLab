#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：字符串清洗（str.*）。
Author: Lambert

题目：
给定一个字符串 Series：
- 去掉首尾空白
- 统一小写
- 连续空白压缩为一个空格

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/09_string_cleaning.py
"""

from __future__ import annotations

import pandas as pd


def clean_text(s: pd.Series) -> pd.Series:
    cleaned = s.astype("string").str.strip().str.lower()
    return cleaned.str.replace(r"\s+", " ", regex=True)


def check_series(label: str, got: pd.Series, expected: pd.Series) -> None:
    ok = got.equals(expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->")
        print(got)
        print("expected ->")
        print(expected)


def main() -> None:
    s = pd.Series(["  Alice  ", "BOB", None, "  A   b  "])
    result = clean_text(s)
    expected = pd.Series(["alice", "bob", pd.NA, "a b"], dtype="string")
    check_series("clean_text", result, expected)


if __name__ == "__main__":
    main()