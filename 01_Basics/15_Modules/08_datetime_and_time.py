#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：日期与时间。

- datetime.now / utcnow / timezone
- strftime 格式化、strptime 解析
- 时间戳与 sleep
"""

from __future__ import annotations

import datetime as dt
import time


def show_now() -> None:
    now = dt.datetime.now()
    utc = dt.datetime.now(dt.timezone.utc)
    print("本地时间 ->", now)
    print("UTC 时间 ->", utc)
    print("日期部分 ->", now.date())
    print("时间部分 ->", now.time().replace(microsecond=0))


def format_and_parse() -> None:
    now = dt.datetime(2024, 5, 20, 14, 30, 0)
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    parsed = dt.datetime.strptime(formatted, "%Y-%m-%d %H:%M:%S")
    print("strftime ->", formatted)
    print("strptime ->", parsed, parsed.tzinfo)


def timestamps() -> None:
    now = dt.datetime.now()
    ts = now.timestamp()
    restored = dt.datetime.fromtimestamp(ts)
    print("时间戳 ->", ts)
    print("fromtimestamp ->", restored)


def sleep_demo() -> None:
    start = time.perf_counter()
    time.sleep(0.05)
    duration_ms = (time.perf_counter() - start) * 1000
    print(f"time.sleep(0.05) 实际耗时约 {duration_ms:.2f} ms")


def main() -> None:
    print("== 当前时间 ==")
    show_now()

    print("\n== 格式化与解析 ==")
    format_and_parse()

    print("\n== 时间戳 ==")
    timestamps()

    print("\n== 睡眠示例 ==")
    sleep_demo()


if __name__ == "__main__":
    main()
