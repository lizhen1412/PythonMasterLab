#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：yield from 扁平化嵌套列表。

题目：
实现生成器函数 `flatten(rows)`：
- 输入：二维列表（list[list[int]]）
- 输出：按行扁平化的惰性序列

示例：
    [[1,2],[3],[4,5]] -> 1,2,3,4,5

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/21_Iterators_Generators/Exercises/06_yield_from_flatten.py
"""


def flatten(rows):
    for row in rows:
        yield from row


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    rows = [[1, 2], [3], [4, 5]]
    check("flatten", list(flatten(rows)), [1, 2, 3, 4, 5])
    check("empty", list(flatten([])), [])


if __name__ == "__main__":
    main()
