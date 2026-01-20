#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 53：窗口函数参数详解。

运行：
    python3 02_Frameworks/01_Pandas/53_window_params_complete.py

知识点：
- rolling 参数：window/min_periods/center/closed/on/axis/method
- expanding 参数：min_periods/center/axis/method
- ewm 参数：alpha/com/span/halflife/adjust/ignore_na/axis/method
- 成对滚动窗口：rolling().cov/rolling().corr
- 自定义窗口函数：apply
- 时间序列窗口：offset/窗口频率
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    # 创建示例数据
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=20, freq="D")
    df = pd.DataFrame(
        {"value": np.random.randn(20).cumsum(), "value2": np.random.randn(20).cumsum()},
        index=dates,
    )

    print("=" * 70)
    print("原始数据")
    print("=" * 70)
    print(df.head(10))

    print("\n" + "=" * 70)
    print("1. Rolling 参数详解")
    print("=" * 70)

    print("\n1.1 window - 窗口大小")
    print("-" * 70)

    # 整数窗口
    print("rolling(window=3).mean() ->")
    print(df["value"].rolling(window=3).mean().head(10))

    # 偏移窗口（时间序列）
    print("\nrolling(window='3D').mean() (3天窗口) ->")
    print(df["value"].rolling(window="3D").mean().head(10))

    print("\n1.2 min_periods - 最小观测值数")
    print("-" * 70)

    print("rolling(window=5, min_periods=1).mean() ->")
    print("允许窗口内的非空值少到1个就计算")
    print(df["value"].rolling(window=5, min_periods=1).mean().head(10))

    print("\nrolling(window=5, min_periods=3).mean() ->")
    print("至少需要3个非空值才计算")
    print(df["value"].rolling(window=5, min_periods=3).mean().head(10))

    print("\n1.3 center - 窗口居中")
    print("-" * 70)

    print("rolling(window=5, center=False).mean() (默认，右对齐) ->")
    print(df["value"].rolling(window=5, center=False).mean().head(10))

    print("\nrolling(window=5, center=True).mean() (居中) ->")
    print(df["value"].rolling(window=5, center=True).mean().head(10))

    print("\n1.4 closed - 区间闭合方式")
    print("-" * 70)

    # 创建有索引的数据
    df_idx = pd.DataFrame({"value": range(10)}, index=list("abcdefghij"))
    print("原始数据 ->")
    print(df_idx)

    print("\nrolling(window=3, closed='right').mean() (默认，右闭) ->")
    print(df_idx["value"].rolling(window=3, closed="right").mean())

    print("\nrolling(window=3, closed='left').mean() (左闭) ->")
    print(df_idx["value"].rolling(window=3, closed="left").mean())

    print("\nrolling(window=3, closed='both').mean() (左右都闭) ->")
    print(df_idx["value"].rolling(window=3, closed="both").mean())

    print("\nrolling(window=3, closed='neither').mean() (左右都不闭) ->")
    print(df_idx["value"].rolling(window=3, closed="neither").mean())

    print("\n1.5 on - 选择计算列（多列 DataFrame）")
    print("-" * 70)

    df_multi = pd.DataFrame(
        {"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]}, index=pd.date_range("2024-01-01", periods=5)
    )
    print("原始 DataFrame ->")
    print(df_multi)

    print("\nrolling(window=3, on='A').mean() ->")
    print("基于 A 列的值作为窗口")
    print(df_multi.rolling(window=3, on="A").mean())

    print("\n1.6 axis - 滚动方向")
    print("-" * 70)

    df_axis = pd.DataFrame(np.arange(12).reshape(3, 4), columns=["A", "B", "C", "D"])
    print("原始 DataFrame ->")
    print(df_axis)

    print("\nrolling(window=2, axis=0).mean() (纵向滚动) ->")
    print(df_axis.rolling(window=2, axis=0).mean())

    print("\nrolling(window=2, axis=1).mean() (横向滚动) ->")
    print(df_axis.rolling(window=2, axis=1).mean())

    print("\n1.7 method - 计算方法")
    print("-" * 70)

    print("rolling(window=5, method='single').mean() (默认) ->")
    print("一次计算整个窗口")
    result_single = df["value"].rolling(window=5, method="single").mean()
    print(result_single.head(10))

    print("\nrolling(window=5, method='table').mean() ->")
    print("使用表方法，可能更快但需要更多内存")
    result_table = df["value"].rolling(window=5, method="table").mean()
    print(result_table.head(10))

    print("\n" + "=" * 70)
    print("2. Expanding 参数详解")
    print("=" * 70)

    print("expanding().sum() (累积求和) ->")
    print(df["value"].expanding().sum().head(10))

    print("\n2.1 min_periods")
    print("-" * 70)

    print("expanding(min_periods=1).mean() ->")
    print(df["value"].expanding(min_periods=1).mean().head(10))

    print("\nexpanding(min_periods=5).mean() ->")
    print(df["value"].expanding(min_periods=5).mean().head(10))

    print("\n2.2 center")
    print("-" * 70)

    print("expanding(center=True).mean() ->")
    print(df["value"].expanding(center=True).mean().head(10))

    print("\n2.3 axis")
    print("-" * 70)

    print("DataFrame 上 expanding(axis=1).mean() ->")
    print(df_axis.expanding(axis=1).mean())

    print("\n2.4 method")
    print("-" * 70)

    print("expanding(method='single').std() ->")
    print(df["value"].expanding(method="single").std().head(10))

    print("\n" + "=" * 70)
    print("3. EWM (指数加权移动) 参数详解")
    print("=" * 70)

    print("\n3.1 alpha - 平滑系数（直接指定）")
    print("-" * 70)

    print("ewm(alpha=0.3).mean() ->")
    print(df["value"].ewm(alpha=0.3).mean().head(10))

    print("\n3.2 com - 衰减系数（中心质量）")
    print("-" * 70)

    print("ewm(com=0.5).mean() ->")
    print("alpha = 1 / (1 + com) = 1 / 1.5 ≈ 0.667")
    print(df["value"].ewm(com=0.5).mean().head(10))

    print("\n3.3 span - 跨度")
    print("-" * 70)

    print("ewm(span=3).mean() ->")
    print("alpha = 2 / (span + 1) = 2 / 4 = 0.5")
    print(df["value"].ewm(span=3).mean().head(10))

    print("\n3.4 halflife - 半衰期")
    print("-" * 70)

    print("ewm(halflife='3D').mean() ->")
    print("alpha = 1 - exp(log(0.5) / halflife)")
    print(df["value"].ewm(halflife="3D").mean().head(10))

    print("\n3.5 adjust - 递归公式调整")
    print("-" * 70)

    print("ewm(alpha=0.5, adjust=True).mean() ->")
    print("使用递归公式，考虑历史所有数据")
    print(df["value"].ewm(alpha=0.5, adjust=True).mean().head(10))

    print("\newm(alpha=0.5, adjust=False).mean() ->")
    print("简化公式，只考虑窗口内数据")
    print(df["value"].ewm(alpha=0.5, adjust=False).mean().head(10))

    print("\n3.6 ignore_na - 忽略 NaN")
    print("-" * 70)

    s_na = pd.Series([1, np.nan, 3, 4, 5])
    print(f"带 NaN 的数据: {s_na.tolist()}")

    print("\newm(alpha=0.5, ignore_na=False).mean() ->")
    print(s_na.ewm(alpha=0.5, ignore_na=False).mean())

    print("\newm(alpha=0.5, ignore_na=True).mean() ->")
    print(s_na.ewm(alpha=0.5, ignore_na=True).mean())

    print("\n" + "=" * 70)
    print("4. 窗口聚合函数")
    print("=" * 70)

    print("4.1 常用统计函数")
    print("-" * 70)

    print("rolling(window=5) ->")
    rolling = df["value"].rolling(window=5)
    print(f"  .mean() -> {rolling.mean().iloc[4]:.4f}")
    print(f"  .std() -> {rolling.std().iloc[4]:.4f}")
    print(f"  .var() -> {rolling.var().iloc[4]:.4f}")
    print(f"  .min() -> {rolling.min().iloc[4]:.4f}")
    print(f"  .max() -> {rolling.max().iloc[4]:.4f}")
    print(f"  .median() -> {rolling.median().iloc[4]:.4f}")
    print(f"  .sum() -> {rolling.sum().iloc[4]:.4f}")
    print(f"  .count() -> {rolling.count().iloc[4]}")

    print("\n4.2 分位数函数")
    print("-" * 70)

    print("rolling(window=5).quantile(0.25) ->")
    print(df["value"].rolling(window=5).quantile(0.25).head(10))

    print("\nrolling(window=5).quantile([0.25, 0.5, 0.75]) ->")
    print(df["value"].rolling(window=5).quantile([0.25, 0.5, 0.75]).head(10))

    print("\n4.3 应用自定义函数")
    print("-" * 70)

    print("rolling(window=5).apply(lambda x: x.max() - x.min()) ->")
    print(df["value"].rolling(window=5).apply(lambda x: x.max() - x.min()).head(10))

    print("\nrolling(window=5).apply(lambda x: (x > x.mean()).sum()) ->")
    print("计算窗口内大于均值的个数")
    print(df["value"].rolling(window=5).apply(lambda x: (x > x.mean()).sum()).head(10))

    print("\n" + "=" * 70)
    print("5. 成对滚动窗口（Pairwise Rolling）")
    print("=" * 70)

    print("5.1 滚动协方差")
    print("-" * 70)

    print("rolling(window=5).cov(df['value2']) ->")
    print(df["value"].rolling(window=5).cov(df["value2"]).head(10))

    print("\n5.2 滚动相关系数")
    print("-" * 70)

    print("rolling(window=5).corr(df['value2']) ->")
    print(df["value"].rolling(window=5).corr(df["value2"]).head(10))

    print("\n5.3 DataFrame 的滚动相关")
    print("-" * 70)

    print("df.rolling(window=5).corr() ->")
    print(df.rolling(window=5).corr().head(15))

    print("\n" + "=" * 70)
    print("6. 时间序列特有参数")
    print("=" * 70)

    # 创建时间序列数据（工作日）
    dates_work = pd.bdate_range("2024-01-01", periods=10)
    df_work = pd.DataFrame({"value": range(10)}, index=dates_work)

    print("工作日数据 ->")
    print(df_work)

    print("\n6.1 使用时间偏移作为窗口")
    print("-" * 70)

    print("rolling(window='3D').mean() ->")
    print(df_work.rolling(window="3D").mean())

    print("\n6.2 closed 参数与时间窗口")
    print("-" * 70)

    print("rolling(window='3D', closed='right').mean() ->")
    print(df_work.rolling(window="3D", closed="right").mean())

    print("\nrolling(window='3D', closed='left').mean() ->")
    print(df_work.rolling(window="3D", closed="left").mean())

    print("\nrolling(window='3D', closed='both').mean() ->")
    print(df_work.rolling(window="3D", closed="both").mean())

    print("\n6.3 origin - 窗口起点设置")
    print("-" * 70)

    print("df.resample('D').mean() ->")
    print(df_work.resample("D").mean().head(10))

    print("\ndf.resample('D', origin='epoch').mean() ->")
    print("从 Unix 时间戳起点开始")
    print(df_work.resample("D", origin="epoch").mean().head(10))

    print("\ndf.resample('D', origin='start').mean() ->")
    print("从数据起点开始")
    print(df_work.resample("D", origin="start").mean().head(10))

    print("\ndf.resample('D', origin='start_day').mean() ->")
    print("从每天起点开始")
    print(df_work.resample("D", origin="start_day").mean().head(10))

    print("\n" + "=" * 70)
    print("7. 实际应用示例")
    print("=" * 70)

    # 示例 1: 金融数据移动平均
    print("示例 1: 金融技术指标")
    prices = pd.Series(
        [100, 102, 105, 103, 107, 110, 108, 112, 115, 113, 118, 120],
        index=pd.date_range("2024-01-01", periods=12),
    )

    # 简单移动平均
    sma_5 = prices.rolling(window=5).mean()
    # 指数移动平均
    ema_5 = prices.ewm(span=5).mean()
    # 布林带
    sma_20 = prices.rolling(window=5).mean()
    std_20 = prices.rolling(window=5).std()
    upper_band = sma_20 + 2 * std_20
    lower_band = sma_20 - 2 * std_20

    result = pd.DataFrame({"价格": prices, "SMA5": sma_5, "EMA5": ema_5, "上轨": upper_band, "下轨": lower_band})
    print(result)

    # 示例 2: 检测异常值（移动标准差）
    print("\n示例 2: 基于移动标准差检测异常")
    values = pd.Series([10, 11, 10, 12, 11, 10, 25, 11, 10, 12])  # 25 是异常值
    rolling_mean = values.rolling(window=3).mean()
    rolling_std = values.rolling(window=3).std()
    # 超过 3 个标准差认为是异常
    anomalies = values[np.abs(values - rolling_mean) > 3 * rolling_std]
    print(f"检测到的异常值位置和值: {anomalies.to_dict()}")

    # 示例 3: 滚动回归统计
    print("\n示例 3: 滚动相关系数")
    df_stock = pd.DataFrame(
        {"stock_a": [100, 101, 102, 103, 104, 105], "stock_b": [50, 51, 50, 52, 51, 53]},
        index=pd.date_range("2024-01-01", periods=6),
    )
    print("股票价格数据 ->")
    print(df_stock)

    rolling_corr = df_stock["stock_a"].rolling(window=3).corr(df_stock["stock_b"])
    print("\n滚动相关系数(窗口3) ->")
    print(rolling_corr)

    print("\n" + "=" * 70)
    print("8. 性能提示")
    print("=" * 70)

    print("""
性能优化建议：
1. 使用 method='table' 可以提高大数据集的性能
2. 对于时间序列，使用时间偏移（如 '3D'）比整数窗口更准确
3. 成对操作（cov/corr）计算量较大，注意窗口大小
4. 自定义 apply 函数通常比内置函数慢，优先使用内置函数
5. 只需要单个值时，考虑使用 expanding() 而不是 rolling(window=n)
""")


if __name__ == "__main__":
    main()
