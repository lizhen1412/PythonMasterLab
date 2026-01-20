#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：用 raise 做参数校验（validate age）

题目：
实现函数 `validate_age(age)`：
- age 必须是 int
- age 必须在 0..150 之间（含边界）
- 合法返回 age；非法抛异常：
  - 类型不对 -> TypeError
  - 范围不对 -> ValueError

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/04_validate_age_raise.py
"""

from __future__ import annotations


def validate_age(age: object) -> int:
    if not isinstance(age, int):
        raise TypeError("age must be int")
    if not 0 <= age <= 150:
        raise ValueError("age must be between 0 and 150")
    return age


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def check_raises(label: str, fn, exc_type: type[BaseException]) -> None:
    try:
        fn()
    except exc_type:
        print(f"[OK] {label}: raised {exc_type.__name__}")
    except Exception as exc:
        print(f"[FAIL] {label}: raised {type(exc).__name__}, expected {exc_type.__name__}")
    else:
        print(f"[FAIL] {label}: no exception, expected {exc_type.__name__}")


def main() -> None:
    check("validate_age(0)", validate_age(0), 0)
    check("validate_age(150)", validate_age(150), 150)
    check_raises("validate_age(-1)", lambda: validate_age(-1), ValueError)
    check_raises("validate_age(999)", lambda: validate_age(999), ValueError)
    check_raises("validate_age('18')", lambda: validate_age("18"), TypeError)


if __name__ == "__main__":
    main()

