#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：函数定义/调用/返回值，docstring 与类型注解。

- 定义：`def name(params) -> return_type: ...`
- 调用：位置/关键字实参；未显式 return 默认 `None`
- 文档字符串：`func.__doc__`；配合 `help`
- 类型注解：帮助阅读/工具检查，不会强制运行时类型
"""

from __future__ import annotations

from typing import Any


def add(a: int, b: int) -> int:
    """返回两个整数之和。"""
    return a + b


def greet(name: str, prefix: str = "Hi") -> str:
    """格式化问候语，默认前缀是 Hi。"""
    return f"{prefix}, {name}!"


def print_and_return_none(message: str) -> None:
    """显式返回 None，与“无 return 语句”等价。"""
    print(f"[LOG] {message}")
    return None


def no_return_statement(x: int, y: int) -> int:
    """
    没有写 return 时，Python 会在函数末尾隐式返回 None。
    这里的返回类型注解只是“期望”，运行时不会强制执行。
    """
    _ = x + y
    # 没有 return 语句，实际返回 None


def demonstrate_call_styles() -> None:
    """对比位置实参、关键字实参混用的调用方式。"""
    print("add(1, 2) ->", add(1, 2))
    print("add(a=3, b=5) ->", add(a=3, b=5))
    print("add(b=10, a=1) ->", add(b=10, a=1))
    print("greet('Alice') ->", greet("Alice"))
    print("greet(name='Bob', prefix='Hello') ->", greet(name="Bob", prefix="Hello"))


def inspect_doc_and_annotations() -> None:
    """读取 docstring 与注解，说明它们是“元数据”，不会强制类型。"""
    print("add.__doc__ ->", add.__doc__)
    print("greet.__annotations__ ->", greet.__annotations__)
    print("help(greet) ->")
    help(greet)


def main() -> None:
    print("== 定义与调用 ==")
    demonstrate_call_styles()

    print("\n== 返回值与 None ==")
    result: Any = print_and_return_none("side effect then None")
    print("print_and_return_none(...) ->", result)
    print("no_return_statement(1, 2) ->", no_return_statement(1, 2))

    print("\n== docstring 与注解 ==")
    inspect_doc_and_annotations()


if __name__ == "__main__":
    main()
