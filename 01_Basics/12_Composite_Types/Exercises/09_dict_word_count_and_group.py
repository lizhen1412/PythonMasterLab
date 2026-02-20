#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：dict 计数与分组（get / setdefault）
Author: Lambert

题目：
实现两个函数：
1) word_count(words)：统计每个单词出现次数，返回 dict[str,int]
2) group_by_first_letter(words)：按首字母分组，返回 dict[str, list[str]]

要求：
- word_count 使用 `get(key, default)` 或 `setdefault` 完成
- group_by_first_letter 使用 `setdefault` 完成

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/09_dict_word_count_and_group.py
"""

from __future__ import annotations


def word_count(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


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
    check("word_count", word_count(words), {"apple": 2, "ape": 1, "banana": 1, "book": 1})
    check(
        "group_by_first_letter",
        group_by_first_letter(words),
        {"a": ["apple", "ape", "apple"], "b": ["banana", "book"]},
    )


if __name__ == "__main__":
    main()
