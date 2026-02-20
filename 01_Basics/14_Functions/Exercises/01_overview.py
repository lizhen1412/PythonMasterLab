#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：函数（Functions）章节练习（每题一个文件）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/14_Functions/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_fix_mutable_default.py", "修复可变默认值陷阱，使用 None 哨兵"),
    ("03_kwonly_api_design.py", "设计带关键字仅限参数的 API 并演示调用"),
    ("04_closure_counter.py", "闭包计数器：nonlocal 累积状态"),
    ("05_lambda_sort_and_filter.py", "lambda 排序/过滤一批记录，比较可读性"),
    ("06_implement_simple_map_filter.py", "手写简化版 map/filter，并与内置对照"),
    ("07_factorial_recursive_vs_iterative.py", "阶乘递归 vs 迭代，讨论递归深度限制"),
    ("08_timer_decorator.py", "编写计时装饰器，透传 *args/**kwargs"),
    ("09_card_system_feature.py", "为名片系统补充“按姓名模糊搜索”功能"),
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