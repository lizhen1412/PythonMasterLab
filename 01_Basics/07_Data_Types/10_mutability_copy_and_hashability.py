#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：可变性 / 拷贝 / 可哈希性（理解“为什么 list 不能当 dict key”）。
Author: Lambert

你会学到：
1) 可变对象的别名问题：`b = a` 不是复制
2) 浅拷贝 vs 深拷贝：嵌套结构里差别巨大
3) 可哈希（hashable）与“能否当 dict key / set 元素”的关系
4) tuple 作为 key 时，内部元素也必须可哈希

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/10_mutability_copy_and_hashability.py
"""

from __future__ import annotations

import copy


def main() -> None:
    print("1) b = a 不是复制（只是多了一个名字）：")
    a = [1, 2]
    b = a
    b.append(3)
    print("a =", a)
    print("b =", b)
    print("a is b ->", a is b)

    print("\n2) 浅拷贝 vs 深拷贝（嵌套结构）：")
    nested = [[1], [2]]
    shallow = list(nested)  # 或 nested.copy()
    deep = copy.deepcopy(nested)
    nested[0].append(99)
    print("nested  =", nested)
    print("shallow =", shallow, "（浅拷贝共享内部 list）")
    print("deep    =", deep, "（深拷贝不共享内部 list）")

    print("\n3) 可哈希性：")
    print("hash(123) ->", hash(123))
    print("hash('hi') ->", hash("hi"))
    print("hash((1,2)) ->", hash((1, 2)))
    try:
        print("hash([1,2]) ->", hash([1, 2]))
    except TypeError as exc:
        print("hash([1,2]) -> TypeError:", exc)

    print("\n4) dict key 规则：")
    ok = {(1, 2): "tuple ok"}
    print("ok =", ok)
    try:
        m2: dict[object, str] = {}
        m2[[1, 2]] = "list not ok"
    except TypeError as exc:
        print("list 不能当 key：", exc)

    print("\n5) tuple 里包含 list 也不行：")
    try:
        m3: dict[object, str] = {}
        m3[(1, [2])] = "no"
    except TypeError as exc:
        print("(1, [2]) 不能当 key：", exc)


if __name__ == "__main__":
    main()