#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：可变 vs 不可变（别名、浅拷贝/深拷贝、嵌套陷阱）
Author: Lambert

你会学到：
1) b = a 不是复制（只是同一个对象的别名）
2) list/dict/set 可变：原地修改会影响别名
3) str/tuple 不可变：看起来“修改”其实是新对象
4) 浅拷贝 vs 深拷贝：嵌套结构内层是否共享

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/11_mutability_and_copy.py
"""

from __future__ import annotations

import copy


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 别名：b = a 不是复制")
    a = [1, 2]
    b = a
    a.append(3)
    print("a ->", a)
    print("b ->", b, "(a is b ->", a is b, ")")

    show("2) 不可变对象：str 的“修改”会产生新对象")
    s1 = "hi"
    s2 = s1
    s1 += "!"
    print("s1 ->", s1)
    print("s2 ->", s2, "(s1 is s2 ->", s1 is s2, ")")

    show("3) 浅拷贝 vs 深拷贝（嵌套结构）")
    nested = [[1, 2], [3, 4]]
    shallow = copy.copy(nested)
    deep = copy.deepcopy(nested)
    nested[0].append(99)
    print("nested ->", nested)
    print("shallow ->", shallow, "(share inner ->", shallow[0] is nested[0], ")")
    print("deep ->", deep, "(share inner ->", deep[0] is nested[0], ")")

    show("4) 元组自身不可变，但可能包含可变对象")
    inner: list[int] = [1, 2]
    t = (inner, "ok")
    inner.append(3)
    print("tuple ->", t)


if __name__ == "__main__":
    main()
