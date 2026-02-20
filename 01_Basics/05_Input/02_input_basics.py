#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：input() 基础。
Author: Lambert

你会学到：
1) `input(prompt)` 会从标准输入（stdin）读“一行”，返回 **str**
2) 返回值不包含结尾的换行符 `\\n`
3) 空输入：直接回车会得到空字符串 `""`
4) 空白字符（空格/Tab）不会自动去掉；需要自己 `.strip()`

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/02_input_basics.py
"""

from __future__ import annotations


def run() -> None:
    name = input("1) 请输入你的名字：")
    print("name =", name)
    print("type(name) =", type(name))
    print("repr(name) =", repr(name))
    print("len(name) =", len(name))

    raw = input("\n2) 输入一段带前后空格的文本（例如：  hi  ）：")
    print("repr(raw)       =", repr(raw))
    print("repr(raw.strip) =", repr(raw.strip()))

    empty = input("\n3) 直接回车（得到空字符串）：")
    print("empty == '' ->", empty == "")


def main() -> None:
    try:
        run()
    except EOFError:
        print("\nEOFError：没有读到输入（stdin 可能已到 EOF / 你按了 Ctrl-D 或 Ctrl-Z）。")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt：你中断了输入（Ctrl-C）。")


if __name__ == "__main__":
    main()
