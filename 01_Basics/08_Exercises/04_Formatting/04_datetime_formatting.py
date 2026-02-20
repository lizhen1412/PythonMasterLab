#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：datetime 格式化（strftime vs isoformat）
Author: Lambert

题目：
实现 `format_datetime(dt)`，返回两个字符串：
1) `iso`：`dt.isoformat(timespec="seconds")`
2) `human`：`YYYY-MM-DD HH:MM:SS`（用 strftime）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/04_Formatting/04_datetime_formatting.py
"""

from datetime import datetime


def format_datetime(dt: datetime) -> tuple[str, str]:
    iso = dt.isoformat(timespec="seconds")
    human = dt.strftime("%Y-%m-%d %H:%M:%S")
    return iso, human


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    dt = datetime(2025, 12, 15, 9, 30, 5)
    iso, human = format_datetime(dt)
    check("iso", iso, "2025-12-15T09:30:05")
    check("human", human, "2025-12-15 09:30:05")


if __name__ == "__main__":
    main()
