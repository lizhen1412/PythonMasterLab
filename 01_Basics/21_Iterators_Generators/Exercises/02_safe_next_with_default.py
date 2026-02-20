#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：实现安全的 next_or。
Author: Lambert

题目：
实现函数 `next_or(it, default=None)`：
- 如果迭代器还有元素，返回 next(it)
- 如果耗尽，返回 default

示例：
    it = iter([1])
    next_or(it) -> 1
    next_or(it, 99) -> 99

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/21_Iterators_Generators/Exercises/02_safe_next_with_default.py
"""


def next_or(it, default=None):
    try:
        return next(it)
    except StopIteration:
        return default


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    it = iter([1])
    check("next_or first", next_or(it), 1)
    check("next_or default", next_or(it, 99), 99)
    check("next_or None", next_or(it), None)


if __name__ == "__main__":
    main()