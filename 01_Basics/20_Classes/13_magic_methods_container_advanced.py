#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：容器协议进阶（__delitem__/__reversed__）。
Author: Lambert

你会学到：
1) del obj[i] 触发 __delitem__
2) reversed(obj) 触发 __reversed__

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/13_magic_methods_container_advanced.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Deck:
    def __init__(self, cards: list[str]) -> None:
        self._cards = list(cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __delitem__(self, index) -> None:
        del self._cards[index]

    def __reversed__(self):
        return reversed(self._cards)


def main() -> None:
    show("1) __delitem__")
    deck = Deck(["A", "K", "Q", "J"])
    print("before ->", deck._cards)
    del deck[1]
    print("after  ->", deck._cards)

    show("2) __reversed__")
    print("reversed ->", list(reversed(deck)))


if __name__ == "__main__":
    main()