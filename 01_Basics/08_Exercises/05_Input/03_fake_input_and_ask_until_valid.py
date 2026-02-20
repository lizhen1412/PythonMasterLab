#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：依赖注入 input（fake_input + 校验重试）
Author: Lambert

题目：
1) 实现 `make_fake_input(items)`：返回一个函数，可替代 `input()`（每次返回下一条预置输入）
2) 实现 `ask_until_valid(prompt, input_func, parse_func)`：解析失败就重试

参考答案：
- 本文件函数实现即参考答案；`main()` 用 fake_input 做自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/05_Input/03_fake_input_and_ask_until_valid.py
"""

from collections.abc import Callable


InputFunc = Callable[[str], str]


def make_fake_input(items: list[str]) -> InputFunc:
    it = iter(items)

    def _fake(prompt: str = "") -> str:
        _ = prompt
        return next(it)

    return _fake


def parse_int(text: str) -> int | None:
    try:
        return int(text.strip())
    except ValueError:
        return None


def ask_until_valid(prompt: str, input_func: InputFunc, parse_func):
    while True:
        raw = input_func(prompt)
        value = parse_func(raw)
        if value is not None:
            return value


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    fake = make_fake_input(["x", "  42  "])
    age = ask_until_valid("age> ", fake, parse_int)
    check("age", age, 42)


if __name__ == "__main__":
    main()
