#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 54：计算工具全集。

运行：
    python3 02_Frameworks/01_Pandas/54_calculation_tools_complete.py

知识点：
- 累积函数：cumsum/cummax/cummin/cumprod
- 分位数：percentile/quantile/median
- 统计函数：mad/kurt/skew/sem/std/var
- 排名：rank（所有 method）
- 变化率：pct_change 详细参数
- 差分：diff
- 其他：abs/clip/round
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "B": [10, 20, 15, 25, 20, 30, 25, 35, 30, 40],
            "C": [5, 3, 8, 2, 9, 1, 7, 4, 6, 0],
        }
    )

    print("=" * 70)
    print("原始数据")
    print("=" * 70)
    print(df)

    print("\n" + "=" * 70)
    print("1. 累积函数")
    print("=" * 70)

    print("\n1.1 cumsum - 累积和")
    print("-" * 70)
    print("cumsum() ->")
    print(df[["A", "B", "C"]].cumsum())

    print("\ncumsum(axis=1) ->")
    print(df[["A", "B", "C"]].cumsum(axis=1))

    print("\n1.2 cummax - 累积最大值")
    print("-" * 70)
    print("cummax() ->")
    print(df[["A", "B", "C"]].cummax())

    print("\ncummax(axis=1) ->")
    print(df[["A", "B", "C"]].cummax(axis=1))

    print("\n1.3 cummin - 累积最小值")
    print("-" * 70)
    print("cummin() ->")
    print(df[["A", "B", "C"]].cummin())

    print("\n1.4 cumprod - 累积乘积")
    print("-" * 70)
    df_prod = pd.DataFrame({"A": [1, 2, 3, 4], "B": [2, 2, 2, 2]})
    print("原始数据 ->")
    print(df_prod)

    print("\ncumprod() ->")
    print(df_prod.cumprod())

    print("\n1.5 累积函数与 NaN")
    print("-" * 70)
    df_nan = pd.DataFrame({"A": [1, np.nan, 3, 4, np.nan, 6]})
    print("含 NaN 数据 ->")
    print(df_nan)

    print("\ncumsum() 默认跳过 NaN ->")
    print(df_nan.cumsum())

    print("\ncumsum(skipna=False) ->")
    print(df_nan.cumsum(skipna=False))

    print("\n" + "=" * 70)
    print("2. 分位数函数")
    print("=" * 70)

    print("\n2.1 quantile - 分位数")
    print("-" * 70)

    print("quantile(0.25) ->")
    print(df.quantile(0.25))

    print("\nquantile(0.5) ->")
    print(df.quantile(0.5))

    print("\nquantile([0.25, 0.5, 0.75]) ->")
    print(df.quantile([0.25, 0.5, 0.75]))

    print("\nquantile(0.5, axis=1) ->")
    print(df[["A", "B", "C"]].quantile(0.5, axis=1))

    print("\nquantile(0.5, interpolation='linear') ->")
    print("linear: 线性插值（默认）")
    print(df.quantile(0.5, interpolation="linear"))

    print("\nquantile(0.5, interpolation='lower') ->")
    print("lower: 向下取整")
    print(df.quantile(0.5, interpolation="lower"))

    print("\nquantile(0.5, interpolation='higher') ->")
    print("higher: 向上取整")
    print(df.quantile(0.5, interpolation="higher"))

    print("\nquantile(0.5, interpolation='midpoint') ->")
    print("midpoint: 中点值")
    print(df.quantile(0.5, interpolation="midpoint"))

    print("\nquantile(0.5, interpolation='nearest') ->")
    print("nearest: 最近值")
    print(df.quantile(0.5, interpolation="nearest"))

    print("\n2.2 percentile - 百分位数")
    print("-" * 70)

    print("percentile(25) ->")
    print(df[["A", "B", "C"]].percentile(25))

    print("\npercentile([25, 50, 75]) ->")
    print(df[["A", "B", "C"]].percentile([25, 50, 75]))

    print("\n2.3 median - 中位数")
    print("-" * 70)

    print("median() ->")
    print(df.median())

    print("\nmedian(axis=1) ->")
    print(df[["A", "B", "C"]].median(axis=1))

    print("\nmedian(skipna=False) ->")
    df_with_nan = df.copy()
    df_with_nan.loc[2, "B"] = np.nan
    print(df_with_nan.median(skipna=False))

    print("\n" + "=" * 70)
    print("3. 统计描述函数")
    print("=" * 70)

    print("\n3.1 mad - 平均绝对偏差")
    print("-" * 70)
    print("mad() ->")
    print(df.mad())

    print("\nmad(axis=1) ->")
    print(df[["A", "B", "C"]].mad(axis=1))

    print("\n3.2 kurt - 峰度（Kurtosis）")
    print("-" * 70)
    print("kurt() ->")
    print(df.kurt())

    print("\nkurt(axis=1) ->")
    print(df[["A", "B", "C"]].kurt(axis=1))

    print("\nkurt(fisher=False) ->")
    print("fisher=False 表示使用峰度（而非超额峰度）")
    print(df.kurt(fisher=False))

    print("\n3.3 skew - 偏度")
    print("-" * 70)
    print("skew() ->")
    print(df.skew())

    print("\nskew(axis=1) ->")
    print(df[["A", "B", "C"]].skew(axis=1))

    print("\nskew(bias=False) ->")
    print("bias=False 表示使用无偏估计")
    print(df.skew(bias=False))

    print("\n3.4 sem - 标准误差（Standard Error of Mean）")
    print("-" * 70)
    print("sem() ->")
    print(df.sem())

    print("\nsem(axis=1) ->")
    print(df[["A", "B", "C"]].sem(axis=1))

    print("\nsem(ddof=1) ->")
    print("ddof: Delta Degrees of Freedom，默认为1")
    print(df.sem(ddof=1))

    print("\n3.5 std - 标准差")
    print("-" * 70)
    print("std() ->")
    print(df.std())

    print("\nstd(ddof=0) ->")
    print("ddof=0 表示总体标准差（而非样本标准差）")
    print(df.std(ddof=0))

    print("\nstd(ddof=1) ->")
    print("ddof=1 表示样本标准差（默认）")
    print(df.std(ddof=1))

    print("\n3.6 var - 方差")
    print("-" * 70)
    print("var() ->")
    print(df.var())

    print("\nvar(ddof=0) ->")
    print(df.var(ddof=0))

    print("\n" + "=" * 70)
    print("4. 排名函数")
    print("=" * 70)

    df_rank = pd.DataFrame({"score": [100, 100, 95, 90, 90, 85], "name": ["A", "B", "C", "D", "E", "F"]})

    print("\n原始数据 ->")
    print(df_rank)

    print("\n4.1 rank(method='average') - 平均排名（默认）")
    print("-" * 70)
    print("rank(method='average') ->")
    print(df_rank["score"].rank(method="average"))

    print("\n4.2 rank(method='min') - 最小排名")
    print("-" * 70)
    print("rank(method='min') ->")
    print(df_rank["score"].rank(method="min"))

    print("\n4.3 rank(method='max') - 最大排名")
    print("-" * 70)
    print("rank(method='max') ->")
    print(df_rank["score"].rank(method="max"))

    print("\n4.4 rank(method='dense') - 密集排名（不跳过名次）")
    print("-" * 70)
    print("rank(method='dense') ->")
    print(df_rank["score"].rank(method="dense"))

    print("\n4.5 rank(method='first') - 先到先得")
    print("-" * 70)
    print("rank(method='first') ->")
    print(df_rank["score"].rank(method="first"))

    print("\n4.6 ascending 参数")
    print("-" * 70)
    print("rank(ascending=False) ->")
    print(df_rank["score"].rank(ascending=False))

    print("\n4.7 na_option 参数（处理 NaN）")
    print("-" * 70)
    df_rank_nan = pd.DataFrame({"score": [100, np.nan, 95, 90, np.nan, 85]})
    print("含 NaN 数据 ->")
    print(df_rank_nan)

    print("\nrank(na_option='keep') ->")
    print("keep: 保持 NaN")
    print(df_rank_nan["score"].rank(na_option="keep"))

    print("\nrank(na_option='top') ->")
    print("top: NaN 排在最前")
    print(df_rank_nan["score"].rank(na_option="top"))

    print("\nrank(na_option='bottom') ->")
    print("bottom: NaN 排在最后")
    print(df_rank_nan["score"].rank(na_option="bottom"))

    print("\n4.8 pct 参数（返回百分比排名）")
    print("-" * 70)
    print("rank(pct=True) ->")
    print(df_rank["score"].rank(pct=True))

    print("\n" + "=" * 70)
    print("5. 变化率函数")
    print("=" * 70)

    df_prices = pd.DataFrame(
        {"price": [100, 102, 101, 105, 107, 106, 110]}, index=pd.date_range("2024-01-01", periods=7)
    )

    print("\n原始价格数据 ->")
    print(df_prices)

    print("\n5.1 pct_change - 百分比变化")
    print("-" * 70)

    print("pct_change() ->")
    print(df_prices["price"].pct_change())

    print("\npct_change(periods=2) ->")
    print("计算与前2期的变化率")
    print(df_prices["price"].pct_change(periods=2))

    print("\npct_change(fill_method=None) ->")
    print("不填充 NaN")
    print(df_prices["price"].pct_change(fill_method=None))

    print("\npct_change(freq='M') ->")
    print("按频率计算（需要时间序列索引）")

    print("\n5.2 diff - 差分")
    print("-" * 70)

    print("diff() ->")
    print(df_prices["price"].diff())

    print("\ndiff(periods=2) ->")
    print(df_prices["price"].diff(periods=2))

    print("\ndiff(axis=0) ->")
    print("纵向差分（默认）")

    print("\n5.3 shift - 位移")
    print("-" * 70)

    print("shift(1) ->")
    print(df_prices["price"].shift(1))

    print("\nshift(-1) ->")
    print(df_prices["price"].shift(-1))

    print("\nshift(periods=2, fill_value=0) ->")
    print(df_prices["price"].shift(periods=2, fill_value=0))

    print("\n" + "=" * 70)
    print("6. 其他计算函数")
    print("=" * 70)

    df_other = pd.DataFrame({"A": [-1.5, 2.3, -3.7, 4.1, -5.9], "B": [10, 20, 30, 40, 50]})

    print("\n原始数据 ->")
    print(df_other)

    print("\n6.1 abs - 绝对值")
    print("-" * 70)
    print("abs() ->")
    print(df_other[["A", "B"]].abs())

    print("\n6.2 clip - 裁剪值")
    print("-" * 70)
    print("clip(lower=-2, upper=2) ->")
    print(df_other["A"].clip(lower=-2, upper=2))

    print("\nclip(lower=15, upper=35) ->")
    print(df_other["B"].clip(lower=15, upper=35))

    print("\n6.3 round - 四舍五入")
    print("-" * 70)
    df_round = pd.DataFrame({"A": [1.234, 2.567, 3.891], "B": [10.111, 20.555, 30.999]})
    print("原始数据 ->")
    print(df_round)

    print("\nround() ->")
    print(df_round.round())

    print("\nround(decimals=1) ->")
    print(df_round.round(decimals=1))

    print("\nround({'A': 1, 'B': 2}) ->")
    print(df_round.round({"A": 1, "B": 2}))

    print("\n6.4 clip_lower / clip_upper (已废弃，使用 clip)")
    print("-" * 70)
    print("推荐使用 clip(lower=) 或 clip(upper=)")

    print("\n" + "=" * 70)
    print("7. 描述性统计")
    print("=" * 70)

    print("\ndescribe() ->")
    print(df.describe())

    print("\ndescribe(percentiles=[0.1, 0.5, 0.9]) ->")
    print(df.describe(percentiles=[0.1, 0.5, 0.9]))

    print("\ndescribe(include='all') ->")
    df_mixed = pd.DataFrame({"num": [1, 2, 3], "str": ["a", "b", "c"]})
    print(df_mixed.describe(include="all"))

    print("\ndescribe(include=[np.number]) ->")
    print(df_mixed.describe(include=[np.number]))

    print("\n" + "=" * 70)
    print("8. 实际应用示例")
    print("=" * 70)

    # 示例 1: 累积回报计算
    print("\n示例 1: 计算累积回报")
    returns = pd.Series([0.01, 0.02, -0.01, 0.03, 0.02])
    print("日回报率 ->")
    print(returns)

    cumulative_returns = (1 + returns).cumprod() - 1
    print("\n累积回报率 ->")
    print(cumulative_returns)

    # 示例 2: 移动排名
    print("\n示例 2: 计算移动排名")
    scores = pd.DataFrame(
        {"name": ["A", "B", "C", "D", "E"], "score": [85, 92, 88, 95, 90]},
        index=pd.date_range("2024-01-01", periods=5),
    )
    print("成绩数据 ->")
    print(scores)

    # 使用 expanding 计算累积排名
    scores["cummax_rank"] = scores["score"].expanding().rank()
    print("\n累积排名 ->")
    print(scores)

    # 示例 3: 检测异常值（基于分位数）
    print("\n示例 3: 基于分位数检测异常值")
    data = pd.DataFrame({"value": np.random.randn(100) * 10 + 50})
    q1 = data["value"].quantile(0.25)
    q3 = data["value"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = data[(data["value"] < lower_bound) | (data["value"] > upper_bound)]
    print(f"Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
    print(f"异常值界限: [{lower_bound:.2f}, {upper_bound:.2f}]")
    print(f"检测到 {len(outliers)} 个异常值")

    # 示例 4: 股票相对强弱指标
    print("\n示例 4: 股票相对强弱（相对均值）")
    prices = pd.DataFrame(
        {"stock": [100, 102, 105, 103, 107, 110]}, index=pd.date_range("2024-01-01", periods=6)
    )
    prices["mean_5"] = prices["stock"].rolling(window=5).mean()
    prices["relative_strength"] = (prices["stock"] / prices["mean_5"] - 1) * 100
    print(prices)

    print("\n" + "=" * 70)
    print("9. 参数速查表")
    print("=" * 70)

    print("""
常用参数速查：

累积函数：
- axis: 0（纵向）/ 1（横向）
- skipna: True（跳过 NaN）/ False

分位数函数：
- q: 分位数（0-1）
- interpolation: linear / lower / higher / midpoint / nearest
- axis: 计算方向

排名函数：
- method: average / min / max / dense / first
- ascending: True / False
- na_option: keep / top / bottom
- pct: True / False

pct_change:
- periods: 前几期
- fill_method: ffill / bfill / None
- limit: 填充限制
- freq: 时间频率

diff:
- periods: 前几期
- axis: 计算方向

shift:
- periods: 移动位数
- freq: 时间频率
- axis: 计算方向
- fill_value: 填充值
""")


if __name__ == "__main__":
    main()
