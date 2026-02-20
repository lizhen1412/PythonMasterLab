#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：序列类型（list / tuple / range）。
Author: Lambert

你会学到：
1) list：可变序列（append/extend/insert/pop/sort）
2) tuple：不可变序列（常用于“固定结构的数据”与解包）
3) range：整数序列的“惰性表示”（省内存），常用于 for 循环
4) 解包：`a, b = ...`、`first, *middle, last = ...`

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/06_list_tuple_range.py
"""

from __future__ import annotations


def main() -> None:
    print("1) list：")
    items = [3, 1, 2]
    print("items =", items)
    items.append(4)
    print("append ->", items)
    items.extend([5, 6])
    print("extend ->", items)
    items.insert(0, 0)
    print("insert ->", items)
    popped = items.pop()
    print("pop ->", popped, "items now ->", items)
    items.sort()
    print("sort ->", items)
    print("slice items[1:4] ->", items[1:4])

    print("\n2) tuple：")
    t = (10, 20, 30)
    print("t =", t)
    a, b, c = t
    print("unpack ->", a, b, c)
    single = (1,)  # 单元素 tuple 必须带逗号
    print("single tuple ->", single)

    print("\n3) range：")
    r = range(1, 10, 2)
    print("range(1, 10, 2) ->", r)
    print("list(r) ->", list(r))
    print("len(r) ->", len(r))
    print("5 in r ->", 5 in r)
    print("6 in r ->", 6 in r)

    print("\n4) 星号解包：")
    first, *middle, last = [1, 2, 3, 4, 5]
    print("first =", first)
    print("middle =", middle)
    print("last =", last)


if __name__ == "__main__":
    main()
