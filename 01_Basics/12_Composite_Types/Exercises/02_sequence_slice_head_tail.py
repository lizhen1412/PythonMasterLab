#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：序列（Sequence）切片与 head/tail（first/middle/last）

题目：
实现 3 个函数（支持 list/tuple/str/range 等“可切片序列”）：
1) head(seq, n)：返回前 n 个元素（n>=0）
2) tail(seq, n)：返回后 n 个元素（n>=0）
3) first_middle_last(seq)：返回 (first, middle, last)

约定：
- n < 0：抛 ValueError
- first_middle_last：len(seq) < 2 视为非法：抛 ValueError

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/02_sequence_slice_head_tail.py
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def head(seq: Sequence[T], n: int) -> Sequence[T]:
    if n < 0:
        raise ValueError("n must be >= 0")
    return seq[:n]


def tail(seq: Sequence[T], n: int) -> Sequence[T]:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return seq[:0]
    return seq[-n:]


def first_middle_last(seq: Sequence[T]) -> tuple[T, Sequence[T], T]:
    if len(seq) < 2:
        raise ValueError("seq length must be >= 2")
    return seq[0], seq[1:-1], seq[-1]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("head([1,2,3,4], 2)", head([1, 2, 3, 4], 2), [1, 2])
    check("tail([1,2,3,4], 2)", tail([1, 2, 3, 4], 2), [3, 4])
    check(
        "first_middle_last([1,2,3,4])",
        first_middle_last([1, 2, 3, 4]),
        (1, [2, 3], 4),
    )

    check("head((1,2,3), 10)", head((1, 2, 3), 10), (1, 2, 3))
    check("tail((1,2,3), 0)", tail((1, 2, 3), 0), ())
    check("first_middle_last('abcd')", first_middle_last("abcd"), ("a", "bc", "d"))

    r = range(5)
    check("head(range(5), 2)", head(r, 2), range(2))
    check("tail(range(5), 2)", tail(r, 2), range(3, 5))
    check("first_middle_last(range(5))", first_middle_last(r), (0, range(1, 4), 4))


if __name__ == "__main__":
    main()

