#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11：猜数字（while + break + continue + while-else）

题目：
实现 `play(secret, guesses, max_attempts=5)`，规则：
- guesses 是一串“输入”（object），其中只有 int 才算“有效猜测”
- 有效猜测会消耗一次尝试次数；无效输入跳过（用 continue）
- 有效猜测：
  - 等于 secret -> WIN（并 break）
  - 不等于 secret -> 继续猜，直到尝试用完
- 如果尝试次数用完仍未猜中 -> LOSE（用 while-else 表达“没 break”）

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/11_Loops/Exercises/11_guess_number_simulated.py
"""

from __future__ import annotations


def play(secret: int, guesses: list[object], max_attempts: int = 5) -> str:
    attempt = 0
    i = 0
    while attempt < max_attempts and i < len(guesses):
        raw = guesses[i]
        i += 1
        if not isinstance(raw, int):
            continue

        attempt += 1
        if raw == secret:
            break
    else:
        return "LOSE"
    return "WIN"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("win", play(7, [None, "x", 3, 9, 7], max_attempts=3), "WIN")
    check("lose", play(7, [1, 2, 3, 4], max_attempts=3), "LOSE")
    check("invalid_only", play(7, [None, "x"], max_attempts=3), "LOSE")


if __name__ == "__main__":
    main()

