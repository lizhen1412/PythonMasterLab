#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：lambda 排序与过滤。
Author: Lambert

要求：
- 有一批记录（姓名、年龄、城市）
- 用 lambda 排序（按年龄升序），再过滤出特定城市
- 对比“命名函数”写法的可读性
"""

from __future__ import annotations


def main() -> None:
    people = [
        {"name": "Alice", "age": 30, "city": "Beijing"},
        {"name": "Bob", "age": 22, "city": "Shanghai"},
        {"name": "Charlie", "age": 28, "city": "Beijing"},
    ]

    sorted_by_age = sorted(people, key=lambda p: p["age"])
    bj_only = list(filter(lambda p: p["city"] == "Beijing", sorted_by_age))
    print("lambda ->", [p["name"] for p in bj_only])

    # 同样逻辑，用命名函数可读性更高
    def by_age(person: dict[str, object]) -> int:
        return int(person["age"])

    def is_beijing(person: dict[str, object]) -> bool:
        return person["city"] == "Beijing"

    sorted_by_age_named = sorted(people, key=by_age)
    bj_only_named = [p for p in sorted_by_age_named if is_beijing(p)]
    print("命名函数 ->", [p["name"] for p in bj_only_named])


if __name__ == "__main__":
    main()