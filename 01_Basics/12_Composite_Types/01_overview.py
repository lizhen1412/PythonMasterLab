#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 组合数据类型（Composite Types）相关示例索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_sequences_overview.py", "序列通用操作：索引/切片/解包/拼接/成员测试"),
    ("03_list_creation.py", "list 创建方式：字面量/构造/推导式/解包/常见坑"),
    ("04_list_daily_operations.py", "list 日常操作：增删改查、排序、拷贝与别名"),
    ("05_list_traversal.py", "list 遍历：for/enumerate/reversed/推导式/安全修改"),
    ("06_tuple_creation_and_ops.py", "tuple 创建与常用操作：解包、不可变、count/index"),
    ("07_range_basics.py", "range：区间、步长、索引/切片、与 list 的区别"),
    ("13_range_edge_cases.py", "range 边界与易错点：空区间、负步长、切片、相等比较"),
    ("08_string_basics.py", "str：序列特性 + 高频文本方法（split/join/replace）"),
    ("09_dict_basics.py", "dict：创建/访问/更新/遍历/计数分组套路"),
    ("10_set_basics.py", "set：去重、成员测试、集合运算、frozenset"),
    ("11_mutability_and_copy.py", "可变 vs 不可变：别名、浅拷贝/深拷贝、嵌套陷阱"),
    ("12_chapter_summary.py", "本章总结：关键规则 + 常见误区清单"),
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
