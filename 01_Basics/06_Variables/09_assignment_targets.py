#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：赋值目标（assignment targets）。

你会学到：
1) 赋值不只是 `x = ...`，还可以写到：
   - 属性：`obj.attr = ...`
   - 下标：`items[i] = ...`
   - 切片：`items[1:3] = ...`
2) 多目标解包赋值：`a, b = ...`
3) 赋值表达式 `:=` 可以在表达式里“绑定名字”（谨慎使用）

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/09_assignment_targets.py
"""

from __future__ import annotations


class Box:
    def __init__(self) -> None:
        self.value = 0


def main() -> None:
    print("1) 名字赋值：")
    x = 1
    print("x =", x)

    print("\n2) 属性赋值：")
    box = Box()
    print("before box.value =", box.value)
    box.value = 99
    print("after  box.value =", box.value)

    print("\n3) 下标赋值：")
    items = [10, 20, 30]
    print("before items =", items)
    items[1] = 200
    print("after  items =", items)

    print("\n4) 切片赋值：")
    items[1:3] = [7, 8, 9]
    print("slice assign items =", items)

    print("\n5) 解包赋值：")
    a, b = (1, 2)
    print("a =", a, "b =", b)

    print("\n6) 赋值表达式（海象运算符）:=：")
    if (n := len(items)) > 0:
        print("len(items) =", n)


if __name__ == "__main__":
    main()

