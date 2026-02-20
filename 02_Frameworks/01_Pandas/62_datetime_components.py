#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 62：DateTime 组件高级操作 (dt.* 方法和属性)。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/62_datetime_components.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    print("=== 创建带 datetime 的 DataFrame ===")

    df = pd.DataFrame(
        {
            "date": pd.to_datetime(
                [
                    "2023-01-15",
                    "2023-02-28",
                    "2023-03-31",
                    "2023-04-15",
                    "2023-05-01",
                    "2023-06-30",
                    "2023-07-15",
                    "2023-12-31",
                ]
            ),
            "value": [10, 20, 30, 40, 50, 60, 70, 80],
        }
    )

    print(df)

    # 1. 基础日期组件
    print("\n=== 基础日期组件 ===")
    print(f"年: {df['date'].dt.year.tolist()}")
    print(f"月: {df['date'].dt.month.tolist()}")
    print(f"日: {df['date'].dt.day.tolist()}")
    print(f"季度: {df['date'].dt.quarter.tolist()}")
    print(f"星期几(0=周一): {df['date'].dt.dayofweek.tolist()}")
    print(f"星期几(名称): {df['date'].dt.day_name().tolist()}")
    print(f"一年中第几天: {df['date'].dt.dayofyear.tolist()}")
    print(f"月中第几周: {df['date'].dt.week.tolist()}")

    # 2. 时间组件
    print("\n=== 时间组件 ===")
    df["datetime"] = pd.to_datetime(
        [
            "2023-01-15 09:30:45",
            "2023-02-28 14:20:30",
            "2023-03-31 23:59:59",
        ]
    )
    print("时: ", df["datetime"].dt.hour.tolist())
    print("分: ", df["datetime"].dt.minute.tolist())
    print("秒: ", df["datetime"].dt.second.tolist())
    print("微秒: ", df["datetime"].dt.microsecond.tolist())

    # 3. is_* 判断属性
    print("\n=== is_* 判断属性 ===")
    print("is_month_start:")
    print(df["date"].dt.is_month_start.tolist())
    print("\nis_month_end:")
    print(df["date"].dt.is_month_end.tolist())
    print("\nis_quarter_start:")
    print(df["date"].dt.is_quarter_start.tolist())
    print("\nis_quarter_end:")
    print(df["date"].dt.is_quarter_end.tolist())
    print("\nis_year_start:")
    print(df["date"].dt.is_year_start.tolist())
    print("\nis_year_end:")
    print(df["date"].dt.is_year_end.tolist())
    print("\nis_leap_year:")
    print(df["date"].dt.is_leap_year.tolist())

    # 4. 月份相关
    print("\n=== 月份相关 ===")
    print("月份名称:", df["date"].dt.month_name().tolist())
    print("月份天数:", df["date"].dt.days_in_month.tolist())
    print("当月天数 (英文):", df["date"].dt.daysinmonth.tolist())

    # 5. 时间差组件
    print("\n=== 时间差组件 (timedelta) ===")
    df_td = pd.DataFrame(
        {
            "timedelta": pd.to_timedelta(
                ["1 days 02:03:45", "2 days 04:05:30", "30 days 10:20:15"]
            )
        }
    )
    print(df_td)
    print("\n天数:", df_td["timedelta"].dt.days.tolist())
    print("秒数:", df_td["timedelta"].dt.seconds.tolist())
    print("微秒:", df_td["timedelta"].dt.microseconds.tolist())
    print("总秒数:", df_td["timedelta"].dt.total_seconds().tolist())

    # 6. 日期运算
    print("\n=== 日期运算 ===")
    df["date_plus_month"] = df["date"] + pd.DateOffset(months=1)
    df["date_plus_week"] = df["date"] + pd.DateOffset(weeks=1)
    df["date_plus_year_end"] = df["date"] + pd.offsets.YearEnd(0)
    print(df[["date", "date_plus_month", "date_plus_week", "date_plus_year_end"]])

    # 7. 月份开始/结束
    print("\n=== 月份开始/结束 ===")
    df["month_start"] = df["date"].dt.to_period("M").dt.to_timestamp()
    df["month_end"] = df["date"].dt.to_period("M").dt.to_timestamp(how="end")
    print(df[["date", "month_start", "month_end"]])

    # 8. 季度开始/结束
    print("\n=== 季度开始/结束 ===")
    df["quarter_start"] = df["date"].dt.to_period("Q").dt.to_timestamp()
    df["quarter_end"] = df["date"].dt.to_period("Q").dt.to_timestamp(how="end")
    print(df[["date", "quarter_start", "quarter_end"]])

    # 9. 日期归一化（去掉时间部分）
    print("\n=== 日期归一化 ===")
    df["normalized"] = df["date"].dt.normalize()
    print(df[["datetime", "normalized"]])

    # 10. 时间戳转换
    print("\n=== 时间戳转换 ===")
    timestamps = df["date"].astype("int64") // 10**9  # 转为 Unix 时间戳（秒）
    print("Unix 时间戳:", timestamps.tolist())
    print("\n从时间戳恢复:")
    print(pd.to_datetime(timestamps, unit="s"))

    # 11. 时区处理
    print("\n=== 时区处理 ===")
    df_utc = pd.DataFrame(
        {
            "date": pd.date_range("2023-01-01", periods=3, tz="UTC"),
        }
    )
    print("UTC 时间:")
    print(df_utc)
    print("\n转换为北京时间 (UTC+8):")
    df_utc["beijing"] = df_utc["date"].dt.tz_convert("Asia/Shanghai")
    print(df_utc)

    # 12. 时区本地化
    print("\n=== 时区本地化 ===")
    df_naive = pd.DataFrame(
        {"date": ["2023-01-01", "2023-06-01", "2023-12-01"]}
    )
    df_naive["date"] = pd.to_datetime(df_naive["date"])
    print("无时区:")
    print(df_naive["date"].dt.tz)
    print("\n本地化到 UTC:")
    df_naive["date_utc"] = df_naive["date"].dt.tz_localize("UTC")
    print(df_naive["date_utc"].dt.tz)

    # 13. 单位转换
    print("\n=== 时间单位转换 ===")
    df_ns = pd.DataFrame(
        {"date": pd.to_datetime(["2023-01-01", "2023-01-02"])}
    )
    print("默认 (ns):", df_ns["date"].dtype)
    print("转为秒:", df_ns["date"].astype("datetime64[s]").dtype)
    print("转为毫秒:", df_ns["date"].astype("datetime64[ms]").dtype)

    # 14. 日期范围判断
    print("\n=== 日期范围判断 ===")
    target = pd.Timestamp("2023-03-15")
    df["is_in_q1"] = df["date"].dt.quarter == 1
    df["is_in_first_half"] = df["date"].dt.month <= 6
    df["is_weekend"] = df["date"].dt.dayofweek >= 5
    print(df[["date", "is_in_q1", "is_in_first_half", "is_weekend"]])

    # 15. 实用：按日期组件分组统计
    print("\n=== 按年月分组统计 ===")
    df_grouped = (
        df.groupby([df["date"].dt.year, df["date"].dt.month])["value"]
        .sum()
        .reset_index()
    )
    df_grouped.columns = ["year", "month", "total"]
    print(df_grouped)

    # 16. 实用：计算两个日期之间的工作日
    print("\n=== 计算工作日 ===")
    df_dates = pd.DataFrame(
        {
            "start": pd.to_datetime(["2023-01-01", "2023-02-01"]),
            "end": pd.to_datetime(["2023-01-31", "2023-02-28"]),
        }
    )
    # 使用 bdate_range 计算工作日
    df_dates["work_days"] = [
        len(pd.bdate_range(start, end)) for start, end in zip(df_dates["start"], df_dates["end"])
    ]
    print(df_dates)

    # 17. 日期取整
    print("\n=== 日期取整 ===")
    df_dates_exact = pd.DataFrame(
        {"datetime": pd.to_datetime(["2023-01-15 14:35:22", "2023-02-28 09:12:45"])}
    )
    df_dates_exact["rounded_hour"] = df_dates_exact["datetime"].dt.round("H")
    df_dates_exact["floored_day"] = df_dates_exact["datetime"].dt.floor("D")
    df_dates_exact["ceiled_month"] = df_dates_exact["datetime"].dt.ceil("M")
    print(df_dates_exact)

    # 18. 日期周期
    print("\n=== 日期周期 ===")
    df["week_of_year"] = df["date"].dt.isocalendar().week
    df["week_day_iso"] = df["date"].dt.isocalendar().day
    print(df[["date", "week_of_year", "week_day_iso"]])


if __name__ == "__main__":
    main()