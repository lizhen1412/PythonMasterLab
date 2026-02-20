#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：文档字符串（docstring）基础示例：模块/类/函数。
Author: Lambert

docstring 是“字符串字面量”，但有一个特殊规则：
- 如果它作为模块、类、函数体中的第一条语句出现，它会成为该对象的文档字符串，
  可通过 `__doc__`、`help()`、`inspect.getdoc()` 等读取。

对比：
- 普通注释（# ...）不会进入运行时对象模型。
- docstring 会进入运行时（除非用 `python -OO` 运行，会移除 docstring）。
"""

from __future__ import annotations

import inspect


class Greeter:
    """一个非常简单的示例类：用于演示类 docstring。"""

    def __init__(self, name: str) -> None:
        """创建一个问候者。"""

        self.name = name

    def greet(self) -> str:
        """返回一条问候语。"""

        return f"Hello, {self.name}!"


def add(a: int, b: int) -> int:
    """返回 a + b。"""

    return a + b


def main() -> None:
    print("模块 __doc__：")
    print(inspect.getdoc(__import__(__name__)))
    print()

    print("类 Greeter.__doc__：")
    print(inspect.getdoc(Greeter))
    print()

    print("方法 Greeter.greet.__doc__：")
    print(inspect.getdoc(Greeter.greet))
    print()

    print("函数 add.__doc__：")
    print(inspect.getdoc(add))
    print()

    print(add(1, 2))
    print(Greeter("Python").greet())


if __name__ == "__main__":
    main()