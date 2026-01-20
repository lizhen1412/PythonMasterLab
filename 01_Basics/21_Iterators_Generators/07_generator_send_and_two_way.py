#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：生成器的 send() 双向通信。

你会学到：
1) next(gen) 等价于 gen.send(None)
2) send(value) 把值传入生成器内部
3) 第一次必须先“预激活”（prime）

运行：
    python3 01_Basics/21_Iterators_Generators/07_generator_send_and_two_way.py
"""


def running_average():
    total = 0.0
    count = 0
    avg = None
    while True:
        value = yield avg
        if value is None:
            continue
        total += value
        count += 1
        avg = total / count


def main() -> None:
    gen = running_average()

    print("prime ->", next(gen))
    print("send 10 ->", gen.send(10))
    print("send 20 ->", gen.send(20))
    print("send 0 ->", gen.send(0))

    print("\nnext == send(None)")
    print("next ->", next(gen))


if __name__ == "__main__":
    main()
