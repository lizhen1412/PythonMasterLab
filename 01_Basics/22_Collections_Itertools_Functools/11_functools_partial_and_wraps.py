#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：functools.partial 与 wraps。
Author: Lambert

你会学到：
1) partial 固定部分参数
2) wraps 保留被装饰函数的元信息

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/11_functools_partial_and_wraps.py
"""

from functools import partial, wraps


def power(base: int, exp: int) -> int:
    return base**exp


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} args={args} kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


def main() -> None:
    square = partial(power, exp=2)
    cube = partial(power, exp=3)
    print("square(5) ->", square(5))
    print("cube(2) ->", cube(2))

    @logger
    def add(a: int, b: int) -> int:
        """add two numbers"""
        return a + b

    print("add.__name__ ->", add.__name__)
    print("add.__doc__ ->", add.__doc__)
    print("add(2, 3) ->", add(2, 3))


if __name__ == "__main__":
    main()