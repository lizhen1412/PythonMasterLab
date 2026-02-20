#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：赋值目标（assignment targets）。
Author: Lambert

在 Python 里，`=` 左边不仅可以是“变量名”，还可以是：
1) 属性：obj.attr = ...
2) 下标：seq[i] = ...、mapping[key] = ...
3) 切片：seq[i:j] = ...
4) 解包目标：a, b = ...

运行：
    python3 01_Basics/02_Variables/05_assignment_targets.py
"""

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def main() -> None:
    print("1) 给变量名赋值：")
    value = 123
    print("value =", value)

    print("\n2) 给对象属性赋值：")
    p = Point(1, 2)
    print("before:", p)
    p.x = 10
    p.y = 20
    print("after :", p)

    print("\n3) 给列表下标/切片赋值：")
    numbers = [0, 1, 2, 3, 4]
    print("before:", numbers)
    numbers[0] = 999
    numbers[1:3] = [7, 8, 9]
    print("after :", numbers)

    print("\n4) 给字典 key 赋值：")
    config: dict[str, object] = {"host": "127.0.0.1"}
    config["port"] = 8080
    print("config =", config)


if __name__ == "__main__":
    main()
