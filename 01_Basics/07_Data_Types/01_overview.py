#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 数据类型（Data Types）示例索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_type_system_and_categories.py", "类型系统概览：type/isinstance/真值测试/可变性/可哈希性"),
    ("03_none_and_bool.py", "None 与 bool：空值、条件判断、True/False 与陷阱"),
    ("04_numbers_int_float_complex.py", "数字类型：int/float/complex、运算、精度与 Decimal/Fraction"),
    ("05_strings_str.py", "字符串 str：创建、索引切片、常用方法、编码/解码基础"),
    ("06_list_tuple_range.py", "序列类型：list/tuple/range（可变 vs 不可变、解包）"),
    ("07_dict_mapping.py", "映射类型 dict：创建、访问、遍历、合并、常用方法"),
    ("08_set_frozenset.py", "集合 set/frozenset：去重、集合运算、成员测试"),
    ("09_bytes_bytearray_memoryview.py", "二进制：bytes/bytearray/memoryview（编码、切片、零拷贝视图）"),
    ("10_mutability_copy_and_hashability.py", "可变性/拷贝/可哈希：为什么 list 不能当 dict key"),
    ("11_common_conversions_and_helpers.py", "常见转换与工具：str/repr/ascii、len/iter/enumerate、sorted"),
    ("12_str_methods_reference.py", "str 方法全覆盖：清理/查找/替换/判断/格式化/编码"),
    ("13_sequence_methods_reference.py", "序列方法全覆盖：list/tuple/range"),
    ("14_mapping_and_set_methods_reference.py", "映射与集合方法全覆盖：dict/set/frozenset"),
    ("15_binary_types_methods_reference.py", "二进制方法全覆盖：bytes/bytearray/memoryview"),
    ("16_numeric_types_methods_reference.py", "数值方法全覆盖：int/float/complex"),
    ("17_collection_method_variants.py", "集合类方法参数与边界：list/tuple/dict/set"),
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
