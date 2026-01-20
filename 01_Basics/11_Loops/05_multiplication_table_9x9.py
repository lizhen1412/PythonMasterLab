#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：九九乘法表（Nested loops）

你会学到：
1) 嵌套 for：外层控制行，内层控制列
2) 用字符串拼接/对齐输出，让表格更整齐

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/05_multiplication_table_9x9.py
"""

from __future__ import annotations


def multiplication_table(n: int = 9) -> str:
    lines: list[str] = []
    for i in range(1, n + 1):
        parts: list[str] = []
        for j in range(1, i + 1):
            parts.append(f"{j}*{i}={i*j:<2}")
        lines.append("\t".join(parts))
    return "\n".join(lines)


def main() -> None:
    print(multiplication_table(9))


if __name__ == "__main__":
    main()

