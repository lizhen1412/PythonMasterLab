#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：collections.namedtuple。
Author: Lambert

你会学到：
1) namedtuple 创建轻量记录类型
2) 支持属性访问与解包
3) 不可变，但可用 _replace 创建新实例

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/06_collections_namedtuple.py
"""

from collections import namedtuple


def main() -> None:
    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print("point ->", p)
    print("p.x ->", p.x)
    print("p.y ->", p.y)
    print("asdict ->", p._asdict())

    p2 = p._replace(x=10)
    print("replace ->", p2)


if __name__ == "__main__":
    main()