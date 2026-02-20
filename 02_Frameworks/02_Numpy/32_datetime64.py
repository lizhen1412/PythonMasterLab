#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 32：NumPy datetime64 和 timedelta64 操作。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/32_datetime64.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=== datetime64 基础 ===")

    # 1. 创建 datetime64
    print("日期字符串创建:")
    d1 = np.datetime64("2023-01-15")
    d2 = np.datetime64("2023-01-15T12:30:45")
    d3 = np.datetime64("2023-01", "D")  # 指定精度

    print(f"d1 (日期): {d1}")
    print(f"d2 (日期时间): {d2}")
    print(f"d3 (指定精度为天): {d3}")

    # 2. datetime64 数组
    print("\n=== datetime64 数组 ===")

    dates = np.array(["2023-01-01", "2023-01-02", "2023-01-03"], dtype="datetime64")
    print("日期数组:")
    print(dates)
    print(f"dtype: {dates.dtype}")

    # 3. 日期范围 (arange)
    print("\n=== 日期范围 ===")
    date_range = np.arange("2023-01-01", "2023-01-10", dtype="datetime64[D]")
    print("np.arange 生成日期:")
    print(date_range)

    # 4. timedelta64 基础
    print("\n=== timedelta64 基础 ===")

    td1 = np.timedelta64(1, "D")  # 1天
    td2 = np.timedelta64(2, "W")  # 2周
    td3 = np.timedelta64(3, "h")  # 3小时

    print(f"1天: {td1}")
    print(f"2周: {td2}")
    print(f"3小时: {td3}")

    # 5. datetime64 运算
    print("\n=== datetime64 运算 ===")

    d1 = np.datetime64("2023-01-01")
    d2 = np.datetime64("2023-01-15")

    print(f"d1: {d1}")
    print(f"d2: {d2}")
    print(f"d2 - d1 = {d2 - d1}")
    print(f"d1 + 7天 = {d1 + np.timedelta64(7, 'D')}")

    # 6. timedelta64 数组运算
    print("\n=== timedelta64 数组 ===")

    dates = np.array(["2023-01-01", "2023-01-02", "2023-01-03"], dtype="datetime64[D]")
    offsets = np.array([1, 2, 3], dtype="timedelta64[D]")

    print("日期:", dates)
    print("偏移:", offsets)
    print("相加:", dates + offsets)

    # 7. 不同精度的时间
    print("\n=== 不同精度 ===")

    # 从年到纳秒
    precisions = ["Y", "M", "W", "D", "h", "m", "s", "ms", "us", "ns"]
    print("不同精度的 datetime64:")
    for p in precisions:
        dt = np.datetime64("2023-01-01", p)
        print(f"  {p}: {dt}")

    # 8. timedelta64 运算
    print("\n=== timedelta64 运算 ===")

    td1 = np.timedelta64(5, "D")
    td2 = np.timedelta64(3, "D")

    print(f"td1: {td1}")
    print(f"td2: {td2}")
    print(f"相加: {td1 + td2}")
    print(f"相减: {td1 - td2}")
    print(f"乘法: {td1 * 2}")
    print(f"除法: {td1 / np.timedelta64(1, 'D')}")  # 转换为天数

    # 9. 工作日计算
    print("\n=== 工作日计算 ===")

    start = np.datetime64("2023-01-02")  # 周一
    # 找下一个周五
    target = start + np.timedelta64(4, "D")
    print(f"周一: {start}")
    print(f"加4天 (周五): {target}")

    # 10. 日期比较
    print("\n=== 日期比较 ===")

    dates = np.array(["2023-01-01", "2023-01-15", "2023-02-01"], dtype="datetime64[D]")
    cutoff = np.datetime64("2023-01-10")

    print("日期:", dates)
    print(f"截止日期: {cutoff}")
    print("大于截止:", dates > cutoff)

    # 11. 日期排序和搜索
    print("\n=== 日期排序和搜索 ===")

    dates = np.array(["2023-03-01", "2023-01-15", "2023-02-10"], dtype="datetime64[D]")
    print("原始:", dates)

    sorted_dates = np.sort(dates)
    print("排序后:", sorted_dates)

    # 搜索
    target = np.datetime64("2023-02-01")
    idx = np.searchsorted(sorted_dates, target)
    print(f"查找 {target} 的插入位置: {idx}")

    # 12. 日期统计
    print("\n=== 日期统计 ===")

    dates = np.array(
        ["2023-01-05", "2023-01-15", "2023-02-05", "2023-02-15"],
        dtype="datetime64[D]"
    )

    print("日期:", dates)
    print("最小:", np.min(dates))
    print("最大:", np.max(dates))
    print("中位数:", np.median(dates))

    # 日期差
    diff = dates[-1] - dates[0]
    print(f"时间跨度: {diff}")

    # 13. timedelta64 转换
    print("\n=== timedelta64 单位转换 ===")

    td = np.timedelta64(1, "W")
    print(f"1周: {td}")
    print(f"转为天: {td / np.timedelta64(1, 'D')} 天")
    print(f"转为小时: {td / np.timedelta64(1, 'h')} 小时")
    print(f"转为秒: {td / np.timedelta64(1, 's')} 秒")

    # 14. datetime64 与字符串转换
    print("\n=== 字符串转换 ===")

    dt_str = "2023-01-15T12:30:45"
    dt = np.datetime64(dt_str)
    print(f"字符串 -> datetime64: {dt}")
    print(f"datetime64 -> 字符串: {str(dt)}")

    # 15. datetime64 与 Unix 时间戳
    print("\n=== Unix 时间戳 ===")

    # datetime64 默认是从 1970-01-01 开始的毫秒/纳秒数
    epoch = np.datetime64("1970-01-01T00:00:00", "s")
    now = np.datetime64("2023-01-01T00:00:00", "s")

    timestamp = (now - epoch) / np.timedelta64(1, "s")
    print(f"从 epoch 到现在的秒数: {timestamp}")

    # 16. 处理时区
    print("\n=== 时区处理 ===")
    print("注意: NumPy 的 datetime64 不存储时区信息")
    print("时区感知的 datetime 需要使用 pandas 或 Python datetime")

    # 17. 日期舍入
    print("\n=== 日期舍入 ===")

    dt = np.datetime64("2023-01-15T14:30:45")
    print(f"原始: {dt}")

    # 转换为不同精度会自动舍入
    print(f"按天: {dt.astype('datetime64[D]')}")
    print(f"按月: {dt.astype('datetime64[M]')}")
    print(f"按年: {dt.astype('datetime64[Y]')}")

    # 18. 日期数组操作
    print("\n=== 日期数组操作 ===")

    # 创建一个月的日期
    dates = np.arange("2023-01-01", "2023-02-01", dtype="datetime64[D]")
    print(f"一月日期数: {len(dates)}")

    # 筛选周末
    weekdays = dates.astype("datetime64[D]").view("int64") % 7
    # 注意: 1970-01-01 是周四，所以需要调整
    # 这里简化处理，实际应用建议用 pandas
    print(f"日期数组长度: {len(dates)}")


if __name__ == "__main__":
    main()