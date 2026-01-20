#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11：singledispatch 格式化。

题目：
实现函数 `format_value(x)`：
- 默认返回 str(x)
- int -> "int(<value>)"
- list -> "list[len]=[...]"

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/11_functools_singledispatch_format.py
"""

from functools import singledispatch


@singledispatch
def format_value(x) -> str:
    return str(x)


@format_value.register
def _(x: int) -> str:
    return f"int({x})"


@format_value.register
def _(x: list) -> str:
    return f"list[{len(x)}]={x}"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("int", format_value(3), "int(3)")
    check("list", format_value([1, 2]), "list[2]=[1, 2]")
    check("str", format_value("hi"), "hi")


if __name__ == "__main__":
    main()
