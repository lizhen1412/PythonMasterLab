#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：numpy 本章总结。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/17_chapter_summary.py
"""

from __future__ import annotations


SUMMARY: list[str] = [
    "掌握 ndarray 的创建、dtype/shape 基础属性",
    "理解索引/切片与视图/拷贝区别",
    "熟悉 reshape/transpose 与广播规则",
    "掌握 axis 聚合与 NaN 处理",
    "了解排序、拼接、随机与线性代数基础",
    "会用 save/load 与常见 ufunc",
]


def main() -> None:
    print("本章总结（numpy 2.4.0）：")
    for i, line in enumerate(SUMMARY, start=1):
        print(f"{i}. {line}")
    print("
下一步：运行练习索引 -> python3 02_Frameworks/02_Numpy/Exercises/01_overview.py")


if __name__ == "__main__":
    main()