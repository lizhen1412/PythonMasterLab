#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：严格解析 int（自定义错误信息 + 异常链）
Author: Lambert

题目：
实现函数 `parse_int_strict(text)`：
- 成功：返回 int
- 失败：抛 ValueError，并带更清晰的提示
- 要求：使用 `raise ... from exc` 保留原始异常链

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/03_parse_int_strict.py
"""

from __future__ import annotations


def parse_int_strict(text: object) -> int:
    try:
        return int(text)  # type: ignore[arg-type]
    except (TypeError, ValueError) as exc:
        raise ValueError(f"无法解析为 int: {text!r}") from exc


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
    check("parse_int_strict('42')", parse_int_strict("42"), 42)

    def bad():
        parse_int_strict("x")

    check_raises("parse_int_strict('x')", bad, ValueError)
    try:
        bad()
    except ValueError as exc:
        check("exc.__cause__ is not None", exc.__cause__ is not None, True)


if __name__ == "__main__":
    main()
