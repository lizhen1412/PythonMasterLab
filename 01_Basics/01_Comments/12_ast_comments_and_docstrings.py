#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：AST 中看不到普通注释；docstring/type_comment 是例外。
Author: Lambert

说明：
1) 普通 `# ...` 注释不会进入 AST。
2) docstring（第一条字符串语句）可以通过 `ast.get_docstring()` 读取。
3) type comments（`# type: ...`）在 `ast.parse(..., type_comments=True)` 时会被保留。
"""

from __future__ import annotations

import ast
from textwrap import dedent


CODE = dedent(
    '''
    """这是模块 docstring。"""

    # 这是普通注释：AST 里看不到
    x = 1  # type: int

    def add(a, b):  # type: (int, int) -> int
        """这是函数 docstring。"""
        # 这里也有普通注释：AST 里看不到
        return a + b
    '''
)


def main() -> None:
    tree_no_type = ast.parse(CODE, mode="exec")
    tree_with_type = ast.parse(CODE, mode="exec", type_comments=True)

    print("模块 docstring =", ast.get_docstring(tree_no_type))

    # 找到 x = 1 这条 Assign
    assign_no_type = next(n for n in tree_no_type.body if isinstance(n, ast.Assign))
    assign_with_type = next(n for n in tree_with_type.body if isinstance(n, ast.Assign))

    print("Assign 在未开启 type_comments 时的 type_comment =", getattr(assign_no_type, "type_comment", None))
    print("Assign 在开启 type_comments 时的 type_comment   =", assign_with_type.type_comment)

    func = next(n for n in tree_with_type.body if isinstance(n, ast.FunctionDef))
    print("函数 docstring =", ast.get_docstring(func))
    print("FunctionDef.type_comment =", func.type_comment)

    print("\n备注：你会发现 AST 里没有任何一个节点对应普通 `# ...` 注释。")


if __name__ == "__main__":
    main()