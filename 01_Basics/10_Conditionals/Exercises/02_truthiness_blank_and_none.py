#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：真值测试（区分 None 与空字符串/0/False）

题目：
实现下面两个函数：
1) `coalesce_none(value, default)`：仅当 value is None 时返回 default
2) `normalize_text(value)`：
   - value 为 None -> 返回 None
   - value 为 str 且 strip 后为空 -> 返回 None
   - 否则返回 strip 后的字符串

提示：
- 不能用 `value or default` 实现 None 合并：因为 0/""/False 也会被当成“缺失值”。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/10_Conditionals/Exercises/02_truthiness_blank_and_none.py
"""

from __future__ import annotations


def coalesce_none(value: object, default: object) -> object:
    return default if value is None else value


def normalize_text(value: str | None) -> str | None:
    if value is None:
        return None
    s = value.strip()
    if not s:
        return None
    return s


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("none", coalesce_none(None, 10), 10)
    check("zero", coalesce_none(0, 10), 0)
    check("empty", coalesce_none("", "x"), "")
    check("false", coalesce_none(False, True), False)

    check("normalize_none", normalize_text(None), None)
    check("normalize_blank", normalize_text("   "), None)
    check("normalize_text", normalize_text("  Alice  "), "Alice")


if __name__ == "__main__":
    main()

