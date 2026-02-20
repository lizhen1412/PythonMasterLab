#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：range 生成与切片（切片结果仍是 range）
Author: Lambert

题目：
实现函数 `slice_range(r, start, stop, step)`：
- 输入：一个 range r，以及可选的 start/stop/step（允许为 None）
- 输出：对 r 做切片后的结果（仍为 range）

要求：
- 使用 `slice(start, stop, step)` + `r[slice_obj]` 完成

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/07_range_generate_slices.py
"""

from __future__ import annotations


def slice_range(r: range, start: int | None, stop: int | None, step: int | None) -> range:
    return r[slice(start, stop, step)]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    r = range(2, 20, 2)  # 2,4,6,...,18
    s1 = slice_range(r, 1, 5, None)
    check("slice 1..5", s1, range(4, 12, 2))
    check("type is range", isinstance(s1, range), True)

    r2 = range(10)
    s2 = slice_range(r2, None, None, 3)
    check("range(10)[::3]", s2, range(0, 10, 3))

    s3 = slice_range(r2, None, None, -1)
    check("range(10)[::-1]", s3, range(9, -1, -1))


if __name__ == "__main__":
    main()
