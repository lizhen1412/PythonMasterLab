#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：多来源输入（fileinput）。
Author: Lambert

你会学到：
1) fileinput 统一处理：文件列表 + stdin
2) fileinput.filename / filelineno 获取来源信息
3) 用 StringIO 模拟 stdin

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/16_fileinput_multiple_sources.py file1.txt file2.txt
"""

from __future__ import annotations

import fileinput
from io import StringIO
import sys


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo_with_stdin_simulated() -> None:
    show("1) 模拟 stdin（files=['-']）")
    old = sys.stdin
    sys.stdin = StringIO("alpha\\nbeta\\n")
    try:
        for line in fileinput.input(files=["-"]):
            print(f"{fileinput.filename()}:{fileinput.filelineno()} -> {line.rstrip()}")
    finally:
        fileinput.close()
        sys.stdin = old


def demo_with_files(paths: list[str]) -> None:
    show("2) 读取指定文件")
    for line in fileinput.input(files=paths):
        print(f"{fileinput.filename()}:{fileinput.filelineno()} -> {line.rstrip()}")
    fileinput.close()


def main() -> None:
    if len(sys.argv) > 1:
        demo_with_files(sys.argv[1:])
    else:
        demo_with_stdin_simulated()
        print("\nTIP: 你也可以传入文件名列表进行读取。")


if __name__ == "__main__":
    main()