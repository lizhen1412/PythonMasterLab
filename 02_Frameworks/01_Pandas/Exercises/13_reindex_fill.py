#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 13：reindex + fill_value。

题目：
将 Series 按指定索引重排，不存在的用 0 填充。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/13_reindex_fill.py
"""

from __future__ import annotations

import pandas as pd


def reindex_fill(s: pd.Series, new_index: list[str]) -> pd.Series:
    return s.reindex(new_index, fill_value=0)


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
    s = pd.Series([10, 20], index=["a", "b"], name="value")
    result = reindex_fill(s, ["b", "c", "a"])
    expected = pd.Series([20, 0, 10], index=["b", "c", "a"], name="value")
    check_series("reindex_fill", result, expected)


if __name__ == "__main__":
    main()
