#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 52：Sparse Arrays - 稀疏数组。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/52_sparse_arrays.py

稀疏数组是一种高效存储大量重复值（通常是零或 NaN）的数据结构。
当数据中有很多重复值时，使用稀疏数组可以大幅减少内存占用。

本节演示：
1. 创建稀疏数组 (SparseDtype)
2. 稀疏数组的基本操作
3. 稀疏 DataFrame
4. 内存效率对比
5. 稀疏数组的方法和属性
6. 密集数组与稀疏数组互转
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. 创建稀疏数组")
    print("=" * 60)

    # 方法1: 从数组创建稀疏数组
    arr = pd.arrays.SparseArray([0, 0, 0, 1, 0, 0, 2, 0, 0])
    print("\n稀疏数组:")
    print(arr)
    print(f"类型: {type(arr)}")
    print(f"dtype: {arr.dtype}")
    print(f"填充值 (fill_value): {arr.fill_value}")
    print(f"非零值数量 (npoints): {arr.npoints}")
    print(f"稀疏度: {arr.sparsity:.2%}")

    # 方法2: 指定不同的填充值
    arr_nan = pd.arrays.SparseArray([1, np.nan, 2, np.nan, 3, np.nan])
    print("\n以 NaN 为填充值的稀疏数组:")
    print(arr_nan)
    print(f"填充值: {arr_nan.fill_value}")

    # 方法3: 从 Series 创建
    s = pd.Series([0, 0, 0, 5, 0, 0, 0, 8], dtype="Sparse[int64]")
    print("\n稀疏 Series:")
    print(s)
    print(f"dtype: {s.dtype}")

    print("\n" + "=" * 60)
    print("2. 稀疏 DataFrame")
    print("=" * 60)

    # 创建稀疏 DataFrame
    df_sparse = pd.DataFrame(
        {
            "A": pd.arrays.SparseArray([0, 0, 1, 0, 0, 2]),
            "B": pd.arrays.SparseArray([0, 3, 0, 0, 0, 0]),
            "C": [0, 0, 0, 0, 4, 0],  # 会自动转换
        }
    )
    df_sparse = df_sparse.astype("Sparse[int64]")
    print("\n稀疏 DataFrame:")
    print(df_sparse)
    print(f"\ndtypes:")
    print(df_sparse.dtypes)

    print("\n" + "=" * 60)
    print("3. 内存效率对比")
    print("=" * 60)

    # 创建一个包含大量零的数组
    size = 100000
    dense_arr = np.zeros(size)
    dense_arr[::1000] = np.random.randint(1, 100, size=size // 1000)

    # 密集版本
    df_dense = pd.DataFrame({"values": dense_arr})
    print(f"\n密集 DataFrame 内存使用:")
    print(f"  {df_dense.memory_usage(deep=True).sum() / 1024:.2f} KB")

    # 稀疏版本
    df_sparse_mem = pd.DataFrame({"values": pd.arrays.SparseArray(dense_arr)})
    print(f"\n稀疏 DataFrame 内存使用:")
    print(f"  {df_sparse_mem.memory_usage(deep=True).sum() / 1024:.2f} KB")

    # 计算节省比例
    dense_mem = df_dense.memory_usage(deep=True).sum()
    sparse_mem = df_sparse_mem.memory_usage(deep=True).sum()
    savings = (1 - sparse_mem / dense_mem) * 100
    print(f"\n内存节省: {savings:.1f}%")

    print("\n" + "=" * 60)
    print("4. 稀疏数组操作")
    print("=" * 60)

    arr1 = pd.arrays.SparseArray([1, 0, 2, 0, 0, 3])
    arr2 = pd.arrays.SparseArray([0, 1, 0, 2, 0, 0])

    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")

    # 算术运算
    print(f"\narr1 + arr2: {arr1 + arr2}")
    print(f"arr1 * 2: {arr1 * 2}")

    # 比较运算
    print(f"arr1 > 1: {arr1 > 1}")

    # 统计运算
    print(f"sum: {arr1.sum()}")
    print(f"mean: {arr1.mean():.2f}")
    print(f"max: {arr1.max()}")

    print("\n" + "=" * 60)
    print("5. 密集与稀疏互转")
    print("=" * 60)

    original = np.array([0, 0, 1, 0, 0, 0, 2, 0, 0, 0])

    # 密集 -> 稀疏
    sparse_arr = pd.arrays.SparseArray(original)
    print(f"\n原始数组: {original}")
    print(f"转换为稀疏: {sparse_arr}")

    # 稀疏 -> 密集
    dense_from_sparse = sparse_arr.to_dense()
    print(f"转回密集: {dense_from_sparse}")

    # 从 sparse dtype 转换
    s_sparse = pd.Series([0, 0, 1, 0, 0, 2], dtype="Sparse[int]")
    s_dense = s_sparse.sparse.to_dense()
    print(f"\n稀疏 Series:\n{s_sparse}")
    print(f"\n密集 Series:\n{s_dense}")

    print("\n" + "=" * 60)
    print("6. 稀疏数组属性详解")
    print("=" * 60)

    arr = pd.arrays.SparseArray([0, 0, 0, 1, 0, 0, 2, 0, 3, 0])
    print(f"数组: {arr}")
    print(f"\n属性:")
    print(f"  fill_value: {arr.fill_value}  # 填充值")
    print(f"  sparsity: {arr.sparsity:.2%}  # 稀疏度（0-1之间的值）")
    print(f"  npoints: {arr.npoints}  # 非填充值数量")
    print(f"  dtype: {arr.dtype}  # 数据类型")
    print(f"  size: {arr.size}  # 总元素数")

    # 访问内部存储
    print(f"\n内部存储:")
    print(f"  sparse_index: {arr.sp_index}")  # 非零值索引
    print(f"  sparse_values: {arr.sp_values}")  # 非零值

    print("\n" + "=" * 60)
    print("7. 实际应用场景")
    print("=" * 60)

    # 场景1: 推荐系统（用户-商品评分矩阵）
    print("\n场景1: 用户评分矩阵（大部分用户未评分大部分商品）")
    ratings = pd.DataFrame(
        {
            "user_id": [1, 1, 1, 2, 2, 3],
            "item_id": [101, 102, 105, 101, 103, 102],
            "rating": [5, 4, 3, 5, 2, 4],
        }
    )

    # 创建完整的评分矩阵（使用稀疏）
    all_users = [1, 2, 3]
    all_items = [101, 102, 103, 104, 105]

    rating_matrix = pd.DataFrame(0, index=all_users, columns=all_items, dtype="Sparse[int]")

    for _, row in ratings.iterrows():
        rating_matrix.loc[row["user_id"], row["item_id"]] = row["rating"]

    print("\n评分矩阵:")
    print(rating_matrix)
    print(f"\n内存使用: {rating_matrix.memory_usage(deep=True).sum() / 1024:.2f} KB")

    # 场景2: 文本特征（词袋模型）
    print("\n" + "-" * 40)
    print("\n场景2: 文本的词袋特征（大部分文档不包含大部分词）")

    vocab = ["apple", "banana", "cherry", "date", "elderberry"]
    documents = pd.DataFrame(
        {
            "doc_id": [1, 2, 3],
            "apple": pd.arrays.SparseArray([2, 0, 0]),
            "banana": pd.arrays.SparseArray([0, 1, 0]),
            "cherry": pd.arrays.SparseArray([0, 0, 3]),
            "date": pd.arrays.SparseArray([1, 0, 0]),
            "elderberry": pd.arrays.SparseArray([0, 0, 0]),
        }
    )

    print("\n文档-词频矩阵:")
    print(documents)

    print("\n" + "=" * 60)
    print("8. 稀疏数组的填充值操作")
    print("=" * 60)

    # 创建自定义填充值的稀疏数组
    arr_custom = pd.arrays.SparseArray([1, 1, 1, 2, 1, 1, 3, 1], fill_value=1)
    print(f"以 1 为填充值的稀疏数组: {arr_custom}")
    print(f"填充值: {arr_custom.fill_value}")
    print(f"非填充值数量: {arr_custom.npoints}")

    # 更改填充值
    print(f"\n将填充值改为 0:")
    arr_new_fill = arr_custom.astype(pd.SparseDtype(arr.dtype, fill_value=0))
    print(arr_new_fill)

    print("\n" + "=" * 60)
    print("9. 稀疏数组的注意事项")
    print("=" * 60)

    print("\n注意事项:")
    print("1. 稀疏数组适合填充值占比 > 70% 的数据")
    print("2. 稀疏数组不支持某些操作（如 inplace 修改）")
    print("3. 计算时可能会转换为密集数组，注意内存")
    print("4. 选择合适的填充值很重要（通常是 0 或 NaN）")

    # 演示稀疏度的影响
    print("\n稀疏度与内存效率的关系:")
    for sparsity in [0.5, 0.7, 0.9, 0.95, 0.99]:
        n = 10000
        n_nonzero = int(n * (1 - sparsity))
        arr = np.zeros(n)
        arr[:n_nonzero] = np.random.randn(n_nonzero)
        np.random.shuffle(arr)

        sparse = pd.arrays.SparseArray(arr)
        dense_mem = n * 8  # 假设 float64
        sparse_mem = sparse.npoints * 8 + sparse.npoints * 4  # 值 + 索引
        print(f"  稀疏度 {sparsity:.0%}: 密集 {dense_mem/1024:.1f}KB, "
              f"稀疏 {sparse_mem/1024:.1f}KB, "
              f"节省 {(1-sparse_mem/dense_mem)*100:.1f}%")


if __name__ == "__main__":
    main()