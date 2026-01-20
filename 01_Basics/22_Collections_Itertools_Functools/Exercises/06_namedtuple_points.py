#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：namedtuple 表示点。

题目：
使用 namedtuple 定义 Point(x, y)，实现函数 `distance(p)`：
- 返回点到原点的距离

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/06_namedtuple_points.py
"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def distance(p: Point) -> float:
    return (p.x ** 2 + p.y ** 2) ** 0.5


def check(label: str, got: object, expected: object) -> None:
    ok = abs(got - expected) < 1e-9
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("(3,4)", distance(Point(3, 4)), 5.0)
    check("(0,0)", distance(Point(0, 0)), 0.0)


if __name__ == "__main__":
    main()
