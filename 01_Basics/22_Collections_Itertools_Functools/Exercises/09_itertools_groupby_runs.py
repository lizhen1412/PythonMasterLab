#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：groupby 连续分组。

题目：
实现函数 `run_lengths(values)`：
- 返回连续相同元素的 (value, count) 列表

示例：
    ["a","a","b","b","b","a"] -> [("a",2),("b",3),("a",1)]

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/09_itertools_groupby_runs.py
"""

from itertools import groupby


def run_lengths(values: list[str]) -> list[tuple[str, int]]:
    result: list[tuple[str, int]] = []
    for key, group in groupby(values):
        result.append((key, len(list(group))))
    return result


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    values = ["a", "a", "b", "b", "b", "a"]
    expected = [("a", 2), ("b", 3), ("a", 1)]
    check("runs", run_lengths(values), expected)
    check("empty", run_lengths([]), [])


if __name__ == "__main__":
    main()
