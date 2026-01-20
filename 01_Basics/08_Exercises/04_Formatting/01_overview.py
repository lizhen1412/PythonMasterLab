#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：格式化（Formatting）练习索引（每题一个文件）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/08_Exercises/04_Formatting/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_format_spec_numbers.py", "格式化规格：金额/百分比/对齐输出"),
    ("03_render_table.py", "渲染对齐文本表格（按列宽自动对齐）"),
    ("04_datetime_formatting.py", "datetime 格式化：strftime vs isoformat"),
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

