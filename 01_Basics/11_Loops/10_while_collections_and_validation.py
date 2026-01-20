#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：while 的容器处理与校验模式（stack/queue/验证循环）

你会学到：
1) while + 容器真值：常用于“处理到为空”为止
2) list 当栈（LIFO），deque 当队列（FIFO）
3) 校验/重试模式：while True + try/except + continue/break
4) 多条件 while：边扫描边累计，满足条件才继续

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/10_while_collections_and_validation.py
"""

from __future__ import annotations

from collections import deque


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) while + list：当栈（LIFO）")
    stack = [1, 2, 3]
    while stack:
        value = stack.pop()
        print("pop ->", value, "stack ->", stack)

    show("2) while + deque：当队列（FIFO）")
    queue: deque[str] = deque(["A", "B", "C"])
    while queue:
        value = queue.popleft()
        print("popleft ->", value, "queue ->", list(queue))

    show("3) 校验/重试：while True + try/except")
    inputs = ["x", "  ", "-3", "8", "q"]
    it = iter(inputs)
    while True:
        raw = next(it, "q")
        if raw == "q":
            print("quit")
            break
        raw = raw.strip()
        if not raw:
            print("blank -> skip")
            continue
        try:
            n = int(raw)
        except ValueError:
            print("invalid ->", raw)
            continue
        if n <= 0:
            print("non-positive ->", n)
            continue
        print("ok ->", n)
        break

    show("4) 多条件 while：扫描 + 累计上限")
    nums = [5, 3, 7, 2, 1]
    limit = 10
    total = 0
    i = 0
    while i < len(nums) and total + nums[i] <= limit:
        total += nums[i]
        i += 1
    print("nums ->", nums, "limit ->", limit)
    print("stopped at index ->", i, "total ->", total)


if __name__ == "__main__":
    main()
