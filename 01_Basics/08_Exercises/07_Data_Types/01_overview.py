#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：数据类型（Data Types）练习索引（每题一个文件）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/08_Exercises/07_Data_Types/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_coalesce_none_vs_or.py", "None 与真值测试：只把 None 当缺失值"),
    ("03_dict_count_and_group.py", "dict：计数与分组"),
    ("04_set_operations.py", "set：并/交/差/对称差"),
    ("05_bytes_memoryview_patch.py", "bytes/bytearray/memoryview：原地修改缓冲区"),
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

