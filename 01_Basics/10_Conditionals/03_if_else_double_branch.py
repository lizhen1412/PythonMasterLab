#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：条件分支——双分支 if/else（Two-branch）

你会学到：
1) `if ... else ...`：二选一
2) `x if cond else y`：条件表达式（用于“产生一个值”）
3) 什么时候用 if/else 语句块，什么时候用条件表达式

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/03_if_else_double_branch.py
"""

from __future__ import annotations


def parity_label(n: int) -> str:
    # 条件表达式：适合简单二选一（返回值）
    return "even" if n % 2 == 0 else "odd"


def abs_manual(x: int) -> int:
    # if/else 语句块：适合需要多行逻辑/副作用的分支
    if x >= 0:
        return x
    else:
        return -x


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) if/else：二选一")
    for x in [3, 0, -3]:
        print(f"abs_manual({x}) ->", abs_manual(x))

    show("2) 条件表达式：一行产生值")
    for n in range(5):
        print(f"{n} ->", parity_label(n))

    show("3) 可读性建议：复杂条件表达式不建议嵌套")
    score = 73
    # 这个例子只是展示语法；真实项目建议用 if/elif/else
    level = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "D"))
    print("nested conditional expression ->", level)


if __name__ == "__main__":
    main()

