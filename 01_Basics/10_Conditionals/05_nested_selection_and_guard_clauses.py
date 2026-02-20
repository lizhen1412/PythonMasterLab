#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：嵌套选择 vs 卫语句（Guard Clauses）
Author: Lambert

你会学到：
1) 嵌套 if 会增加缩进层级，读起来更累
2) 常用替代写法：卫语句（不满足条件就提前 return/continue）
3) “先处理异常/边界条件，再处理主路径”通常更清晰

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/05_nested_selection_and_guard_clauses.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    is_active: bool
    is_admin: bool
    quota_mb: int


def can_upload_nested(user: User | None, size_mb: int) -> bool:
    if user is not None:
        if user.is_active:
            if user.is_admin:
                return True
            else:
                if size_mb <= user.quota_mb:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


def can_upload_guard(user: User | None, size_mb: int) -> bool:
    if user is None:
        return False
    if not user.is_active:
        return False
    if user.is_admin:
        return True
    if size_mb > user.quota_mb:
        return False
    return True


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 嵌套 vs 卫语句：结果一致但可读性不同")
    users = [
        None,
        User("Alice", is_active=True, is_admin=False, quota_mb=10),
        User("Bob", is_active=False, is_admin=False, quota_mb=10),
        User("Root", is_active=True, is_admin=True, quota_mb=0),
    ]
    for u in users:
        for size in [1, 20]:
            nested = can_upload_nested(u, size)
            guard = can_upload_guard(u, size)
            print(f"user={u!r:<60} size={size:<2} -> nested={nested} guard={guard}")

    show("2) 在循环里常见的卫语句：continue 过滤不需要处理的元素")
    items = ["", "  ", "Alice", "Bob"]
    out: list[str] = []
    for raw in items:
        if not raw.strip():
            continue
        out.append(raw.strip())
    print("filtered ->", out)


if __name__ == "__main__":
    main()
