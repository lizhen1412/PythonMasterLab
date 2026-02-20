#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：多分支 if/elif/else（Multi-branch）
Author: Lambert

你会学到：
1) `elif`：按顺序匹配，命中第一个就停止（后面的不会再判断）
2) 分支顺序很重要：范围判断要从“更严格”到“更宽泛”
3) `else` 作为兜底：保证所有路径都有返回值/行为

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/04_if_elif_else_multi_branch.py
"""

from __future__ import annotations


def grade(score: int) -> str:
    if not (0 <= score <= 100):
        return "INVALID"

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) if/elif/else：按顺序命中第一个分支")
    for s in [105, 95, 83, 70, 60, 59]:
        print(f"score={s:>3} -> grade={grade(s)}")

    show("2) 对比：多个独立 if vs elif 链")
    x = 5
    print("x =", x)
    if x > 0:
        print("if: x > 0")
    if x > 3:
        print("if: x > 3（独立 if，会继续执行）")

    if x > 0:
        print("elif-chain: x > 0")
    elif x > 3:
        # 这一行永远到不了，因为上面已命中并结束
        print("elif-chain: x > 3")


if __name__ == "__main__":
    main()
