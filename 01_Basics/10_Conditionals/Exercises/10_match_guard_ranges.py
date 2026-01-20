#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：match + guard（范围判断）

题目：
实现 `classify(obj)`，规则：
- obj 是 int 且 < 0 -> "negative"
- obj == 0 -> "zero"
- obj 是 int 且 > 0 -> "positive"
- 其他 -> "other"

要求：
- 使用 match/case
- 使用 guard：`case int() as n if n < 0: ...`

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/10_Conditionals/Exercises/10_match_guard_ranges.py
"""

from __future__ import annotations


def classify(obj: object) -> str:
    match obj:
        case int() as n if n < 0:
            return "negative"
        case 0:
            return "zero"
        case int() as n if n > 0:
            return "positive"
        case _:
            return "other"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("neg", classify(-1), "negative")
    check("zero", classify(0), "zero")
    check("pos", classify(1), "positive")
    check("other", classify("1"), "other")


if __name__ == "__main__":
    main()

