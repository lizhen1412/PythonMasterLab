#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：输入（Input）练习索引（每题一个文件）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/08_Exercises/05_Input/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_parse_bool.py", "解析 bool：自定义规则（y/n/true/false/1/0/on/off）"),
    ("03_fake_input_and_ask_until_valid.py", "依赖注入 input：fake_input + 校验重试"),
    ("04_parse_csv_line.py", "csv 解析：正确处理引号与逗号"),
    ("05_multiline_until_end.py", "多行输入直到 END（模拟）"),
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
