#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：sys.stdin.readline/read 到 EOF（以及与 input() 的关系）。

你会学到：
1) `input()`：读一行并去掉结尾换行符（没读到会 EOFError）
2) `sys.stdin.readline()`：读一行，**可能包含结尾 \\n**；到 EOF 返回 ""
3) `sys.stdin.read()`：读剩余全部内容；到 EOF 返回 ""
4) 读取“未知行数”的输入：经常用 `for line in sys.stdin: ...`
5) 专业小技巧：prompt 写到 stderr（stdout 保持干净可被管道处理）

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/10_sys_stdin_readline_and_pipe.py

可选：你也可以用“管道/重定向”喂输入（仍然不需要切换目录）：
    printf "a\\nb\\n" | python3 01_Basics/05_Input/10_sys_stdin_readline_and_pipe.py
"""

from __future__ import annotations

from io import StringIO
import sys


def demo_with_stringio() -> None:
    print("1) demo：用 StringIO 模拟 stdin，演示 readline / read：")
    old = sys.stdin
    sys.stdin = StringIO("a\\nb\\n")
    try:
        line1 = sys.stdin.readline()
        line2 = sys.stdin.readline()
        line3 = sys.stdin.readline()  # EOF -> ""
        print("readline #1 repr =", repr(line1))
        print("readline #2 repr =", repr(line2))
        print("readline #3 repr =", repr(line3))

        sys.stdin = StringIO("x\\ny\\n")
        rest = sys.stdin.read()
        print("read() repr =", repr(rest))
    finally:
        sys.stdin = old


def read_line_with_stderr_prompt(prompt: str) -> str:
    print(prompt, end="", file=sys.stderr, flush=True)
    line = sys.stdin.readline()
    if line == "":
        raise EOFError("stdin reached EOF")
    return line.rstrip("\n")


def interactive_one_line() -> None:
    if not sys.stdin.isatty():
        return

    print("\n2) 交互演示：请输入一行文本（我们用 sys.stdin.readline 读取）：")
    line = sys.stdin.readline()
    if line == "":
        print("EOF：没有读到任何内容")
        return

    print("repr(line) =", repr(line))
    print("rstrip('\\n') =", repr(line.rstrip(\"\\n\")))

    try:
        text = input("\n3) 再用 input() 读一行（它会自动去掉结尾换行）：")
        print("repr(text) =", repr(text))
    except EOFError:
        print("\nEOFError：input 没读到任何内容")

    try:
        value = read_line_with_stderr_prompt("\n4) （prompt 写到 stderr）请输入一个值：")
        print("value =", repr(value))
    except EOFError:
        print("\nEOF：没有读到任何内容")


def main() -> None:
    demo_with_stringio()
    interactive_one_line()

    print("\n5) 读取到 EOF 的常用写法：")
    print("   for line in sys.stdin: ...（适合管道/文件重定向）")


if __name__ == "__main__":
    main()
