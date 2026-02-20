#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：range 的边界与易错点（空区间/负步长/切片/相等比较）
Author: Lambert

你会学到：
1) 空 range 的判断与 len 行为
2) step 不能为 0（会抛 ValueError）
3) 负步长的区间方向与成员测试
4) 切片仍是 range（支持负步长）
5) count/index 的差异：count 返回 0，index 抛 ValueError
6) range 的相等比较按“序列值”判断（空序列也相等）

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/13_range_edge_cases.py
"""

from __future__ import annotations

from collections.abc import Callable


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo(label: str, value: object) -> None:
    print(f"{label:<30} -> {value!r}")


def try_demo(label: str, func: Callable[[], object]) -> None:
    try:
        value = func()
    except Exception as exc:
        print(f"{label:<30} -> {type(exc).__name__}: {exc}")
        return
    demo(label, value)


def main() -> None:
    show("1) 空 range 与方向")
    r1 = range(5, 5)
    demo("range(5, 5)", list(r1))
    demo("len(range(5, 5))", len(r1))
    r2 = range(5, 2)
    demo("range(5, 2)", list(r2))
    r3 = range(5, 2, -1)
    demo("range(5, 2, -1)", list(r3))

    show("2) step=0 会报错")
    try_demo("range(0, 5, 0)", lambda: range(0, 5, 0))

    show("3) 负步长与成员测试")
    r = range(10, 0, -3)
    demo("r", list(r))
    demo("10 in r", 10 in r)
    demo("7 in r", 7 in r)
    demo("1 in r", 1 in r)
    demo("0 in r", 0 in r)

    show("4) 切片仍是 range")
    r = range(0, 10, 2)
    sub = r[1:4]
    demo("r", r)
    demo("r[1:4]", sub)
    demo("list(r[1:4])", list(sub))
    rev = r[::-1]
    demo("r[::-1]", rev)
    demo("list(r[::-1])", list(rev))
    demo("r[::2]", r[::2])

    show("5) count/index 的行为")
    demo("r.count(4)", r.count(4))
    demo("r.count(5)", r.count(5))
    demo("r.index(4)", r.index(4))
    try_demo("r.index(5)", lambda: r.index(5))

    show("6) range 的相等比较")
    demo("range(0, 3) == range(3)", range(0, 3) == range(3))
    demo("range(0, 3) == range(0, 4)", range(0, 3) == range(0, 4))
    demo("range(0, 0) == range(5, 5)", range(0, 0) == range(5, 5))


if __name__ == "__main__":
    main()