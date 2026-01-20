#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：条件判断（Conditionals）章节练习（每题一个文件）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_truthiness_blank_and_none.py", "真值测试：区分 None 与空字符串/0/False"),
    ("03_single_branch_append_if_missing.py", "单分支 if：如果不存在就追加（in/not in）"),
    ("04_double_branch_parity_label.py", "双分支：奇偶判断（if/else 与条件表达式）"),
    ("05_multi_branch_grade.py", "多分支：分数 -> 等级（if/elif/else）"),
    ("06_nested_vs_guard_access.py", "嵌套选择 vs 卫语句：实现 can_upload"),
    ("07_match_command_tuple.py", "match：解析命令元组（add/mul/neg）"),
    ("08_match_sequence_unpack.py", "match：序列模式（[x,y]、[head,*tail]）"),
    ("09_match_mapping_event.py", "match：映射模式（dict 结构）"),
    ("10_match_guard_ranges.py", "match：用 guard 实现范围判断（<0/==0/>0）"),
    ("11_precedence_and_short_circuit.py", "优先级与短路：若干表达式与安全写法"),
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

