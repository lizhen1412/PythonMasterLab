#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：输入校验与重试（让程序“专业好用”）。

你会学到：
1) while True + try/except：反复提示直到输入合法
2) 数值范围校验：min/max
3) 选择题：只能选某几个值
4) yes/no：解析成 bool，并支持默认值
5) 遇到 EOF/中断：优雅退出（返回默认/抛异常都可以，这里选择返回默认）

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/06_validation_loops.py
"""

from __future__ import annotations


def read_int(prompt: str, *, min_value: int | None = None, max_value: int | None = None) -> int | None:
    while True:
        try:
            raw = input(prompt).strip()
        except EOFError:
            return None
        except KeyboardInterrupt:
            print("\n输入被中断。")
            return None

        if raw == "":
            print("请输入一个整数（不能为空）。")
            continue

        try:
            value = int(raw)
        except ValueError:
            print("不是合法整数，请重试。")
            continue

        if min_value is not None and value < min_value:
            print(f"太小了：至少是 {min_value}。")
            continue
        if max_value is not None and value > max_value:
            print(f"太大了：最多是 {max_value}。")
            continue

        return value


def read_choice(prompt: str, choices: set[str]) -> str | None:
    normalized_choices = {c.strip() for c in choices}
    while True:
        try:
            raw = input(prompt).strip()
        except EOFError:
            return None
        except KeyboardInterrupt:
            print("\n输入被中断。")
            return None

        if raw in normalized_choices:
            return raw
        print(f"只能输入 {sorted(normalized_choices)} 之一，请重试。")


def read_yes_no(prompt: str, *, default: bool | None = None) -> bool | None:
    mapping = {"y": True, "yes": True, "n": False, "no": False}
    suffix = {True: " [Y/n]", False: " [y/N]", None: " [y/n]"}[default]
    while True:
        try:
            raw = input(prompt + suffix + "：").strip().lower()
        except EOFError:
            return default
        except KeyboardInterrupt:
            print("\n输入被中断。")
            return default

        if raw == "" and default is not None:
            return default
        if raw in mapping:
            return mapping[raw]
        print("请输入 y/yes 或 n/no。")


def main() -> None:
    age = read_int("1) 请输入年龄（0~120）：", min_value=0, max_value=120)
    if age is None:
        print("没有拿到年龄，结束。")
        return

    level = read_choice("\n2) 请选择难度（1/2/3）：", {"1", "2", "3"})
    if level is None:
        print("没有选择难度，结束。")
        return

    ok = read_yes_no("\n3) 是否确认提交？", default=False)
    print("\n结果：")
    print("age =", age)
    print("level =", level)
    print("ok =", ok)


if __name__ == "__main__":
    main()

