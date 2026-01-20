#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：print 基础：打印变量与常用参数。

你会学到：
1) `print(*objects)`：打印多个值
2) `sep`：多个值之间的分隔符
3) `end`：行尾结束符（默认换行）
4) `file`：把输出写到一个“类文件对象”（本例用 StringIO 演示）
5) `flush`：是否立即刷新缓冲（在某些实时输出场景有用）

运行：
    python3 01_Basics/02_Variables/13_print_basics.py
"""

from io import StringIO


def main() -> None:
    user = "Alice"
    score = 98
    print("user =", user, "score =", score)

    print("\nsep 示例：")
    print(1, 2, 3, sep=" | ")

    print("\nend 示例：")
    print("Hello", end=" ... ")
    print("World")

    print("\nfile 示例（把输出写到内存缓冲区）：")
    buf = StringIO()
    print("line1", file=buf)
    print("line2", file=buf)
    captured = buf.getvalue()
    print("captured =", captured.replace("\n", "\\n"))

    print("\nflush 示例：")
    print("this is flushed", flush=True)


if __name__ == "__main__":
    main()

