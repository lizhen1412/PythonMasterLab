#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：集合（set / frozenset）。

你会学到：
1) set：无序、元素唯一、支持集合运算（并/交/差/对称差）
2) 去重：list -> set -> list（注意顺序会丢失；需要排序就用 sorted）
3) frozenset：不可变集合（可哈希，可做 dict key / set 元素）

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/08_set_frozenset.py
"""

from __future__ import annotations


def main() -> None:
    print("1) set 创建与成员测试：")
    s = {1, 2, 2, 3}
    print("s =", s)
    print("2 in s ->", 2 in s)
    s.add(4)
    print("add(4) ->", s)
    s.discard(999)  # 不存在不会报错
    print("discard(999) ->", s)

    print("\n2) 集合运算：")
    a = {1, 2, 3}
    b = {3, 4, 5}
    print("a =", a)
    print("b =", b)
    print("a | b (union) ->", sorted(a | b))
    print("a & b (intersection) ->", sorted(a & b))
    print("a - b (difference) ->", sorted(a - b))
    print("a ^ b (sym diff) ->", sorted(a ^ b))

    print("\n3) 去重：")
    nums = [3, 1, 2, 1, 3, 3]
    print("nums =", nums)
    print("dedupe (unordered) ->", list(set(nums)))
    print("dedupe + sorted ->", sorted(set(nums)))

    print("\n4) frozenset：不可变集合（可哈希）")
    fs = frozenset({1, 2})
    print("fs =", fs)
    mapping = {fs: "value"}
    print("dict with frozenset key ->", mapping)


if __name__ == "__main__":
    main()

