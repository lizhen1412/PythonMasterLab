#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：enumerate + zip（对齐两列数据）
Author: Lambert

题目：
实现 `format_rows(names, scores)`，要求：
- names: list[str]
- scores: list[int]
- 使用 zip(..., strict=True) 并行遍历
- 使用 enumerate(..., start=1) 为每行加序号
- 返回 list[str]，每行格式：`"{i}. {name}: {score}"`

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/11_Loops/Exercises/06_enumerate_and_zip.py
"""

from __future__ import annotations


def format_rows(names: list[str], scores: list[int]) -> list[str]:
    rows: list[str] = []
    for i, (name, score) in enumerate(zip(names, scores, strict=True), start=1):
        rows.append(f"{i}. {name}: {score}")
    return rows


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    names = ["Alice", "Bob"]
    scores = [98, 7]
    check("rows", format_rows(names, scores), ["1. Alice: 98", "2. Bob: 7"])


if __name__ == "__main__":
    main()
