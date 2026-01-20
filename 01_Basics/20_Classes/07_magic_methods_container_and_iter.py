#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：容器与迭代相关的魔法方法。

你会学到：
1) __len__ / __getitem__ / __setitem__ / __contains__
2) __iter__ 与 for 循环
3) __next__ 与 StopIteration

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/07_magic_methods_container_and_iter.py
"""

from __future__ import annotations

from collections.abc import Iterator


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Bag:
    def __init__(self, items: list[str]) -> None:
        self._items = list(items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> str:
        return self._items[index]

    def __setitem__(self, index: int, value: str) -> None:
        self._items[index] = value

    def __contains__(self, item: str) -> bool:
        return item in self._items

    def __iter__(self) -> Iterator[str]:
        return iter(self._items)


class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class Switch:
    def __init__(self, on: bool) -> None:
        self.on = on

    def __bool__(self) -> bool:
        return self.on


def main() -> None:
    show("1) Bag：容器协议")
    bag = Bag(["apple", "banana", "cherry"])
    print("len(bag) ->", len(bag))
    print("bag[1] ->", bag[1])
    bag[1] = "blueberry"
    print("bag[1] after set ->", bag[1])
    print("'apple' in bag ->", "apple" in bag)
    print("list(bag) ->", list(bag))
    print("bool(bag) ->", bool(bag))

    show("2) Countdown：迭代器协议")
    counter = Countdown(3)
    print("next(counter) ->", next(counter))
    print("remaining ->", list(counter))

    show("3) __bool__ 控制真值")
    print("bool(Switch(True)) ->", bool(Switch(True)))
    print("bool(Switch(False)) ->", bool(Switch(False)))


if __name__ == "__main__":
    main()
