#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：列表 list 的日常操作（增删改查、排序、拷贝）

你会学到：
1) 索引/切片读取与切片赋值
2) append/extend/insert
3) remove/pop/del/clear
4) in/index/count
5) sort/sorted/reverse
6) copy 与别名：b = a 不是复制

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/04_list_daily_operations.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    items = [3, 1, 4, 1, 5]

    show("1) 读取：索引与切片")
    print("items ->", items)
    print("items[0] ->", items[0])
    print("items[-1] ->", items[-1])
    print("items[1:4] ->", items[1:4])

    show("2) 修改：索引赋值与切片赋值")
    items[0] = 99
    print("after items[0]=99 ->", items)
    items[1:3] = [10, 20, 30]
    print("after slice assign ->", items)

    show("3) 增：append / extend / insert")
    items.append(7)
    print("append ->", items)
    items.extend([8, 9])
    print("extend ->", items)
    items.insert(0, -1)
    print("insert ->", items)

    show("4) 删：remove / pop / del / clear")
    items.remove(1)  # 删除第一个匹配项
    print("remove(1) ->", items)
    last = items.pop()
    print("pop() ->", last, "remaining ->", items)
    del items[0]
    print("del items[0] ->", items)
    tmp = items.copy()
    tmp.clear()
    print("clear ->", tmp)

    show("5) 查：in / index / count")
    print("3 in items ->", 3 in items)
    print("items.count(1) ->", items.count(1))
    if 10 in items:
        print("items.index(10) ->", items.index(10))

    show("6) 排序：sort vs sorted")
    nums = [3, 1, 4, 1, 5]
    sorted_nums = sorted(nums)
    nums.sort(reverse=True)
    print("sorted(nums) ->", sorted_nums, "(nums still:", nums, "after sort reverse)")

    show("6.1) reverse：原地反转（不排序）")
    xs = [1, 2, 3]
    xs.reverse()
    print("after reverse ->", xs)

    show("7) copy 与别名")
    a = [1, 2]
    b = a
    c = a.copy()
    a.append(3)
    print("a ->", a)
    print("b (alias) ->", b)
    print("c (copy)  ->", c)


if __name__ == "__main__":
    main()
