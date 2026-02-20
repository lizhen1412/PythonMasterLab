#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：while 循环（while loops）
Author: Lambert

你会学到：
1) while 的核心：初始化 -> 条件 -> 循环体 -> 更新
2) while True + break：把“退出条件”写在循环体里（常用于 sentinel/读输入）
3) continue：跳过本轮剩余逻辑（while 里要注意不要跳过更新语句）
4) while ... else：只有“正常结束（条件变 False）”时才执行 else；break 不会执行 else

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/02_while_loops.py
"""

from __future__ import annotations


def find_first_even(nums: list[int]) -> int | None:
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            return nums[i]
        i += 1
    return None


def search_with_while_else(nums: list[int], target: int) -> bool:
    i = 0
    while i < len(nums):
        if nums[i] == target:
            break
        i += 1
    else:
        # 没有 break，说明遍历完了也没找到
        return False
    return True


def consume_until_sentinel(items: list[str], sentinel: str = "END") -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(items):
        item = items[i].strip()
        i += 1
        if not item:
            continue
        if item == sentinel:
            break
        out.append(item)
    return out


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 基本 while：计数循环")
    i = 1
    while i <= 5:
        print("i =", i)
        i += 1

    show("2) while True + break（sentinel）")
    data = ["Alice\n", "  \n", "Bob\n", "END\n", "Ignored\n"]
    cleaned = consume_until_sentinel(data, sentinel="END")
    print("input =", [x.strip() for x in data])
    print("cleaned until END ->", cleaned)

    show("3) continue：跳过本轮（过滤空白）")
    nums = [1, 2, 3, 4, 5]
    i = 0
    odds: list[int] = []
    while i < len(nums):
        n = nums[i]
        i += 1
        if n % 2 == 0:
            continue
        odds.append(n)
    print("nums ->", nums)
    print("odds ->", odds)

    show("4) while-else：是否找到目标")
    print("find_first_even([1,3,5]) ->", find_first_even([1, 3, 5]))
    print("find_first_even([1,3,4]) ->", find_first_even([1, 3, 4]))
    print("search_with_while_else([1,2,3], 2) ->", search_with_while_else([1, 2, 3], 2))
    print("search_with_while_else([1,2,3], 9) ->", search_with_while_else([1, 2, 3], 9))


if __name__ == "__main__":
    main()
