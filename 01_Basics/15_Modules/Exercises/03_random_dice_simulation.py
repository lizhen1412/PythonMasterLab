#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：随机掷骰子模拟。

要求：
- 掷 10_000 次六面骰，统计每个点数出现次数与占比
- 可选：设定种子便于复现
"""

from __future__ import annotations

import random
from collections import Counter


def simulate_dice(times: int = 10_000) -> Counter[int]:
    random.seed(123)
    rolls = [random.randint(1, 6) for _ in range(times)]
    return Counter(rolls)


def main() -> None:
    stats = simulate_dice()
    total = sum(stats.values())
    for face in range(1, 7):
        count = stats[face]
        ratio = count / total * 100
        print(f"{face}: {count} ({ratio:.2f}%)")


if __name__ == "__main__":
    main()
