#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：修复一次性迭代器被耗尽的 bug。
Author: Lambert

题目：
实现函数 `mean_and_total(nums)`：
- 输入可以是列表或生成器
- 返回 (mean, total)

要求：
- 修复“迭代器被消费一次就没了”的问题

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/21_Iterators_Generators/Exercises/08_exhaustion_fix.py
"""


def mean_and_total(nums) -> tuple[float, int]:
    cached = list(nums)
    total = sum(cached)
    mean = total / len(cached) if cached else 0.0
    return mean, total


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("list", mean_and_total([1, 2, 3]), (2.0, 6))
    gen = (n for n in [1, 2, 3])
    check("gen", mean_and_total(gen), (2.0, 6))
    check("empty", mean_and_total([]), (0.0, 0))


if __name__ == "__main__":
    main()