#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：成员运算符 in（dict 的 in 检查 key）
Author: Lambert

题目：
实现两个函数：
1) `has_key(mapping, key)`：用 `key in mapping` 判断 key 是否存在
2) `has_value(mapping, value)`：判断 value 是否存在（提示：用 mapping.values()）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/09_Operators/Exercises/09_membership_in_dict.py
"""

from __future__ import annotations


def has_key(mapping: dict[str, int], key: str) -> bool:
    return key in mapping


def has_value(mapping: dict[str, int], value: int) -> bool:
    return value in mapping.values()


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    m = {"a": 1, "b": 2}
    check("key_a", has_key(m, "a"), True)
    check("key_1", has_key(m, "1"), False)
    check("value_1", has_value(m, 1), True)
    check("value_9", has_value(m, 9), False)


if __name__ == "__main__":
    main()
