#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 61：Period 高级操作。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/61_period_advanced.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    print("=== Period 基础创建 ===")

    # 1. 创建 Period
    p1 = pd.Period("2023-01", freq="M")
    p2 = pd.Period("2023-Q1", freq="Q")
    p3 = pd.Period("2023", freq="A")

    print(f"月度 Period: {p1}")
    print(f"季度 Period: {p2}")
    print(f"年度 Period: {p3}")

    # 2. Period 属性
    print("\n=== Period 属性 ===")
    print(f"年: {p1.year}, 月: {p1.month}, 日: {p1.day}")
    print(f"季度: {p2.quarter}")
    print(f"星期: {p1.day_of_week}")
    print(f"月中第几天: {p1.day_of_year}")
    print(f"月中第几周: {p1.week}")

    # 3. Period 运算
    print("\n=== Period 运算 ===")
    p = pd.Period("2023-06", freq="M")
    print(f"原始: {p}")
    print(f"+1 月: {p + 1}")
    print(f"-3 月: {p - 3}")
    print(f"+1 季度: {p + pd.offsets.QuarterEnd()}")

    # 4. Period_range 创建
    print("\n=== Period_range ===")
    periods = pd.period_range("2023-01", periods=12, freq="M")
    print("月度 Period range:")
    print(periods)

    quarterly = pd.period_range("2023-Q1", periods=4, freq="Q")
    print("\n季度 Period range:")
    print(quarterly)

    # 5. PeriodIndex
    print("\n=== PeriodIndex ===")
    idx = pd.PeriodIndex(
        ["2023-01", "2023-02", "2023-03"], freq="M", name="month"
    )
    print(idx)

    # 使用 PeriodIndex 创建 Series
    s = pd.Series([10, 20, 30], index=idx)
    print("\n带 PeriodIndex 的 Series:")
    print(s)

    # 6. Period 转换
    print("\n=== Period 转换 ===")
    p_month = pd.Period("2023-06", freq="M")
    print(f"月度转季度: {p_month.asfreq('Q')}")
    print(f"月度转年度: {p_month.asfreq('A')}")
    print(f"月度转日度 (月末): {p_month.asfreq('D', how='end')}")
    print(f"月度转日度 (月初): {p_month.asfreq('D', how='start')}")

    # 7. PeriodIndex 转换为 DatetimeIndex
    print("\n=== PeriodIndex 转 DatetimeIndex ===")
    periods = pd.period_range("2023-01", periods=6, freq="M")
    print("PeriodIndex:")
    print(periods)
    print("\n转 DatetimeIndex (月末):")
    print(periods.to_timestamp())
    print("\n转 DatetimeIndex (月初):")
    print(periods.to_timestamp(how="start"))

    # 8. DatetimeIndex 转 PeriodIndex
    print("\n=== DatetimeIndex 转 PeriodIndex ===")
    dates = pd.date_range("2023-01-01", periods=6, freq="M")
    print("DatetimeIndex:")
    print(dates)
    print("\n转 PeriodIndex:")
    print(dates.to_period())

    # 9. Period 比较和判断
    print("\n=== Period 比较 ===")
    p1 = pd.Period("2023-06", freq="M")
    p2 = pd.Period("2023-07", freq="M")
    p3 = pd.Period("2023-06", freq="M")

    print(f"{p1} < {p2}: {p1 < p2}")
    print(f"{p1} == {p3}: {p1 == p3}")
    print(f"{p2} in 2023-Q2: {p2 in pd.Period('2023-Q2', freq='Q')}")

    # 10. Period 的 is_ 属性
    print("\n=== Period 的 is_ 属性 ===")
    p = pd.Period("2023-03-15", freq="D")
    print(f"日期: {p}")
    print(f"is_month_start: {p.is_month_start}")
    print(f"is_month_end: {p.is_month_end}")
    print(f"is_quarter_start: {p.is_quarter_start}")
    print(f"is_quarter_end: {p.is_quarter_end}")
    print(f"is_year_start: {p.is_year_start}")
    print(f"is_year_end: {p.is_year_end}")

    # 11. Period 在 DataFrame 中的应用
    print("\n=== DataFrame 中的 Period ===")
    df = pd.DataFrame(
        {
            "period": pd.period_range("2023-Q1", periods=4, freq="Q"),
            "sales": [100, 120, 140, 160],
        }
    )
    print(df)
    print(f"\nperiod dtype: {df['period'].dtype}")

    # 按 Period 分组
    print("\n按 Period 分组统计:")
    df["year"] = df["period"].dt.year
    print(df.groupby("year")["sales"].sum())

    # 12. PeriodIndex 的部分选择
    print("\n=== PeriodIndex 选择 ===")
    idx = pd.period_range("2023-01", periods=24, freq="M")
    s = pd.Series(range(24), index=idx)
    print("选择 2023 年:")
    print(s["2023"])
    print("\n选择 2023-Q1:")
    print(s["2023-Q1"])

    # 13. Period 的频率字符串
    print("\n=== Period 频率说明 ===")
    freq_map = {
        "D": "日历日",
        "W": "周",
        "M": "月",
        "Q": "季度",
        "A": "年",
        "H": "小时",
        "T": "分钟",
        "S": "秒",
    }
    for code, name in freq_map.items():
        p = pd.Period("2023-01-01", freq=code)
        print(f"{code} ({name}): {p}")

    # 14. Period 的 strftime
    print("\n=== Period 格式化 ===")
    p = pd.Period("2023-06-15", freq="D")
    print(f"默认: {p}")
    print(f"YYYY-MM: {p.strftime('%Y-%m')}")
    print(f"YYYY年MM月: {p.strftime('%Y年%m月')}")

    # 15. Period 的差值
    print("\n=== Period 差值 ===")
    p1 = pd.Period("2023-01", freq="M")
    p2 = pd.Period("2023-06", freq="M")
    diff = p2 - p1
    print(f"{p2} - {p1} = {diff} 个月")
    print(f"差值类型: {type(diff)}")


if __name__ == "__main__":
    main()