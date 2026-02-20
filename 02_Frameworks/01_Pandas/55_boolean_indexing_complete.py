#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 55：布尔索引进阶。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/55_boolean_indexing_complete.py

知识点：
- where/mask 详细用法
- query 性能与陷阱
- 复杂条件组合最佳实践
- 布尔索引性能优化
- isin / between
- 与/或/非运算
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy", "David", "Eve"],
            "age": [20, 21, 19, 22, 20],
            "score": [88, 75, 92, 85, 90],
            "dept": ["A", "B", "A", "B", "A"],
        }
    )

    print("=" * 70)
    print("原始数据")
    print("=" * 70)
    print(df)

    print("\n" + "=" * 70)
    print("1. where - 条件保留（不满足的设为 NaN）")
    print("=" * 70)

    print("\n1.1 where 基础用法")
    print("-" * 70)

    result = df["score"].where(df["score"] > 80)
    print("df['score'].where(df['score'] > 80) ->")
    print(result)

    print("\n1.2 where 指定其他值")
    print("-" * 70)

    result = df["score"].where(df["score"] > 80, other=0)
    print("df['score'].where(df['score'] > 80, other=0) ->")
    print(result)

    print("\n1.3 DataFrame where")
    print("-" * 70)

    result = df.where(df["score"] > 80)
    print("df.where(df['score'] > 80) ->")
    print(result)

    result = df.where(df["score"] > 80, other={"score": 0, "age": df["age"]})
    print("\ndf.where(df['score'] > 80, other={'score': 0, 'age': df['age']}) ->")
    print(result)

    print("\n1.4 where 与 inplace")
    print("-" * 70)

    df_copy = df.copy()
    df_copy["score"].where(df_copy["score"] > 80, other=0, inplace=True)
    print("inplace=True 原地修改 ->")
    print(df_copy)

    print("\n1.5 where 的 axis 参数")
    print("-" * 70)

    df_vals = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])
    print("原始 ->")
    print(df_vals)

    print("\ndf_vals.where(df_vals > 5, axis=0) ->")
    print(df_vals.where(df_vals > 5, axis=0))

    print("\n1.6 where 与 level 参数（多级索引）")
    print("-" * 70)

    df_multi = pd.DataFrame(
        {"value": [1, 2, 3, 4]}, index=pd.MultiIndex.from_tuples([("A", 1), ("A", 2), ("B", 1), ("B", 2)])
    )
    print("多级索引数据 ->")
    print(df_multi)

    result = df_multi.where(df_multi > 2, axis=0, level=1)
    print("\ndf_multi.where(df_multi > 2, level=1) ->")
    print(result)

    print("\n" + "=" * 70)
    print("2. mask - 条件掩码（与 where 相反）")
    print("=" * 70)

    print("\n2.1 mask 基础用法")
    print("-" * 70)

    result = df["score"].mask(df["score"] > 80)
    print("df['score'].mask(df['score'] > 80) ->")
    print("(满足条件的设为 NaN，与 where 相反)")
    print(result)

    print("\n2.2 where vs mask 对比")
    print("-" * 70)

    print("where: 保留 True，替换 False")
    print(f"  df['score'].where(df['score'] > 80) ->")
    print(f"  {df['score'].where(df['score'] > 80).tolist()}")

    print("\nmask: 替换 True，保留 False")
    print(f"  df['score'].mask(df['score'] > 80) ->")
    print(f"  {df['score'].mask(df['score'] > 80).tolist()}")

    print("\n2.3 mask 指定其他值")
    print("-" * 70)

    result = df["score"].mask(df["score"] > 80, other=0)
    print("df['score'].mask(df['score'] > 80, other=0) ->")
    print(result)

    print("\n" + "=" * 70)
    print("3. query - 字符串表达式查询")
    print("=" * 70)

    print("\n3.1 query 基础用法")
    print("-" * 70)

    result = df.query("score > 80 and age == 20")
    print("df.query('score > 80 and age == 20') ->")
    print(result)

    print("\n3.2 query 引用外部变量")
    print("-" * 70)

    threshold = 85
    result = df.query("score > @threshold")
    print(f"threshold = {threshold}")
    print(f"df.query('score > @threshold') ->")
    print(result)

    print("\n3.3 query 与列名包含空格")
    print("-" * 70)

    df_space = pd.DataFrame({"first name": ["Alice", "Bob"], "last name": ["Smith", "Jones"], "age": [20, 21]})
    print("列名包含空格 ->")
    print(df_space)

    # 使用反引号引用列名
    result = df_space.query("`first name` == 'Alice'")
    print("\ndf_space.query('`first name` == \"Alice\"') ->")
    print(result)

    print("\n3.4 query 性能优势")
    print("-" * 70)

    # 创建大数据集对比性能
    import time

    large_df = pd.DataFrame(
        {"A": np.random.randn(100000), "B": np.random.randn(100000), "C": np.random.randn(100000)}
    )

    # 布尔索引
    start = time.perf_counter()
    result_bool = large_df[(large_df["A"] > 0) & (large_df["B"] > 0)]
    time_bool = time.perf_counter() - start

    # query
    start = time.perf_counter()
    result_query = large_df.query("A > 0 and B > 0")
    time_query = time.perf_counter() - start

    print(f"布尔索引耗时: {time_bool:.6f} 秒")
    print(f"query 耗时: {time_query:.6f} 秒")
    print(f"query 相对速度: {time_bool / time_query:.2f}x")

    print("\n3.5 query 与 inplace")
    print("-" * 70)

    df_copy = df.copy()
    df_copy.query("score > 80", inplace=True)
    print("query('score > 80', inplace=True) ->")
    print(df_copy)

    print("\n" + "=" * 70)
    print("4. 复杂条件组合")
    print("=" * 70)

    print("\n4.1 与运算（&）")
    print("-" * 70)

    result = df[(df["score"] > 80) & (df["age"] >= 20)]
    print("df[(df['score'] > 80) & (df['age'] >= 20)] ->")
    print(result)

    print("\n4.2 或运算（|）")
    print("-" * 70)

    result = df[(df["score"] > 90) | (df["age"] < 20)]
    print("df[(df['score'] > 90) | (df['age'] < 20)] ->")
    print(result)

    print("\n4.3 非运算（~）")
    print("-" * 70)

    result = df[~(df["dept"] == "A")]
    print("df[~(df['dept'] == 'A')] ->")
    print(result)

    print("\n4.4 组合条件")
    print("-" * 70)

    result = df[((df["dept"] == "A") & (df["score"] > 85)) | ((df["dept"] == "B") & (df["age"] > 20))]
    print("复杂条件组合 ->")
    print(result)

    print("\n4.5 isin - 成员检查")
    print("-" * 70)

    result = df[df["dept"].isin(["A", "C"])]
    print("df[df['dept'].isin(['A', 'C'])] ->")
    print(result)

    print("\ndf[~df['dept'].isin(['A', 'C'])] ->")
    result = df[~df["dept"].isin(["A", "C"])]
    print(result)

    print("\n4.6 between - 范围检查")
    print("-" * 70)

    result = df[df["age"].between(19, 21)]
    print("df[df['age'].between(19, 21)] ->")
    print(result)

    print("\ndf[df['age'].between(19, 21, inclusive='left')] ->")
    result = df[df["age"].between(19, 21, inclusive="left")]
    print(result)

    print("\n4.7 str.contains - 字符串匹配")
    print("-" * 70)

    result = df[df["name"].str.contains("a|e", case=False)]
    print("df[df['name'].str.contains('a|e', case=False)] ->")
    print(result)

    print("\n" + "=" * 70)
    print("5. 布尔索引陷阱与最佳实践")
    print("=" * 70)

    print("\n5.1 运算符优先级陷阱")
    print("-" * 70)

    print("错误写法: df[df['score'] > 80 & df['age'] > 20]")
    print("  这会被解析为: df['score'] > (80 & df['age']) > 20")
    print("\n正确写法: df[(df['score'] > 80) & (df['age'] > 20)]")
    print("  使用括号明确优先级")

    print("\n5.2 链式比较陷阱")
    print("-" * 70)

    print("错误写法: df[80 < df['score'] < 90]")
    print("  Python 不支持链式比较，应该使用:")
    print("正确写法: df[(df['score'] > 80) & (df['score'] < 90)]")

    print("\n5.3 and/or/not 陷阱")
    print("-" * 70)

    print("错误写法: df[df['score'] > 80 and df['age'] > 20]")
    print("  and/or/not 是 Python 关键字，不能用于数组")
    print("\n正确写法: df[(df['score'] > 80) & (df['age'] > 20)]")
    print("  使用 & / | / ~ 运算符")

    print("\n5.4 None vs NaN")
    print("-" * 70)

    df_none = pd.DataFrame({"A": [1, 2, None, 4], "B": [5, None, 7, 8]})
    print("含 None 数据 ->")
    print(df_none)

    print("\ndf_none[df_none['A'].notnull()] ->")
    print(df_none[df_none["A"].notnull()])

    print("\ndf_none[df_none['A'].isnull()] ->")
    print(df_none[df_none["A"].isnull()])

    print("\n5.5 索引对齐问题")
    print("-" * 70)

    s1 = pd.Series([True, False, True], index=[0, 1, 2])
    s2 = pd.Series([True, True, False], index=[0, 1, 3])

    print("s1 ->")
    print(s1)
    print("\ns2 ->")
    print(s2)

    print("\ns1 & s2 (索引自动对齐) ->")
    print(s1 & s2)
    print("注意索引 2 和 3 的对齐结果")

    print("\n" + "=" * 70)
    print("6. 性能优化技巧")
    print("=" * 70)

    # 创建大数据集
    large_df = pd.DataFrame(
        {
            "A": np.random.randn(1000000),
            "B": np.random.randn(1000000),
            "C": np.random.choice(["X", "Y", "Z"], 1000000),
        }
    )

    import time

    print("\n6.1 使用 .loc vs 直接布尔索引")
    print("-" * 70)

    start = time.perf_counter()
    result1 = large_df.loc[(large_df["A"] > 0) & (large_df["B"] > 0)]
    time1 = time.perf_counter() - start

    start = time.perf_counter()
    result2 = large_df[(large_df["A"] > 0) & (large_df["B"] > 0)]
    time2 = time.perf_counter() - start

    print(f".loc 方式: {time1:.6f} 秒")
    print(f"直接索引: {time2:.6f} 秒")

    print("\n6.2 使用 query vs 布尔索引")
    print("-" * 70)

    start = time.perf_counter()
    result1 = large_df[(large_df["A"] > 0) & (large_df["B"] > 0)]
    time1 = time.perf_counter() - start

    start = time.perf_counter()
    result2 = large_df.query("A > 0 and B > 0")
    time2 = time.perf_counter() - start

    print(f"布尔索引: {time1:.6f} 秒")
    print(f"query: {time2:.6f} 秒")

    print("\n6.3 使用 .isin vs 多个 or")
    print("-" * 70)

    start = time.perf_counter()
    result1 = large_df[(large_df["C"] == "X") | (large_df["C"] == "Y")]
    time1 = time.perf_counter() - start

    start = time.perf_counter()
    result2 = large_df[large_df["C"].isin(["X", "Y"])]
    time2 = time.perf_counter() - start

    print(f"多个 or: {time1:.6f} 秒")
    print(f".isin(): {time2:.6f} 秒")

    print("\n6.4 使用 .between vs 多个比较")
    print("-" * 70)

    start = time.perf_counter()
    result1 = large_df[(large_df["A"] > -1) & (large_df["A"] < 1)]
    time1 = time.perf_counter() - start

    start = time.perf_counter()
    result2 = large_df[large_df["A"].between(-1, 1)]
    time2 = time.perf_counter() - start

    print(f"多个比较: {time1:.6f} 秒")
    print(f".between(): {time2:.6f} 秒")

    print("\n6.5 避免重复计算")
    print("-" * 70)

    # 不推荐
    start = time.perf_counter()
    result = large_df[(large_df["A"] > 0) & (large_df["A"] < 1) & (large_df["B"] > 0)]
    time1 = time.perf_counter() - start

    # 推荐（对于复杂条件）
    mask = (large_df["A"] > 0) & (large_df["A"] < 1)
    start = time.perf_counter()
    result = large_df[mask & (large_df["B"] > 0)]
    time2 = time.perf_counter() - start

    print(f"直接计算: {time1:.6f} 秒")
    print(f"预计算 mask: {time2:.6f} 秒")

    print("\n" + "=" * 70)
    print("7. 实际应用示例")
    print("=" * 70)

    # 示例 1: 数据清洗 - 过滤异常值
    print("\n示例 1: 过滤异常值（3倍标准差）")
    df_stats = pd.DataFrame({"value": np.random.randn(100) * 10 + 50})
    mean = df_stats["value"].mean()
    std = df_stats["value"].std()
    df_clean = df_stats[df_stats["value"].between(mean - 3 * std, mean + 3 * std)]
    print(f"原始: {len(df_stats)} 行, 清洗后: {len(df_clean)} 行")

    # 示例 2: 多条件筛选
    print("\n示例 2: 查找符合多项条件的记录")
    df_sales = pd.DataFrame(
        {
            "product": ["A", "B", "C", "D", "E"],
            "price": [100, 200, 150, 250, 180],
            "category": ["电子", "电子", "服装", "服装", "食品"],
            "stock": [50, 10, 30, 5, 100],
        }
    )
    print("销售数据 ->")
    print(df_sales)

    # 电子类且价格 > 150，或者库存 < 20 的商品
    result = df_sales[((df_sales["category"] == "电子") & (df_sales["price"] > 150)) | (df_sales["stock"] < 20)]
    print("\n符合条件的商品 ->")
    print(result)

    # 示例 3: 动态条件构建
    print("\n示例 3: 动态构建查询条件")
    def build_query(conditions: dict) -> str:
        """根据字典构建 query 字符串"""
        parts = []
        for col, (op, val) in conditions.items():
            if op == "==":
                parts.append(f"`{col}` == '{val}'" if isinstance(val, str) else f"`{col}` == {val}")
            elif op == ">":
                parts.append(f"`{col}` > {val}")
            elif op == "<":
                parts.append(f"`{col}` < {val}")
            elif op == "in":
                vals = "', '".join(val) if isinstance(val[0], str) else ", ".join(map(str, val))
                parts.append(f"`{col}` in ['{vals}']")
        return " and ".join(parts)

    conditions = {"dept": ("==", "A"), "score": (">", 80), "age": ("<", 22)}
    query_str = build_query(conditions)
    print(f"构建的查询: {query_str}")
    print(f"查询结果:")
    print(df.query(query_str))


if __name__ == "__main__":
    main()