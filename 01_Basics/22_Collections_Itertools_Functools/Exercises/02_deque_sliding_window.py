#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：deque 实现滑动窗口。
Author: Lambert

题目：
实现函数 `window_sums(nums, size)`：
- 返回长度为 size 的滑动窗口之和列表
- size <= 0 或 nums 为空时返回 []

示例：
    nums=[1,2,3,4], size=2 -> [3,5,7]

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/02_deque_sliding_window.py
"""

from collections import deque


def window_sums(nums: list[int], size: int) -> list[int]:
    if size <= 0 or not nums:
        return []
    if size > len(nums):
        return []

    window = deque(maxlen=size)
    result: list[int] = []
    total = 0

    for n in nums:
        if len(window) == size:
            total -= window[0]
        window.append(n)
        total += n
        if len(window) == size:
            result.append(total)

    return result


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("size=2", window_sums([1, 2, 3, 4], 2), [3, 5, 7])
    check("size=3", window_sums([1, 2, 3, 4], 3), [6, 9])
    check("empty", window_sums([], 2), [])
    check("size>len", window_sums([1, 2], 3), [])


if __name__ == "__main__":
    main()