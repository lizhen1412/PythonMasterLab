#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：把“读输入”写得可测试（专业工程写法）。

很多新手写输入代码会把 `input()` 散落在各处，导致：
- 不好测试（只能人工敲键盘）
- 逻辑/IO 混在一起，难维护

你会学到：
1) 把“业务逻辑”写成函数，把 `input()` 作为依赖注入（input_func 参数）
2) 用一个假的 input 函数（从列表依次取值）来模拟用户输入
3) 这样你就能在不敲键盘的情况下验证逻辑

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/11_testable_input_functions.py
"""

from __future__ import annotations

from collections.abc import Callable, Iterator


InputFunc = Callable[[str], str]


def make_fake_input(lines: list[str]) -> InputFunc:
    it: Iterator[str] = iter(lines)

    def fake_input(prompt: str) -> str:
        # 打印 prompt，模拟真实 input() 的交互感（不强求完全一致）
        print(prompt, end="")
        try:
            value = next(it)
        except StopIteration:
            raise EOFError("no more fake input")
        print(value)
        return value

    return fake_input


def ask_user_profile(input_func: InputFunc) -> tuple[str, int]:
    name = input_func("name: ").strip() or "Anonymous"

    while True:
        raw_age = input_func("age (int): ").strip()
        try:
            age = int(raw_age)
        except ValueError:
            print("age 必须是整数，请重试。")
            continue
        return name, age


def main() -> None:
    print("1) 用 fake_input 演示（不需要你敲键盘）：")
    fake = make_fake_input(["Alice", "not int", "20"])
    name, age = ask_user_profile(fake)
    print("result =", (name, age))

    print("\n2) 真实交互：你也可以把 input 传进去：")
    try:
        name2, age2 = ask_user_profile(input)
        print("result =", (name2, age2))
    except (EOFError, KeyboardInterrupt):
        print("\n退出。")


if __name__ == "__main__":
    main()

