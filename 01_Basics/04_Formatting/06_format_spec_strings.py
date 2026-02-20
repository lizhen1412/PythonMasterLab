#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：格式化规格——字符串（str）。
Author: Lambert

你会学到：
1) 宽度/对齐：`<`/`>`/`^`
2) 填充字符：`*<10`、`-^20` 等
3) 截断（precision）：`{s:.5}`（只保留前 5 个字符）
4) 把“多个字段对齐输出”做得更专业

运行：
    python3 01_Basics/04_Formatting/06_format_spec_strings.py
"""


def main() -> None:
    s = "hello"
    long = "This is a very long string"

    print("1) 对齐：")
    print(f"[{s:<10}] left")
    print(f"[{s:>10}] right")
    print(f"[{s:^10}] center")

    print("\n2) 填充：")
    print(f"[{s:*<10}]")
    print(f"[{s:*>10}]")
    print(f"[{s:-^10}]")

    print("\n3) 截断：")
    print(f"orig: {long}")
    print(f"cut : {long:.10} ...")

    print("\n4) 做一个简单“对齐表格”：")
    rows = [
        ("Alice", "Beijing"),
        ("Bob", "Shenzhen"),
        ("Charlie", "Hangzhou"),
    ]
    for name, city in rows:
        print(f"{name:<10} | {city:<10}")


if __name__ == "__main__":
    main()
