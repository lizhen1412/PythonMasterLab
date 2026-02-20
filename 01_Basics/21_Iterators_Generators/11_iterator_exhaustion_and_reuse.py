#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：一次性迭代器的耗尽与复用策略。
Author: Lambert

你会学到：
1) 生成器/迭代器只能消费一次
2) 需要复用时，可先缓存为 list/tuple

运行：
    python3 01_Basics/21_Iterators_Generators/11_iterator_exhaustion_and_reuse.py
"""


def sum_twice_bad(it) -> int:
    return sum(it) + sum(it)


def sum_twice_good(it) -> int:
    cached = list(it)
    return sum(cached) + sum(cached)


def main() -> None:
    gen = (n for n in range(4))
    print("bad ->", sum_twice_bad(gen))

    gen2 = (n for n in range(4))
    print("good ->", sum_twice_good(gen2))

    nums = [0, 1, 2, 3]
    print("list ->", sum_twice_good(nums))


if __name__ == "__main__":
    main()