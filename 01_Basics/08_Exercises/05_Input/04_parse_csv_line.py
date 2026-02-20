#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：csv 解析（正确处理引号与逗号）
Author: Lambert

题目：
实现 `parse_csv_row(line)`，要求：
- 使用 `csv.reader` 解析单行 CSV
- 正确处理引号中的逗号，例如：
  `2025-12-15,"food,drink",12.50,"lunch"`

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/05_Input/04_parse_csv_line.py
"""

import csv


def parse_csv_row(line: str) -> list[str]:
    reader = csv.reader([line])
    return next(reader)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    row = parse_csv_row('2025-12-15,"food,drink",12.50,"lunch"')
    check("col_count", len(row), 4)
    check("category", row[1], "food,drink")


if __name__ == "__main__":
    main()
