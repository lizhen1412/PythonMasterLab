#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：一行输入多个值（split/unpack/map/shlex.split）。
Author: Lambert

你会学到：
1) `line.split()`：按空白切分（多个空格也 OK）
2) 解包：`a, b = parts`（个数不对会 ValueError，需要保护）
3) `map(int, parts)`：把多个 token 转成 int
4) `maxsplit`：控制最多切几刀（把剩余部分当成一个字段）
5) `shlex.split`：支持引号（例如 name="Alice Bob"）
6) 逗号分隔：简单场景用 `split(',')` + strip；复杂场景用 `csv`

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/05_multiple_values_split.py
"""

from __future__ import annotations

import csv
import shlex


def main() -> None:
    try:
        line = input("1) 输入两个整数（空格分隔，例如：10 20）：").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n未输入：跳过 1)")
        line = ""

    if line:
        parts = line.split()
        try:
            a_str, b_str = parts
            a, b = int(a_str), int(b_str)
            print(f"a={a}, b={b}, sum={a + b}")
        except ValueError:
            print("解析失败：请确保只输入两个整数，例如：10 20")

    try:
        line2 = input("\n2) 输入 3 个名字（逗号分隔，例如：Alice,Bob,Charlie）：").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n未输入：跳过 2)")
        line2 = ""

    if line2:
        # 简单场景：手动 split + strip
        names_simple = [p.strip() for p in line2.split(",") if p.strip()]
        print("names (simple) =", names_simple)

        # 复杂场景：csv 能处理引号与逗号
        names_csv = next(csv.reader([line2], skipinitialspace=True))
        names_csv = [p.strip() for p in names_csv if p.strip()]
        print("names (csv)    =", names_csv)

    try:
        line3 = input('\n3) 输入：name="Alice Bob" city=Beijing（演示 shlex.split）：').strip()
    except (EOFError, KeyboardInterrupt):
        print("\n未输入：跳过 3)")
        line3 = ""

    if line3:
        tokens = shlex.split(line3)
        print("tokens =", tokens)

    try:
        line4 = input("\n4) 输入一句话（我们只切两刀，其余作为 comment）：").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n未输入：跳过 4)")
        line4 = ""

    if line4:
        head1, head2, comment = (line4.split(maxsplit=2) + ["", "", ""])[:3]
        print("field1 =", head1)
        print("field2 =", head2)
        print("comment =", comment)


if __name__ == "__main__":
    main()
