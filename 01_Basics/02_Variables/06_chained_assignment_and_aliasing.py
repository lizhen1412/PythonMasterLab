#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：链式赋值与别名陷阱（a = b = ...）。

链式赋值会把“同一个对象”绑定给多个名字：
    a = b = some_object

对于不可变对象（int/str/tuple...），通常没问题；
但对于可变对象（list/dict/set...），非常容易踩坑：
    a = b = []
    a.append(1)
    # b 也会变，因为 a 和 b 指向同一份列表

运行：
    python3 01_Basics/02_Variables/06_chained_assignment_and_aliasing.py
"""


def main() -> None:
    print("1) 不可变对象：链式赋值一般没问题")
    x = y = 0
    print("x, y =", x, y, "| x is y =", x is y)
    x += 1
    print("x += 1 -> x, y =", x, y, "| x is y =", x is y)

    print("\n2) 可变对象：链式赋值容易产生“别名”")
    a = b = []
    print("a is b =", a is b)
    a.append("from a")
    print("a =", a)
    print("b =", b)

    print("\n3) 正确写法：分别创建对象")
    c, d = [], []
    print("c is d =", c is d)
    c.append("only c")
    print("c =", c)
    print("d =", d)


if __name__ == "__main__":
    main()

