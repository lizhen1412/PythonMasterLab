#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：变量（进阶，02_Variables）练习索引（每题一个文件）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/08_Exercises/02_Variables/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_unpacking_star_middle.py", "解包：first/*middle/last"),
    ("03_aliasing_and_chained_assignment.py", "别名陷阱：a = b = []；以及正确写法"),
    ("04_augmented_assignment_vs_concat.py", "a += ... vs a = a + ...（别名与可变性）"),
    ("05_copy_shallow_vs_deep.py", "浅拷贝 vs 深拷贝：嵌套结构共享问题"),
    ("06_scope_nonlocal_counter.py", "nonlocal：闭包计数器"),
    ("07_walrus_sum_until_blank.py", "海象运算符 :=：读取/strip/累加直到空行"),
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
