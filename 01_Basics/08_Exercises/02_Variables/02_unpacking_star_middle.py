#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：解包 first/*middle/last
Author: Lambert

题目：
实现 `split_head_middle_tail(items)`，要求：
- 输入 list 至少包含 2 个元素
- 返回 `(first, middle_list, last)`

参考答案：
- 本文件中函数实现即为参考答案；`main()` 里带自测输出（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/02_Variables/02_unpacking_star_middle.py
"""


def split_head_middle_tail(items: list[int]) -> tuple[int, list[int], int]:
    first, *middle, last = items
    return first, middle, last


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    first, middle, last = split_head_middle_tail([10, 20, 30, 40])
    check("first", first, 10)
    check("middle", middle, [20, 30])
    check("last", last, 40)


if __name__ == "__main__":
    main()
