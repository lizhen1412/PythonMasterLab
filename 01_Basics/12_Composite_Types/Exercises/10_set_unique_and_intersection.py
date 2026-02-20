#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：set 去重与交集（集合运算）
Author: Lambert

题目：
实现两个函数：
1) unique(items)：返回去重后的集合 set
2) intersection(a, b)：返回两个列表的“交集集合”

示例：
    a=[1,2,2,3], b=[2,3,4] -> {2,3}

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/10_set_unique_and_intersection.py
"""

from __future__ import annotations


def unique(items: list[int]) -> set[int]:
    return set(items)


def intersection(a: list[int], b: list[int]) -> set[int]:
    return set(a) & set(b)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("unique", unique([1, 2, 2, 3]), {1, 2, 3})
    check("intersection", intersection([1, 2, 2, 3], [2, 3, 4]), {2, 3})
    check("intersection empty", intersection([1], [2]), set())


if __name__ == "__main__":
    main()
