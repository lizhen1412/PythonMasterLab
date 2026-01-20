#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 15：shift 与 pct_change。

题目：
给定 Series，返回包含 shift 与 pct_change 的 DataFrame。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/15_shift_pct_change.py
"""

from __future__ import annotations

import pandas as pd


def build_shift_pct(s: pd.Series) -> pd.DataFrame:
    return pd.DataFrame({"shift": s.shift(1), "pct_change": s.pct_change()})


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
    s = pd.Series([10, 20, 30], name="value")
    result = build_shift_pct(s)
    expected = pd.DataFrame(
        {
            "shift": [float("nan"), 10.0, 20.0],
            "pct_change": [float("nan"), 1.0, 0.5],
        }
    )
    check_df("shift_pct_change", result, expected)


if __name__ == "__main__":
    main()
