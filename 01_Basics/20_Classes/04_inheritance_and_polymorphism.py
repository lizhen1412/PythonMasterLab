#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：继承与多态（重写、super、isinstance）。

你会学到：
1) 子类重写父类方法
2) super() 调用父类初始化逻辑
3) 多态：同一个接口，不同实现

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/04_inheritance_and_polymorphism.py
"""

from __future__ import annotations


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."

    def info(self) -> str:
        return f"{self.name}: {self.speak()}"


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        return "woof"


class Cat(Animal):
    def speak(self) -> str:
        return "meow"


def main() -> None:
    pets: list[Animal] = [Dog("Lucky", "Corgi"), Cat("Mimi"), Animal("Mystery")]
    for pet in pets:
        print(pet.info())

    print("isinstance(pets[0], Animal) ->", isinstance(pets[0], Animal))
    print("issubclass(Dog, Animal) ->", issubclass(Dog, Animal))


if __name__ == "__main__":
    main()
