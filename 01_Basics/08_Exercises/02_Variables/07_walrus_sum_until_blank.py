#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：海象运算符 :=（读取/strip/累加直到空行）
Author: Lambert

题目：
实现 `sum_numbers_until_blank(lines)`，要求：
- 逐行读取字符串
- 用 `:=` 把 `strip()` 结果绑定到变量
- 遇到空行（strip 后为空字符串）就停止
- 返回累加的整数和

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/02_Variables/07_walrus_sum_until_blank.py
"""

from collections.abc import Iterable


def sum_numbers_until_blank(lines: Iterable[str]) -> int:
    total = 0
    for raw in lines:
        if not (s := raw.strip()):
            break
        total += int(s)
    return total


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    total = sum_numbers_until_blank(["10\n", "20\n", "  \n", "999\n"])
    check("sum", total, 30)


if __name__ == "__main__":
    main()
