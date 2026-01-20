#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 条件判断（Conditionals）相关示例索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_if_single_branch.py", "条件判断：单分支 if（含 pass/guard 的常见写法）"),
    ("03_if_else_double_branch.py", "条件分支：双分支 if/else + 条件表达式"),
    ("04_if_elif_else_multi_branch.py", "多分支：if/elif/else，顺序与覆盖范围"),
    ("05_nested_selection_and_guard_clauses.py", "嵌套选择 vs 卫语句：减少缩进、提升可读性"),
    ("06_truthiness_and_condition_building.py", "真值测试 + 组合条件：and/or/not、in、is、优先级"),
    ("07_match_basics.py", "match 基础：字面量/单例/OR/guard/默认分支"),
    ("08_match_structural_patterns.py", "match 进阶：序列/映射/类模式、as、*star"),
    ("10_leap_year_check.py", "闰年判断：if/else 分支规则与布尔表达式写法"),
    ("11_if_condition_patterns.py", "if 条件书写模式：范围/否定/多行/推导式条件"),
    ("09_chapter_summary.py", "本章总结：关键规则 + 常见误区清单"),
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
