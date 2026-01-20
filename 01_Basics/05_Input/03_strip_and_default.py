#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：strip 与默认值（处理“空输入 / 空白输入”）。

你会学到：
1) `input()` 返回的字符串不会自动去掉空白；常用 `.strip()` 清理前后空白
2) “默认值”写法：`value = input(...).strip() or "default"`
3) `strip/lstrip/rstrip` 的差异

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/03_strip_and_default.py
"""

from __future__ import annotations


def main() -> None:
    try:
        raw = input("请输入昵称（直接回车将使用默认值 Anonymous）：")
    except (EOFError, KeyboardInterrupt):
        print("\n没有输入：使用默认值 Anonymous")
        raw = ""

    nickname = raw.strip() or "Anonymous"
    print("raw      =", repr(raw))
    print("nickname =", repr(nickname))

    text = "   hello   \n"
    print("\nstrip 家族示例（不依赖 input，方便你对比理解）：")
    print("text         =", repr(text))
    print("strip()      =", repr(text.strip()))
    print("lstrip()     =", repr(text.lstrip()))
    print("rstrip()     =", repr(text.rstrip()))
    print("rstrip('\\n') =", repr(text.rstrip(\"\\n\")))


if __name__ == "__main__":
    main()

