#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：用三引号把代码“注释掉”的坑与替代方案。

很多人会这样“注释掉一段代码”：

    '''
    some_code()
    other_code()
    '''

但这并不是注释，而是一个“字符串字面量表达式”：
- 如果它出现在模块/函数/类体的第一条语句位置，它会变成 docstring（影响 __doc__）。
- 如果它出现在其它位置，它会被编译进常量表并在运行时执行为“无用语句”（LOAD_CONST/POP_TOP）。

更推荐的做法：
1) 删除代码（交给版本控制）
2) 或使用多行 # 块注释临时禁用
"""

from __future__ import annotations


def good_way() -> None:
    # 临时禁用某段代码，使用连续的 # 注释更明确：
    # print("this is disabled")
    # print("still disabled")
    print("enabled code runs")


def triple_quote_pitfall() -> None:
    """这个 docstring 会存在。"""

    # 下面这段“不是注释”，只是一个普通字符串表达式语句：
    """
    print("你以为这被注释掉了，但它只是一个字符串字面量。")
    """

    print("function body continues")


def main() -> None:
    good_way()
    triple_quote_pitfall()
    print("triple_quote_pitfall.__doc__ =", triple_quote_pitfall.__doc__)


if __name__ == "__main__":
    main()
