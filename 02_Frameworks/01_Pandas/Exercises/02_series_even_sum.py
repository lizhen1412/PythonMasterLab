#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：Series 过滤与求和（偶数求和）。

题目：
给定一个整数 Series，筛选出偶数并求和。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/02_series_even_sum.py
"""

from __future__ import annotations

import pandas as pd


def sum_even_values(s: pd.Series) -> int:
    even = s[s % 2 == 0]
    return int(even.sum())


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    s = pd.Series([1, 2, 3, 4, 5, 6])
    check("sum_even", sum_even_values(s), 12)


if __name__ == "__main__":
    main()
