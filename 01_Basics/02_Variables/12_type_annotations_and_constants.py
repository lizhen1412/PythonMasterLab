#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：变量类型注解（type annotations）与“常量”约定。
Author: Lambert

重要认知：
1) Python 的类型注解主要给工具（IDE/类型检查器）用；运行时不会强制类型
2) 常量在 Python 里通常是“约定”：用全大写变量名表达“请不要改”
3) `typing.Final`/`typing.ClassVar` 能更清晰地表达意图（仍主要给工具用）

运行：
    python3 01_Basics/02_Variables/12_type_annotations_and_constants.py
"""

from typing import ClassVar, Final


PI: Final[float] = 3.1415926
DEFAULT_TIMEOUT_SECONDS: Final[int] = 30

# “先声明类型，后赋值”也可以（常见于：先占位，后从配置/输入读取）
count: int
count = 0


class Settings:
    DEFAULT_PORT: ClassVar[int] = 8080  # 类变量（所有实例共享）

    def __init__(self, host: str) -> None:
        self.host: str = host  # 实例属性


def main() -> None:
    print("PI =", PI)
    print("DEFAULT_TIMEOUT_SECONDS =", DEFAULT_TIMEOUT_SECONDS)
    print("count =", count)

    s = Settings("127.0.0.1")
    print("settings.host =", s.host)
    print("Settings.DEFAULT_PORT =", Settings.DEFAULT_PORT)

    print("\n模块级 __annotations__：")
    print(__annotations__)
    print("\n类 Settings.__annotations__：")
    print(Settings.__annotations__)


if __name__ == "__main__":
    main()
