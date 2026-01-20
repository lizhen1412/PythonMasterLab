#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：一行打印多个内容的常见错误（并给出正确写法）。

你会学到：
1) `+` 拼接要求两边同类型：字符串 + 非字符串会 TypeError
2) `join` 要求元素都是 str
3) `sep` 必须是 str（不是 int/bool）
4) 想打印列表元素：用 `print(*items)`，不要误以为 `print(items)` 会自动展开
5) 反例里用到 `typing.cast` 让静态类型检查器不告警（注意：cast 不会做运行时类型转换）

运行：
    python3 01_Basics/03_Printing/11_common_mistakes.py
"""

from typing import cast


def main() -> None:
    age = 20

    print("1) 字符串拼接 + 非字符串：")
    try:
        _ = "age=" + cast(str, age)
    except TypeError as exc:
        print("TypeError:", exc)
        print("正确写法：", f"age={age}")

    print("\n2) join 非字符串元素：")
    nums = [1, 2, 3]
    try:
        _ = ",".join(cast(list[str], nums))
    except TypeError as exc:
        print("TypeError:", exc)
        print("正确写法 A：", ",".join(map(str, nums)))
        print("正确写法 B：", *nums, sep=",")

    print("\n3) sep 不是字符串：")
    try:
        print(1, 2, sep=cast(str, 0))
    except TypeError as exc:
        print("TypeError:", exc)
        print("正确写法：", 1, 2, sep="0")

    print("\n4) print(items) vs print(*items)：")
    items = ["a", "b", "c"]
    print("print(items)   ->", items)
    print("print(*items)  ->", *items)
    print("print(*items, sep='|')->", *items, sep="|")


if __name__ == "__main__":
    main()
