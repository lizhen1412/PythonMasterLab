#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 注释相关示例索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/01_Comments/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_single_line.py", "单行注释与行尾注释（#）"),
    ("03_inline_and_joining.py", "行尾注释规范、括号隐式换行、反斜杠续行陷阱"),
    ("04_block_comments.py", "块注释（多行 #）与使用场景"),
    ("05_docstrings_basics.py", "文档字符串：模块/类/函数，以及 __doc__/inspect.getdoc"),
    ("06_docstring_vs_string_literal.py", "docstring 与普通三引号字符串表达式的区别"),
    ("07_type_comments.py", "类型注释（# type: ...）与 type: ignore"),
    ("08_encoding_cookie.py", "编码声明注释（coding: ...）与检测"),
    ("09_shebang.py", "shebang（#!）在类 Unix 系统上的作用"),
    ("10_tooling_directives.py", "工具指令注释：noqa/fmt/isort/pylint/pragma 等"),
    ("11_tokenize_extract_comments.py", "用 tokenize 提取源码中的注释"),
    ("12_ast_comments_and_docstrings.py", "AST 中看不到普通注释；docstring/type_comment 例外"),
    ("13_commenting_out_code_pitfalls.py", "用三引号“注释掉代码”的坑与替代方案"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
