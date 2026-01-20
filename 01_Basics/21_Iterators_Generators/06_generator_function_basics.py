#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：生成器函数基础。

你会学到：
1) 使用 yield 定义生成器函数
2) 生成器是惰性的：按需产出
3) 生成器对象本身是迭代器

运行：
    python3 01_Basics/21_Iterators_Generators/06_generator_function_basics.py
"""


def count_up_to(limit: int):
    print("  (generator started)")
    for i in range(limit + 1):
        yield i
    print("  (generator ended)")


def main() -> None:
    gen = count_up_to(3)
    print("gen ->", gen)
    print("iter(gen) is gen ->", iter(gen) is gen)

    print("\n逐步 next():")
    print(next(gen))
    print(next(gen))

    print("\n继续 for 循环消费:")
    for value in gen:
        print(value)


if __name__ == "__main__":
    main()
