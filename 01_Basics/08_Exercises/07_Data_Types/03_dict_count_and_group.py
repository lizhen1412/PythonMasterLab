#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：dict 计数与分组

题目：
1) 实现 `count_words(words)`：把字符串列表计数成 dict[str, int]
2) 实现 `group_by_first_letter(words)`：按首字母分组到 dict[str, list[str]]
   - 组内保持原顺序即可（不要求排序）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/07_Data_Types/03_dict_count_and_group.py
"""

from collections import Counter


def count_words(words: list[str]) -> dict[str, int]:
    return dict(Counter(words))


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for w in words:
        key = w[:1]
        groups.setdefault(key, []).append(w)
    return groups


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    words = ["apple", "ape", "banana", "book", "apple"]
    check("count", count_words(words), {"apple": 2, "ape": 1, "banana": 1, "book": 1})
    check("group", group_by_first_letter(words), {"a": ["apple", "ape", "apple"], "b": ["banana", "book"]})


if __name__ == "__main__":
    main()

