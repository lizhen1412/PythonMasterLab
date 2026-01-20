#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：序列方法全覆盖（list / tuple / range）。

你会学到：
1) list 的全部常用方法
2) tuple 的 count/index
3) range 的 count/index 与 start/stop/step 属性

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/13_sequence_methods_reference.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo(label: str, value: object) -> None:
    print(f"{label:<28} -> {value!r}")


def main() -> None:
    show("1) list 方法")
    items = [3, 1, 4, 1, 5]
    demo("count(1)", items.count(1))
    demo("index(4)", items.index(4))
    demo("copy()", items.copy())

    tmp = items.copy()
    tmp.append(9)
    demo("append(9)", tmp)
    tmp = items.copy()
    tmp.extend([2, 6])
    demo("extend([2,6])", tmp)
    tmp = items.copy()
    tmp.insert(1, 99)
    demo("insert(1,99)", tmp)
    tmp = items.copy()
    tmp.remove(1)
    demo("remove(1)", tmp)
    tmp = items.copy()
    popped = tmp.pop()
    demo("pop()", popped)
    demo("after pop", tmp)
    tmp = items.copy()
    tmp.reverse()
    demo("reverse()", tmp)
    tmp = items.copy()
    tmp.sort()
    demo("sort()", tmp)
    tmp.clear()
    demo("clear()", tmp)

    show("2) tuple 方法")
    t = ("a", "b", "a")
    demo("count('a')", t.count("a"))
    demo("index('b')", t.index("b"))

    show("3) range 方法与属性")
    r = range(1, 10, 2)
    demo("start", r.start)
    demo("stop", r.stop)
    demo("step", r.step)
    demo("count(5)", r.count(5))
    demo("index(7)", r.index(7))


if __name__ == "__main__":
    main()
