#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：type/isinstance（bool 是 int 子类）

题目：
实现 `classify(value)`，要求：
- 返回 "bool" / "int" / "float" / "str" / "other"
- 必须先判断 bool，再判断 int（因为 `isinstance(True, int)` 为 True）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/06_Variables/04_type_checks_and_bool_is_int.py
"""


def classify(value: object) -> str:
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str"
    return "other"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("True", classify(True), "bool")
    check("1", classify(1), "int")
    check("1.0", classify(1.0), "float")
    check("s", classify("s"), "str")
    check("list", classify([]), "other")


if __name__ == "__main__":
    main()

