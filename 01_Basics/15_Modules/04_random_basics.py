#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：random 基础。

- 随机整数、浮点、选择、打乱、采样
- 设定种子以获得可重复结果
"""

from __future__ import annotations

import random
from statistics import mean


def basic_apis() -> None:
    """常用随机 API。"""
    print("randint(1, 6) ->", random.randint(1, 6))  # 含端点
    print("random() ->", random.random())
    print("uniform(1, 3) ->", random.uniform(1, 3))
    print("choice(['🍎','🍌','🍊']) ->", random.choice(["🍎", "🍌", "🍊"]))
    print("sample(range(10), 3) ->", random.sample(range(10), 3))

    cards = ["A", "2", "3", "J", "Q", "K"]
    random.shuffle(cards)
    print("shuffle ->", cards)


def with_seed() -> None:
    """设定随机种子，结果可重复。"""
    random.seed(42)
    rolls = [random.randint(1, 6) for _ in range(5)]
    print("seed=42 骰子序列 ->", rolls)

    random.seed(42)
    again = [random.randint(1, 6) for _ in range(5)]
    print("相同种子再次生成 ->", again)
    print("两次一致?", rolls == again)


def simulate_dice(times: int = 1000) -> None:
    """小实验：掷骰子统计均值。"""
    rolls = [random.randint(1, 6) for _ in range(times)]
    print(f"{times} 次掷骰子均值 ~", round(mean(rolls), 2))


def main() -> None:
    print("== 基础 API ==")
    basic_apis()

    print("\n== 种子 ==")
    with_seed()

    print("\n== 模拟实验 ==")
    simulate_dice(200)


if __name__ == "__main__":
    main()
