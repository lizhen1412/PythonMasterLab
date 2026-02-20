#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：if 条件书写的常见模式（范围判断/否定形式/多行条件/推导式条件）
Author: Lambert

你会学到：
1) 链式比较：`0 <= x <= 100` 用于范围判断
2) 否定形式：`not in` / `is not` 更清晰
3) 多行条件：用括号换行，不用反斜杠
4) 赋值表达式 `:=`：避免重复计算
5) 推导式中的 `if`：过滤 vs 条件表达式（产生值）

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/11_if_condition_patterns.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 链式比较：范围判断")
    for score in [-1, 0, 60, 100, 101]:
        if 0 <= score <= 100:
            print(f"{score:>3} -> valid")
        else:
            print(f"{score:>3} -> invalid")

    show("2) not in / is not：否定形式更直观")
    banned = {"root", "admin"}
    for name in ["alice", "root", "bob"]:
        if name not in banned:
            print(f"{name:<5} -> allowed")
        else:
            print(f"{name:<5} -> blocked")

    for token in [None, "abc"]:
        if token is not None:
            print("token ->", token)
        else:
            print("token -> missing")

    show("3) 多行条件：用括号换行")
    is_active = True
    role = "editor"
    is_owner = True
    is_archived = False
    if (
        is_active
        and role in {"editor", "admin"}
        and is_owner
        and not is_archived
    ):
        print("can_edit -> True")
    else:
        print("can_edit -> False")

    show("4) := 在条件里减少重复计算")
    for raw in ["  Alice  ", "   "]:
        if (name := raw.strip()):
            print("name ->", name)
        else:
            print(f"blank -> {raw!r}")
    items = [10, 20, 30]
    if (n := len(items)) > 0:
        print("items length ->", n)

    show("5) 推导式 if：过滤 vs 产生值")
    nums = [-2, -1, 0, 1, 2]
    positives = [n for n in nums if n > 0]
    labels = ["pos" if n > 0 else "non-pos" for n in nums]
    print("nums ->", nums)
    print("positives ->", positives)
    print("labels ->", labels)


if __name__ == "__main__":
    main()