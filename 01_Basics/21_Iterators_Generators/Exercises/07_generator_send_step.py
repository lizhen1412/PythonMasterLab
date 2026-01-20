#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：send 改变生成器步长。

题目：
实现生成器函数 `stepper(start=0, step=1)`：
- 正常 next()：按当前步长递增
- send(new_step)：更新步长

示例：
    gen = stepper(0, 1)
    next(gen) -> 0
    next(gen) -> 1
    gen.send(3) -> 4
    next(gen) -> 7

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/21_Iterators_Generators/Exercises/07_generator_send_step.py
"""


def stepper(start: int = 0, step: int = 1):
    current = start
    while True:
        new_step = yield current
        if new_step is not None:
            step = new_step
        current += step


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    gen = stepper(0, 1)
    check("next1", next(gen), 0)
    check("next2", next(gen), 1)
    check("send(3)", gen.send(3), 4)
    check("next3", next(gen), 7)


if __name__ == "__main__":
    main()
