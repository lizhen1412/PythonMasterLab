#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：格式化规格（format spec mini-language）——一行打印更整齐。
Author: Lambert

你会学到：
1) 宽度/对齐：`{name:<10}`、`{score:>6.2f}`
2) 千分位：`{n:,}`
3) 百分比：`{ratio:.1%}`
4) 打印“表格行”（每行多个字段）

运行：
    python3 01_Basics/03_Printing/06_format_spec_mini_language.py
"""


def main() -> None:
    rows = [
        ("Alice", 98.5, 1234567),
        ("Bob", 7.0, 1200),
        ("Charlie", 100.0, 42),
    ]

    print("name      | score  | count")
    print("-" * 26)
    for name, score, count in rows:
        print(f"{name:<10} | {score:>6.2f} | {count:>8,}")

    print("\n百分比示例：")
    ratio = 0.375
    print(f"ratio={ratio:.1%}")

    print("\n对齐/填充示例：")
    for n in [1, 12, 123]:
        print(f"n={n:0>5}")  # 左侧用 0 填充到 5 位


if __name__ == "__main__":
    main()
