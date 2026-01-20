#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：成员运算符（Membership Operators）

你会学到：
1) `in / not in` 的含义：检查“成员关系”
2) `in` 在 `dict` 上检查的是 key（不是 value）
3) set 的成员测试通常更快（平均 O(1)）
4) 补充：身份运算符 `is / is not`（最常见用法：`x is None`）

运行（在仓库根目录执行）：
    python3 01_Basics/09_Operators/07_membership_operators.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) list / set / str 的成员关系")
    items = [1, 2, 3]
    s = {1, 2, 3}
    text = "hello"
    print("2 in [1,2,3] ->", 2 in items)
    print("9 not in [1,2,3] ->", 9 not in items)
    print("'e' in 'hello' ->", "e" in text)
    print("2 in {1,2,3} ->", 2 in s)

    show("2) dict 的 in：检查 key")
    m = {"a": 1, "b": 2}
    print("'a' in m ->", "a" in m)
    print("1 in m ->", 1 in m, "（不会检查 value）")
    print("1 in m.values() ->", 1 in m.values())

    show("3) is / is not（身份）")
    a = [1, 2]
    b = [1, 2]
    c = a
    print("a == b ->", a == b)
    print("a is b ->", a is b)
    print("a is c ->", a is c)
    x = None
    print("x is None ->", x is None)
    print("x is not None ->", x is not None)
    print("x == None ->", x == None)  # noqa: E711（示例：不推荐写法）


if __name__ == "__main__":
    main()
