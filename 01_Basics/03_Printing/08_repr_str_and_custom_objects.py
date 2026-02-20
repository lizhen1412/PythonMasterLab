#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：str vs repr（对象怎么决定“打印出来长什么样”）
Author: Lambert

结论：
1) `print(obj)` 默认调用 `str(obj)`
2) 调试/日志更常用 `repr(obj)`（信息更完整）
3) 你可以在类里实现 `__str__` / `__repr__` 来控制输出

运行：
    python3 01_Basics/03_Printing/08_repr_str_and_custom_objects.py
"""

from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int

    def __str__(self) -> str:
        return f"{self.name}({self.age})"

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, age={self.age})"


def main() -> None:
    u = User("Alice", 20)

    print("1) print(u) 使用 str：")
    print(u)

    print("\n2) repr(u) 更偏向调试：")
    print(repr(u))

    print("\n3) f-string 控制：")
    print(f"as str -> {u!s}")
    print(f"as repr-> {u!r}")


if __name__ == "__main__":
    main()
