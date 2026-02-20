#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：运算符优先级小测
Author: Lambert

题目：
先不要运行，先手算下面表达式的结果：
1) -2**2
2) (-2)**2
3) False or True and False
4) not 1 == 2
5) 1 < 2 == 2
6) 1 << 2 + 1
7) 1 | 2 & 3

然后实现 `evaluate()` 返回这些结果，并用自测验证你手算的结论。

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/09_Operators/Exercises/10_precedence_puzzles.py
"""

from __future__ import annotations


def evaluate() -> dict[str, object]:
    return {
        "-2**2": -2**2,
        "(-2)**2": (-2) ** 2,
        "False or True and False": False or True and False,
        "not 1 == 2": not 1 == 2,
        "1 < 2 == 2": 1 < 2 == 2,
        "1 << 2 + 1": 1 << 2 + 1,
        "1 | 2 & 3": 1 | 2 & 3,
    }


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    r = evaluate()
    check("-2**2", r["-2**2"], -4)
    check("(-2)**2", r["(-2)**2"], 4)
    check("False or True and False", r["False or True and False"], False)
    check("not 1 == 2", r["not 1 == 2"], True)
    check("1 < 2 == 2", r["1 < 2 == 2"], True)
    check("1 << 2 + 1", r["1 << 2 + 1"], 8)
    check("1 | 2 & 3", r["1 | 2 & 3"], 3)


if __name__ == "__main__":
    main()
