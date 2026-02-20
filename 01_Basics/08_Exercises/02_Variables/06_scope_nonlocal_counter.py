#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：nonlocal（闭包计数器）
Author: Lambert

题目：
实现 `make_counter(start=0)`，要求：
- 返回一个函数 `inc(step=1) -> int`
- 每次调用 `inc` 都会把内部计数加 step 并返回新值
- 必须用 `nonlocal` 修改外层变量

参考答案：
- 本文件实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/02_Variables/06_scope_nonlocal_counter.py
"""


def make_counter(start: int = 0):
    count = start

    def inc(step: int = 1) -> int:
        nonlocal count
        count += step
        return count

    return inc


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    counter = make_counter(100)
    check("counter()", counter(), 101)
    check("counter(10)", counter(10), 111)
    check("counter()", counter(), 112)


if __name__ == "__main__":
    main()
