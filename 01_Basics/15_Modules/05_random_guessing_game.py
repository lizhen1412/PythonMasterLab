#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：随机小游戏（猜数字）。
Author: Lambert

- 目标数使用 random 生成
- 演示交互流程；这里用“预置猜测序列”模拟输入，便于自动运行
"""

from __future__ import annotations

import random
from typing import Iterable


def guess_number(target: int, guesses: Iterable[int]) -> int:
    """
    猜数字核心逻辑。
    返回猜中的次数（失败则返回 len(guesses)）。
    """
    for attempt, value in enumerate(guesses, start=1):
        if value == target:
            print(f"第 {attempt} 次猜中！答案是 {value}")
            return attempt
        hint = "偏大" if value > target else "偏小"
        print(f"第 {attempt} 次猜 {value} -> {hint}")
    print("没有猜中，游戏结束。")
    return attempt  # type: ignore[has-type]


def main() -> None:
    random.seed(7)
    target = random.randint(1, 20)
    simulated_guesses = [10, 3, 15, target]  # 最后一次一定猜中

    print("生成的答案（调试用） ->", target)
    attempts = guess_number(target, simulated_guesses)
    print("总尝试次数 ->", attempts)
    print("提示：将 simulated_guesses 换成 input() 循环即可变成交互版。")


if __name__ == "__main__":
    main()