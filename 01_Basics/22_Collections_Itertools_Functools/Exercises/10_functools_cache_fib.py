#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：lru_cache 斐波那契。

题目：
实现带缓存的 `fib(n)`：
- 使用 functools.lru_cache
- fib(0)=0, fib(1)=1

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/10_functools_cache_fib.py
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("fib(0)", fib(0), 0)
    check("fib(1)", fib(1), 1)
    check("fib(10)", fib(10), 55)


if __name__ == "__main__":
    main()
