#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：while 的补充模式（do-while / := / 迭代器驱动）

你会学到：
1) do-while：Python 没有 do-while，可用 while True + break 保证至少执行一次
2) := 在 while 条件里：常见于“读一行/读一块”直到空字符串
3) next + sentinel：用迭代器驱动 while，避免手动索引
4) while-else 搭配迭代器搜索：没 break 才会进入 else

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/09_while_patterns_and_edge_cases.py
"""

from __future__ import annotations

import io


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) do-while 模式：至少执行一次")
    i = 0
    while True:
        print("i =", i)
        i += 1
        if i >= 3:
            break

    show("2) := 在 while 条件里（readline 直到空字符串）")
    stream = io.StringIO("Alice\n\nBob\nEND\nIgnored\n")
    out: list[str] = []
    while (line := stream.readline()) != "":
        name = line.strip()
        if not name:
            continue
        if name == "END":
            break
        out.append(name)
    print("out ->", out)

    show("3) next + sentinel 驱动 while")
    it = iter([1, 2, 3])
    sentinel = object()
    total = 0
    while (value := next(it, sentinel)) is not sentinel:
        total += value
    print("sum ->", total)

    show("4) while-else：迭代器搜索")
    it2 = iter([2, 4, 6])
    sentinel2 = object()
    while (n := next(it2, sentinel2)) is not sentinel2:
        if n % 2 == 1:
            print("found odd ->", n)
            break
    else:
        print("all even ->", True)


if __name__ == "__main__":
    main()
