#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：一行打印可迭代对象（iterable）：print(*items)

你会学到：
1) `print(items)`：打印“容器本身”（如列表的 repr）
2) `print(*items)`：把容器“拆开”当作多个参数传给 print
3) `print(*items, sep=", ")`：常见的一行输出方式
4) dict 的 `*` 解包会产生“键”；想打印 key=value 要自己组织
5) set 的顺序不稳定：想要稳定输出用 `sorted(...)`

运行：
    python3 01_Basics/03_Printing/03_unpacking_iterables.py
"""


def main() -> None:
    items = [1, 2, 3]
    print("1) print(items) 打印容器：")
    print(items)

    print("\n2) print(*items) 打印元素：")
    print(*items)

    print("\n3) 指定 sep：")
    print(*items, sep=", ")

    print("\n4) range 也是可迭代对象：")
    print(*range(5), sep=" -> ")

    print("\n5) dict 的 * 解包是 key：")
    cfg = {"host": "127.0.0.1", "port": 8080}
    print("*cfg ->", *cfg)  # 等价于打印 cfg 的 keys

    print("\n6) set 的顺序不稳定：建议排序后再输出：")
    s = {"b", "a", "c"}
    print("raw set  ->", s)
    print("sorted   ->", *sorted(s), sep=", ")


if __name__ == "__main__":
    main()

