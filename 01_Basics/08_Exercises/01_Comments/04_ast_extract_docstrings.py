#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：用 AST 提取 docstring

题目：
1) 实现 `extract_module_docstring(source: str) -> str | None`
2) 实现 `extract_function_docstring(source: str, func_name: str) -> str | None`

要求与提示：
- docstring 是“模块/函数体中的第一个字符串语句”；
- 普通 `# ...` 注释不会进入 AST。

参考答案：
- 本文件中上述函数的实现即为参考答案；`main()` 里带自测输出（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/01_Comments/04_ast_extract_docstrings.py
"""

import ast


def extract_module_docstring(source: str) -> str | None:
    module = ast.parse(source)
    return ast.get_docstring(module)


def extract_function_docstring(source: str, func_name: str) -> str | None:
    module = ast.parse(source)
    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return ast.get_docstring(node)
    return None


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    source = '''# comment
"""module doc"""

"not a docstring"

def greet() -> str:
    """function doc"""
    return "hi"
'''
    check("module_doc", extract_module_docstring(source), "module doc")
    check("func_doc", extract_function_docstring(source, "greet"), "function doc")
    check("missing_func", extract_function_docstring(source, "missing"), None)


if __name__ == "__main__":
    main()

