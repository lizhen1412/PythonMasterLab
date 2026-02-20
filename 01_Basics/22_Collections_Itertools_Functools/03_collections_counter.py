#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：collections.Counter。
Author: Lambert

你会学到：
1) Counter 统计频率
2) most_common 获取 top-k
3) update/subtract 用于增减计数

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/03_collections_counter.py
"""

from collections import Counter


def main() -> None:
    text = "banana"
    counter = Counter(text)
    print("Counter ->", counter)
    print("count('a') ->", counter["a"])
    print("most_common(2) ->", counter.most_common(2))

    counter.update("aa")
    print("after update('aa') ->", counter)

    counter.subtract("an")
    print("after subtract('an') ->", counter)


if __name__ == "__main__":
    main()