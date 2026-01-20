#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：格式化规格（金额/百分比/对齐）

题目：
实现下面两个函数：
1) `format_amount(amount, width=10)`：右对齐、带千分位、保留 2 位小数
2) `format_percent(value, precision=1)`：百分比格式（例如 0.125 -> "12.5%"）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/04_Formatting/02_format_spec_numbers.py
"""


def format_amount(amount: float, width: int = 10) -> str:
    return f"{amount:>{width},.2f}"


def format_percent(value: float, precision: int = 1) -> str:
    return f"{value:.{precision}%}"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("amount", format_amount(1234.5, width=10), "  1,234.50")
    check("percent", format_percent(0.125, precision=1), "12.5%")


if __name__ == "__main__":
    main()

