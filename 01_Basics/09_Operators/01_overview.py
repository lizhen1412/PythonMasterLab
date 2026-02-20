#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 运算符（Operators）相关示例索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/09_Operators/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_arithmetic_operators.py", "算术运算符：+ - * / // % ** @ 与 divmod"),
    ("03_assignment_operators.py", "赋值运算符：=、解包、增强赋值（含 @=）、以及 :="),
    ("04_comparison_operators.py", "比较运算符：== != < <= > >=、链式比较、浮点比较"),
    ("05_logical_operators.py", "逻辑运算符：and/or/not、短路、返回值与常见坑"),
    ("06_bitwise_operators.py", "位运算符：& | ^ ~ << >> 与位标志（flags）"),
    ("07_membership_operators.py", "成员运算符：in / not in（补充：is / is not）"),
    ("08_operator_precedence.py", "运算符优先级：用例子解释为什么要加括号"),
    ("09_chapter_summary.py", "本章总结：关键规则 + 常见误区清单"),
    ("Exercises/01_overview.py", "练习题索引（每题一个文件）"),
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