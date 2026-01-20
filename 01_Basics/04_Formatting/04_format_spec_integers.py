#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：格式化规格（format spec）——整数（int）。

本文件覆盖“常见且必须会”的整数格式化：
1) 进制：b/o/d/x/X
2) `#`：带前缀（0b/0o/0x）
3) 宽度/对齐/填充：`{n:>8}`、`{n:0>8}`
4) 符号：`+`/空格/默认
5) 分组：`,`（千分位）和 `_`（下划线分组）
6) `c`：把整数当 Unicode 码点输出字符（谨慎使用）
7) `n`：locale-aware 数字（环境相关，可能因系统 locale 不同而不同）

运行：
    python3 01_Basics/04_Formatting/04_format_spec_integers.py
"""

import locale


def main() -> None:
    n = 255
    neg = -42

    print("1) 进制与前缀：")
    print(f"n={n} bin={n:b} oct={n:o} dec={n:d} hex={n:x} HEX={n:X}")
    print(f"with prefix: {n:#b} {n:#o} {n:#x} {n:#X}")

    print("\n2) 宽度/对齐/填充：")
    print(f"[{n:>8}] right")
    print(f"[{n:<8}] left")
    print(f"[{n:^8}] center")
    print(f"[{n:0>8}] zero-pad")

    print("\n3) 符号：")
    print(f"default: {neg:d}")
    print(f"always : {neg:+d} {n:+d}")
    print(f"space  : {neg: d} {n: d}")

    print("\n4) 分组：")
    big = 1234567890
    print(f"comma      : {big:,}")
    print(f"underscore : {big:_}")

    print("\n5) c（码点转字符）：")
    print(f"65 -> {65:c} (expect 'A')")

    print("\n6) n（locale-aware）：")
    try:
        locale.setlocale(locale.LC_ALL, "")
        print("current locale =", locale.getlocale())
        print(f"{big:n}")
    except Exception as exc:
        print("locale not available:", exc)


if __name__ == "__main__":
    main()

