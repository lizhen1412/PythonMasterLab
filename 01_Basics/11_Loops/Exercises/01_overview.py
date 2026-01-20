#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：循环（Loops）章节练习（每题一个文件）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/11_Loops/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_sum_1_to_n.py", "for/while：实现 1..n 求和"),
    ("03_for_else_prime_check.py", "for-else：素数判断（未 break 才算 prime）"),
    ("04_continue_skip_blanks.py", "continue：过滤空白并规范化字符串列表"),
    ("05_break_nested_search.py", "break：在嵌套循环中查找坐标（flag vs return）"),
    ("06_enumerate_and_zip.py", "enumerate/zip：对齐两列数据并生成行"),
    ("07_range_step_reverse.py", "range：步长与反向遍历"),
    ("08_multiplication_table_9x9.py", "九九乘法表：生成字符串表格（嵌套循环）"),
    ("09_powerset_count_exponential.py", "指数爆炸：计算 2^n 与生成小规模 powerset"),
    ("10_fizzbuzz.py", "综合：FizzBuzz（for + 条件分支）"),
    ("11_guess_number_simulated.py", "while：猜数字（模拟输入），练习 break/continue/while-else"),
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
