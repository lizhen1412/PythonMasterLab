#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：f-string（推荐的现代格式化方式）。

你会学到：
1) f-string 可以在一行里拼出结构化字符串（k=v 风格很常见）
2) 表达式：`f"{a+b}"`
3) 调试输出：`f"{var=}"`（自动打印变量名和值）
4) 转换：`!r`/`!s`/`!a`
5) 格式化规格：`f"{pi:.2f}"`（背后用的是 format spec mini-language）
6) 转义：输出字面量 `{` / `}` 要写成 `{{` / `}}`

运行：
    python3 01_Basics/04_Formatting/03_fstrings_basics.py
"""

from datetime import datetime, timezone


def main() -> None:
    name = "Alice"
    age = 20
    pi = 3.1415926

    print("1) 一行拼字段（最常用）：")
    print(f"name={name} age={age} pi={pi}")

    print("\n2) 表达式：")
    print(f"{age=} next_year={age + 1}")

    print("\n3) !r（调试更清晰）：")
    text = "hi\n"
    print(f"{text=}")
    print(f"{text=!r}")

    print("\n4) 格式化规格：")
    n = 1234567
    print(f"pi={pi:.2f} n={n:,}")

    print("\n5) 日期时间也能直接格式化：")
    now = datetime.now(timezone.utc)
    print(f"now={now:%Y-%m-%d %H:%M:%S %Z}")

    print("\n6) 输出字面量大括号：")
    print(f"literal braces: {{ and }}")


if __name__ == "__main__":
    main()

