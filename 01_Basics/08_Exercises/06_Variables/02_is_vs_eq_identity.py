#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：is vs ==（身份与值）

题目：
实现 `compare(a, b)`，返回一个 dict，包含：
- `same_object`: a is b
- `same_value`: a == b

要求：
- 用 list 举例，避免小整数缓存导致的“偶然相同”。

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/06_Variables/02_is_vs_eq_identity.py
"""


def compare(a: object, b: object) -> dict[str, bool]:
    return {"same_object": a is b, "same_value": a == b}


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    a = [1, 2]
    b = [1, 2]
    c = a
    check("a_vs_b", compare(a, b), {"same_object": False, "same_value": True})
    check("a_vs_c", compare(a, c), {"same_object": True, "same_value": True})


if __name__ == "__main__":
    main()

