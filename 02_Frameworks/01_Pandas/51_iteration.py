#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 51：迭代方法（iteritems/iterrows/itertuples）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/51_iteration.py

知识点：
- iteritems：迭代 (列名, Series) 对
- iterrows：迭代 (索引, 行) 对，返回 Series
- itertuples：迭代命名元组，最快
- 性能对比：itertuples > list comprehension > iterrows
- 最佳实践：优先使用向量化操作，避免迭代
"""

from __future__ import annotations

import pandas as pd
import time


def time_it(func, *args, **kwargs):
    """简单的计时函数"""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end - start


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy", "David"],
            "score": [88, 75, 92, 85],
            "age": [20, 21, 19, 22],
        }
    )

    print("=" * 60)
    print("原始 DataFrame")
    print("=" * 60)
    print(df)

    print("\n" + "=" * 60)
    print("1. iteritems() - 迭代列")
    print("=" * 60)

    print("iteritems() 返回 (列名, Series) 对：")
    for col_name, series in df.iteritems():
        print(f"列名: {col_name}")
        print(f"Series:\n{series}")
        print(f"类型: {type(series)}")
        print("-" * 40)

    print("\n" + "=" * 60)
    print("2. iterrows() - 迭代行")
    print("=" * 60)

    print("iterrows() 返回 (索引, Series) 对：")
    for idx, row in df.iterrows():
        print(f"索引: {idx}")
        print(f"行数据:\n{row}")
        print(f"name: {row['name']}, score: {row['score']}")
        print("-" * 40)

    print("\n警告：iterrows() 返回的 Series 是副本，修改不会影响原 DataFrame")

    print("\n" + "=" * 60)
    print("3. itertuples() - 迭代命名元组（推荐）")
    print("=" * 60)

    print("itertuples() 返回命名元组：")
    for row in df.itertuples():
        print(f"类型: {type(row)}")
        print(f"索引: {row.Index}")
        print(f"name: {row.name}, score: {row.score}, age: {row.age}")
        print(f"访问方式: row[0], row[1], row[2] -> {row[0]}, {row[1]}, {row[2]}")
        print("-" * 40)

    print("itertuples(name='CustomName') 自定义名称：")
    for row in df.itertuples(name="Person"):
        print(f"{Person.__name__}: {row}")

    print("\nitertuples(index=False) 不包含索引：")
    for row in df.itertuples(index=False):
        print(row)

    print("\n" + "=" * 60)
    print("4. 性能对比")
    print("=" * 60)

    # 创建更大的 DataFrame 进行性能测试
    large_df = pd.DataFrame(
        {
            "A": range(10000),
            "B": range(10000, 20000),
            "C": range(20000, 30000),
        }
    )

    print(f"测试 DataFrame 形状: {large_df.shape}")

    # iterrows
    def sum_iterrows(df):
        total = 0
        for _, row in df.iterrows():
            total += row["A"] + row["B"] + row["C"]
        return total

    _, iterrows_time = time_it(sum_iterrows, large_df)
    print(f"\niterrows() 耗时: {iterrows_time:.4f} 秒")

    # itertuples
    def sum_itertuples(df):
        total = 0
        for row in df.itertuples():
            total += row.A + row.B + row.C
        return total

    _, itertuples_time = time_it(sum_itertuples, large_df)
    print(f"itertuples() 耗时: {itertuples_time:.4f} 秒")

    # 向量化操作（最佳实践）
    def sum_vectorized(df):
        return df["A"].sum() + df["B"].sum() + df["C"].sum()

    _, vectorized_time = time_it(sum_vectorized, large_df)
    print(f"向量化操作 耗时: {vectorized_time:.6f} 秒")

    # 性能对比
    print(f"\n性能对比（相对于向量化）：")
    print(f"itertuples 比 iterrows 快: {iterrows_time / itertuples_time:.1f}x")
    print(f"向量化比 itertuples 快: {itertuples_time / vectorized_time:.1f}x")
    print(f"向量化比 iterrows 快: {iterrows_time / vectorized_time:.1f}x")

    print("\n" + "=" * 60)
    print("5. 迭代的常见用途示例")
    print("=" * 60)

    # 示例 1: 条件判断（不推荐，应使用向量化）
    print("示例 1: 根据多列条件创建新列")

    # 不推荐的方式（迭代）
    df_test = pd.DataFrame({"x": [1, 2, 3, 4], "y": [10, 20, 30, 40]})

    result_iter = []
    for _, row in df_test.iterrows():
        if row["x"] > 2:
            result_iter.append(row["y"] * 2)
        else:
            result_iter.append(row["y"])
    df_test["z_iter"] = result_iter
    print("迭代方式:")
    print(df_test)

    # 推荐的方式（向量化）
    df_test["z_vec"] = df_test["y"].where(df_test["x"] <= 2, df_test["y"] * 2)
    df_test = df_test.drop(columns=["z_iter"])
    print("\n向量化方式:")
    print(df_test)

    # 示例 2: 字符串拼接（迭代更清晰）
    print("\n示例 2: 复杂字符串处理")

    df_names = pd.DataFrame({"first": ["Alice", "Bob"], "last": ["Smith", "Jones"]})

    # 迭代方式（对于复杂逻辑更清晰）
    names_iter = []
    for row in df_names.itertuples():
        names_iter.append(f"{row.last}, {row.first[0]}.")
    df_names["full_name_iter"] = names_iter
    print("迭代方式:")
    print(df_names)

    # 向量化方式（也可以）
    df_names["full_name_vec"] = df_names["last"] + ", " + df_names["first"].str[0] + "."
    df_names = df_names.drop(columns=["full_name_iter"])
    print("\n向量化方式:")
    print(df_names)

    print("\n" + "=" * 60)
    print("6. 迭代时的注意事项")
    print("=" * 60)

    df_warning = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    print("警告 1: iterrows 返回的行是副本，修改无效")
    for idx, row in df_warning.iterrows():
        row["A"] = 100  # 这不会修改原 DataFrame
    print(f"迭代后 DataFrame:\n{df_warning}")
    print("可以看到 A 列没有被修改")

    print("\n警告 2: 迭代时不要修改 DataFrame 结构")
    print("添加/删除列会导致不可预测的行为")

    print("\n警告 3: iterrows 的 dtype 不保证一致")
    df_mixed = pd.DataFrame({"A": [1, 2, 3], "B": [1.5, 2.5, 3.5]})
    for idx, row in df_mixed.iterrows():
        print(f"行 {idx} 的 dtype: {row['A'].dtype}, {row['B'].dtype}")

    print("\n" + "=" * 60)
    print("7. 最佳实践建议")
    print("=" * 60)

    print("""
推荐顺序：
1. 优先使用 pandas/NumPy 向量化操作
2. 使用 .apply() 处理复杂逻辑
3. 如果必须迭代，使用 itertuples()
4. 只有在必要时才使用 iterrows()

何时使用迭代：
- 需要逐行处理复杂逻辑
- 需要调用外部 API
- 需要与 Python 对象交互
- 向量化实现过于复杂

何时避免迭代：
- 简单的数学运算
- 条件过滤
- 字符串操作（有 str 访问器）
- 聚合操作
""")

    print("\n" + "=" * 60)
    print("8. 实际应用示例")
    print("=" * 60)

    # 示例：根据复杂规则计算折扣
    df_products = pd.DataFrame(
        {
            "product": ["A", "B", "C", "D"],
            "price": [100, 200, 150, 80],
            "category": ["electronics", "electronics", "clothing", "clothing"],
            "stock": [50, 5, 20, 100],
        }
    )

    print("产品数据:")
    print(df_products)

    # 使用 itertuples 计算折扣
    discounts = []
    for row in df_products.itertuples():
        if row.stock < 10:
            discount = 0.2  # 库存少，不打折
        elif row.category == "electronics" and row.price > 150:
            discount = 0.15  # 高价电子产品
        elif row.category == "clothing":
            discount = 0.1  # 服装统一折扣
        else:
            discount = 0.05  # 默认折扣
        discounts.append(discount)

    df_products["discount"] = discounts
    df_products["final_price"] = df_products["price"] * (1 - df_products["discount"])

    print("\n计算折扣后:")
    print(df_products)


if __name__ == "__main__":
    main()