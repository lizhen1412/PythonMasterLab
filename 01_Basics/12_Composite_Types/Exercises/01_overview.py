#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：组合数据类型（Composite Types）章节练习（每题一个文件）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_sequence_slice_head_tail.py", "序列：切片/解包 head-tail（first/middle/last）"),
    ("03_list_dedup_preserve_order.py", "list：去重但保持顺序（不使用 set 破坏顺序）"),
    ("04_list_stack_ops.py", "list：用 append/pop 实现栈（push/pop/peek）"),
    ("05_list_filter_and_square.py", "list：过滤 + 映射（推导式）"),
    ("06_tuple_unpack_swap.py", "tuple：解包与交换变量（a,b=b,a）"),
    ("07_range_generate_slices.py", "range：生成区间并演示切片结果仍为 range"),
    ("08_string_split_join_normalize.py", "str：split/join + 规范化空白"),
    ("09_dict_word_count_and_group.py", "dict：计数与分组（get/setdefault）"),
    ("10_set_unique_and_intersection.py", "set：去重与交集（集合运算）"),
    ("11_mutability_copy_fix.py", "可变性：修复嵌套列表的共享引用坑"),
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
