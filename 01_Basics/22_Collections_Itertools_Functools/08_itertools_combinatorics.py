#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：itertools 组合类工具。

你会学到：
1) product：笛卡尔积
2) permutations：排列（有序）
3) combinations：组合（无序）
4) combinations_with_replacement：允许重复

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/08_itertools_combinatorics.py
"""

from itertools import combinations, combinations_with_replacement, permutations, product


def main() -> None:
    items = ["A", "B", "C"]
    print("product ->", list(product([1, 2], ["x", "y"])))
    print("permutations ->", list(permutations(items, 2)))
    print("combinations ->", list(combinations(items, 2)))
    print("combinations_with_replacement ->", list(combinations_with_replacement(items, 2)))


if __name__ == "__main__":
    main()
