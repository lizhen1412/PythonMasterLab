#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：列表 list 的创建方式

你会学到：
1) 字面量：[]
2) 构造：list(iterable)
3) 推导式：[expr for x in it if cond]
4) 星号解包：[*iterable]
5) 常见坑：[[0]] * n 会共享内层 list

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/03_list_creation.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 字面量与构造函数")
    a = []
    b = list()
    c = list(range(5))
    d = list("abc")
    print("a ->", a)
    print("b ->", b)
    print("c ->", c)
    print("d ->", d)

    show("2) 推导式（map/filter 的常用替代）")
    squares = [x * x for x in range(6)]
    evens = [x for x in range(10) if x % 2 == 0]
    print("squares ->", squares)
    print("evens ->", evens)

    show("3) 星号解包：[*iterable]")
    items = [10, 20]
    merged = [0, *items, 30]
    print("merged ->", merged)

    show("4) 常见坑：重复创建嵌套 list")
    ok = [[0] for _ in range(3)]
    bad = [[0]] * 3
    bad[0].append(1)
    print("ok  ->", ok, "（互相独立）")
    print("bad ->", bad, "（共享同一个内层 list）")


if __name__ == "__main__":
    main()

