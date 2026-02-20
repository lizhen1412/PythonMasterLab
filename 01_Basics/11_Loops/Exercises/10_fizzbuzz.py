#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：FizzBuzz（for + 条件分支）
Author: Lambert

题目：
实现 `fizzbuzz(n)`，返回 1..n 的字符串列表：
- 3 的倍数 -> "Fizz"
- 5 的倍数 -> "Buzz"
- 15 的倍数 -> "FizzBuzz"
- 其他 -> 数字本身（转为字符串）

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/11_Loops/Exercises/10_fizzbuzz.py
"""

from __future__ import annotations


def fizzbuzz(n: int) -> list[str]:
    if n < 0:
        raise ValueError("n must be >= 0")
    out: list[str] = []
    for x in range(1, n + 1):
        if x % 15 == 0:
            out.append("FizzBuzz")
        elif x % 3 == 0:
            out.append("Fizz")
        elif x % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(x))
    return out


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    out = fizzbuzz(15)
    check("len", len(out), 15)
    check("3", out[2], "Fizz")
    check("5", out[4], "Buzz")
    check("15", out[14], "FizzBuzz")


if __name__ == "__main__":
    main()
