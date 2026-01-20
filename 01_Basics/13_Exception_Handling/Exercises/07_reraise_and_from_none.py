#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：re-raise 与 from None 的对比（__cause__/__context__）

题目：
实现 2 个函数：
1) parse_int_from_none(text)：解析 int；失败时 raise ValueError(...) from None
2) run_and_reraise(fn)：运行 fn；捕获 Exception 后做点事情，然后用 `raise` 重新抛出

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/07_reraise_and_from_none.py
"""

from __future__ import annotations


def parse_int_from_none(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        raise ValueError(f"invalid int: {text!r}") from None


def run_and_reraise(fn) -> None:
    try:
        fn()
    except Exception:
        # 这里可以写：记录日志/清理状态/统计计数等
        raise


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    try:
        parse_int_from_none("x")
    except ValueError as exc:
        check("from None: __cause__ is None", exc.__cause__ is None, True)
        check("from None: __suppress_context__", exc.__suppress_context__, True)

    def fail():
        int("x")

    try:
        run_and_reraise(fail)
    except ValueError as exc:
        check("re-raised type", type(exc).__name__, "ValueError")


if __name__ == "__main__":
    main()

