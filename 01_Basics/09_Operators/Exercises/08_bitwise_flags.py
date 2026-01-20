#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：flags（位标志）

题目：
用位运算实现一套“权限 flags”，并实现三个函数：
1) `enable(flags, mask)`：开启某个/某些标志位（用 |）
2) `disable(flags, mask)`：关闭某个/某些标志位（用 & 与 ~）
3) `has(flags, mask)`：判断是否包含某个/某些标志位（用 &）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/09_Operators/Exercises/08_bitwise_flags.py
"""

from __future__ import annotations


READ = 1 << 0
WRITE = 1 << 1
EXEC = 1 << 2


def enable(flags: int, mask: int) -> int:
    return flags | mask


def disable(flags: int, mask: int) -> int:
    return flags & ~mask


def has(flags: int, mask: int) -> bool:
    return (flags & mask) == mask


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    perms = 0
    perms = enable(perms, READ | EXEC)
    check("has_read", has(perms, READ), True)
    check("has_exec", has(perms, EXEC), True)
    check("has_write", has(perms, WRITE), False)

    perms = enable(perms, WRITE)
    check("has_write_after_enable", has(perms, WRITE), True)

    perms = disable(perms, EXEC)
    check("exec_disabled", has(perms, EXEC), False)
    check("read_still", has(perms, READ), True)


if __name__ == "__main__":
    main()

