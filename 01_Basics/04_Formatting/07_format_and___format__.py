#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：format() 与 __format__ ——格式化是怎么“落到对象身上”的。

关键认知：
1) `format(value, spec)` 会调用 `value.__format__(spec)`
2) f-string 里的 `{value:spec}` 本质上也会走 `format(value, spec)`
3) 你可以为自定义类实现 `__format__` 来支持自己的格式化规则

运行：
    python3 01_Basics/04_Formatting/07_format_and___format__.py
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __format__(self, spec: str) -> str:
        # spec 为空：默认格式
        if spec == "":
            return f"({self.x}, {self.y})"

        # 支持两种自定义 spec：
        # - "cart": 笛卡尔坐标（默认）
        # - "tuple:.2f": 指定数值格式（只做演示，不追求极致通用）
        if spec == "cart":
            return f"({self.x}, {self.y})"

        if spec.startswith("tuple:"):
            number_spec = spec.removeprefix("tuple:")
            return f"({format(self.x, number_spec)}, {format(self.y, number_spec)})"

        raise ValueError(f"Unsupported format spec for Point: {spec!r}")


def main() -> None:
    p = Point(1.23456, 7.89)

    print("1) format(p, '') ->", format(p, ""))
    print("2) f-string default ->", f"{p}")
    print("3) custom spec 'cart' ->", f"{p:cart}")
    print("4) custom spec 'tuple:.2f' ->", f"{p:tuple:.2f}")

    print("\n5) 反例：不支持的 spec（捕获异常演示）：")
    try:
        print(f"{p:unknown}")
    except ValueError as exc:
        print("ValueError:", exc)


if __name__ == "__main__":
    main()

