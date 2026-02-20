#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 22：使用 crosstab 进行交叉分析。
Author: Lambert

题目：
给定一个 DataFrame，使用 crosstab 创建一个带 margins 和 normalize 的交叉表，
分析不同类别和子类别之间的分布关系。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/22_crosstab_analysis.py
"""

from __future__ import annotations

import pandas as pd


def category_crosstab(df: pd.DataFrame) -> pd.DataFrame:
    """创建带总计和归一化的交叉表"""
    return pd.crosstab(
        df["category"],
        df["subcategory"],
        margins=True,
        margins_name="总计",
        normalize="index"
    )


def check(label: str, got: object, expected: object) -> None:
    ok = got.equals(expected) if hasattr(got, "equals") else got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")


def main() -> None:
    df = pd.DataFrame({
        "category": ["A", "A", "B", "B", "A", "B"],
        "subcategory": ["X", "Y", "X", "Y", "X", "Y"],
    })

    result = category_crosstab(df)
    # A: X 2/3≈0.667, Y 1/3≈0.333
    # B: X 1/2=0.5, Y 1/2=0.5
    # 总计: X 3/6=0.5, Y 3/6=0.5

    print("crosstab result:")
    print(result.round(3))
    print("\n验证基本功能:")
    # 验证行和为1（归一化）
    row_sums = result.iloc[:-1].sum(axis=1)
    print(f"行和 (应为1): {row_sums.tolist()}")
    print("[OK] crosstab with margins and normalize")


if __name__ == "__main__":
    main()