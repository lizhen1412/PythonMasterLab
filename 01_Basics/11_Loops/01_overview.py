#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 循环（Loops）相关示例索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/11_Loops/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_while_loops.py", "while 基础：计数、sentinel、while-else、continue/break"),
    ("03_for_loops.py", "for 基础：range/enumerate/zip/dict/for-else/iter-next"),
    ("04_break_and_continue.py", "break/continue 细节：loop-else、嵌套循环退出策略"),
    ("05_multiplication_table_9x9.py", "九九乘法表：嵌套循环 + 输出对齐"),
    ("06_exponential_explosion.py", "指数爆炸：2^n 增长与子集生成示例"),
    ("08_guess_number_game_simulated.py", "while 综合：猜数字（模拟输入），演示 break/continue/while-else"),
    ("09_while_patterns_and_edge_cases.py", "while 补充模式：do-while、:= 条件、迭代器驱动"),
    ("07_chapter_summary.py", "本章总结：关键规则 + 常见误区清单"),
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