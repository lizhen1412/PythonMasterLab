#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：逻辑运算符（Logical Operators）
Author: Lambert

你会学到：
1) `and / or / not` 的真值逻辑与短路（short-circuit）
2) `and/or` 返回的是“参与运算的对象”，不一定是 bool
3) 常见坑：`x or default` 不是 “None 合并”（0/""/False 会误触发）

运行（在仓库根目录执行）：
    python3 01_Basics/09_Operators/05_logical_operators.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def probe(name: str, value: object) -> object:
    print(f"probe({name}) called")
    return value


def coalesce_none(value: object, default: object) -> object:
    return default if value is None else value


def main() -> None:
    show("1) 真值测试（truthiness）")
    samples: list[object] = [None, False, True, 0, 1, "", "hi", [], [1]]
    for s in samples:
        print(f"{s!r:<8} -> bool={bool(s)}")

    show("1.1) not：取反")
    print("not True ->", not True)
    print("not 0 ->", not 0)
    print("not [] ->", not [])
    print("not (1 < 2) ->", not (1 < 2))

    show("1.2) and / or 真值表")
    pairs = [(False, False), (False, True), (True, False), (True, True)]
    for a, b in pairs:
        print(f"{a} and {b} -> {a and b} | {a} or {b} -> {a or b}")

    show("2) 短路：and/or 不一定会执行右侧")
    print("False and probe('R', 123) ->", False and probe("R", 123))
    print("True  or  probe('R', 123) ->", True or probe("R", 123))
    print("True and probe('R', 123) ->", True and probe("R", 123))
    print("False or  probe('R', 123) ->", False or probe("R", 123))

    show("3) 返回值：and/or 返回的是对象")
    print("0 or 99 ->", 0 or 99)
    print("'' or 'fallback' ->", "" or "fallback")
    print("'hi' and 123 ->", "hi" and 123)
    print("[] and 123 ->", [] and 123)

    show("4) 常见坑：or 不是 None 合并")
    print("0 or 10 ->", 0 or 10, "（0 被当成 False）")
    print("coalesce_none(0, 10) ->", coalesce_none(0, 10))
    print("coalesce_none(None, 10) ->", coalesce_none(None, 10))


if __name__ == "__main__":
    main()