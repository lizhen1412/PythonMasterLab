#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：throw/close 与清理。

你会学到：
1) throw() 在生成器内部抛异常
2) close() 触发 GeneratorExit
3) 用 try/finally 做清理

运行：
    python3 01_Basics/21_Iterators_Generators/08_generator_throw_and_close.py
"""


def ticker():
    i = 0
    try:
        while True:
            try:
                yield i
            except ValueError as exc:
                print("caught:", exc)
            i += 1
    finally:
        print("cleanup: generator closed")


def main() -> None:
    gen = ticker()
    print("next ->", next(gen))
    print("throw ->", gen.throw(ValueError("bad value")))
    print("next ->", next(gen))
    print("close")
    gen.close()


if __name__ == "__main__":
    main()
