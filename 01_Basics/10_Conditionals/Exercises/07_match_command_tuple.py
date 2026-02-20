#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：match（解析命令元组）
Author: Lambert

题目：
实现 `eval_command(cmd)`，支持：
- ("add", a, b) -> a + b
- ("mul", a, b) -> a * b
- ("neg", x)    -> -x

要求：
- 使用 match/case
- 对 a/b/x 仅接受 int（用 `int() as n` 形式匹配）
- 不支持的命令抛 ValueError

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/10_Conditionals/Exercises/07_match_command_tuple.py
"""

from __future__ import annotations


def eval_command(cmd: object) -> int:
    match cmd:
        case ("add", int() as a, int() as b):
            return a + b
        case ("mul", int() as a, int() as b):
            return a * b
        case ("neg", int() as x):
            return -x
        case _:
            raise ValueError(f"unsupported command: {cmd!r}")


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("add", eval_command(("add", 2, 3)), 5)
    check("mul", eval_command(("mul", 2, 3)), 6)
    check("neg", eval_command(("neg", 2)), -2)
    try:
        _ = eval_command(("add", "2", 3))
    except ValueError:
        print("[OK] invalid args -> ValueError")
    try:
        _ = eval_command(("unknown", 1, 2))
    except ValueError:
        print("[OK] unknown cmd -> ValueError")


if __name__ == "__main__":
    main()
