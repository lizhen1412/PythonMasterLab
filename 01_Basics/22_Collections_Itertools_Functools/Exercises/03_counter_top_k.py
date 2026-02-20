#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：Counter 统计 top-k。
Author: Lambert

题目：
实现函数 `top_k_words(words, k)`：
- 返回出现次数最高的 k 个词（按频率降序）

示例：
    ["a","b","a","c","b","a"], k=2 -> ["a", "b"]

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/03_counter_top_k.py
"""

from collections import Counter


def top_k_words(words: list[str], k: int) -> list[str]:
    if k <= 0:
        return []
    counter = Counter(words)
    return [word for word, _ in counter.most_common(k)]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    words = ["a", "b", "a", "c", "b", "a"]
    check("top2", top_k_words(words, 2), ["a", "b"])
    check("k=0", top_k_words(words, 0), [])


if __name__ == "__main__":
    main()