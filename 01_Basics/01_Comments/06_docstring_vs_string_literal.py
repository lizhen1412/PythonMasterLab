#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：docstring 与普通三引号字符串表达式的区别。
Author: Lambert

规则回顾：
- 只有“第一条语句”的字符串字面量，才会被当作 docstring。
- 其它位置的三引号字符串，只是一个“无用的表达式语句”，不会成为 __doc__。

注意：
- 用三引号把代码“包起来当注释”，本质上不是注释，仍会被编译进字节码常量表。
"""

from __future__ import annotations

import dis


def demo() -> int:
    """这是 demo 的 docstring。"""

    "这是一条普通字符串表达式：不会成为 docstring，也不会被赋值。"  # noqa: B018

    return 123


def main() -> None:
    print("demo.__doc__ =")
    print(demo.__doc__)
    print()

    print("反汇编 demo()，可以看到额外的字符串会被 LOAD_CONST 然后 POP_TOP：")
    dis.dis(demo)
    print()

    print("demo() =", demo())


if __name__ == "__main__":
    main()