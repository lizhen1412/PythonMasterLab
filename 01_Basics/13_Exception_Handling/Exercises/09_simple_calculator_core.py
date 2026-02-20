#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：实现计算器核心函数（不使用 eval）
Author: Lambert

题目：
实现函数 `calculate_expr(expr)`：
- 支持：+ - * / // % **
- 支持输入：'2+3'、'2 + 3'、'10//3'、'2 ** 8'
- 非法输入：抛 ValueError（提示格式/运算符不支持）

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/09_simple_calculator_core.py
"""

from __future__ import annotations

import operator
import re
from collections.abc import Callable


OPS: dict[str, Callable[[float, float], float]] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow,
}

_NUMBER_RE = r"[+-]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)"
_OP_RE = "|".join(re.escape(op) for op in sorted(OPS, key=len, reverse=True))
_EXPR_RE = re.compile(rf"^\\s*(?P<a>{_NUMBER_RE})\\s*(?P<op>{_OP_RE})\\s*(?P<b>{_NUMBER_RE})\\s*$")


def _parse_number(text: str) -> float:
    if re.fullmatch(r"[+-]?\\d+", text.strip()):
        return float(int(text))
    return float(text)


def calculate_expr(expr: str) -> float:
    expr = expr.strip()
    if not expr:
        raise ValueError("empty expression")

    parts = expr.split()
    if len(parts) == 3:
        a_text, op, b_text = parts
    else:
        m = _EXPR_RE.match(expr)
        if not m:
            raise ValueError("bad format, example: '2+3' or '2 + 3'")
        a_text, op, b_text = m.group("a"), m.group("op"), m.group("b")

    if op not in OPS:
        raise ValueError(f"unsupported operator: {op!r}")
    a = _parse_number(a_text)
    b = _parse_number(b_text)
    return OPS[op](a, b)


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
    check("2+3", calculate_expr("2+3"), 5.0)
    check("10 // 3", calculate_expr("10 // 3"), 3.0)
    check("2 ** 8", calculate_expr("2 ** 8"), 256.0)
    check_raises("bad input", lambda: calculate_expr("hello"), ValueError)
    check_raises("empty", lambda: calculate_expr(""), ValueError)


if __name__ == "__main__":
    main()
