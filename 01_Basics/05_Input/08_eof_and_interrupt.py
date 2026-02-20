#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：EOFError / KeyboardInterrupt（优雅退出）。
Author: Lambert

你会学到：
1) stdin 到 EOF：`input()` 会抛 `EOFError`
   - macOS/Linux: 通常是 Ctrl-D
   - Windows: 通常是 Ctrl-Z 然后回车
2) 用户中断：Ctrl-C 会触发 `KeyboardInterrupt`
3) 专业写法：捕获异常，打印提示，正常退出（不要堆栈刷屏）

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/08_eof_and_interrupt.py
"""

from __future__ import annotations

from io import StringIO
import sys


def demo_eoferror() -> None:
    print("1) 演示 EOFError（用空的 StringIO 模拟 stdin 已到 EOF）：")
    old = sys.stdin
    sys.stdin = StringIO("")
    try:
        _ = input("will raise EOFError: ")
    except EOFError:
        print("捕获到 EOFError：stdin 已到 EOF")
    finally:
        sys.stdin = old


def demo_keyboardinterrupt() -> None:
    print("\n2) 演示 KeyboardInterrupt（这里用手动 raise 模拟）：")
    try:
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        print("捕获到 KeyboardInterrupt：用户中断（通常是 Ctrl-C）")


def interactive_loop() -> None:
    print("\n3) 交互演示：输入任意内容；输入 quit 退出；Ctrl-D/Ctrl-Z 或 Ctrl-C 也会退出")
    while True:
        try:
            line = input("> ")
        except EOFError:
            print("\nEOF：再见。")
            return
        except KeyboardInterrupt:
            print("\n中断：再见。")
            return

        if line.strip().lower() == "quit":
            print("正常退出：再见。")
            return
        print("你输入的是：", repr(line))


def main() -> None:
    demo_eoferror()
    demo_keyboardinterrupt()
    interactive_loop()


if __name__ == "__main__":
    main()
