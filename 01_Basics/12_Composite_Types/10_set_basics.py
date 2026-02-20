#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：集合 set（去重 + 集合运算）
Author: Lambert

你会学到：
1) 创建：set() / {1,2,3}（注意：{} 是空 dict，不是空 set）
2) add/update/remove/discard
3) 集合运算：并(|)、交(&)、差(-)、对称差(^)
4) frozenset：不可变集合

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/10_set_basics.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 创建：空 set 必须用 set()")
    empty = set()
    non_empty = {1, 2, 3, 3}
    print("empty ->", empty)
    print("non_empty ->", non_empty, "（自动去重）")

    show("2) add/update/remove/discard")
    s = {1, 2}
    s.add(3)
    s.update([3, 4, 5])
    print("after add/update ->", s)
    s.remove(5)
    s.discard(999)  # 不存在也不会报错
    print("after remove/discard ->", s)

    show("3) 集合运算")
    a = {1, 2, 3}
    b = {3, 4}
    print("a | b ->", a | b)
    print("a & b ->", a & b)
    print("a - b ->", a - b)
    print("a ^ b ->", a ^ b)
    print("a <= (a|b) ->", a <= (a | b))

    show("4) frozenset：不可变集合")
    fs = frozenset({1, 2})
    print("frozenset ->", fs)


if __name__ == "__main__":
    main()
