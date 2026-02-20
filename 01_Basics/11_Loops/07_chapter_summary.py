#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：循环——本章总结
Author: Lambert

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/07_chapter_summary.py
"""

from __future__ import annotations


SUMMARY: list[str] = [
    "while：注意更新变量；while True + break 常用于 sentinel/读输入",
    "while 的常见模板：次数限制（最多尝试 N 次）+ break 成功；配合 while-else 表达“失败”",
    "补充：do-while 可用 while True 模拟；:=/next+sentinel 常用于流式读取",
    "for：遍历 iterable；range/enumerate/zip/dict.items 是最常用组合",
    "break：只退出当前一层循环；continue：只跳过当前迭代",
    "loop-else：只有“没有 break”才执行 else（常用于查找/验证）",
    "嵌套循环：注意复杂度；两层通常 O(n^2)，指数爆炸常见于 2^n 分叉",
    "九九乘法表：典型嵌套循环练习，重点是行列控制与输出对齐",
]


def main() -> None:
    print("本章总结（Loops）：")
    for i, line in enumerate(SUMMARY, start=1):
        print(f"{i}. {line}")
    print("\n下一步：运行练习题索引 -> python3 01_Basics/11_Loops/Exercises/01_overview.py")


if __name__ == "__main__":
    main()