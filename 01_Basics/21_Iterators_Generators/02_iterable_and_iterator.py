#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：可迭代对象 vs 迭代器。

你会学到：
1) iterable：能被 iter(x) 转成迭代器
2) iterator：实现 __iter__ + __next__，并可被 next() 拉取
3) iterator 自身也是 iterable（iter(it) is it）

运行：
    python3 01_Basics/21_Iterators_Generators/02_iterable_and_iterator.py
"""


def describe(obj: object, label: str) -> None:
    has_iter = hasattr(obj, "__iter__")
    has_next = hasattr(obj, "__next__")
    print(f"{label:<10} iterable={has_iter} iterator={has_next}")


def main() -> None:
    items = [1, 2, 3]
    it = iter(items)

    print("== 类型与协议 ==")
    describe(items, "list")
    describe(it, "iterator")

    print("\n== iterator 也是 iterable ==")
    print("iter(it) is it ->", iter(it) is it)

    print("\n== 字符串也是 iterable ==")
    text = "abc"
    describe(text, "str")
    print("iter(str) ->", iter(text))


if __name__ == "__main__":
    main()
