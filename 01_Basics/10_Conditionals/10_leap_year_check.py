#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：条件判断——闰年判断（Leap Year）

题目/目标：
实现闰年判断函数 `is_leap_year(year)`，并用 if/else 与布尔表达式两种写法对照。

规则（公历 Gregorian）：
1) 能被 400 整除 -> 闰年
2) 能被 100 整除 -> 平年
3) 能被 4 整除   -> 闰年
4) 其他           -> 平年

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/10_leap_year_check.py
"""

from __future__ import annotations


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def is_leap_year_expr(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    samples: list[tuple[int, bool]] = [
        (2000, True),
        (1900, False),
        (2004, True),
        (2001, False),
        (2024, True),
        (2025, False),
        (2400, True),
        (2100, False),
    ]
    for year, expected in samples:
        check(f"is_leap_year({year})", is_leap_year(year), expected)
        check(f"is_leap_year_expr({year})", is_leap_year_expr(year), expected)


if __name__ == "__main__":
    main()

