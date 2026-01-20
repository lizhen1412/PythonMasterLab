#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：双分支（奇偶判断）

题目：
实现两个函数：
1) `parity_label_if(n)`：用 if/else 返回 "even" 或 "odd"
2) `parity_label_expr(n)`：用条件表达式返回 "even" 或 "odd"

参考答案：
- 本文件函数实现即为参考答案；`main()` 会对 0..4 做自测。

运行：
    python3 01_Basics/10_Conditionals/Exercises/04_double_branch_parity_label.py
"""

from __future__ import annotations


def parity_label_if(n: int) -> str:
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


def parity_label_expr(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    for n in range(5):
        check(f"if_{n}", parity_label_if(n), parity_label_expr(n))
    check("if_0", parity_label_if(0), "even")
    check("if_1", parity_label_if(1), "odd")


if __name__ == "__main__":
    main()

