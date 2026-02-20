#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：变量是什么？——名字绑定对象（name binding）
Author: Lambert

很多语言里，“变量”更像一个能装值的盒子；但在 Python 里更准确的理解是：

- **变量名（name）**：一个“标签”
- **对象（object）**：真正保存数据的实体
- **赋值（=）**：把“名字”绑定到“对象”（把标签贴到某个对象上）

你会在本例中看到：
1) `type(x)`：对象的类型
2) `id(x)`：对象在本次运行中的身份标识（可理解为“地址的抽象”）
3) 重新绑定：同一个名字可以绑定到新对象（动态类型）
4) 可变对象（list）被原地修改时，`id` 不变；不可变对象（int/str）变更通常会产生新对象

运行：
    python3 01_Basics/02_Variables/02_variable_basics.py
"""


def describe(label: str, value: object) -> None:
    type_name = type(value).__name__
    print(f"{label:<18} value={value!r:<20} type={type_name:<10} id=0x{id(value):x}")


def main() -> None:
    print("1) 不可变对象：int 重新绑定会产生新对象")
    x = 10
    y = x
    describe("x", x)
    describe("y", y)

    x += 1
    print("x += 1 之后：")
    describe("x", x)
    describe("y", y)
    print("x is y =", x is y)

    print("\n2) 可变对象：list 原地修改通常 id 不变")
    items = [1, 2, 3]
    describe("items (before)", items)
    items.append(4)
    describe("items (after)", items)

    print("\n3) 别名（alias）：多个名字指向同一个对象")
    a = ["A"]
    b = a
    describe("a (before)", a)
    describe("b (before)", b)
    b.append("B")
    print("b.append('B') 之后：")
    describe("a (after)", a)
    describe("b (after)", b)
    print("a is b =", a is b)

    print("\n4) 动态类型：同一个名字可绑定不同类型的对象")
    value: object = 123
    describe("value (int)", value)
    value = "now a str"
    describe("value (str)", value)
    value = {"k": "v"}
    describe("value (dict)", value)


if __name__ == "__main__":
    main()
