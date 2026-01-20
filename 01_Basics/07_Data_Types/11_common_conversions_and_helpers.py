#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：常见转换与工具函数（把各种类型用起来）。

你会学到：
1) str / repr / ascii：面向用户 vs 面向调试
2) list/tuple/set/dict 的常见构造方式
3) len / iter / next：迭代器基础
4) sorted / reversed：排序与反转（注意：sorted 返回新列表）

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/11_common_conversions_and_helpers.py
"""

from __future__ import annotations


def main() -> None:
    print("1) str/repr/ascii：")
    text = "hi\n你好"
    print("str  ->", str(text))
    print("repr ->", repr(text))
    print("ascii->", ascii(text))

    print("\n2) 构造 list/tuple/set/dict：")
    it = range(3)
    print("list(range(3)) ->", list(it))
    print("tuple(range(3)) ->", tuple(range(3)))
    print("set([1,1,2]) ->", set([1, 1, 2]))
    print("dict([('a',1),('b',2)]) ->", dict([("a", 1), ("b", 2)]))

    print("\n3) iter/next：")
    iterator = iter(["a", "b", "c"])
    print("next ->", next(iterator))
    print("next ->", next(iterator))
    print("rest as list ->", list(iterator))

    print("\n4) sorted/reversed：")
    nums = [3, 1, 2]
    print("nums =", nums)
    print("sorted(nums) ->", sorted(nums))
    print("nums still ->", nums)
    print("reversed(nums) ->", list(reversed(nums)))


if __name__ == "__main__":
    main()

