#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：match 进阶（序列/映射/类模式、as、*star）
Author: Lambert

你会学到：
1) 序列模式：`case [x, y]`、`case [head, *tail]`
2) 映射模式：`case {"type": "user", "id": user_id}`、`case {"type": t, **rest}`
3) 类模式：`case Point(x, y)` 与关键字属性匹配 `Point(x=0, y=y)`
4) `as`：同时拿到“整体对象”与“解构后的部分”

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/08_match_structural_patterns.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def parse_point(obj: object) -> Point | None:
    match obj:
        case Point(x, y):
            return Point(x, y)
        case [x, y]:
            return Point(int(x), int(y))
        case {"x": x, "y": y}:
            return Point(int(x), int(y))
        case _:
            return None


def describe(obj: object) -> str:
    match obj:
        case [x, y]:
            return f"2-item sequence: x={x!r} y={y!r}"
        case [head, *tail]:
            return f"sequence: head={head!r} tail={tail!r}"
        case {"type": "user", "id": user_id, **rest}:
            return f"user(id={user_id!r}) rest={rest!r}"
        case Point(x=0, y=y) as p0:
            return f"point_on_y_axis: {p0!r} y={y}"
        case int() as n if n % 2 == 0:
            return f"even int: {n}"
        case _:
            return f"unknown: {obj!r}"


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) parse_point：支持 class/sequence/mapping 三种输入")
    for item in [Point(1, 2), [3, 4], {"x": "5", "y": 6}, "bad"]:
        print(item, "->", parse_point(item))

    show("2) describe：展示多种结构化模式")
    samples: list[object] = [
        [1, 2],
        [1, 2, 3, 4],
        {"type": "user", "id": 7, "name": "Alice"},
        Point(0, 9),
        10,
        "x",
    ]
    for s in samples:
        print(describe(s))


if __name__ == "__main__":
    main()
