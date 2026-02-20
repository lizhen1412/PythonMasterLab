#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：综合练习（Exercises）索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/08_Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_enumerate_all_lessons.py", "枚举 01_Basics/ 全部章节与脚本（读取每章 TOPICS）"),
    ("01_Comments/01_overview.py", "01 注释练习索引（每题一个文件）"),
    ("02_Variables/01_overview.py", "02 变量（进阶）练习索引（每题一个文件）"),
    ("03_Printing/01_overview.py", "03 打印练习索引（每题一个文件）"),
    ("04_Formatting/01_overview.py", "04 格式化练习索引（每题一个文件）"),
    ("05_Input/01_overview.py", "05 输入练习索引（每题一个文件）"),
    ("06_Variables/01_overview.py", "06 变量（入门）练习索引（每题一个文件）"),
    ("07_Data_Types/01_overview.py", "07 数据类型练习索引（每题一个文件）"),
    ("08_mini_project_expense_report.py", "小项目：解析“记账 CSV”，分组统计并输出对齐报表/JSON"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()