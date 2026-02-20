#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：datetime 的格式化输出。
Author: Lambert

你会学到：
1) `datetime.strftime()`：经典方式
2) f-string 的 `:{...}` 对 datetime 有特殊支持：`f"{dt:%Y-%m-%d}"`
3) `isoformat()`：机器友好，常用于接口/日志
4) timedelta 的简单输出

运行：
    python3 01_Basics/04_Formatting/11_datetime_formatting.py
"""

from datetime import datetime, timedelta, timezone


def main() -> None:
    now = datetime.now(timezone.utc)
    delta = timedelta(days=2, hours=3, minutes=4, seconds=5)

    print("1) str(now)（默认显示）：")
    print(now)

    print("\n2) strftime：")
    print(now.strftime("%Y-%m-%d %H:%M:%S %Z"))

    print("\n3) f-string datetime format：")
    print(f"{now:%Y-%m-%d %H:%M:%S %Z}")

    print("\n4) isoformat（机器更友好）：")
    print(now.isoformat())

    print("\n5) timedelta：")
    print("delta =", delta)
    print("delta seconds =", int(delta.total_seconds()))


if __name__ == "__main__":
    main()
