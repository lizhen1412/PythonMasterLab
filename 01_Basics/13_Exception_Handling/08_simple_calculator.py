#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：简单计算器（不使用 eval）
Author: Lambert

支持运算符：
    +  -  *  /  //  %  **

支持输入格式：
1) 带空格： 2 + 3
2) 不带空格：2+3、10//3、2**8

你会学到：
1) 解析输入（字符串 -> 数字/运算符）
2) try/except：给出友好的错误提示
3) raise：对非法输入主动报错
4) 可选 REPL：传入 --repl 进入交互模式

运行（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/08_simple_calculator.py
    python3 01_Basics/13_Exception_Handling/08_simple_calculator.py --repl
"""

from __future__ import annotations

import logging
import operator
import re
import sys
from collections.abc import Callable


logger = logging.getLogger("calculator")


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


def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")


def parse_number(text: str) -> float:
    text = text.strip()
    if re.fullmatch(r"[+-]?\\d+", text):
        return float(int(text))
    return float(text)


def parse_expression(expr: str) -> tuple[float, str, float]:
    expr = expr.strip()
    if not expr:
        raise ValueError("空表达式：请输入如 '2+3' 或 '2 + 3'")

    parts = expr.split()
    if len(parts) == 3:
        a_text, op, b_text = parts
        if op not in OPS:
            raise ValueError(f"不支持的运算符: {op!r}")
        return parse_number(a_text), op, parse_number(b_text)

    m = _EXPR_RE.match(expr)
    if not m:
        raise ValueError("表达式格式错误：示例 '2+3'、'10//3'、'2 ** 8'")
    a = parse_number(m.group("a"))
    op = m.group("op")
    b = parse_number(m.group("b"))
    return a, op, b


def calculate(expr: str) -> float:
    a, op, b = parse_expression(expr)
    logger.debug("parsed: a=%s op=%s b=%s", a, op, b)
    func = OPS[op]
    return func(a, b)


def run_examples() -> None:
    examples = [
        "2+3",
        "10 // 3",
        "2 ** 8",
        "1/0",
        "hello",
    ]
    for s in examples:
        try:
            result = calculate(s)
        except Exception as exc:
            print(f"[ERROR] {s!r} -> {type(exc).__name__}: {exc}")
        else:
            print(f"[OK] {s!r} = {result}")


def repl() -> None:
    print("简单计算器（输入 exit/quit 退出）")
    while True:
        try:
            line = input("calc> ").strip()
        except EOFError:
            break
        if line in {"exit", "quit"}:
            break
        try:
            print(calculate(line))
        except Exception as exc:
            print(f"{type(exc).__name__}: {exc}")


def main(argv: list[str] | None = None) -> None:
    configure_logging()
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--repl" in argv:
        repl()
        return
    run_examples()


if __name__ == "__main__":
    main()
