#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：实现 None 合并（避免 x or default 的坑）

题目：
实现 `coalesce_none(value, default)`，要求：
- 仅当 value is None 时返回 default
- 不能用 `value or default`（0/""/False 都会被误当成“缺失值”）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/09_Operators/Exercises/07_logical_coalesce_none.py
"""

from __future__ import annotations


def coalesce_none(value: object, default: object) -> object:
    return default if value is None else value


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("none", coalesce_none(None, 10), 10)
    check("zero", coalesce_none(0, 10), 0)
    check("empty_str", coalesce_none("", "x"), "")
    check("false", coalesce_none(False, True), False)


if __name__ == "__main__":
    main()

