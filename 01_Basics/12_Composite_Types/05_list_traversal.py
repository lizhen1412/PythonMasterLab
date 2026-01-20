#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：列表 list 的遍历（for/enumerate/reversed/推导式/安全修改）

你会学到：
1) for 遍历与 enumerate
2) reversed 遍历
3) 推导式：映射/过滤
4) 遍历时不要原地删除元素（会跳元素）；更稳：生成新列表或遍历副本

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/05_list_traversal.py
"""

from __future__ import annotations


def safe_filter_odds(nums: list[int]) -> list[int]:
    return [n for n in nums if n % 2 == 1]


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    items = ["Alice", "Bob", "Carol"]

    show("1) for 遍历")
    for name in items:
        print("name ->", name)

    show("2) enumerate：拿到索引（推荐）")
    for i, name in enumerate(items, start=1):
        print(i, name)

    show("3) reversed：反向遍历")
    for name in reversed(items):
        print("rev ->", name)

    show("4) 推导式：映射/过滤")
    upper = [s.upper() for s in items]
    long_names = [s for s in items if len(s) >= 4]
    print("upper ->", upper)
    print("len>=4 ->", long_names)

    show("5) 常见坑：遍历时删除元素会跳元素（不推荐）")
    nums = [1, 2, 3, 4, 5]
    removed: list[int] = []
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)
            removed.append(n)
    print("removed ->", removed)
    print("nums after remove in-loop ->", nums)
    print("safe_filter_odds([1..5]) ->", safe_filter_odds([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()

