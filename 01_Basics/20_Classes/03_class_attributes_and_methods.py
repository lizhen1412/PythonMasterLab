#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：类属性/实例属性、classmethod/staticmethod、@property。
Author: Lambert

你会学到：
1) 类属性与实例属性的差异（共享 vs 每个实例独有）
2) @classmethod 操作“类本身”
3) @staticmethod 只是“放在类里的函数”
4) @property 用于校验与派生属性

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/03_class_attributes_and_methods.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Counter:
    total_created = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Counter.total_created += 1

    @classmethod
    def reset_total(cls) -> None:
        cls.total_created = 0

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return bool(name.strip())


class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32


def main() -> None:
    show("1) 类属性 vs 实例属性")
    print("Counter.total_created ->", Counter.total_created)
    a = Counter("A")
    b = Counter("B")
    print("Counter.total_created ->", Counter.total_created)
    print("a.total_created ->", a.total_created)

    a.total_created = 99
    print("a.total_created (instance) ->", a.total_created)
    print("Counter.total_created ->", Counter.total_created)
    del a.total_created
    print("a.total_created (back to class) ->", a.total_created)

    Counter.reset_total()
    print("Counter.total_created (reset) ->", Counter.total_created)
    print("is_valid_name('  ') ->", Counter.is_valid_name("  "))

    show("2) @property 做校验与派生属性")
    t = Temperature(25.0)
    print("celsius ->", t.celsius)
    print("fahrenheit ->", t.fahrenheit)
    try:
        t.celsius = -300.0
    except ValueError as exc:
        print("ValueError:", exc)


if __name__ == "__main__":
    main()