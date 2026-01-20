#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11：可变性（修复嵌套列表的“共享引用”坑）

题目：
很多人会写出这种二维表格：
    grid = [[0] * cols] * rows
它会让每一行都指向同一个内层 list，导致“改一行，全变”。

请实现：
1) make_grid(rows, cols, fill)：正确创建二维列表（行彼此独立）
2) make_grid_factory(rows, cols, factory)：当 fill 是“可变对象”时，用 factory 每格生成新对象

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/11_mutability_copy_fix.py
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def make_grid(rows: int, cols: int, fill: T) -> list[list[T]]:
    if rows < 0 or cols < 0:
        raise ValueError("rows/cols must be >= 0")
    return [[fill] * cols for _ in range(rows)]


def make_grid_factory(rows: int, cols: int, factory: Callable[[], T]) -> list[list[T]]:
    if rows < 0 or cols < 0:
        raise ValueError("rows/cols must be >= 0")
    return [[factory() for _ in range(cols)] for _ in range(rows)]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    bad = [[0] * 3] * 2
    bad[0][0] = 99
    check("bad shared rows", bad, [[99, 0, 0], [99, 0, 0]])

    good = make_grid(2, 3, 0)
    good[0][0] = 99
    check("good independent rows", good, [[99, 0, 0], [0, 0, 0]])

    cells = make_grid_factory(2, 2, list)
    cells[0][0].append("x")
    check("mutable cells isolated", cells, [[["x"], []], [[], []]])


if __name__ == "__main__":
    main()

