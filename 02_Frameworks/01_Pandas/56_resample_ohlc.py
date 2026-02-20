#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 56：Resample OHLC - 金融数据重采样。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/56_resample_ohlc.py

OHLC (Open-High-Low-Close) 是金融数据分析中最重要的重采样方法之一。
它将时间序列数据聚合为开、高、低、收四个价格点。

本节演示：
1. OHLC 重采样基础
2. 创建模拟价格数据
3. 不同时间周期的 OHLC
4. OHLC 与其他聚合结合
5. 金融分析实际应用
6. Volume 加权平均价格 (VWAP)
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def create_sample_price_data(n_days: int = 30) -> pd.DataFrame:
    """创建模拟价格数据"""
    # 创建日期范围（交易日）
    dates = pd.bdate_range(start='2024-01-01', periods=n_days * 78)  # 假设每天 78 个 5 分钟

    # 创建日内数据（每 5 分钟）
    n_points = len(dates)

    # 模拟价格走势（随机游走）
    np.random.seed(42)
    returns = np.random.normal(0.0002, 0.02, n_points)
    price = 100 * np.cumprod(1 + returns)

    # 模拟成交量
    volume = np.random.randint(1000, 10000, n_points)

    df = pd.DataFrame({
        'datetime': dates,
        'price': price,
        'volume': volume
    })
    df.set_index('datetime', inplace=True)

    return df


def main() -> None:
    print("=" * 60)
    print("1. OHLC 重采样基础")
    print("=" * 60)

    # 创建简单的日内数据
    dates = pd.date_range('2024-01-01 09:30', '2024-01-01 16:00', freq='5min')
    np.random.seed(42)
    prices = 100 + np.cumsum(np.random.randn(len(dates)) * 0.5)

    df = pd.DataFrame({
        'price': prices,
        'volume': np.random.randint(100, 1000, len(dates))
    }, index=dates)

    print("\n原始 5 分钟数据 (前 15 行):")
    print(df.head(15))

    # OHLC 重采样到 30 分钟
    print("\n重采样到 30 分钟 OHLC:")
    ohlc_30min = df['price'].resample('30min').ohlc()
    print(ohlc_30min)

    # 解释 OHLC 含义
    print("\nOHLC 含义:")
    print("  Open (开): 该时段第一个价格")
    print("  High (高): 该时段最高价格")
    print("  Low (低): 该时段最低价格")
    print("  Close (收): 该时段最后一个价格")

    print("\n" + "=" * 60)
    print("2. 不同时间周期的 OHLC")
    print("=" * 60)

    # 使用更长的时间序列
    df_daily = create_sample_price_data(5)  # 5 个交易日

    print(f"\n数据范围: {df_daily.index.min()} 到 {df_daily.index.max()}")
    print(f"数据点数: {len(df_daily)}")

    # 5 分钟 -> 1 小时
    print("\n1 小时 OHLC:")
    ohlc_1h = df_daily['price'].resample('1h').ohlc()
    print(ohlc_1h.head())

    # 5 分钟 -> 1 天
    print("\n日 OHLC:")
    ohlc_1d = df_daily['price'].resample('1D').ohlc()
    print(ohlc_1d)

    # 周 OHLC
    print("\n周 OHLC:")
    ohlc_1w = df_daily['price'].resample('1W').ohlc()
    print(ohlc_1w)

    print("\n" + "=" * 60)
    print("3. OHLC 成交量分析")
    print("=" * 60)

    # 价格 OHLC
    price_ohlc = df_daily['price'].resample('1h').ohlc()

    # 成交量求和
    volume_sum = df_daily['volume'].resample('1h').sum()

    # 成交笔数
    volume_count = df_daily['volume'].resample('1h').count()

    # 合并
    combined = pd.concat([price_ohlc, volume_sum, volume_count], axis=1)
    combined.columns = ['open', 'high', 'low', 'close', 'volume', 'count']

    print("\n价格 + 成交量（1 小时）:")
    print(combined.head())

    print("\n" + "=" * 60)
    print("4. OHLC 与其他聚合结合")
    print("=" * 60)

    # 创建包含多列的数据
    df_multi = pd.DataFrame({
        'bid': 100 + np.random.randn(100).cumsum() * 0.1,
        'ask': 100.2 + np.random.randn(100).cumsum() * 0.1,
        'volume': np.random.randint(100, 1000, 100)
    }, index=pd.date_range('2024-01-01', periods=100, freq='10min'))

    print("\n原始数据:")
    print(df_multi.head(10))

    # 对每列单独聚合
    print("\n重采样（30 分钟）:")
    resampled = df_multi.resample('30min').agg({
        'bid': 'ohlc',      # bid 使用 OHLC
        'ask': 'ohlc',      # ask 使用 OHLC
        'volume': 'sum'     # volume 求和
    })
    print(resampled.head())

    print("\n" + "=" * 60)
    print("5. 金融分析：K 线图数据准备")
    print("=" * 60)

    # 创建日内数据
    dates = pd.date_range('2024-01-02 09:30', '2024-01-02 16:00', freq='1min')
    np.random.seed(42)
    base_price = 100
    noise = np.random.randn(len(dates)) * 0.05
    trend = np.linspace(0, 2, len(dates))
    prices = base_price + trend + noise

    df_intraday = pd.DataFrame({'price': prices}, index=dates)

    print(f"\n数据点数: {len(df_intraday)}")
    print(f"时间范围: {df_intraday.index.min()} 到 {df_intraday.index.max()}")

    # 5 分钟 K 线
    kline_5min = df_intraday['price'].resample('5min').ohlc()
    print("\n5 分钟 K 线数据:")
    print(kline_5min)

    # 15 分钟 K 线
    kline_15min = df_intraday['price'].resample('15min').ohlc()
    print("\n15 分钟 K 线数据:")
    print(kline_15min)

    # 30 分钟 K 线
    kline_30min = df_intraday['price'].resample('30min').ohlc()
    print("\n30 分钟 K 线数据:")
    print(kline_30min)

    # 计算涨跌
    kline_30min['change'] = kline_30min['close'] - kline_30min['open']
    kline_30min['pct_change'] = (kline_30min['change'] / kline_30min['open']) * 100
    print("\n30 分钟 K 线（含涨跌）:")
    print(kline_30min)

    print("\n" + "=" * 60)
    print("6. Volume Weighted Average Price (VWAP)")
    print("=" * 60)

    # VWAP = Sum(Price * Volume) / Sum(Volume)
    df = pd.DataFrame({
        'price': [100.5, 100.8, 101.0, 100.7, 100.9],
        'volume': [1000, 1500, 800, 1200, 900]
    })

    print("\n逐笔数据:")
    print(df)

    # 计算 VWAP
    vwap = (df['price'] * df['volume']).sum() / df['volume'].sum()
    print(f"\nVWAP: {vwap:.2f}")
    print(f"平均价格: {df['price'].mean():.2f}")
    print(f"收盘价: {df['price'].iloc[-1]:.2f}")

    # 使用 resample 计算 VWAP
    dates = pd.date_range('2024-01-01 09:30', periods=20, freq='5min')
    df_time = pd.DataFrame({
        'price': 100 + np.random.randn(20) * 0.5,
        'volume': np.random.randint(500, 2000, 20)
    }, index=dates)

    print("\n\n时间序列数据:")
    print(df_time)

    # 15 分钟 VWAP
    def calculate_vwap(group):
        return (group['price'] * group['volume']).sum() / group['volume'].sum()

    vwap_15min = df_time.resample('15min').apply(calculate_vwap)
    vwap_15min.name = 'vwap'

    # 15 分钟 OHLC
    ohlc_15min = df_time['price'].resample('15min').ohlc()

    # 合并
    result = pd.concat([ohlc_15min, vwap_15min], axis=1)
    print("\n15 分钟 OHLC + VWAP:")
    print(result)

    print("\n" + "=" * 60)
    print("7. 实际应用案例")
    print("=" * 60)

    print("\n案例1: 日内交易分析")
    print("-" * 40)

    # 创建一个交易日的数据
    dates = pd.date_range('2024-01-15 09:30', '2024-01-15 16:00', freq='5min')
    # 模拟价格：开盘上涨，中午下跌，尾盘回升
    t = np.linspace(0, 2*np.pi, len(dates))
    base = 100
    pattern = 2 * np.sin(t) + 0.5 * np.sin(3*t)  # 主趋势 + 波动
    noise = np.random.randn(len(dates)) * 0.3
    prices = base + pattern + noise

    df_trading = pd.DataFrame({'price': prices}, index=dates)

    # 30 分钟 K 线
    klines = df_trading['price'].resample('30min').ohlc()

    print("30 分钟 K 线:")
    print(klines)

    # 计算技术指标
    klines['range'] = klines['high'] - klines['low']  # 价格振幅
    klines['body'] = abs(klines['close'] - klines['open'])  # K 线实体
    klines['trend'] = np.where(klines['close'] > klines['open'], 'up', 'down')

    print("\n技术指标:")
    print(klines)

    print("\n案例2: 多日数据汇总")
    print("-" * 40)

    # 创建多日数据
    multi_day = create_sample_price_data(10)

    # 日线 OHLC
    daily_ohlc = multi_day['price'].resample('1D').ohlc()
    daily_volume = multi_day['volume'].resample('1D').sum()

    daily_summary = pd.concat([daily_ohlc, daily_volume], axis=1)
    daily_summary.columns = ['open', 'high', 'low', 'close', 'volume']

    print("\n日线汇总:")
    print(daily_summary)

    print("\n案例3: 缺口分析")
    print("-" * 40)

    # 检测价格跳空
    daily_summary['prev_close'] = daily_summary['close'].shift(1)
    daily_summary['gap'] = daily_summary['open'] - daily_summary['prev_close']
    daily_summary['gap_pct'] = (daily_summary['gap'] / daily_summary['prev_close']) * 100

    print("\n缺口分析:")
    print(daily_summary[['open', 'close', 'prev_close', 'gap', 'gap_pct']])

    # 找出显著缺口
    significant_gaps = daily_summary[abs(daily_summary['gap_pct']) > 1]
    print(f"\n显著缺口 (>1%):")
    print(significant_gaps[['open', 'close', 'gap_pct']])

    print("\n" + "=" * 60)
    print("8. OHLC 速查")
    print("=" * 60)

    print("\n重采样频率别名:")
    aliases = {
        'B': '工作日频率',
        'D': '日历日频率',
        'W': '周频率',
        'M': '月末频率',
        'Q': '季度末频率',
        'Y': '年末频率',
        'H': '小时频率',
        'T, min': '分钟频率',
        'S': '秒频率',
    }

    for alias, desc in aliases.items():
        print(f"  {alias:10s} # {desc}")

    print("\n常用 OHLC 模式:")
    print("  df['price'].resample('5min').ohlc()           # 基础 OHLC")
    print("  df.resample('1D').agg({'price': 'ohlc',       # 多列聚合")
    print("                         'volume': 'sum'})")
    print("  (df['price'] * df['volume']).sum() / df['volume'].sum()  # VWAP")

    print("\n技术指标计算:")
    print("  klines['range'] = high - low                   # 振幅")
    print("  klines['body'] = abs(close - open)            # 实体")
    print("  klines['trend'] = close > open                 # 涨跌")

    print("\n" + "=" * 60)
    print("9. 注意事项")
    print("=" * 60)

    print("\n重采样注意事项:")
    print("  1. 确保索引是 DatetimeIndex")
    print("  2. 使用 closed 参数控制区间边界 ('left', 'right')")
    print("  3. 使用 label 参数控制结果标签位置")
    print("  4. 缺失数据会影响 OHLC 计算")
    print("  5. 对于金融数据，注意处理非交易时段")

    # 演示 closed 和 label 参数
    df_sample = pd.DataFrame({
        'value': [1, 2, 3, 4, 5, 6, 7, 8]
    }, index=pd.date_range('2024-01-01', periods=8, freq='30min'))

    print("\n\nclosed 和 label 参数示例:")
    print("原始数据:")
    print(df_sample)

    print("\nclosed='left', label='left' (默认):")
    print(df_sample.resample('1h', closed='left', label='left').ohlc())

    print("\nclosed='right', label='right':")
    print(df_sample.resample('1h', closed='right', label='right').ohlc())


if __name__ == "__main__":
    main()