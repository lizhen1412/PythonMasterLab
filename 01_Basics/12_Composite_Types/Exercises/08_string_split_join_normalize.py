#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：字符串 split/join + 规范化空白
Author: Lambert

题目：
实现函数 `normalize_whitespace(text)`：
- 把任意数量的空格/Tab/换行等空白，规范化为“单个空格”
- 并去掉首尾空白

提示：
- `text.split()`（不传分隔符）会按“任意空白”拆分，并自动去掉多余空白
- `" ".join(parts)` 用单个空格拼回去

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/08_string_split_join_normalize.py
"""

from __future__ import annotations


def normalize_whitespace(text: str) -> str:
    parts = text.split()
    return " ".join(parts)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("normalize empty", normalize_whitespace(""), "")
    check("normalize spaces", normalize_whitespace("  hello   world  "), "hello world")
    check("normalize mixed", normalize_whitespace("a\\n\\t  b   c\\n"), "a b c")


if __name__ == "__main__":
    main()
