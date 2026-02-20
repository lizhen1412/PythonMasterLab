#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：itertools 基本积木。
Author: Lambert

你会学到：
1) count：无限序列
2) islice：对迭代器切片
3) chain：连接多个迭代器
4) repeat/cycle：重复元素或循环

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/07_itertools_building_blocks.py
"""

from itertools import chain, count, cycle, islice, repeat


def main() -> None:
    print("count + islice ->", list(islice(count(10, 2), 5)))
    print("chain ->", list(chain([1, 2], [3], [4, 5])))
    print("repeat ->", list(repeat("x", 3)))
    print("cycle + islice ->", list(islice(cycle("AB"), 6)))


if __name__ == "__main__":
    main()