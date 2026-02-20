#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：itertools.groupby。
Author: Lambert

你会学到：
1) groupby 只分“相邻的相同 key”
2) 想要全量分组，先按 key 排序

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/09_itertools_groupby.py
"""

from itertools import groupby


def main() -> None:
    items = ["a1", "a2", "b1", "a3", "b2"]
    key_func = lambda s: s[0]

    print("原始顺序分组:")
    for key, group in groupby(items, key=key_func):
        print(key, "->", list(group))

    print("\n先排序再分组:")
    for key, group in groupby(sorted(items, key=key_func), key=key_func):
        print(key, "->", list(group))


if __name__ == "__main__":
    main()