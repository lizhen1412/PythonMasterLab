#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：islice 实现分块。
Author: Lambert

题目：
实现函数 `chunked(items, size)`：
- 返回按 size 切分的二维列表
- 最后一块可能不足 size

示例：
    [1,2,3,4,5], size=2 -> [[1,2],[3,4],[5]]

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/07_itertools_chunked.py
"""

from itertools import islice


def chunked(items: list[int], size: int) -> list[list[int]]:
    if size <= 0:
        return []
    result: list[list[int]] = []
    it = iter(items)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        result.append(chunk)
    return result


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("size=2", chunked([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
    check("size=3", chunked([1, 2, 3, 4], 3), [[1, 2, 3], [4]])
    check("size<=0", chunked([1, 2], 0), [])


if __name__ == "__main__":
    main()