#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：条件判断——单分支 if（Single-branch）
Author: Lambert

你会学到：
1) if 的基本语法：`if condition: ...`（没有 else）
2) 代码块由“缩进”定义；冒号 `:` 表示后面进入一个代码块
3) `pass`：占位（让代码先能跑起来）
4) 常见 guard 写法：用 if 在不满足条件时直接 return（减少嵌套）

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/02_if_single_branch.py
"""

from __future__ import annotations


def greet_if_name_provided(name: str | None) -> str:
    if name is None:
        return "Hello, stranger."

    # 单分支 if：只在条件满足时执行
    if name.strip():
        return f"Hello, {name.strip()}!"
    return "Hello, stranger."


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 单分支 if：满足条件才执行")
    x = 10
    if x > 5:
        print("x > 5 -> run block")
    if x < 0:
        print("x < 0 -> never prints")

    show("2) pass：占位（语法上需要一个块）")
    flag = True
    if flag:
        pass
    print("flag=True but we did nothing (pass).")

    show("3) guard：条件不满足就提前返回（减少嵌套）")
    for name in [None, "", "  ", "Alice"]:
        print(f"name={name!r} ->", greet_if_name_provided(name))


if __name__ == "__main__":
    main()
