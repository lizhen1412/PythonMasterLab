#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：作用域与生命周期（变量在哪可见、什么时候消失）。
Author: Lambert

你会学到：
1) LEGB：Local / Enclosing / Global / Builtins
2) `global` / `nonlocal`：修改外层绑定时才需要
3) `del name` 删除的是“名字绑定”，不是“强制销毁对象”
4) `globals()` / `locals()`：名字表（dict）

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/08_scope_and_lifetime.py
"""

from __future__ import annotations


GLOBAL_X = "global x"


def demo_legb() -> None:
    outer = "outer"

    def inner() -> None:
        local = "local"
        print("GLOBAL_X =", GLOBAL_X)
        print("outer =", outer)
        print("local =", local)

    inner()


def demo_nonlocal() -> None:
    count = 0

    def inc() -> int:
        nonlocal count
        count += 1
        return count

    print("nonlocal demo:", inc(), inc(), inc())


def demo_global() -> None:
    global GLOBAL_X
    GLOBAL_X = "changed global x"


def demo_del() -> None:
    data = [1, 2, 3]
    alias = data
    print("before del, data =", data, "alias =", alias)
    del data
    print("after del data, alias still =", alias)


def main() -> None:
    print("1) LEGB：")
    demo_legb()

    print("\n2) nonlocal：")
    demo_nonlocal()

    print("\n3) global：")
    print("GLOBAL_X before =", GLOBAL_X)
    demo_global()
    print("GLOBAL_X after  =", GLOBAL_X)

    print("\n4) del：")
    demo_del()

    print("\n5) globals/locals：")
    print("globals has GLOBAL_X ->", "GLOBAL_X" in globals())
    local_vars = locals()
    print("locals keys sample ->", sorted(k for k in local_vars.keys() if not k.startswith("__"))[:10])


if __name__ == "__main__":
    main()
