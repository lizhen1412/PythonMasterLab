#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：元组 tuple 的创建与常用操作
Author: Lambert

你会学到：
1) 创建：()、(1,)、tuple(iterable)、打包/解包
2) 常用操作：索引/切片/拼接/重复/in/count/index
3) 不可变：不能修改元组“槽位”；但元组里如果放的是可变对象，内部仍可被修改

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/06_tuple_creation_and_ops.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 创建：空元组/单元素/构造")
    empty = ()
    single = (1,)
    made = tuple([1, 2, 3])
    print("empty ->", empty)
    print("single ->", single)
    print("made ->", made)

    show("2) 打包/解包")
    a, b = 1, 2  # packing
    x, y = (3, 4)  # unpacking
    print("a,b ->", a, b)
    print("x,y ->", x, y)
    first, *middle, last = (10, 20, 30, 40)
    print("first,middle,last ->", first, middle, last)

    show("3) 常用操作：索引/切片/拼接/重复")
    t = (10, 20, 30, 20)
    print("t[0] ->", t[0])
    print("t[1:3] ->", t[1:3])
    print("t + (40,) ->", t + (40,))
    print("(1,)*3 ->", (1,) * 3)

    show("4) 方法：count/index 与成员测试")
    print("20 in t ->", 20 in t)
    print("t.count(20) ->", t.count(20))
    print("t.index(30) ->", t.index(30))

    show("5) 不可变但可包含可变对象")
    inner: list[int] = [1, 2]
    box = (inner, "ok")
    inner.append(3)
    print("box ->", box, "（元组没变，但内层 list 变了）")

    show("6) 遍历：for / enumerate")
    for v in t:
        print("value ->", v)
    for i, v in enumerate(t, start=1):
        print("index,value ->", i, v)


if __name__ == "__main__":
    main()