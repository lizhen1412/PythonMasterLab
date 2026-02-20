#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：str.format / format_map（旧但仍常见，必须能看懂）。
Author: Lambert

你会学到：
1) 位置参数：`"{0} {1}".format(a, b)`
2) 命名参数：`"{name}".format(name="Alice")`
3) 字段访问：`"{user.name}"`、`"{items[0]}"`
4) `format_map(mapping)`：用 dict 一次性喂进去
5) 转义大括号：`{{` / `}}`

运行：
    python3 01_Basics/04_Formatting/08_str_format_and_format_map.py
"""

from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


def main() -> None:
    name = "Alice"
    age = 20

    print("1) 位置参数：")
    print("name={0} age={1}".format(name, age))

    print("\n2) 命名参数：")
    print("name={name} age={age}".format(name=name, age=age))

    print("\n3) 字段访问：属性/下标：")
    user = User(name="Bob", age=7)
    items = ["x", "y", "z"]
    print("user={u.name} age={u.age} first={items[0]}".format(u=user, items=items))

    print("\n4) format_map：")
    data = {"name": name, "age": age}
    print("name={name} age={age}".format_map(data))

    print("\n5) 转义大括号：")
    print("literal braces: {{ and }} -> {0} {1}".format("{", "}"))


if __name__ == "__main__":
    main()
