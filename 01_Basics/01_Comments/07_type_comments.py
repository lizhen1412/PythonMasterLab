#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：类型注释（type comments）：`# type: ...` 与 `# type: ignore`。
Author: Lambert

说明：
- 类型注释主要给静态类型检查器（mypy/pyright/basedpyright 等）使用，运行时不会影响执行结果。
- 在现代 Python 新代码里，更推荐使用“类型注解”（type annotations），而不是 type comments。
- 但你仍会在旧代码/迁移代码中遇到 type comments，因此理解它们很有价值。
- Python 在 `ast.parse(..., type_comments=True)` 时会把 type comments / `# type: ignore` 保留到 AST 里。

场景：
1) 兼容旧代码/旧语法（历史原因）
2) 某些情况下比注解更方便（例如 lambda 无法写参数注解）

本文件的策略：
- 运行的示例代码使用“类型注解”，避免现代类型检查器对 type comments 的告警
- type comments 作为“源码字符串示例”展示，并通过 AST 解析观察其结构
"""

from __future__ import annotations

import ast
from textwrap import dedent

from typing import cast


# 推荐写法：使用“类型注解”（type annotations）
values: list[int] = []


def inc(x: int) -> int:
    return x + 1


def add(a: int, b: int) -> int:
    return a + b


def demonstrate_runtime_view() -> None:
    # 类型注解主要给“类型检查器/IDE”用；Python 运行时不会因此强制类型。
    values.clear()
    values.extend([1, 2, 3])
    values.append(cast(int, "not int"))  # cast 只影响类型检查；运行时不会转换值
    print("values =", values)
    print("inc(10) =", inc(10))
    print("add(1, 2) =", add(1, 2))
    print("add.__annotations__ =", add.__annotations__)


def demonstrate_ast_type_comments() -> None:
    code = dedent(
        """
        values = []  # type: list[int]
        inc = lambda x: x + 1  # type: Callable[[int], int]
        values.append("not int")  # type: ignore

        def add(a, b):  # type: (int, int) -> int
            return a + b
        """
    )

    tree = ast.parse(code, mode="exec", type_comments=True)
    assigns = [n for n in tree.body if isinstance(n, ast.Assign)]
    functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)]

    print("\nAST 里的 type comments：")
    for a in assigns:
        print("- Assign.type_comment =", a.type_comment)
    for f in functions:
        print("- FunctionDef.type_comment =", f.type_comment)

    print("\nAST 里的 type ignores（# type: ignore...）：")
    for ti in tree.type_ignores:
        print(f"- TypeIgnore(lineno={ti.lineno}, tag={ti.tag!r})")


def main() -> None:
    demonstrate_runtime_view()
    demonstrate_ast_type_comments()


if __name__ == "__main__":
    main()