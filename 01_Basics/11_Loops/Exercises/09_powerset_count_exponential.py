#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：指数爆炸（2^n 与 powerset）

题目：
实现：
1) `powerset_count(n)`：返回子集数量 2^n（n>=0）
2) `powerset(items)`：返回 items 的所有子集（仅用于小规模演示）

提示：
- powerset 的数量是 2^n；n 稍大就会爆内存/爆时间。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/11_Loops/Exercises/09_powerset_count_exponential.py
"""

from __future__ import annotations


def powerset_count(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    return 2**n


def powerset(items: list[str]) -> list[list[str]]:
    subsets: list[list[str]] = [[]]
    for x in items:
        subsets += [s + [x] for s in subsets]
    return subsets


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("count_0", powerset_count(0), 1)
    check("count_4", powerset_count(4), 16)

    items = ["A", "B", "C", "D"]
    ps = powerset(items)
    check("len_ps", len(ps), 16)
    check("first", ps[0], [])
    check("last", ps[-1], ["A", "B", "C", "D"])


if __name__ == "__main__":
    main()

