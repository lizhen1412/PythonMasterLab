#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：break（嵌套循环查找坐标）

题目：
实现两个函数：
1) `find_in_grid_flag(grid, target)`：用 flag + break 跳出两层循环，返回 (row, col) 或 None
2) `find_in_grid_return(grid, target)`：把搜索封装成函数，找到直接 return

参考答案：
- 本文件函数实现即为参考答案；`main()` 会对比两种写法输出一致。

运行：
    python3 01_Basics/11_Loops/Exercises/05_break_nested_search.py
"""

from __future__ import annotations


def find_in_grid_flag(grid: list[list[int]], target: int) -> tuple[int, int] | None:
    found: tuple[int, int] | None = None
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == target:
                found = (r, c)
                break
        if found is not None:
            break
    return found


def find_in_grid_return(grid: list[list[int]], target: int) -> tuple[int, int] | None:
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == target:
                return (r, c)
    return None


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    grid = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    check("flag_found", find_in_grid_flag(grid, 5), (1, 1))
    check("return_found", find_in_grid_return(grid, 5), (1, 1))
    check("flag_not_found", find_in_grid_flag(grid, 9), None)
    check("return_not_found", find_in_grid_return(grid, 9), None)


if __name__ == "__main__":
    main()

