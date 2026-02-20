#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：defaultdict 分组。
Author: Lambert

题目：
实现函数 `group_by_first(words)`：
- 按首字母分组，返回 dict

示例：
    ["apple", "ant", "bear"] -> {"a": ["apple", "ant"], "b": ["bear"]}

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/04_defaultdict_grouping.py
"""

from collections import defaultdict


def group_by_first(words: list[str]) -> dict[str, list[str]]:
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        if not word:
            continue
        groups[word[0]].append(word)
    return dict(groups)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    words = ["apple", "ant", "bear"]
    check("group", group_by_first(words), {"a": ["apple", "ant"], "b": ["bear"]})
    check("empty", group_by_first([]), {})


if __name__ == "__main__":
    main()