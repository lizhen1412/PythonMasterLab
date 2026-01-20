#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：yield from 委托生成器。

你会学到：
1) yield from 把迭代过程委托给子生成器
2) 子生成器 return 的值会成为 yield from 表达式结果

运行：
    python3 01_Basics/21_Iterators_Generators/09_yield_from_delegation.py
"""


def subgen():
    yield "A"
    yield "B"
    return "subgen done"


def delegating():
    result = yield from subgen()
    print("subgen return ->", result)


def main() -> None:
    print("delegating iteration:")
    for item in delegating():
        print("  ->", item)


if __name__ == "__main__":
    main()
