#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：range（整数序列对象）

你会学到：
1) range 的三种写法：range(stop) / range(start, stop) / range(start, stop, step)
2) range 支持：len、成员测试、索引与切片（切片仍是 range）
3) range 是惰性的：适合遍历，不适合无脑 list(...) 展开大范围

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/07_range_basics.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) range 基本写法")
    print("range(5) ->", list(range(5)))
    print("range(2, 8) ->", list(range(2, 8)))
    print("range(10, 0, -3) ->", list(range(10, 0, -3)))

    show("2) 成员测试/索引/切片")
    r = range(2, 10, 2)
    print("r ->", r)
    print("6 in r ->", 6 in r)
    print("7 in r ->", 7 in r)
    print("r[0] ->", r[0], "r[-1] ->", r[-1])
    print("r[1:] ->", r[1:], "list(r[1:]) ->", list(r[1:]))

    show("3) 不要随便展开超大 range")
    big = range(10**12)
    print("len(range(10**12)) ->", len(big))
    print("big[0], big[-1] ->", big[0], big[-1])


if __name__ == "__main__":
    main()

