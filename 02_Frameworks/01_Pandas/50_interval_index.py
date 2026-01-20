#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 50：IntervalIndex（区间索引）。

运行：
    python3 02_Frameworks/01_Pandas/50_interval_index.py

知识点：
- pd.Interval：创建单个区间
- pd.IntervalIndex：创建区间索引
- 区间类型：left/right/both/neither
- 区间运算： overlaps / contains / overlap
- 应用场景：年龄分组、评分区间、价格范围、时间窗口
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    print("=" * 60)
    print("1. Interval 基础")
    print("=" * 60)

    # 创建区间（默认右闭左开）
    interval1 = pd.Interval(0, 5)
    print(f"Interval(0, 5) -> {interval1}")
    print(f"closed 默认 'right' -> {interval1.closed}")

    # 指定闭合方式
    interval_left = pd.Interval(0, 5, closed="left")
    interval_both = pd.Interval(0, 5, closed="both")
    interval_neither = pd.Interval(0, 5, closed="neither")
    print(f"\nclosed='left' -> {interval_left}")
    print(f"closed='both' -> {interval_both}")
    print(f"closed='neither' -> {interval_neither}")

    # 区间属性
    print(f"\ninterval1.left -> {interval1.left}")
    print(f"interval1.right -> {interval1.right}")
    print(f"interval1.closed -> {interval1.closed}")
    print(f"interval1.length -> {interval1.length}")
    print(f"interval1.mid -> {interval1.mid}")

    # 区间运算
    print(f"\n3 in interval1 -> {3 in interval1}")
    print(f"0 in interval1 -> {0 in interval1}")  # 左开，所以 False
    print(f"5 in interval1 -> {5 in interval1}")  # 右闭，所以 True

    print("\n" + "=" * 60)
    print("2. IntervalIndex 创建")
    print("=" * 60)

    # 从列表创建
    idx = pd.IntervalIndex.from_tuples([(0, 1), (1, 2), (2, 3)])
    print(f"from_tuples ->\n{idx}")

    # from_breaks（分段）
    idx_breaks = pd.IntervalIndex.from_breaks([0, 18, 35, 50, 100])
    print(f"\nfrom_breaks [0, 18, 35, 50, 100] ->\n{idx_breaks}")

    # from_arrays（左右边界数组）
    idx_arrays = pd.IntervalIndex.from_arrays(left=[0, 10, 20], right=[10, 20, 30])
    print(f"\nfrom_arrays ->\n{idx_arrays}")

    print("\n" + "=" * 60)
    print("3. IntervalIndex 在 Series/DataFrame 中使用")
    print("=" * 60)

    # 年龄分组示例
    age_groups = pd.IntervalIndex.from_breaks([0, 18, 35, 50, 65, 100])
    ages = pd.Series(
        [5, 12, 18, 25, 30, 40, 55, 70],
        index=pd.interval_range(start=0, end=100, periods=8),
    )
    print("年龄区间索引 ->")
    print(ages)

    # 使用区间索引的 DataFrame
    df = pd.DataFrame(
        {"population": [100, 200, 300, 150, 80]},
        index=pd.IntervalIndex.from_tuples([(0, 18), (18, 35), (35, 50), (50, 65), (65, 100)]),
    )
    df.index.name = "age_group"
    print("\n按年龄分组的人口数据 ->")
    print(df)

    print("\n" + "=" * 60)
    print("4. 区间索引的选择与查询")
    print("=" * 60)

    # 精确匹配
    print(f"df.loc[pd.Interval(0, 18)] ->\n{df.loc[pd.Interval(0, 18)]}")

    # 使用 .left 和 .right 查询
    print(f"\ndf.iloc[0] ->\n{df.iloc[0]}")

    # 检查值是否在区间内
    value = 25
    for idx in df.index:
        if value in idx:
            print(f"\n{value} 在区间 {idx} 中")

    print("\n" + "=" * 60)
    print("5. 区间运算方法")
    print("=" * 60)

    interval_a = pd.Interval(0, 10)
    interval_b = pd.Interval(5, 15)
    interval_c = pd.Interval(20, 30)

    print(f"interval_a: {interval_a}")
    print(f"interval_b: {interval_b}")
    print(f"interval_c: {interval_c}")

    # overlaps - 检查重叠
    print(f"\ninterval_a.overlaps(interval_b) -> {interval_a.overlaps(interval_b)}")
    print(f"interval_a.overlaps(interval_c) -> {interval_a.overlaps(interval_c)}")

    print("\n" + "=" * 60)
    print("6. pd.cut 返回 IntervalIndex")
    print("=" * 60)

    scores = pd.Series([55, 62, 78, 85, 92, 45, 70])
    bins = [0, 60, 70, 80, 90, 100]
    labels = ["F", "D", "C", "B", "A"]

    # cut 返回 Categorical，categories 是 IntervalIndex
    result = pd.cut(scores, bins=bins, labels=labels, right=False)
    print("成绩分段 ->")
    print(result)

    print("\n区间边界 ->")
    print(result.cat.categories)

    print("\n" + "=" * 60)
    print("7. 实际应用：价格区间统计")
    print("=" * 60)

    # 商品价格区间统计
    products = pd.DataFrame(
        {
            "product": ["A", "B", "C", "D", "E", "F", "G"],
            "price": [15, 25, 45, 85, 120, 180, 250],
        }
    )

    # 创建价格区间
    price_bins = [0, 50, 100, 200, 500]
    price_labels = ["低价", "中价", "高价", "奢华"]
    products["price_range"] = pd.cut(products["price"], bins=price_bins, labels=price_labels)

    print("商品价格区间 ->")
    print(products)

    # 按价格区间统计
    print("\n按价格区间统计 ->")
    print(products["price_range"].value_counts().sort_index())

    print("\n" + "=" * 60)
    print("8. 区间索引的高级操作")
    print("=" * 60)

    # is_empty - 检查空区间
    empty_interval = pd.Interval(5, 5, closed="right")
    normal_interval = pd.Interval(0, 10)
    print(f"空区间: {empty_interval}, is_empty -> {empty_interval.is_empty}")
    print(f"普通区间: {normal_interval}, is_empty -> {normal_interval.is_empty}")

    # IntervalIndex 的属性
    idx = pd.IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5)])
    print(f"\nIntervalIndex -> {idx}")
    print(f"is_non_overlapping_monotonic -> {idx.is_non_overlapping_monotonic}")
    print(f"has_duplicates -> {idx.has_duplicates}")

    # 重叠检测
    overlapping_idx = pd.IntervalIndex.from_tuples([(0, 3), (2, 5), (6, 8)])
    print(f"\n重叠的 IntervalIndex -> {overlapping_idx}")
    print(f"is_non_overlapping_monotonic -> {overlapping_idx.is_non_overlapping_monotonic}")

    print("\n" + "=" * 60)
    print("9. 时间区间示例")
    print("=" * 60)

    # 使用 Timestamp 的区间
    import pandas as pd

    start = pd.Timestamp("2024-01-01")
    end = pd.Timestamp("2024-01-31")

    time_interval = pd.Interval(start, end)
    print(f"时间区间: {time_interval}")

    test_date = pd.Timestamp("2024-01-15")
    print(f"{test_date} 在区间内: {test_date in time_interval}")

    print("\n" + "=" * 60)
    print("10. get_indexer_for - 查找位置")
    print("=" * 60)

    intervals = pd.IntervalIndex.from_tuples([(0, 10), (10, 20), (20, 30)])
    print(f"区间索引: {intervals}")

    # 查找值对应的区间位置
    values = pd.Index([5, 15, 25])
    positions = intervals.get_indexer_for(values)
    print(f"\n值 {values.tolist()} 对应的位置: {positions}")

    # 不在区间内的值
    out_values = pd.Index([35, -5])
    out_positions = intervals.get_indexer_for(out_values)
    print(f"值 {out_values.tolist()} 对应的位置: {out_positions}")  # -1 表示不在


if __name__ == "__main__":
    main()
