#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：算术小计算器（+ - * / // % ** divmod）

题目：
实现 `calc(a, b)`，返回一个 dict，包含：
- add/sub/mul/truediv/floordiv/mod/pow/divmod

要求：
- b == 0 时，/、//、%、divmod 这些操作会抛 ZeroDivisionError；
  这里约定：把对应结果设为 None（不要让程序崩溃）。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/09_Operators/Exercises/02_arithmetic_calculator.py
"""

from __future__ import annotations


def calc(a: int, b: int) -> dict[str, object]:
    out: dict[str, object] = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "pow": a**b,
    }

    try:
        out["truediv"] = a / b
        out["floordiv"] = a // b
        out["mod"] = a % b
        out["divmod"] = divmod(a, b)
    except ZeroDivisionError:
        out["truediv"] = None
        out["floordiv"] = None
        out["mod"] = None
        out["divmod"] = None

    return out


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    r = calc(7, 3)
    check("add", r["add"], 10)
    check("sub", r["sub"], 4)
    check("mul", r["mul"], 21)
    check("truediv", r["truediv"], 7 / 3)
    check("floordiv", r["floordiv"], 2)
    check("mod", r["mod"], 1)
    check("pow", r["pow"], 343)
    check("divmod", r["divmod"], (2, 1))

    r2 = calc(7, 0)
    check("zero_div_truediv", r2["truediv"], None)
    check("zero_div_floordiv", r2["floordiv"], None)
    check("zero_div_mod", r2["mod"], None)
    check("zero_div_divmod", r2["divmod"], None)


if __name__ == "__main__":
    main()

