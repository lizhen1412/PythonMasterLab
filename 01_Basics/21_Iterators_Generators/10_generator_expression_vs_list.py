#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：生成器表达式 vs 列表推导式。

你会学到：
1) 生成器表达式是惰性的，只在消费时计算
2) 列表推导式立即生成完整列表
3) 生成器只能消费一次

运行：
    python3 01_Basics/21_Iterators_Generators/10_generator_expression_vs_list.py
"""


def main() -> None:
    gen_expr = (x * x for x in range(5))
    list_comp = [x * x for x in range(5)]

    print("gen_expr ->", gen_expr)
    print("list_comp ->", list_comp)

    print("\n消费生成器:")
    print("sum ->", sum(gen_expr))
    print("再次消费 ->", list(gen_expr))

    print("\n列表可以重复使用:")
    print("sum ->", sum(list_comp))
    print("再次使用 ->", list_comp)


if __name__ == "__main__":
    main()
