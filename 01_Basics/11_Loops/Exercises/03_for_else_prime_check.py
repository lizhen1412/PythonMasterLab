#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：for-else（素数判断）
Author: Lambert

题目：
实现 `is_prime(n)`，要求：
- n < 2 -> False
- 对 2..sqrt(n) 之间的整数做试除
- 必须使用 for-else：
  - 发现因子 -> break -> 不是素数
  - 没有 break -> else -> 是素数

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/11_Loops/Exercises/03_for_else_prime_check.py
"""

from __future__ import annotations


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            break
    else:
        return True
    return False


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    samples: list[tuple[int, bool]] = [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (9, False),
        (13, True),
        (25, False),
    ]
    for n, expected in samples:
        check(f"is_prime({n})", is_prime(n), expected)


if __name__ == "__main__":
    main()
