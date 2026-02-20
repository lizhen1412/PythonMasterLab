#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：用 tokenize 从源码中提取注释。
Author: Lambert

对比：
- 运行时对象/AST 通常“看不到”普通注释。
- 但 token 流里能识别出 COMMENT token，因此工具（格式化、lint、静态分析）能读取注释。
"""

from __future__ import annotations

import io
import tokenize


SOURCE = """\
# 模块注释：tokenize 能读到它
x = 1  # 行尾注释也能读到
y = "# 字符串里的 # 不是注释"

def f():
    # 函数里的注释
    return x
"""


def extract_comments(source: str) -> list[str]:
    comments: list[str] = []
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)
    for tok in tokens:
        if tok.type == tokenize.COMMENT:
            comments.append(tok.string)
    return comments


def main() -> None:
    comments = extract_comments(SOURCE)
    print("提取到的注释：")
    for c in comments:
        print("-", c)


if __name__ == "__main__":
    main()