#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：九九乘法表（生成字符串表格）

题目：
实现 `multiplication_table(n=9)`，要求：
- 生成“下三角”九九乘法表（第 i 行有 i 个式子）
- 使用嵌套 for 循环
- 返回一个字符串（包含换行），不要直接 print（便于测试/复用）

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/11_Loops/Exercises/08_multiplication_table_9x9.py
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


def check(label: str, ok: bool) -> None:
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")


def main() -> None:
    table = multiplication_table(9)
    lines = table.splitlines()
    check("line_count", len(lines) == 9)
    check("first_cell", lines[0].split("\t")[0].strip() == "1*1=1")
    check("last_cell", lines[-1].split("\t")[-1].strip() == "9*9=81")


if __name__ == "__main__":
    main()

