#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 25：pandas 本章总结。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/25_chapter_summary.py
"""

from __future__ import annotations


SUMMARY: list[str] = [
    "掌握 Series/DataFrame 的创建、索引与基础属性",
    "熟悉 loc/iloc 与条件过滤、缺失值处理",
    "理解类型转换、向量化运算与对齐机制",
    "掌握分组聚合、透视/重塑与合并拼接",
    "理解时间序列处理与窗口计算",
    "了解常见 I/O 与性能实践",
]


def main() -> None:
    print("本章总结（pandas 2.3.3）：")
    for i, line in enumerate(SUMMARY, start=1):
        print(f"{i}. {line}")
    print(
        "\n下一步：运行练习索引 -> python3 02_Frameworks/01_Pandas/Exercises/01_overview.py"
    )
    print(
        "生成 API 索引 -> python3 02_Frameworks/01_Pandas/90_generate_api_reference.py"
    )


if __name__ == "__main__":
    main()