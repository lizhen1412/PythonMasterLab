#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：嵌套选择 vs 卫语句（实现 can_upload）

题目：
实现 `can_upload_guard(user, size_mb)`，规则：
- user 为 None -> False
- user.is_active 为 False -> False
- user.is_admin 为 True -> True（管理员无限制）
- 否则：size_mb <= user.quota_mb 才允许上传

要求：
- 用“卫语句”（不满足条件就提前 return），尽量避免深层嵌套

参考答案：
- 本文件 `can_upload_guard` 的实现即为参考答案；
  同时保留一个 `can_upload_nested` 作为对照；`main()` 会比较两者结果一致性。

运行：
    python3 01_Basics/10_Conditionals/Exercises/06_nested_vs_guard_access.py
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


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    users = [
        None,
        User("Alice", is_active=True, is_admin=False, quota_mb=10),
        User("Bob", is_active=False, is_admin=False, quota_mb=10),
        User("Root", is_active=True, is_admin=True, quota_mb=0),
    ]
    for u in users:
        for size in [1, 20]:
            check(
                f"user={getattr(u, 'name', None)!r}_size={size}",
                can_upload_guard(u, size),
                can_upload_nested(u, size),
            )


if __name__ == "__main__":
    main()

