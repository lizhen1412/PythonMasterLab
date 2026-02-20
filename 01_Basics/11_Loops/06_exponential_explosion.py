#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：指数爆炸（2^n 增长）——为什么循环会突然“跑不动”
Author: Lambert

你会学到：
1) 指数增长：每一步“翻倍/分叉”，总量会变成 2^n
2) powerset（子集集）：每加入一个元素，子集数量翻倍 -> 2^n
3) 实战建议：能算数量就别生成全部；n 稍大就会爆内存/爆时间

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/06_exponential_explosion.py
"""

from __future__ import annotations

from collections.abc import Iterable


def powerset(items: list[str]) -> list[list[str]]:
    subsets: list[list[str]] = [[]]
    for x in items:
        # 每加入一个元素，subsets 的数量翻倍
        subsets += [s + [x] for s in subsets]
    return subsets


def doubling_counts(steps: int) -> list[int]:
    out: list[int] = []
    value = 1
    for _ in range(steps + 1):
        out.append(value)
        value *= 2
    return out


def sum_counts(values: Iterable[int]) -> int:
    total = 0
    for v in values:
        total += v
    return total


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 直观感受：每一步翻倍（指数增长）")
    counts = doubling_counts(10)
    for day, count in enumerate(counts):
        print(f"step={day:>2} count={count}")
    print("sum(counts) ->", sum_counts(counts))

    show("2) 子集数量：2^n（n 增加一点点，结果翻倍）")
    for n in range(0, 21):
        print(f"n={n:>2} subsets={2**n}")

    show("3) 生成 powerset（只演示小 n）")
    items = ["A", "B", "C", "D"]
    ps = powerset(items)
    print("items ->", items)
    print("len(powerset) ->", len(ps), "(expected:", 2 ** len(items), ")")
    print("first 8 subsets ->", ps[:8])


if __name__ == "__main__":
    main()
