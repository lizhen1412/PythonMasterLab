#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：match（序列模式：pair / head-tail）

题目：
实现 `describe_sequence(obj)`，规则：
- 如果 obj 是“长度为 2 的序列”（例如 list/tuple）-> "pair"
- 如果 obj 是“长度 >= 1 的序列” -> "head-tail"
- 其他 -> "other"

要求：
- 使用 match/case 的序列模式：
  - `case [x, y]: ...`
  - `case [head, *tail]: ...`

提示：
- 序列模式不会匹配 str/bytes/bytearray（避免把字符串当成字符序列匹配）。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/10_Conditionals/Exercises/08_match_sequence_unpack.py
"""

from __future__ import annotations


def describe_sequence(obj: object) -> str:
    match obj:
        case [_, _]:
            return "pair"
        case [_, *_]:
            return "head-tail"
        case _:
            return "other"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("list_pair", describe_sequence([1, 2]), "pair")
    check("tuple_pair", describe_sequence((1, 2)), "pair")
    check("list_many", describe_sequence([1, 2, 3]), "head-tail")
    check("list_one", describe_sequence([1]), "head-tail")
    check("empty_list", describe_sequence([]), "other")
    check("string_not_sequence_pattern", describe_sequence("ab"), "other")


if __name__ == "__main__":
    main()

