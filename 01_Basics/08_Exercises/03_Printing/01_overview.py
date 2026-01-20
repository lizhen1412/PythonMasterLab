#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：打印（Printing）练习索引（每题一个文件）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/08_Exercises/03_Printing/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_capture_print_output.py", "用 StringIO 捕获 print 输出（sep/end）"),
    ("03_print_dict_formats.py", "把 dict 打印成 k=v / JSON / querystring（稳定顺序）"),
    ("04_unpacking_and_join.py", "print(*items) vs join：把可迭代对象打印成一行"),
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

