#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：collections.defaultdict。

你会学到：
1) defaultdict(list) 用于分组
2) defaultdict(int) 用于计数

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/04_collections_defaultdict.py
"""

from collections import defaultdict


def main() -> None:
    words = ["apple", "ant", "banana", "bear", "apricot"]
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    print("grouped ->", dict(groups))

    counts = defaultdict(int)
    for word in words:
        counts[word[0]] += 1
    print("counts ->", dict(counts))


if __name__ == "__main__":
    main()
