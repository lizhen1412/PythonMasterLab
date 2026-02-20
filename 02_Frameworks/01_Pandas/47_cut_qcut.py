#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 47：分箱 cut/qcut（成绩分档/分位数）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/47_cut_qcut.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    scores = pd.Series([55, 62, 68, 74, 81, 88, 92, 99], name="score")
    print("原始分数 ->")
    print(scores.tolist())

    bins = [0, 60, 70, 80, 90, 100]
    labels = ["F", "D", "C", "B", "A"]

    print("\ncut 固定分档 ->")
    level = pd.cut(scores, bins=bins, labels=labels, include_lowest=True)
    print(level)

    print("\nqcut 分位数 ->")
    quantile = pd.qcut(scores, q=4, labels=["Q1", "Q2", "Q3", "Q4"])
    print(quantile)

    print("\n分档统计 ->")
    print(level.value_counts().sort_index())


if __name__ == "__main__":
    main()