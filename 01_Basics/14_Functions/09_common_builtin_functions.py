#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：常用内置函数（函数式/迭代工具）分类与易错点。
Author: Lambert

- 聚合：len/sum/any/all/min/max
- 迭代/序列：sorted/reversed/zip/enumerate
- 数值：round/divmod/pow/abs
- 函数式：map/filter（与推导式对比）
"""

from __future__ import annotations

from itertools import pairwise
from typing import Iterable


def aggregation_examples() -> None:
    """聚合函数：理解返回类型与适用场景。"""
    data = [1, 2, 3, 4]
    print("len(data) ->", len(data))
    print("sum(data) ->", sum(data))
    print("any([0, '', None, 5]) ->", any([0, "", None, 5]))
    print("all([1, True, 'x']) ->", all([1, True, "x"]))
    print("min/max ->", min(data), max(data))

    # sum 不适合拼接字符串；推荐使用 join
    words = ["hello", "world"]
    print("用 join 拼接字符串 ->", " ".join(words))


def iteration_helpers() -> None:
    """排序/翻转/并行遍历。"""
    items = ["banana", "apple", "cherry"]
    print("sorted 默认按字母 ->", sorted(items))
    print("sorted key=len ->", sorted(items, key=len))
    print("sorted reverse=True ->", sorted(items, reverse=True))
    print("reversed ->", list(reversed(items)))

    a = [1, 2, 3]
    b = ["a", "b", "c"]
    print("zip 并行遍历 ->", list(zip(a, b)))
    print("enumerate start=1 ->", list(enumerate(items, start=1)))

    print("pairwise（3.10+） ->", list(pairwise([10, 20, 30, 40])))


def numeric_helpers() -> None:
    """数值相关内置函数。"""
    print("round(2.675, 2) ->", round(2.675, 2), "(银行家舍入，可能不是直觉值)")
    print("divmod(17, 5) ->", divmod(17, 5))
    print("pow(2, 5) ->", pow(2, 5))
    print("pow(2, 5, 7) ->", pow(2, 5, 7), "(带模，避免大数)")
    print("abs(-3+4j) ->", abs(-3 + 4j))


def map_filter_vs_comprehension() -> None:
    """map/filter 与推导式的对比：可读性优先。"""
    nums = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, nums))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("map/filter ->", doubled, evens)

    # 等价的推导式写法通常更直观
    doubled_comp = [x * 2 for x in nums]
    evens_comp = [x for x in nums if x % 2 == 0]
    print("推导式 ->", doubled_comp, evens_comp)


def main() -> None:
    print("== 聚合函数 ==")
    aggregation_examples()

    print("\n== 迭代/排序辅助 ==")
    iteration_helpers()

    print("\n== 数值辅助 ==")
    numeric_helpers()

    print("\n== map/filter vs 推导式 ==")
    map_filter_vs_comprehension()


if __name__ == "__main__":
    main()