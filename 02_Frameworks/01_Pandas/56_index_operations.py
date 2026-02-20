#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 56：索引运算。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/56_index_operations.py

知识点：
- union: 索引并集
- intersection: 索引导交集
- difference: 索引导差集
- symmetric_difference: 索引导对称差
- 索引比较
- 索引唯一性
- 索引重复检测
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. 索引运算 - union / intersection / difference / symmetric_difference")
    print("=" * 70)

    idx1 = pd.Index([1, 2, 3, 4, 5])
    idx2 = pd.Index([3, 4, 5, 6, 7])

    print("idx1:", idx1.tolist())
    print("idx2:", idx2.tolist())

    print("\n1.1 union - 并集")
    print("-" * 70)
    idx_union = idx1.union(idx2)
    print(f"idx1.union(idx2) -> {idx_union.tolist()}")

    idx_union_sorted = idx1.union(idx2, sort=False)
    print(f"idx1.union(idx2, sort=False) -> {idx_union_sorted.tolist()}")

    # 多个索引的并集
    idx3 = pd.Index([5, 6, 8])
    idx_multi_union = idx1.union([idx2, idx3])
    print(f"idx1.union([idx2, idx3]) -> {idx_multi_union.tolist()}")

    print("\n1.2 intersection - 交集")
    print("-" * 70)
    idx_intersect = idx1.intersection(idx2)
    print(f"idx1.intersection(idx2) -> {idx_intersect.tolist()}")

    idx_intersect_sorted = idx1.intersection(idx2, sort=False)
    print(f"idx1.intersection(idx2, sort=False) -> {idx_intersect_sorted.tolist()}")

    print("\n1.3 difference - 差集")
    print("-" * 70)
    idx_diff = idx1.difference(idx2)
    print(f"idx1.difference(idx2) -> {idx_diff.tolist()}")
    print("（在 idx1 但不在 idx2 中的元素）")

    idx_diff2 = idx2.difference(idx1)
    print(f"idx2.difference(idx1) -> {idx_diff2.tolist()}")
    print("（在 idx2 但不在 idx1 中的元素）")

    print("\n1.4 symmetric_difference - 对称差")
    print("-" * 70)
    idx_symdiff = idx1.symmetric_difference(idx2)
    print(f"idx1.symmetric_difference(idx2) -> {idx_symdiff.tolist()}")
    print("（在任一索引中但不同时在两个索引中的元素）")

    print("\n" + "=" * 70)
    print("2. 字符串索引的集合运算")
    print("=" * 70)

    str_idx1 = pd.Index(["apple", "banana", "cherry", "date"])
    str_idx2 = pd.Index(["banana", "date", "elderberry", "fig"])

    print("str_idx1:", str_idx1.tolist())
    print("str_idx2:", str_idx2.tolist())

    print(f"\nunion -> {str_idx1.union(str_idx2).tolist()}")
    print(f"intersection -> {str_idx1.intersection(str_idx2).tolist()}")
    print(f"difference -> {str_idx1.difference(str_idx2).tolist()}")
    print(f"symmetric_difference -> {str_idx1.symmetric_difference(str_idx2).tolist()}")

    print("\n" + "=" * 70)
    print("3. 索引运算符（|, &, -, ^）")
    print("=" * 70)

    print("注意：索引支持集合运算符，但两边必须都是 Index 对象")
    print("-" * 70)

    idx_a = pd.Index([1, 2, 3])
    idx_b = pd.Index([2, 3, 4])

    print(f"idx_a: {idx_a.tolist()}")
    print(f"idx_b: {idx_b.tolist()}")

    # 并集运算符 |
    result_or = idx_a | idx_b
    print(f"\nidx_a | idx_b (并集) -> {result_or.tolist()}")

    # 交集运算符 &
    result_and = idx_a & idx_b
    print(f"idx_a & idx_b (交集) -> {result_and.tolist()}")

    # 差集运算符 -
    result_sub = idx_a - idx_b
    print(f"idx_a - idx_b (差集) -> {result_sub.tolist()}")

    # 对称差运算符 ^
    result_xor = idx_a ^ idx_b
    print(f"idx_a ^ idx_b (对称差) -> {result_xor.tolist()}")

    print("\n" + "=" * 70)
    print("4. 索引比较")
    print("=" * 70)

    idx_compare1 = pd.Index([1, 2, 3, 4, 5])
    idx_compare2 = pd.Index([1, 2, 3, 4, 5])
    idx_compare3 = pd.Index([1, 2, 3, 4, 6])

    print(f"idx_compare1: {idx_compare1.tolist()}")
    print(f"idx_compare2: {idx_compare2.tolist()}")
    print(f"idx_compare3: {idx_compare3.tolist()}")

    print("\nidx_compare1.equals(idx_compare2) ->", idx_compare1.equals(idx_compare2))
    print("idx_compare1.equals(idx_compare3) ->", idx_compare1.equals(idx_compare3))

    print("\nidx_compare1.identical(idx_compare2) ->", idx_compare1.identical(idx_compare2))
    print("（identical 还检查对象类型和元数据）")

    # 元素级比较
    print("\n元素级比较:")
    idx_a = pd.Index([1, 2, 3])
    idx_b = pd.Index([1, 2, 4])
    print(f"idx_a: {idx_a.tolist()}")
    print(f"idx_b: {idx_b.tolist()}")
    print(f"idx_a == idx_b -> {(idx_a == idx_b).tolist()}")
    print(f"idx_a < idx_b -> {(idx_a < idx_b).tolist()}")

    print("\n" + "=" * 70)
    print("5. 索引唯一性与重复")
    print("=" * 70)

    idx_dup = pd.Index([1, 2, 2, 3, 3, 3, 4])

    print("idx_dup:", idx_dup.tolist())

    print("\n5.1 is_unique - 是否唯一")
    print("-" * 70)
    print(f"idx_dup.is_unique -> {idx_dup.is_unique}")

    idx_unique = pd.Index([1, 2, 3, 4])
    print(f"pd.Index([1,2,3,4]).is_unique -> {idx_unique.is_unique}")

    print("\n5.2 is_monotonic_increasing - 是否单调递增")
    print("-" * 70)
    print(f"idx_dup.is_monotonic_increasing -> {idx_dup.is_monotonic_increasing}")

    idx_desc = pd.Index([4, 3, 2, 1])
    print(f"pd.Index([4,3,2,1]).is_monotonic_increasing -> {idx_desc.is_monotonic_increasing}")

    print("\n5.3 is_monotonic_decreasing - 是否单调递减")
    print("-" * 70)
    print(f"pd.Index([4,3,2,1]).is_monotonic_decreasing -> {idx_desc.is_monotonic_decreasing}")

    print("\n5.4 duplicated - 检测重复")
    print("-" * 70)
    print(f"idx_dup.duplicated() -> {idx_dup.duplicated().tolist()}")
    print("True 表示重复项（保留第一次出现）")

    print(f"\nidx_dup.duplicated(keep='last') -> {idx_dup.duplicated(keep='last').tolist()}")
    print("keep='last' 保留最后一次出现")

    print(f"\nidx_dup.duplicated(keep=False) -> {idx_dup.duplicated(keep=False).tolist()}")
    print("keep=False 标记所有重复项")

    print("\n5.5 unique - 获取唯一值")
    print("-" * 70)
    print(f"idx_dup.unique() -> {idx_dup.unique().tolist()}")

    print("\n5.6 drop_duplicates - 删除重复")
    print("-" * 70)
    print(f"idx_dup.drop_duplicates() -> {idx_dup.drop_duplicates().tolist()}")

    print(f"\nidx_dup.drop_duplicates(keep='last') -> {idx_dup.drop_duplicates(keep='last').tolist()}")

    print("\n" + "=" * 70)
    print("6. 索引包含检查")
    print("=" * 70)

    idx_check = pd.Index([1, 2, 3, 4, 5])

    print(f"idx_check: {idx_check.tolist()}")

    print("\n6.1 in 运算符")
    print("-" * 70)
    print(f"3 in idx_check -> {3 in idx_check}")
    print(f"6 in idx_check -> {6 in idx_check}")

    print("\n6.2 isin 方法")
    print("-" * 70)
    print(f"idx_check.isin([2, 4, 6]) -> {idx_check.isin([2, 4, 6]).tolist()}")

    # 字符串索引
    str_idx = pd.Index(["apple", "banana", "cherry"])
    print(f"\nstr_idx: {str_idx.tolist()}")
    print(f"str_idx.isin(['apple', 'date']) -> {str_idx.isin(['apple', 'date']).tolist()}")

    print("\n" + "=" * 70)
    print("7. 索引的其他操作")
    print("=" * 70)

    idx_ops = pd.Index([1, 2, 3, 4, 5])

    print(f"原始索引: {idx_ops.tolist()}")

    print("\n7.1 append - 追加索引")
    print("-" * 70)
    idx_to_append = pd.Index([6, 7])
    idx_appended = idx_ops.append(idx_to_append)
    print(f"idx_ops.append(pd.Index([6, 7])) -> {idx_appended.tolist()}")

    print("\n7.2 delete - 删除指定位置")
    print("-" * 70)
    idx_deleted = idx_ops.delete(2)
    print(f"idx_ops.delete(2) -> {idx_deleted.tolist()}")
    print("（删除位置 2 的元素，即 3）")

    print("\n7.3 insert - 插入元素")
    print("-" * 70)
    idx_inserted = idx_ops.insert(2, 99)
    print(f"idx_ops.insert(2, 99) -> {idx_inserted.tolist()}")

    print("\n7.4 drop - 删除指定值")
    print("-" * 70)
    idx_dropped = idx_ops.drop([2, 4])
    print(f"idx_ops.drop([2, 4]) -> {idx_dropped.tolist()}")

    print("\n" + "=" * 70)
    print("8. 在 DataFrame 中应用索引运算")
    print("=" * 70)

    df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=["x", "y", "z"])
    df2 = pd.DataFrame({"A": [10, 20, 30], "B": [40, 50, 60]}, index=["y", "z", "w"])

    print("df1:")
    print(df1)
    print("\ndf2:")
    print(df2)

    print("\n8.1 使用索引运算合并数据")
    print("-" * 70)

    # 只保留两个索引都有的行
    common_idx = df1.index.intersection(df2.index)
    print("df1.index.intersection(df2.index) ->", common_idx.tolist())

    df_common = df1.loc[common_idx]
    print("\ndf1.loc[common_idx] ->")
    print(df_common)

    # 保留任一索引的行
    all_idx = df1.index.union(df2.index)
    print("\ndf1.index.union(df2.index) ->", all_idx.tolist())

    # 只在 df1 中的索引
    df1_only_idx = df1.index.difference(df2.index)
    print("\ndf1.index.difference(df2.index) ->", df1_only_idx.tolist())

    print("\n8.2 检查索引一致性")
    print("-" * 70)

    print(f"df1.index.equals(df2.index) -> {df1.index.equals(df2.index)}")

    print(f"df1.index.intersection(df2.index).equals(df2.index.intersection(df1.index)) -> True")

    print("\n" + "=" * 70)
    print("9. MultiIndex 的索引运算")
    print("=" * 70)

    midx1 = pd.MultiIndex.from_tuples([("A", 1), ("A", 2), ("B", 1)])
    midx2 = pd.MultiIndex.from_tuples([("A", 2), ("B", 1), ("B", 2)])

    print("midx1:", midx1.tolist())
    print("midx2:", midx2.tolist())

    print("\nmidx1.union(midx2) ->")
    print(midx1.union(midx2).tolist())

    print("\nmidx1.intersection(midx2) ->")
    print(midx1.intersection(midx2).tolist())

    print("\nmidx1.difference(midx2) ->")
    print(midx1.difference(midx2).tolist())

    print("\n" + "=" * 70)
    print("10. 实际应用示例")
    print("=" * 70)

    # 示例 1: 合并多个数据源时确保索引一致
    print("\n示例 1: 合并多个时间段的数据")
    dates_jan = pd.date_range("2024-01-01", "2024-01-10")
    dates_feb = pd.date_range("2024-02-01", "2024-02-10")

    df_jan = pd.DataFrame({"sales": np.random.randint(10, 100, len(dates_jan))}, index=dates_jan)
    df_feb = pd.DataFrame({"sales": np.random.randint(10, 100, len(dates_feb))}, index=dates_feb)

    print("1月数据索引:", df_jan.index[:3].tolist(), "...")
    print("2月数据索引:", df_feb.index[:3].tolist(), "...")

    # 合并所有日期
    all_dates = df_jan.index.union(df_feb.index)
    print(f"\n合并后的日期范围: {all_dates.min()} 到 {all_dates.max()}, 共 {len(all_dates)} 天")

    # 示例 2: 找出新增/丢失的数据项
    print("\n示例 2: 比较两个版本的产品列表")
    products_v1 = pd.Index(["A", "B", "C", "D", "E"])
    products_v2 = pd.Index(["B", "C", "E", "F", "G"])

    print(f"v1 产品: {products_v1.tolist()}")
    print(f"v2 产品: {products_v2.tolist()}")

    new_products = products_v2.difference(products_v1)
    removed_products = products_v1.difference(products_v2)
    common_products = products_v1.intersection(products_v2)

    print(f"\n新增产品: {new_products.tolist()}")
    print(f"移除产品: {removed_products.tolist()}")
    print(f"保留产品: {common_products.tolist()}")

    # 示例 3: 数据对齐时的索引处理
    print("\n示例 3: 确保两个 DataFrame 有相同的行索引")
    df_a = pd.DataFrame({"value": [1, 2, 3, 4]}, index=["a", "b", "c", "d"])
    df_b = pd.DataFrame({"value": [10, 20, 30]}, index=["b", "c", "e"])

    print("df_a:")
    print(df_a)
    print("\ndf_b:")
    print(df_b)

    # 方法 1: 只保留共同的索引
    common_idx = df_a.index.intersection(df_b.index)
    df_a_aligned = df_a.loc[common_idx]
    df_b_aligned = df_b.loc[common_idx]
    print("\n对齐到共同索引:")
    print(df_a_aligned)
    print(df_b_aligned)

    # 方法 2: 保留所有索引，填充 NaN
    all_idx = df_a.index.union(df_b.index)
    df_a_reindexed = df_a.reindex(all_idx)
    df_b_reindexed = df_b.reindex(all_idx)
    print("\n重新索引到并集（填充 NaN）:")
    print(df_a_reindexed)
    print(df_b_reindexed)

    # 示例 4: 检查数据完整性
    print("\n示例 4: 检查数据是否有缺失的日期")
    expected_dates = pd.date_range("2024-01-01", "2024-01-10")
    actual_dates = pd.DatetimeIndex(
        ["2024-01-01", "2024-01-02", "2024-01-04", "2024-01-05", "2024-01-07", "2024-01-08", "2024-01-10"]
    )

    missing_dates = expected_dates.difference(actual_dates)
    print(f"预期日期: {len(expected_dates)} 天")
    print(f"实际日期: {len(actual_dates)} 天")
    print(f"缺失日期: {missing_dates.tolist()}")

    # 示例 5: 索引排序
    print("\n示例 5: 索引排序")
    unsorted_idx = pd.Index([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"未排序索引: {unsorted_idx.tolist()}")

    sorted_idx = unsorted_idx.sort_values()
    print(f"排序后索引: {sorted_idx.tolist()}")

    # 去重并排序
    unique_sorted_idx = unsorted_idx.unique().sort_values()
    print(f"去重并排序: {unique_sorted_idx.tolist()}")


if __name__ == "__main__":
    main()