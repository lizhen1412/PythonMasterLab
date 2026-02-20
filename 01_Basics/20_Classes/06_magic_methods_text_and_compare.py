#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：文本/比较相关的魔法方法。
Author: Lambert

你会学到：
1) __repr__ / __str__ 控制对象展示
2) __format__ 自定义格式化
3) __eq__ / __lt__ / __hash__ 影响比较与集合行为

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/06_magic_methods_text_and_compare.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Product:
    def __init__(self, pid: int, name: str, price: float) -> None:
        self.pid = pid
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"Product(pid={self.pid!r}, name={self.name!r}, price={self.price!r})"

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"

    def __format__(self, spec: str) -> str:
        if spec in {"", "str"}:
            return str(self)
        if spec == "brief":
            return self.name
        return f"{self.name}:{format(self.price, spec)}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.pid == other.pid

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __hash__(self) -> int:
        return hash(self.pid)


def main() -> None:
    p1 = Product(1, "Apple", 3.5)
    p2 = Product(1, "Apple X", 4.0)
    p3 = Product(2, "Banana", 1.2)

    show("1) __repr__ / __str__ / __format__")
    print("repr(p1) ->", repr(p1))
    print("str(p1)  ->", str(p1))
    print("format brief ->", f"{p1:brief}")
    print("format price ->", f"{p1:.2f}")

    show("2) __eq__ / __lt__ / __hash__")
    print("p1 == p2 ->", p1 == p2)
    print("sorted by price ->", sorted([p1, p3]))
    print("set size ->", len({p1, p2, p3}))


if __name__ == "__main__":
    main()