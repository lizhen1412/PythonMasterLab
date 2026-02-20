#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：cache / lru_cache。
Author: Lambert

你会学到：
1) cache：无限容量的记忆化
2) lru_cache：有容量限制的 LRU 缓存

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/12_functools_cache_lru_cache.py
"""

from functools import cache, lru_cache


@cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=3)
def square(n: int) -> int:
    return n * n


def main() -> None:
    print("fib(10) ->", fib(10))
    print("fib.cache_info ->", fib.cache_info())

    for n in [2, 3, 4, 2, 5, 3, 6]:
        print("square", n, "->", square(n))
    print("square.cache_info ->", square.cache_info())


if __name__ == "__main__":
    main()