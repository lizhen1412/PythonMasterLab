#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：多分支（分数 -> 等级）

题目：
实现 `grade(score)`，规则：
- score 不在 [0, 100] -> "INVALID"
- 90..100 -> "A"
- 80..89  -> "B"
- 70..79  -> "C"
- 60..69  -> "D"
- 0..59   -> "F"

要求：
- 用 if/elif/else
- 使用链式比较验证范围（例如 `0 <= score <= 100`）

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/10_Conditionals/Exercises/05_multi_branch_grade.py
"""

from __future__ import annotations


def grade(score: int) -> str:
    if not (0 <= score <= 100):
        return "INVALID"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("invalid_low", grade(-1), "INVALID")
    check("invalid_high", grade(101), "INVALID")
    check("A", grade(90), "A")
    check("B", grade(89), "B")
    check("C", grade(70), "C")
    check("D", grade(60), "D")
    check("F", grade(59), "F")


if __name__ == "__main__":
    main()

