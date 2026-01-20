#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：别名陷阱（a = b = []）

题目：
1) 写出“错误示例”：`a = b = []`，修改 a 会影响 b（因为同一个 list）
2) 写出“正确写法”：`a, b = [], []`，a 与 b 相互独立

参考答案：
- 本文件实现即参考答案；`main()` 用最小自测展示两种写法的差异。

运行：
    python3 01_Basics/08_Exercises/02_Variables/03_aliasing_and_chained_assignment.py
"""


def make_aliasing_pair() -> tuple[list[int], list[int]]:
    a = b = []
    return a, b


def make_independent_pair() -> tuple[list[int], list[int]]:
    a, b = [], []
    return a, b


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    a1, b1 = make_aliasing_pair()
    a1.append(1)
    check("aliasing_a", a1, [1])
    check("aliasing_b", b1, [1])
    check("aliasing_same_object", a1 is b1, True)

    a2, b2 = make_independent_pair()
    a2.append(1)
    check("independent_a", a2, [1])
    check("independent_b", b2, [])
    check("independent_same_object", a2 is b2, False)


if __name__ == "__main__":
    main()

