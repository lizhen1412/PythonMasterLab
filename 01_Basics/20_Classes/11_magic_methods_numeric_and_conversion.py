#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：数值运算与类型转换相关的魔法方法。

你会学到：
1) 数值运算：__add__/__sub__/__mul__/__truediv__/__floordiv__/__mod__/__pow__
2) 类型转换：__int__/__float__/__complex__/__index__
3) 其他协议：__bytes__/__fspath__

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/11_magic_methods_numeric_and_conversion.py
"""

from __future__ import annotations

import os


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class NumberBox:
    def __init__(self, value: float) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"NumberBox({self.value!r})"

    def _coerce(self, other: object) -> float | None:
        if isinstance(other, NumberBox):
            return other.value
        if isinstance(other, (int, float)):
            return float(other)
        return None

    def __add__(self, other: object) -> "NumberBox":
        other_value = self._coerce(other)
        if other_value is None:
            return NotImplemented
        return NumberBox(self.value + other_value)

    def __radd__(self, other: object) -> "NumberBox":
        return self.__add__(other)

    def __sub__(self, other: object) -> "NumberBox":
        other_value = self._coerce(other)
        if other_value is None:
            return NotImplemented
        return NumberBox(self.value - other_value)

    def __mul__(self, other: object) -> "NumberBox":
        other_value = self._coerce(other)
        if other_value is None:
            return NotImplemented
        return NumberBox(self.value * other_value)

    def __truediv__(self, other: object) -> "NumberBox":
        other_value = self._coerce(other)
        if other_value is None:
            return NotImplemented
        return NumberBox(self.value / other_value)

    def __floordiv__(self, other: object) -> "NumberBox":
        other_value = self._coerce(other)
        if other_value is None:
            return NotImplemented
        return NumberBox(self.value // other_value)

    def __mod__(self, other: object) -> "NumberBox":
        other_value = self._coerce(other)
        if other_value is None:
            return NotImplemented
        return NumberBox(self.value % other_value)

    def __pow__(self, other: object) -> "NumberBox":
        other_value = self._coerce(other)
        if other_value is None:
            return NotImplemented
        return NumberBox(self.value**other_value)

    def __int__(self) -> int:
        return int(self.value)

    def __float__(self) -> float:
        return float(self.value)

    def __complex__(self) -> complex:
        return complex(self.value)

    def __index__(self) -> int:
        return int(self.value)


class Packet:
    def __init__(self, payload: str) -> None:
        self.payload = payload

    def __bytes__(self) -> bytes:
        return self.payload.encode("utf-8")


class FileRef:
    def __init__(self, path: str) -> None:
        self.path = path

    def __fspath__(self) -> str:
        return self.path


def main() -> None:
    show("1) 数值运算")
    a = NumberBox(10)
    b = NumberBox(3)
    print("a + b ->", a + b)
    print("a - 2 ->", a - 2)
    print("a * b ->", a * b)
    print("a / b ->", a / b)
    print("a // b ->", a // b)
    print("a % b ->", a % b)
    print("a ** 2 ->", a**2)
    print("2 + a ->", 2 + a)

    show("2) 类型转换协议")
    print("int(a) ->", int(a))
    print("float(a) ->", float(a))
    print("complex(a) ->", complex(a))
    items = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    print("items[a] ->", items[a])
    print("bin(a) ->", bin(a))

    show("3) __bytes__ / __fspath__")
    packet = Packet("hello")
    print("bytes(packet) ->", bytes(packet))
    ref = FileRef("data/report.txt")
    print("os.fspath(ref) ->", os.fspath(ref))


if __name__ == "__main__":
    main()
