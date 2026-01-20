#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：dataclass 基础用法。

你会学到：
1) 自动生成 __init__/__repr__/__eq__
2) 默认值与 default_factory 的区别
3) frozen=True 让实例“不可变”

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/05_dataclass_basics.py
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError, dataclass, field


@dataclass
class Point:
    x: float
    y: float


@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class FrozenPoint:
    x: float
    y: float


def main() -> None:
    p1 = Point(1.0, 2.0)
    p2 = Point(1.0, 2.0)
    print("p1 ->", p1)
    print("p1 == p2 ->", p1 == p2)

    u1 = User("Alice")
    u1.tags.append("vip")
    u2 = User("Bob")
    print("u1.tags ->", u1.tags)
    print("u2.tags ->", u2.tags)

    fp = FrozenPoint(3.0, 4.0)
    print("fp ->", fp)
    try:
        fp.x = 9.0  # type: ignore[misc]
    except FrozenInstanceError as exc:
        print("FrozenInstanceError:", exc)


if __name__ == "__main__":
    main()
