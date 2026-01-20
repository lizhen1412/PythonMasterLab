#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：accumulate / pairwise / zip_longest。

你会学到：
1) accumulate：累计求和或自定义累积
2) pairwise：相邻元素成对
3) zip_longest：以最长为准对齐

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/10_itertools_accumulate_zip_longest.py
"""

from itertools import accumulate, pairwise, zip_longest


def main() -> None:
    data = [1, 2, 3, 4]
    print("accumulate ->", list(accumulate(data)))
    print("pairwise ->", list(pairwise(data)))

    left = ["A", "B"]
    right = [1, 2, 3]
    print("zip_longest ->", list(zip_longest(left, right, fillvalue=None)))


if __name__ == "__main__":
    main()
