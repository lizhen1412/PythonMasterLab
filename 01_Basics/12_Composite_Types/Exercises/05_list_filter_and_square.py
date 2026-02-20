#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：list 过滤 + 映射（推导式）
Author: Lambert

题目：
实现函数 `even_squares(nums)`：
- 输入：整数列表 nums
- 输出：只保留偶数并求平方后的新列表

示例：
    [1,2,3,4] -> [4, 16]

要求：
- 使用列表推导式完成（推荐写成一行）

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/05_list_filter_and_square.py
"""

from __future__ import annotations


def even_squares(nums: list[int]) -> list[int]:
    return [n * n for n in nums if n % 2 == 0]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("even_squares([])", even_squares([]), [])
    check("even_squares([1,2,3,4])", even_squares([1, 2, 3, 4]), [4, 16])
    check("even_squares([-2,-1,0,3])", even_squares([-2, -1, 0, 3]), [4, 0])


if __name__ == "__main__":
    main()
