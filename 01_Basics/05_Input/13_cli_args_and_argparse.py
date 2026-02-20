#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：命令行参数输入（sys.argv / argparse）。
Author: Lambert

你会学到：
1) sys.argv：原始参数列表
2) argparse：更可读的命令行接口（类型转换/默认值）

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/13_cli_args_and_argparse.py --name Alice --count 2 hello world
"""

from __future__ import annotations

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Input demo: sys.argv and argparse")
    parser.add_argument("items", nargs="*", help="positional items")
    parser.add_argument("--name", default="Guest", help="name to prefix")
    parser.add_argument("--count", type=int, default=1, help="repeat count")
    parser.add_argument("--verbose", action="store_true", help="show raw args")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.verbose:
        print("sys.argv ->", sys.argv)
    print("parsed ->", args)

    if not args.items:
        print("tip: add items, e.g. --name Alice --count 2 hello world")
        return

    for item in args.items:
        print(f"{args.name}: {item}" * args.count)


if __name__ == "__main__":
    main()