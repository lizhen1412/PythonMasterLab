#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：运算符（Operators）章节练习（每题一个文件）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/09_Operators/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_arithmetic_calculator.py", "算术：实现一个小计算器（+ - * / // % ** divmod）"),
    ("03_floor_div_mod_rules.py", "算术：验证 // 与 % 的恒等式（含负数）"),
    ("04_augmented_assignment_mutability.py", "赋值：+= 与 + 在可变对象上的差异（别名影响）"),
    ("05_comparison_chain_between.py", "比较：用链式比较实现 is_between"),
    ("06_float_isclose.py", "比较：用 math.isclose 做浮点相等判断"),
    ("07_logical_coalesce_none.py", "逻辑：实现 None 合并（避免 x or default 的坑）"),
    ("08_bitwise_flags.py", "位运算：实现 flags（设置/清除/检查某个标志位）"),
    ("09_membership_in_dict.py", "成员：dict 的 in 检查 key；以及 values 的检查方式"),
    ("10_precedence_puzzles.py", "优先级：若干表达式的结果（建议先手算再运行）"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习题清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
