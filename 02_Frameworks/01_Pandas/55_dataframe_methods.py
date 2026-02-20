#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 55：DataFrame Methods - 数据框方法补充。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/55_dataframe_methods.py

本节补充一些重要的 DataFrame 方法，这些方法在数据处理中
非常实用但可能在基础课程中没有深入讲解。

本节演示：
1. nlargest / nsmallest - 最大/最小的 N 个值
2. compare - 比较两个 DataFrame 的差异
3. factorize - 将值编码为整数
4. sample - 抽样（简单随机、分层、加权）
5. nunique - 唯一值计数
6. isin - 成员检查
7. between - 范围检查
8. clip - 裁剪值到范围
9. abs - 绝对值
10. round - 四舍五入
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. nlargest / nsmallest - 最大/最小的 N 个值")
    print("=" * 60)

    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'score': [85, 92, 78, 88, 95, 82],
        'age': [25, 30, 35, 28, 22, 40]
    })

    print("\n原始数据:")
    print(df)

    print("\nlargest - 按 score 找出前 3 名:")
    top3 = df.nlargest(3, 'score')
    print(top3)

    print("\nnsmallest - 按 age 找出最小的 2 个:")
    youngest2 = df.nsmallest(2, 'age')
    print(youngest2)

    print("\n多列排序（先按 score，再按 age）:")
    top3_multi = df.nlargest(3, ['score', 'age'])
    print(top3_multi)

    # 与 sort_values 对比
    print("\n等效的 sort_values 方法:")
    top3_sorted = df.sort_values('score', ascending=False).head(3)
    print(top3_sorted)

    print("\n" + "=" * 60)
    print("2. compare - 比较两个 DataFrame 的差异")
    print("=" * 60)

    df1 = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    }, index=['a', 'b', 'c', 'd'])

    df2 = pd.DataFrame({
        'A': [1, 2, 99, 4],
        'B': [5, 6, 7, 88],
        'C': [9, 10, 11, 12]
    }, index=['a', 'b', 'c', 'd'])

    print("\ndf1:")
    print(df1)
    print("\ndf2:")
    print(df2)

    # 比较差异
    print("\ncompare 结果 (哪些值不同):")
    diff = df1.compare(df2)
    print(diff)

    print("\ncompare 结果 (对齐轴):")
    diff_align = df1.compare(df2, align_axis=1)
    print(diff_align)

    print("\n只显示有变化的行:")
    diff_keep_equal = df1.compare(df2, keep_equal=True)
    print(diff_keep_equal)

    print("\n" + "=" * 60)
    print("3. factorize - 将值编码为整数")
    print("=" * 60)

    s = pd.Series(['cat', 'dog', 'cat', 'bird', 'dog', 'cat'])
    print(f"\n原始 Series:")
    print(s)

    # factorize 返回 (编码后的数组, 唯一值)
    codes, uniques = s.factorize()
    print(f"\ncodes (编码后): {codes}")
    print(f"uniques (唯一值): {uniques}")

    # 使用 DataFrame.factorize
    df_cat = pd.DataFrame({
        'category': ['A', 'B', 'A', 'C', 'B', 'A'],
        'value': [10, 20, 30, 40, 50, 60]
    })

    print(f"\n分类数据:")
    print(df_cat)

    codes, uniques = df_cat['category'].factorize()
    df_cat['category_code'] = codes
    print(f"\n添加编码列:")
    print(df_cat)

    # factorize 与 astype('category') 对比
    print(f"\nfactorize vs category:")
    print(f"  factorize: 整数编码，适合算法")
    print(f"  category dtype: 保留原始值，适合分组")

    print("\n" + "=" * 60)
    print("4. sample - 抽样")
    print("=" * 60)

    df = pd.DataFrame({
        'id': range(100),
        'group': np.repeat(['A', 'B', 'C', 'D'], 25),
        'value': np.random.randn(100)
    })

    print(f"\n原始数据: {len(df)} 行")

    # 简单随机抽样
    print("\n简单随机抽样 10 行:")
    simple_sample = df.sample(n=10, random_state=42)
    print(simple_sample)

    # 按比例抽样
    print("\n按比例抽样 20%:")
    frac_sample = df.sample(frac=0.2, random_state=42)
    print(f"抽样数量: {len(frac_sample)}")

    # 加权抽样
    df_weights = pd.DataFrame({
        'item': ['A', 'B', 'C', 'D', 'E'],
        'weight': [0.1, 0.3, 0.2, 0.25, 0.15]
    })

    print(f"\n加权抽样:")
    print(f"  权重: {df_weights['weight'].tolist()}")
    weighted_sample = df_weights.sample(n=3, weights='weight', random_state=42)
    print(weighted_sample)

    # 分层抽样（按 group）
    print("\n分层抽样（每组 2 行）:")
    stratified = df.groupby('group').sample(n=2, random_state=42)
    print(stratified)

    # 替换抽样
    print("\n有放回抽样 5 行:")
    with_replacement = df.sample(n=5, replace=True, random_state=42)
    print(with_replacement)

    print("\n" + "=" * 60)
    print("5. nunique - 唯一值计数")
    print("=" * 60)

    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'],
        'city': ['Beijing', 'Shanghai', 'Beijing', 'Guangzhou', 'Shanghai', 'Shenzhen'],
        'age': [25, 30, 25, 35, 30, 28]
    })

    print("\n数据:")
    print(df)

    print(f"\n每列唯一值数量:")
    print(df.nunique())

    print(f"\nname 列的唯一值:")
    print(df['name'].unique())

    print(f"\nname 列的唯一值数量:")
    print(df['name'].nunique())

    # 与 value_counts 对比
    print(f"\nvalue_counts (带计数):")
    print(df['name'].value_counts())

    print("\n" + "=" * 60)
    print("6. isin - 成员检查")
    print("=" * 60)

    df = pd.DataFrame({
        'product': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
        'price': [5, 3, 8, 12, 15],
        'category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Berry']
    })

    print("\n产品数据:")
    print(df)

    # 检查产品是否在列表中
    target_products = ['Apple', 'Cherry', 'Elderberry']
    print(f"\n目标产品: {target_products}")

    mask = df['product'].isin(target_products)
    print(f"\ninin 结果:")
    print(mask)

    print(f"\n过滤结果:")
    print(df[mask])

    # 多列条件
    print(f"\n多列 isin:")
    filter_df = df[df['product'].isin(['Apple', 'Banana']) & df['category'].isin(['Fruit'])]
    print(filter_df)

    # 反向选择
    print(f"\n反向选择 (~isin):")
    print(df[~df['product'].isin(['Apple', 'Cherry'])])

    print("\n" + "=" * 60)
    print("7. between - 范围检查")
    print("=" * 60)

    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'score': [85, 92, 78, 88, 95],
        'age': [25, 30, 35, 28, 22]
    })

    print("\n学生数据:")
    print(df)

    # between 检查
    print(f"\nscore 在 80-90 之间:")
    mask_score = df['score'].between(80, 90)
    print(df[mask_score])

    print(f"\nage 在 25-30 之间 (inclusive='both'):")
    mask_age = df['age'].between(25, 30, inclusive='both')
    print(df[mask_age])

    print(f"\nage 在 25-30 之间 (inclusive='neither'):")
    mask_age_neither = df['age'].between(25, 30, inclusive='neither')
    print(df[mask_age_neither])

    print("\n" + "=" * 60)
    print("8. clip - 裁剪值到范围")
    print("=" * 60)

    df = pd.DataFrame({
        'value': [-10, -5, 0, 5, 10, 15, 20, 100]
    })

    print("\n原始数据:")
    print(df)

    # 裁剪到 [0, 10]
    df_clipped = df.clip(lower=0, upper=10)
    print(f"\nclip 到 [0, 10]:")
    print(df_clipped)

    # 只裁剪上限
    print(f"\n只裁剪上限 (upper=15):")
    print(df.clip(upper=15))

    # 只裁剪下限
    print(f"\n只裁剪下限 (lower=-5):")
    print(df.clip(lower=-5))

    # 按列裁剪
    df_multi = pd.DataFrame({
        'A': [-10, 0, 10, 20],
        'B': [5, 15, 25, 35],
        'C': [-5, 5, 15, 25]
    })

    print(f"\n多列数据:")
    print(df_multi)

    print(f"\n分别裁剪 A:[-5,15], B:[10,30], C:[0,20]:")
    print(df_multi.clip(lower={'A': -5, 'B': 10, 'C': 0},
                       upper={'A': 15, 'B': 30, 'C': 20}))

    print("\n" + "=" * 60)
    print("9. abs - 绝对值")
    print("=" * 60)

    df = pd.DataFrame({
        'value': [-10, -5, 0, 5, 10],
        'change': [-2.5, 3.8, -1.2, 4.5, -0.8]
    })

    print("\n原始数据:")
    print(df)

    print(f"\nabs() 绝对值:")
    print(df.abs())

    print(f"\n只对 change 列取绝对值:")
    df_copy = df.copy()
    df_copy['change_abs'] = df_copy['change'].abs()
    print(df_copy)

    print("\n" + "=" * 60)
    print("10. round - 四舍五入")
    print("=" * 60)

    df = pd.DataFrame({
        'value': [1.234, 2.567, 3.891, 4.2345],
        'percentage': [12.3456, 23.4567, 34.5678, 45.6789]
    })

    print("\n原始数据:")
    print(df)

    print(f"\nround(0): 保留 0 位小数:")
    print(df.round(0))

    print(f"\nround(2): 保留 2 位小数:")
    print(df.round(2))

    print(f"\n按列指定精度:")
    print(df.round({'value': 1, 'percentage': 3}))

    # 格式化显示（不改变数据）
    print(f"\n格式化显示 (数据不变):")
    pd.set_option('display.precision', 2)
    print(df)
    pd.reset_option('display.precision')

    print("\n" + "=" * 60)
    print("11. 实际应用案例")
    print("=" * 60)

    print("\n案例1: 找出销售额前 5 的产品")
    print("-" * 40)
    sales = pd.DataFrame({
        'product': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        'sales': [120, 85, 200, 150, 95, 180, 110, 75],
        'category': ['Electronics', 'Clothing', 'Electronics', 'Clothing',
                    'Electronics', 'Clothing', 'Electronics', 'Clothing']
    })

    top5 = sales.nlargest(5, 'sales')
    print(f"销售额前 5:")
    print(top5)

    print("\n案例2: 数据版本对比")
    print("-" * 40)
    old_version = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'value': [100, 200, 300]
    })

    new_version = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Robert', 'Charlie'],
        'value': [100, 250, 350]
    })

    print("数据对比结果:")
    print(old_version.compare(new_version))

    print("\n案例3: 异常值检测")
    print("-" * 40)
    measurements = pd.DataFrame({
        'sensor_id': range(1, 11),
        'reading': [25, 27, 26, 100, 24, 23, 99, 25, 26, 24]
    })

    print(f"原始读数:")
    print(measurements)

    # 使用 IQR 方法检测异常值
    Q1 = measurements['reading'].quantile(0.25)
    Q3 = measurements['reading'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    print(f"\n正常范围: [{lower_bound:.1f}, {upper_bound:.1f}]")

    outliers = measurements[~measurements['reading'].between(lower_bound, upper_bound)]
    print(f"异常值:")
    print(outliers)

    print("\n案例4: 分类编码")
    print("-" * 40)
    categories = pd.DataFrame({
        'category': ['Red', 'Blue', 'Green', 'Red', 'Blue', 'Yellow'],
        'count': [10, 15, 8, 12, 20, 5]
    })

    print(f"原始分类:")
    print(categories)

    codes, uniques = categories['category'].factorize()
    categories['category_code'] = codes
    print(f"\n添加编码:")
    print(categories)

    print("\n" + "=" * 60)
    print("12. 方法速查表")
    print("=" * 60)

    methods = {
        'nlargest(n, columns)': '返回按列排序的前 n 行',
        'nsmallest(n, columns)': '返回按列排序的后 n 行',
        'compare(other)': '比较两个 DataFrame 的差异',
        'factorize()': '将值编码为整数（返回 codes, uniques）',
        'sample(n/frac)': '随机抽样（n=数量，frac=比例）',
        'sample(weights=...)': '加权抽样',
        'nunique()': '唯一值计数',
        'unique()': '返回唯一值数组',
        'isin(values)': '成员检查，返回布尔 Series',
        'between(a, b)': '检查值是否在 [a, b] 范围内',
        'clip(lower, upper)': '裁剪值到指定范围',
        'abs()': '绝对值',
        'round(decimals)': '四舍五入到指定小数位',
    }

    print("\nDataFrame 方法速查:")
    for method, desc in methods.items():
        print(f"  {method:30s} # {desc}")


if __name__ == "__main__":
    main()