#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：functools.singledispatch。

你会学到：
1) 按第一个参数类型分发函数实现
2) 用 @func.register(type) 添加分支

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/13_functools_singledispatch.py
"""

from functools import singledispatch


@singledispatch
def describe(value) -> str:
    return f"unknown type: {type(value).__name__}"


@describe.register
def _(value: int) -> str:
    return f"int: {value}"


@describe.register
def _(value: str) -> str:
    return f"str(len={len(value)}): {value!r}"


@describe.register
def _(value: list) -> str:
    return f"list(len={len(value)}): {value}"


def main() -> None:
    print(describe(10))
    print(describe("hello"))
    print(describe([1, 2, 3]))
    print(describe({"a": 1}))


if __name__ == "__main__":
    main()
