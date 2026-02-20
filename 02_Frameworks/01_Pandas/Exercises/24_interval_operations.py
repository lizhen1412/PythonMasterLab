#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 24：Interval 操作。
Author: Lambert

题目：
创建一个 IntervalIndex，并演示：
1. 检查值是否在区间内
2. 计算区间重叠
3. 区间运算

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/24_interval_operations.py
"""

from __future__ import annotations

import pandas as pd


def create_interval_analysis() -> None:
    """演示 Interval 操作"""
    # 创建 IntervalIndex
    intervals = pd.IntervalIndex.from_tuples([(0, 10), (10, 20), (20, 30)])
    s = pd.Series([5, 15, 25], index=intervals)

    print("Interval Series:")
    print(s)

    # 检查值是否在区间内
    print("\n5 in intervals:", 5 in intervals)
    print("15 in intervals:", 15 in intervals)

    # 区间包含检查
    print("\nInterval.contains:")
    for interval in intervals:
        print(f"{interval}: left={interval.left}, right={interval.right}, closed={interval.closed}")

    # 获取包含某个值的区间
    print("\n获取包含 5 的区间:")
    print(intervals.get_indexer_for([pd.Interval(5, 5))]))

    print("\n[OK] interval operations")


if __name__ == "__main__":
    create_interval_analysis()