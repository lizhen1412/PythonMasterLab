#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：None 与真值测试（只把 None 当缺失值）

题目：
实现 `coalesce(value, default)`，要求：
- 仅当 value is None 时返回 default
- 不能用 `value or default`（因为 0/""/False 也会被当成“空”）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/07_Data_Types/02_coalesce_none_vs_or.py
"""


def coalesce(value: object, default: object) -> object:
    return default if value is None else value


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("none", coalesce(None, 10), 10)
    check("zero", coalesce(0, 10), 0)
    check("empty_str", coalesce("", "x"), "")
    check("false", coalesce(False, True), False)


if __name__ == "__main__":
    main()

