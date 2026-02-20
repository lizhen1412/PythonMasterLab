#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：reduce 与 cmp_to_key。
Author: Lambert

你会学到：
1) reduce 做折叠式聚合
2) cmp_to_key 把“比较函数”转成 key

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/14_functools_reduce_and_cmp_to_key.py
"""

from functools import cmp_to_key, reduce


def main() -> None:
    nums = [1, 2, 3, 4]
    total = reduce(lambda acc, x: acc + x, nums, 0)
    print("reduce sum ->", total)

    words = ["pear", "fig", "banana", "kiwi"]

    def cmp_len(a: str, b: str) -> int:
        return len(a) - len(b)

    sorted_words = sorted(words, key=cmp_to_key(cmp_len))
    print("sorted by length ->", sorted_words)


if __name__ == "__main__":
    main()