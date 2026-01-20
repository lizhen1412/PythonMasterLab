#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：海象运算符（:=，assignment expression）。

它的作用是：在表达式内部“顺便把值绑定给一个名字”，减少重复计算/重复调用。

你会看到：
1) 典型用法：if (m := pattern.search(text)) is not None:
2) while 循环读数据：while (line := stream.readline()) != "":
3) 作用域细节：在推导式里，推导式的循环变量不泄漏，但 `:=` 绑定的名字会绑定到外层作用域

运行：
    python3 01_Basics/02_Variables/11_walrus_operator.py
"""

from io import StringIO
import re
from typing import Optional


def demo_regex() -> None:
    text = "Name: Alice\nAge: 20\n"
    pattern = re.compile(r"Name: (\w+)")
    if (m := pattern.search(text)) is not None:
        print("name =", m.group(1))


def demo_read_lines() -> None:
    stream = StringIO("first\n\nsecond\n")
    non_empty: list[str] = []
    while (line := stream.readline()) != "":
        stripped = line.strip()
        if stripped:
            non_empty.append(stripped)
    print("non_empty =", non_empty)


def demo_scope_detail() -> None:
    print("\n作用域细节演示：")
    before = set(locals().keys())

    last: Optional[int] = None
    values = [(last := n) for n in range(3)]

    print("values =", values)
    print("last =", last)
    print("推导式变量 n 是否泄漏？", "n" in locals())
    print(":= 绑定的 last 是否在当前作用域？", "last" in locals())

    after = set(locals().keys())
    print("locals() 变化（新增的名字）=", sorted(after - before))


def main() -> None:
    demo_regex()
    demo_read_lines()
    demo_scope_detail()


if __name__ == "__main__":
    main()
