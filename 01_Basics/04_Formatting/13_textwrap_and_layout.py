#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：文本排版（让输出更“像样”）。

你会学到：
1) `textwrap.fill`：自动换行（控制宽度）
2) `textwrap.indent`：给每行加缩进（做层级结构很常用）
3) 简单列布局：用格式化规格对齐列

运行：
    python3 01_Basics/04_Formatting/13_textwrap_and_layout.py
"""

import textwrap


def main() -> None:
    paragraph = (
        "Python output formatting is not only about f-strings; "
        "sometimes you need wrapping, indentation, and aligned columns."
    )

    print("1) fill：控制行宽：")
    print(textwrap.fill(paragraph, width=50))

    print("\n2) indent：给每行加前缀：")
    wrapped = textwrap.fill(paragraph, width=40)
    print(textwrap.indent(wrapped, prefix="  > "))

    print("\n3) 简单列布局（对齐输出）：")
    rows = [
        ("Alice", 98.5),
        ("Bob", 7.0),
        ("Charlie", 100.0),
    ]
    print(f"{'name':<10} | {'score':>6}")
    print("-" * 20)
    for name, score in rows:
        print(f"{name:<10} | {score:>6.1f}")


if __name__ == "__main__":
    main()

