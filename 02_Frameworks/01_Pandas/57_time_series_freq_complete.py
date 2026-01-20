#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 57：时间序列频率与 asfreq。

运行：
    python3 02_Frameworks/01_Pandas/57_time_series_freq_complete.py

知识点：
- asfreq - 频率转换
- infer_freq - 推断频率
- freq 参数详解（所有别名）
- origin - 窗口起点设置
- bfill/ffill 与频率转换
- freq 与字符串别名对照
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. asfreq - 频率转换")
    print("=" * 70)

    # 创建日频率的时间序列
    dates_daily = pd.date_range("2024-01-01", periods=10, freq="D")
    ts_daily = pd.Series(range(10), index=dates_daily)

    print("原始数据（日频率）:")
    print(ts_daily.head())

    print("\n1.1 转换为小时频率")
    print("-" * 70)
    ts_hourly = ts_daily.asfreq("H")
    print("asfreq('H') -> 转换为小时频率")
    print(ts_hourly.head(15))

    print("\n1.2 转换为月频率")
    print("-" * 70)
    ts_monthly = ts_daily.asfreq("M")
    print("asfreq('M') -> 转换为月末")
    print(ts_monthly)

    print("\n1.3 转换为周频率")
    print("-" * 70)
    ts_weekly = ts_daily.asfreq("W")
    print("asfreq('W') -> 转换为周日（默认）")
    print(ts_weekly)

    print("\n1.4 向前填充和向后填充")
    print("-" * 70)

    # 从日频率转换到小时频率（会产生 NaN）
    ts_to_hourly = ts_daily.asfreq("H")
    print("直接转换（会有 NaN）:")
    print(ts_to_hourly.head(10))

    # 使用向前填充
    ts_ffill = ts_daily.asfreq("H", method="ffill")
    print("\nasfreq('H', method='ffill') -> 前向填充")
    print(ts_ffill.head(10))

    # 使用向后填充
    ts_bfill = ts_daily.asfreq("H", method="bfill")
    print("\nasfreq('H', method='bfill') -> 后向填充")
    print(ts_bfill.head(10))

    # 使用填充值
    ts_fill = ts_daily.asfreq("H", fill_value=0)
    print("\nasfreq('H', fill_value=0) -> 填充 0")
    print(ts_fill.head(10))

    print("\n1.5 how 参数（月末/月初）")
    print("-" * 70)

    ts_daily_month = pd.Series(range(35), index=pd.date_range("2024-01-01", periods=35, freq="D"))

    print("原始数据:")
    print(ts_daily_month.head(10))

    print("\nasfreq('M', how='end') -> 月末（默认）")
    print(ts_daily_month.asfreq("M", how="end"))

    print("\nasfreq('M', how='start') -> 月初")
    print(ts_daily_month.asfreq("M", how="start"))

    print("\n" + "=" * 70)
    print("2. infer_freq - 推断频率")
    print("=" * 70)

    # 创建有规律的日期
    regular_dates = pd.DatetimeIndex(
        ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"]
    )
    inferred_freq = pd.infer_freq(regular_dates)
    print(f"regular_dates: {regular_dates.tolist()}")
    print(f"infer_freq -> {inferred_freq}")

    # 工作日频率
    business_dates = pd.bdate_range("2024-01-01", periods=5)
    inferred_freq = pd.infer_freq(business_dates)
    print(f"\nbusiness_dates: {business_dates.tolist()}")
    print(f"infer_freq -> {inferred_freq}")

    # 小时频率
    hourly_dates = pd.date_range("2024-01-01", periods=5, freq="H")
    inferred_freq = pd.infer_freq(hourly_dates)
    print(f"\nhourly_dates: {hourly_dates.tolist()}")
    print(f"infer_freq -> {inferred_freq}")

    # 不规律的日期
    irregular_dates = pd.DatetimeIndex(["2024-01-01", "2024-01-03", "2024-01-07"])
    inferred_freq = pd.infer_freq(irregular_dates)
    print(f"\nirregular_dates: {irregular_dates.tolist()}")
    print(f"infer_freq -> {inferred_freq}  # None 表示无法推断")

    print("\n" + "=" * 70)
    print("3. 频率别名对照表")
    print("=" * 70)

    print("""
常见频率别名：

日频率：
  D      - 日历日（calendar day）
  B      - 工作日（business day）
  W      - 周（Sunday 为默认）
  W-MON  - 每周一
  W-TUE  - 每周二
  W-WED  - 每周三
  W-THU  - 每周四
  W-FRI  - 每周五
  W-SAT  - 每周六
  W-SUN  - 每周日

月频率：
  M      - 月末（month end）
  MS     - 月初（month start）
  BM     - 月末工作日
  BMS    - 月初工作日

季度频率：
  Q      - 季度末（季度最后一个日历日）
  QS     - 季度初
  BQ     - 季度末工作日
  BQS    - 季度初工作日
  Q-JAN  - 1月结束的季度
  Q-FEB  - 2月结束的季度
  ...

年频率：
  Y      - 年末（year end）
  YS     - 年初（year start）
  BY     - 年末工作日
  BYS    - 年初工作日
  Y-JAN  - 1月结束的年度
  Y-FEB  - 2月结束的年度
  ...

小时/分钟/秒：
  H      - 小时（hourly）
  T, min - 分钟（minutely）
  S      - 秒（secondly）
  L, ms  - 毫秒（milliseconds）
  U, us  - 微秒（microseconds）
  N      - 纳秒（nanoseconds）

复合频率：
  2D     - 每 2 天
  3H     - 每 3 小时
  1h30min - 每 1 小时 30 分钟
  2W     - 每 2 周
  2M     - 每 2 个月
""")

    print("\n" + "=" * 70)
    print("4. 频率转换示例")
    print("=" * 70)

    # 创建分钟级数据
    dates_min = pd.date_range("2024-01-01 09:00", periods=60, freq="T")
    ts_min = pd.Series(np.random.randn(60), index=dates_min)

    print("原始数据（分钟频率）:")
    print(ts_min.head(10))

    print("\n4.1 分钟 -> 小时")
    print("-" * 70)
    ts_hour = ts_min.asfreq("H")
    print("asfreq('H') ->")
    print(ts_hour)

    print("\n4.2 分钟 -> 5分钟")
    print("-" * 70)
    ts_5min = ts_min.asfreq("5T")
    print("asfreq('5T') ->")
    print(ts_5min.head(10))

    print("\n4.3 向下采样（使用聚合函数）")
    print("-" * 70)
    print("使用 resample 而不是 asfreq 进行聚合")
    ts_hour_mean = ts_min.resample("H").mean()
    print("resample('H').mean() ->")
    print(ts_hour_mean)

    ts_hour_sum = ts_min.resample("H").sum()
    print("\nresample('H').sum() ->")
    print(ts_hour_sum)

    print("\n" + "=" * 70)
    print("5. origin 参数（窗口起点设置）")
    print("=" * 70)

    # 创建时间序列
    dates = pd.date_range("2024-01-01 09:30", periods=10, freq="30min")
    ts = pd.Series(range(10), index=dates)

    print("原始数据:")
    print(ts)

    print("\n5.1 resample 中的 origin")
    print("-" * 70)

    print("resample('2H', origin='epoch'):")
    print("从 Unix 时间戳起点（1970-01-01）开始")
    print(ts.resample("2H", origin="epoch").sum())

    print("\nresample('2H', origin='start'):")
    print("从数据起点开始")
    print(ts.resample("2H", origin="start").sum())

    print("\nresample('2H', origin='start_day'):")
    print("从每天起点开始")
    print(ts.resample("2H", origin="start_day").sum())

    print("\n5.2 自定义 origin")
    print("-" * 70)

    custom_origin = "2024-01-01 09:00"
    print(f"resample('2H', origin='{custom_origin}'):")
    print(ts.resample("2H", origin=custom_origin).sum())

    print("\n" + "=" * 70)
    print("6. asof - 向前查找最近值")
    print("=" * 70)

    # 创建时间序列（有间隙）
    dates_with_gaps = pd.to_datetime(
        ["2024-01-01 10:00", "2024-01-01 11:00", "2024-01-01 13:00", "2024-01-01 15:00"]
    )
    ts_gaps = pd.Series([100, 200, 300, 400], index=dates_with_gaps)

    print("有时间间隙的数据:")
    print(ts_gaps)

    print("\n6.1 asof - 查找指定时间的最近值")
    print("-" * 70)

    target_time = pd.Timestamp("2024-01-01 12:30")
    value = ts_gaps.asof(target_time)
    print(f"asof('2024-01-01 12:30') -> {value}")
    print("（返回 11:00 的值 200）")

    target_time2 = pd.Timestamp("2024-01-01 14:00")
    value2 = ts_gaps.asof(target_time2)
    print(f"asof('2024-01-01 14:00') -> {value2}")
    print("（返回 13:00 的值 300）")

    print("\n6.2 多个目标时间")
    print("-" * 70)

    target_times = pd.to_datetime(
        ["2024-01-01 10:30", "2024-01-01 12:00", "2024-01-01 14:30", "2024-01-01 16:00"]
    )
    values = ts_gaps.asof(target_times)
    print(f"目标时间: {target_times.tolist()}")
    print(f"对应值: {values.tolist()}")

    print("\n" + "=" * 70)
    print("7. bfill / ffill 与频率转换组合")
    print("=" * 70)

    # 创建日频数据
    daily_ts = pd.Series([1, 2, 3], index=pd.date_range("2024-01-01", periods=3, freq="D"))

    print("原始日频数据:")
    print(daily_ts)

    print("\n7.1 转换为小时并填充")
    print("-" * 70)

    hourly_ffill = daily_ts.asfreq("H", method="ffill")
    print("asfreq('H', method='ffill') ->")
    print(hourly_ffill.head(10))

    hourly_bfill = daily_ts.asfreq("H", method="bfill")
    print("\nasfreq('H', method='bfill') ->")
    print(hourly_bfill.head(10))

    print("\n7.2 组合使用：先转换再填充")
    print("-" * 70)

    # 转换为小时频率（产生 NaN）
    hourly_with_nan = daily_ts.asfreq("H")

    # 使用 ffill 填充
    hourly_filled = hourly_with_nan.ffill()
    print("asfreq('H').ffill() ->")
    print(hourly_filled.head(10))

    # 使用 bfill 填充
    hourly_filled_back = hourly_with_nan.bfill()
    print("\nasfreq('H').bfill() ->")
    print(hourly_filled_back.head(10))

    # 限制填充距离
    hourly_fill_limit = hourly_with_nan.ffill(limit=2)
    print("\nasfreq('H').ffill(limit=2) ->")
    print(hourly_fill_limit.head(10))

    print("\n" + "=" * 70)
    print("8. 实际应用示例")
    print("=" * 70)

    # 示例 1: 股票数据频率转换
    print("\n示例 1: 日内数据转换为日频")
    # 模拟日内分钟数据
    intraday_dates = pd.date_range("2024-01-01 09:30", "2024-01-01 16:00", freq="T")
    intraday_prices = pd.Series(np.random.randn(391).cumsum() + 100, index=intraday_dates)

    print(f"日内数据点数: {len(intraday_prices)}")

    # 转换为日频（取收盘价）
    daily_close = intraday_prices.asfreq("D", method="ffill")
    print(f"\n日频收盘价: {daily_close.iloc[0]:.2f}")

    # 示例 2: 月度数据转换为季度数据
    print("\n示例 2: 月度数据聚合为季度数据")
    monthly_dates = pd.date_range("2024-01-01", periods=12, freq="MS")
    monthly_sales = pd.Series(np.random.randint(100, 1000, 12), index=monthly_dates)

    print("月度销售:")
    print(monthly_sales)

    # 使用 asfreq（只取季度末的值）
    quarterly_end = monthly_sales.asfreq("Q")
    print("\nasfreq('Q') -> 季度末的月度值:")
    print(quarterly_end)

    # 使用 resample（聚合）
    quarterly_sum = monthly_sales.resample("Q").sum()
    print("\nresample('Q').sum() -> 季度总和:")
    print(quarterly_sum)

    # 示例 3: 处理缺失的时间点
    print("\n示例 3: 检测和填充缺失时间点")
    # 创建有缺失的时间序列
    irregular_dates = pd.to_datetime(
        [
            "2024-01-01",
            "2024-01-02",
            "2024-01-04",  # 缺失 01-03
            "2024-01-05",
            "2024-01-08",  # 缺失 01-06, 01-07
        ]
    )
    irregular_ts = pd.Series(range(5), index=irregular_dates)

    print("不规则时间序列:")
    print(irregular_ts)

    # 转换为完整的日频
    full_range = pd.date_range(start=irregular_ts.index.min(), end=irregular_ts.index.max(), freq="D")
    regular_ts = irregular_ts.reindex(full_range)

    print("\n填充后的完整序列:")
    print(regular_ts)

    # 向前填充
    regular_ffill = regular_ts.ffill()
    print("\n向前填充:")
    print(regular_ffill)

    # 示例 4: 时间窗口对齐
    print("\n示例 4: 对齐不同频率的数据")
    # 日频数据
    daily_data = pd.DataFrame(
        {"price": [100, 101, 102, 103, 104]}, index=pd.date_range("2024-01-01", periods=5, freq="D")
    )

    # 小时频数据
    hourly_data = pd.DataFrame(
        {"volume": [1000, 1100, 1050]}, index=pd.date_range("2024-01-01 09:00", periods=3, freq="H")
    )

    print("日频数据:")
    print(daily_data)
    print("\n小时频数据:")
    print(hourly_data)

    # 将小时数据转换为日频（求和）
    hourly_to_daily = hourly_data.resample("D").sum()
    print("\n小时数据转换为日频:")
    print(hourly_to_daily)

    # 合并
    combined = pd.concat([daily_data, hourly_to_daily], axis=1)
    print("\n合并后的数据:")
    print(combined)

    # 示例 5: 使用 asof 合并不匹配的时间戳
    print("\n示例 5: 使用 merge_asof 合并数据")
    trades = pd.DataFrame(
        {"time": pd.to_datetime(["2024-01-01 10:01", "2024-01-01 10:05", "2024-01-01 10:10"]), "price": [100, 101, 102]}
    )

    quotes = pd.DataFrame(
        {"time": pd.to_datetime(["2024-01-01 10:00", "2024-01-01 10:04", "2024-01-01 10:11"]), "bid": [99, 100, 101]}
    )

    print("交易数据:")
    print(trades)
    print("\n报价数据:")
    print(quotes)

    # 使用 merge_asof
    merged = pd.merge_asof(trades, quotes, on="time")
    print("\nmerge_asof 结果（匹配最近的报价）:")
    print(merged)


if __name__ == "__main__":
    main()
