#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：组合枚举。

题目：
实现函数 `choose(items, k)`：
- 使用 itertools.combinations
- 返回所有长度为 k 的组合列表

示例：
    ["A","B","C"], k=2 -> [("A","B"),("A","C"),("B","C")]

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/08_itertools_combinations.py
"""

from itertools import combinations


def choose(items: list[str], k: int) -> list[tuple[str, ...]]:
    return list(combinations(items, k))


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    items = ["A", "B", "C"]
    expected = [("A", "B"), ("A", "C"), ("B", "C")]
    check("choose", choose(items, 2), expected)
    check("k=0", choose(items, 0), [()])


if __name__ == "__main__":
    main()
