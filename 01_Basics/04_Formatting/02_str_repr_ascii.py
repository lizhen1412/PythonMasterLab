#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：str / repr / ascii ——“打印给谁看”的第一原则。

你会学到：
1) `str(obj)`：面向用户/界面的可读文本（print 默认用它）
2) `repr(obj)`：面向开发者的“尽量不丢信息”的表示（调试/日志常用）
3) `ascii(obj)`：类似 repr，但会把非 ASCII 字符转义（便于在纯 ASCII 环境里查看）
4) f-string 里可以用 `!s`/`!r`/`!a` 强制选择

运行：
    python3 01_Basics/04_Formatting/02_str_repr_ascii.py
"""

from dataclasses import dataclass


@dataclass
class User:
    name: str
    city: str

    def __str__(self) -> str:
        return f"{self.name} from {self.city}"

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, city={self.city!r})"


def main() -> None:
    u = User(name="Alice", city="北京")
    text = "hello\n世界"

    print("1) print(u) 默认用 str(u)：")
    print(u)

    print("\n2) repr(u) 更适合调试：")
    print(repr(u))

    print("\n3) ascii(text) 会把非 ASCII 字符转义：")
    print("text =", text)
    print("repr =", repr(text))
    print("ascii=", ascii(text))

    print("\n4) f-string 的 !s/!r/!a：")
    print(f"{u!s}")
    print(f"{u!r}")
    print(f"{u!a}")
    print(f"{text!r}")
    print(f"{text!a}")


if __name__ == "__main__":
    main()

