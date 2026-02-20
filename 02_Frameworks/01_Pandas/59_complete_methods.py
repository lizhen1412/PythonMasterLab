#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 59：Pandas Complete Methods - 补充剩余方法。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/59_complete_methods.py

本节补充 Pandas 中尚未覆盖的重要方法和功能，
确保达到 100% 的方法覆盖。

本节演示：
1. corr/cov - 相关性和协方差矩阵
2. rank - 排名的所有参数
3. pct_change - 百分比变化
4. shift/lag - 数据移位
5. diff - 差分
6. cummax/cummin - 累计最大/最小值
7. expanding - 累计窗口
8. bfill/ffill with limit - 填充限制
9. explode - 列表展开
10. get_dummies - 独热编码
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. corr/cov - 相关性和协方差")
    print("=" * 60)

    # 创建示例数据
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [2, 4, 6, 8, 10],
        'C': [5, 4, 3, 2, 1],
        'D': [1, 3, 5, 7, 9]
    })

    print("\n数据:")
    print(df)

    # 相关系数
    print(f"\n相关系数矩阵 (method='pearson'):")
    print(df.corr())

    print(f"\n相关系数矩阵 (method='spearman'):")
    print(df.corr(method='spearman'))

    print(f"\n相关系数矩阵 (method='kendall'):")
    print(df.corr(method='kendall'))

    # 与单个 Series 的相关性
    print(f"\nA 列与其他列的相关性:")
    print(df.corrwith(df['A']))

    # 协方差矩阵
    print(f"\n协方差矩阵:")
    print(df.cov())

    # min_periods 参数
    df_nan = df.copy()
    df_nan.iloc[0, 0] = np.nan
    df_nan.iloc[1, 1] = np.nan

    print(f"\n含 NaN 的数据:")
    print(df_nan)

    print(f"\n相关系数 (min_periods=3):")
    print(df_nan.corr(min_periods=3))

    print("\n" + "=" * 60)
    print("2. rank - 排名完整参数")
    print("=" * 60)

    df = pd.DataFrame({
        'score': [100, 90, 90, 80, 80, 80, 70],
        'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    })

    print("\n数据:")
    print(df)

    # average 参数
    print(f"\nrank(method='average') - 并列取平均:")
    print(f"  {df['score'].rank(method='average').values}")

    print(f"\nrank(method='min') - 并列取最小:")
    print(f"  {df['score'].rank(method='min').values}")

    print(f"\nrank(method='max') - 并列取最大:")
    print(f"  {df['score'].rank(method='max').values}")

    print(f"\nrank(method='dense') - 密集排名:")
    print(f"  {df['score'].rank(method='dense').values}")

    print(f"\nrank(method='first') - 先到先得:")
    print(f"  {df['score'].rank(method='first').values}")

    # ascending 参数
    print(f"\nrank(ascending=False) - 降序:")
    print(f"  {df['score'].rank(ascending=False).values}")

    # pct 参数
    print(f"\nrank(pct=True) - 百分比排名:")
    print(f"  {df['score'].rank(pct=True).values}")

    print("\n" + "=" * 60)
    print("3. pct_change - 百分比变化")
    print("=" * 60)

    # 股票价格
    prices = pd.Series([100, 102, 105, 103, 108, 110, 108])

    print(f"\n价格序列:")
    print(prices)

    # 百分比变化
    print(f"\npct_change() - 简单变化:")
    print(prices.pct_change())

    print(f"\npct_change(periods=2) - 与2期前相比:")
    print(prices.pct_change(periods=2))

    print(f"\npct_change(fill_method='ffill') - 用前值填充:")
    print(prices.pct_change(fill_method='ffill'))

    print(f"\npct_change(limit=1) - 只计算一次变化:")
    print(prices.pct_change(limit=1))

    # 多列
    df = pd.DataFrame({
        'A': [100, 105, 102, 108],
        'B': [200, 195, 198, 205]
    })

    print(f"\n多列百分比变化:")
    print(df.pct_change())

    print("\n" + "=" * 60)
    print("4. shift/lag - 数据移位")
    print("=" * 60)

    df = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=5),
        'value': [10, 20, 30, 40, 50]
    })

    print("\n原始数据:")
    print(df)

    # shift
    print(f"\nshift(1) - 向下移动:")
    print(df[['value']].shift(1))

    print(f"\nshift(-1) - 向上移动:")
    print(df[['value']].shift(-1))

    print(f"\nshift(2) - 向下移动2位:")
    print(df[['value']].shift(2))

    # freq 参数
    ts = pd.Series([1, 2, 3, 4, 5],
                  index=pd.date_range('2024-01-01', periods=5, freq='D'))

    print(f"\n时间序列 shift(freq='1D'):")
    print(ts.shift(freq='1D'))

    print(f"\n时间序列 shift(freq='ME') - 月末:")
    print(ts.shift(freq='ME'))

    # tshift (时间索引平移)
    print(f"\ntshift(1) - 时间索引平移:")
    print(ts.tshift(1))

    print("\n" + "=" * 60)
    print("5. diff - 差分")
    print("=" * 60)

    df = pd.DataFrame({
        'value': [10, 15, 12, 18, 20, 25, 22]
    })

    print("\n原始值:")
    print(df)

    print(f"\ndiff(1) - 一阶差分:")
    print(df.diff())

    print(f"\ndiff(2) - 二阶差分:")
    print(df.diff(2))

    # 时间序列差分
    ts = pd.Series([100, 105, 102, 110, 108, 115],
                  index=pd.date_range('2024-01-01', periods=6))

    print(f"\n时间序列 diff:")
    print(ts)
    print(f"\ndiff(1):")
    print(ts.diff(1))

    print(f"\ndiff(periods=2):")
    print(ts.diff(periods=2))

    print("\n" + "=" * 60)
    print("6. cummax/cummin - 累计最大/最小值")
    print("=" * 60)

    df = pd.DataFrame({
        'value': [10, 5, 15, 3, 20, 8, 25]
    })

    print("\n原始值:")
    print(df)

    print(f"\ncummax() - 累计最大值:")
    print(df[['value']].cummax())

    print(f"\ncummin() - 累计最小值:")
    print(df[['value']].cummin())

    # axis 参数
    df_multi = pd.DataFrame({
        'A': [1, 3, 2, 5, 4],
        'B': [5, 2, 4, 1, 3],
        'C': [3, 4, 1, 2, 5]
    })

    print(f"\n多列数据:")
    print(df_multi)

    print(f"\ncummax(axis=1) - 横向累计最大:")
    print(df_multi.cummax(axis=1))

    print(f"\ncummin(axis=1) - 横向累计最小:")
    print(df_multi.cummin(axis=1))

    print("\n" + "=" * 60)
    print("7. expanding - 累计窗口")
    print("=" * 60)

    df = pd.DataFrame({
        'value': [10, 20, 15, 30, 25, 40]
    })

    print("\n数据:")
    print(df)

    # expanding 窗口
    print(f"\nexpanding().mean() - 累计平均:")
    print(df[['value']].expanding().mean())

    print(f"\nexpanding().sum() - 累计和:")
    print(df[['value']].expanding().sum())

    print(f"\nexpanding().min() - 累计最小:")
    print(df[['value']].expanding().min())

    print(f"\nexpanding().max() - 累计最大:")
    print(df[['value']].expanding().max())

    # min_periods
    print(f"\nexpanding(min_periods=3).mean() - 至少3个值:")
    print(df[['value']].expanding(min_periods=3).mean())

    print("\n" + "=" * 60)
    print("8. bfill/ffill with limit - 填充限制")
    print("=" * 60)

    df = pd.DataFrame({
        'A': [1, np.nan, np.nan, 4, 5],
        'B': [np.nan, 2, np.nan, np.nan, 5]
    })

    print("\n原始数据:")
    print(df)

    print(f"\nffill(limit=1) - 向前填充最多1个:")
    print(df.ffill(limit=1))

    print(f"\nffill(limit=2) - 向前填充最多2个:")
    print(df.ffill(limit=2))

    print(f"\nbfill(limit=1) - 向后填充最多1个:")
    print(df.bfill(limit=1))

    print(f"\nbfill(limit=2) - 向后填充最多2个:")
    print(df.bfill(limit=2))

    print("\n" + "=" * 60)
    print("9. explode - 列表展开")
    print("=" * 60)

    df = pd.DataFrame({
        'id': [1, 2, 3],
        'tags': [['python', 'data'], ['pandas', 'numpy'], ['ml', 'dl', 'ai']],
        'scores': [[80, 85], [90, 95], [70, 75, 85]]
    })

    print("\n原始数据:")
    print(df)

    print(f"\nexplode('tags') - 展开标签:")
    exploded = df.explode('tags')
    print(exploded)

    print(f"\nexplode(['tags', 'scores']) - 同时展开多列:")
    # 注意：只有长度一致时才能同时展开
    df_subset = df[['id', 'tags']].copy()
    print(df_subset.explode('tags'))

    print("\nignore_index 参数:")
    print(df.explode('tags', ignore_index=True))

    print("\n" + "=" * 60)
    print("10. get_dummies - 独热编码")
    print("=" * 60)

    df = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'category': ['A', 'B', 'A', 'C'],
        'color': ['red', 'blue', 'green', 'red']
    })

    print("\n原始数据:")
    print(df)

    # 基础独热编码
    print(f"\nget_dummies(['category']):")
    dummies = pd.get_dummies(df[['category']])
    print(dummies)

    # 前缀
    print(f"\nget_dummies(['category'], prefix='cat'):")
    print(pd.get_dummies(df[['category']], prefix='cat'))

    # 多列
    print(f"\nget_dummies(['category', 'color']):")
    print(pd.get_dummies(df[['category', 'color']]))

    # drop_first 避免多重共线性
    print(f"\nget_dummies(..., drop_first=True):")
    print(pd.get_dummies(df[['category']], drop_first=True))

    # dtype 参数
    print(f"\nget_dummies(..., dtype=float):")
    print(pd.get_dummies(df[['category']], dtype=float))

    print("\n" + "=" * 60)
    print("11. 其他重要方法补充")
    print("=" * 60)

    # sample
    df = pd.DataFrame({
        'value': range(100)
    })

    print(f"\nsample(n=5) - 随机抽样5行:")
    print(df.sample(n=5))

    print(f"\nsample(frac=0.1) - 抽样10%:")
    print(df.sample(frac=0.1))

    print(f"\nsample(n=3, replace=True) - 有放回抽样:")
    print(df.sample(n=3, replace=True))

    print(f"\nsample(n=3, weights='value') - 加权抽样:")
    print(df.sample(n=3, weights='value'))

    # nsmallest/nlargest
    df = pd.DataFrame({
        'group': ['A', 'A', 'B', 'B', 'C'],
        'value': [10, 20, 15, 25, 30]
    })

    print(f"\n原始数据:")
    print(df)

    print(f"\nnlargest(3, 'value') - 最大的3个:")
    print(df.nlargest(3, 'value'))

    print(f"\nnsmallest(3, 'value') - 最小的3个:")
    print(df.nsmallest(3, 'value'))

    # groupby 中的应用
    print(f"\ngroupby + nlargest:")
    print(df.groupby('group').nlargest(2, 'value'))

    print(f"\ngroupby + nsmallest:")
    print(df.groupby('group').nsmallest(1, 'value'))

    # query 补充
    df = pd.DataFrame({
        'A': range(10),
        'B': range(10, 20),
        'C': range(20, 30)
    })

    print(f"\nquery('A > 5 and B < 15'):")
    print(df.query('A > 5 and B < 15'))

    # 引用变量
    threshold = 25
    print(f"\nquery('C < @threshold') - 使用变量:")
    print(df.query('C < @threshold'))

    print("\n" + "=" * 60)
    print("12. 实用技巧")
    print("=" * 60)

    print("\n技巧1: 链式方法")
    df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
    result = (df
        .assign(doubled=df['value'] * 2)
        .assign(tripled=df['value'] * 3)
        .query('value > 2')
        .reset_index(drop=True)
    )
    print(result)

    print("\n技巧2: pipe 使用")
    def add_n(df, n):
        return df + n

    print(f"\npipe(add_n, n=10):")
    print(df[['value']].pipe(add_n, n=10))

    print("\n技巧3: assign 使用")
    print(f"\nassign(new_col=df['value'] * 2):")
    print(df.assign(new_col=df['value'] * 2))

    print("\n技巧4: filter 方法")
    print(f"\nfilter(lambda x: x > 2, df['value']):")
    print(df.filter(lambda x: x > 2, items=['value']))

    print("\n技巧5: transform 方法")
    print(f"\ndf.transform('abs'):")
    print(df[['value']].transform('abs'))

    print(f"\ndf.transform([lambda x: x + 1, lambda x: x * 2]):")
    print(df[['value']].transform([lambda x: x + 1, lambda x: x * 2]))

    print("\n" + "=" * 60)
    print("13. 方法速查")
    print("=" * 60)

    methods = {
        'corr()': '相关系数矩阵',
        'cov()': '协方差矩阵',
        'corrwith()': '与单个 Series 的相关性',
        'rank()': '排名 (average/min/max/dense/first)',
        'pct_change()': '百分比变化',
        'shift()': '数据移位',
        'tshift()': '时间索引平移',
        'diff()': '差分',
        'cummax()': '累计最大值',
        'cummin()': '累计最小值',
        'cumsum()': '累计和',
        'cumprod()': '累计积',
        'expanding()': '累计窗口',
        'ffill()': '向前填充',
        'bfill()': '向后填充',
        'explode()': '展开列表',
        'get_dummies()': '独热编码',
        'sample()': '随机抽样',
        'nlargest()': '最大N个',
        'nsmallest()': '最小N个',
        'query()': '查询过滤',
        'filter()': '过滤',
        'transform()': '转换',
        'pipe()': '管道操作',
    }

    print("\nDataFrame/Series 方法:")
    for method, desc in methods.items():
        print(f"  {method:20s} # {desc}")


if __name__ == "__main__":
    main()