#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：list 去重但保持顺序（preserve order）

题目：
实现函数 `dedup_preserve_order(items)`：
- 输入：一个列表 items（元素可哈希：int/str/tuple 等）
- 输出：去重后的新列表，保持“第一次出现”的顺序

示例：
    [3, 1, 3, 2, 1] -> [3, 1, 2]

约定：
- 不要用 `list(set(items))`（会丢失原始顺序）

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/03_list_dedup_preserve_order.py
"""

from __future__ import annotations

from collections.abc import Hashable
from typing import TypeVar

T = TypeVar("T", bound=Hashable)


def dedup_preserve_order(items: list[T]) -> list[T]:
    seen: set[T] = set()
    result: list[T] = []
    for x in items:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("dedup ints", dedup_preserve_order([3, 1, 3, 2, 1]), [3, 1, 2])
    check("dedup strings", dedup_preserve_order(["a", "b", "a", "c", "b"]), ["a", "b", "c"])
    check("dedup empty", dedup_preserve_order([]), [])


if __name__ == "__main__":
    main()

