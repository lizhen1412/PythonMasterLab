#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：生成器 - 偶数平方。

题目：
实现生成器函数 `even_squares(nums)`：
- 输入：整数序列
- 输出：只产出偶数的平方（惰性）

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/21_Iterators_Generators/Exercises/05_generator_even_squares.py
"""


def even_squares(nums):
    for n in nums:
        if n % 2 == 0:
            yield n * n


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    result = list(even_squares([1, 2, 3, 4]))
    check("even_squares", result, [4, 16])
    check("empty", list(even_squares([])), [])


if __name__ == "__main__":
    main()
