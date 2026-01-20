#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：序列（Sequence）通用操作

本例用 list/tuple/range/str 演示序列的共通能力：
1) 索引与负索引
2) 切片（start/stop/step）
3) 成员测试：in / not in
4) 拼接与重复：+ / *
5) 解包：a, b = seq；first, *middle, last = seq

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/02_sequences_overview.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 索引与切片（list / tuple / str）")
    items = [10, 20, 30, 40, 50]
    t = (10, 20, 30, 40, 50)
    s = "abcdef"
    print("items[0] ->", items[0])
    print("items[-1] ->", items[-1])
    print("items[1:4] ->", items[1:4])
    print("items[::2] ->", items[::2])
    print("t[1:4] ->", t[1:4])
    print("s[::-1] ->", s[::-1])

    show("2) range 也支持 len/索引/切片")
    r = range(2, 10, 2)
    print("range ->", r)
    print("len(range) ->", len(r))
    print("range[0] ->", r[0])
    print("range[-1] ->", r[-1])
    print("range[1:] ->", r[1:], "（切片仍是 range）")

    show("3) 成员测试 in")
    print("30 in items ->", 30 in items)
    print("'cd' in s ->", "cd" in s)
    print("6 in r ->", 6 in r)
    print("7 in r ->", 7 in r)

    show("4) 拼接与重复（注意：只有同类型序列才能 +）")
    print("[1,2] + [3] ->", [1, 2] + [3])
    print("'ab' * 3 ->", "ab" * 3)
    print("(1,2) + (3,) ->", (1, 2) + (3,))

    show("5) 解包（unpacking）")
    a, b, c = [1, 2, 3]
    print("a,b,c ->", a, b, c)
    first, *middle, last = [10, 20, 30, 40]
    print("first,middle,last ->", first, middle, last)


if __name__ == "__main__":
    main()

