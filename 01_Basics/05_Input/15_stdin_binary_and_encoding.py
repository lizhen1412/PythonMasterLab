#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：二进制 stdin 与编码（sys.stdin.buffer）。
Author: Lambert

你会学到：
1) sys.stdin 是“文本流”，sys.stdin.buffer 是“字节流”
2) 二进制读取后手动 decode
3) 用 BytesIO 模拟二进制输入

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/15_stdin_binary_and_encoding.py
    printf "hello\\n" | python3 01_Basics/05_Input/15_stdin_binary_and_encoding.py
"""

from __future__ import annotations

from io import BytesIO
import sys


def demo_bytesio() -> None:
    print("1) BytesIO 模拟二进制输入：")
    data = b"hello\\nline2\\n"
    bio = BytesIO(data)
    print("readline #1 ->", bio.readline())
    print("readline #2 ->", bio.readline())
    print("readline #3 ->", bio.readline())


def read_from_stdin_buffer() -> None:
    if sys.stdin.isatty():
        print("\n2) stdin 是 TTY：跳过真实读取（避免阻塞）")
        return
    raw = sys.stdin.buffer.read()
    print("\n2) stdin.buffer.read() ->", raw)
    print("decoded ->", raw.decode("utf-8", errors="replace"))


def main() -> None:
    demo_bytesio()
    read_from_stdin_buffer()


if __name__ == "__main__":
    main()