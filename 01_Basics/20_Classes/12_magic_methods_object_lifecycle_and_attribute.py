#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：对象生命周期与属性访问（__new__/__del__/__getattribute__）。
Author: Lambert

你会学到：
1) __new__ 创建实例、__init__ 初始化
2) __del__ 作为“析构提示”（不保证立即执行）
3) __getattribute__ 拦截所有属性访问

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/12_magic_methods_object_lifecycle_and_attribute.py
"""

from __future__ import annotations

import gc


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Order:
    def __new__(cls, code: str) -> "Order":
        print("Order.__new__")
        return super().__new__(cls)

    def __init__(self, code: str) -> None:
        print("Order.__init__")
        self.code = code


class Spy:
    def __init__(self, value: int) -> None:
        self.value = value

    def __getattribute__(self, name: str):
        if name.startswith("_"):
            return super().__getattribute__(name)
        print(f"__getattribute__ -> {name}")
        return super().__getattribute__(name)


class Tracer:
    def __del__(self) -> None:
        print("Tracer.__del__ called")


def main() -> None:
    show("1) __new__ 与 __init__ 的调用顺序")
    order = Order("A001")
    print("order.code ->", order.code)

    show("2) __getattribute__ 拦截属性访问")
    s = Spy(42)
    print("s.value ->", s.value)

    show("3) __del__ 的调用时机不确定")
    t = Tracer()
    del t
    gc.collect()
    print("del 后可能看到 __del__ 输出，但不保证时机")


if __name__ == "__main__":
    main()