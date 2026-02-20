#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：break / continue（以及 loop-else 与嵌套循环退出策略）
Author: Lambert

你会学到：
1) break：跳出当前这一层循环（只影响最内层）
2) continue：跳过本轮剩余语句，进入下一轮
3) loop-else：for/while 的 else 只会在“没有 break”的情况下执行
4) 多层循环退出常见写法：flag / 提前 return / 把搜索封装成函数

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/04_break_and_continue.py
"""

from __future__ import annotations


def find_in_grid_flag(grid: list[list[int]], target: int) -> tuple[int, int] | None:
    found: tuple[int, int] | None = None
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == target:
                found = (r, c)
                break
        if found is not None:
            break
    return found


def find_in_grid_return(grid: list[list[int]], target: int) -> tuple[int, int] | None:
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == target:
                return (r, c)
    return None


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) continue：过滤数据（跳过空白）")
    raw = ["", "  ", "Alice", "Bob", "   Carol  "]
    out: list[str] = []
    for s in raw:
        if not s.strip():
            continue
        out.append(s.strip())
    print("raw ->", raw)
    print("out ->", out)

    show("2) break：找到就停止")
    nums = [1, 3, 5, 7, 8, 9]
    for n in nums:
        if n % 2 == 0:
            print("first even ->", n)
            break
    else:
        print("no even number")

    show("3) loop-else：查找失败才执行 else")
    target = 4
    for n in nums:
        if n == target:
            print("found target ->", target)
            break
    else:
        print("not found ->", target)

    show("4) 嵌套循环：break 只退出最内层")
    grid = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    print("find_in_grid_flag(grid, 5) ->", find_in_grid_flag(grid, 5))
    print("find_in_grid_return(grid, 5) ->", find_in_grid_return(grid, 5))
    print("find_in_grid_flag(grid, 9) ->", find_in_grid_flag(grid, 9))


if __name__ == "__main__":
    main()
