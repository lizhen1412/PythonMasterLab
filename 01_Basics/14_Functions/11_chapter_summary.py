#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：本章总结与常见误区。
Author: Lambert
"""

from __future__ import annotations


RULES = [
    "默认值在定义时求值，避免使用可变对象；必要时用 None 哨兵 + 函数体创建",
    "掌握五类参数位：a, /, b, c=0, *args, d, e=1, **kwargs（位置仅限 / 关键字仅限）",
    "`got multiple values for argument` 多半是“位置 + 关键字重复传递”",
    "函数是一等公民：可以存入容器、作为参数/返回值、返回闭包",
    "出现 UnboundLocalError：局部作用域里赋值同名变量导致；用 nonlocal/global 修复",
    "闭包捕获循环变量会延迟绑定；需要用默认参数或内部作用域固定当前值",
    "装饰器务必使用 functools.wraps 保留原函数元数据",
    "递归必须有基线与收敛步骤；Python 无尾递归优化，深递归要谨慎",
    "内置函数需理解返回值与副作用；交互/动态执行类函数要小心使用",
]


PITFALLS = [
    "把 `lambda` 写成多行/复杂逻辑：此时请改用 def，便于调试与注释",
    "用 sum 拼接字符串：效率低且类型不匹配；应使用 str.join",
    "误用 `*`/`**`：解包顺序错误会导致覆盖或 TypeError",
    "忽略关键字仅限参数：易造成调用时位置实参顺序错误或可读性差",
    "在递归里忘记返回递归结果：会得到 None 并导致 TypeError",
]


def main() -> None:
    print("== 规则清单 ==")
    for idx, rule in enumerate(RULES, start=1):
        print(f"{idx:02d}. {rule}")

    print("\n== 常见误区 ==")
    for idx, pitfall in enumerate(PITFALLS, start=1):
        print(f"{idx:02d}. {pitfall}")


if __name__ == "__main__":
    main()