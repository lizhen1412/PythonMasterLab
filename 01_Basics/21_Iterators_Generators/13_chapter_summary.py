#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：本章总结（迭代器与生成器）。
Author: Lambert

运行：
    python3 01_Basics/21_Iterators_Generators/13_chapter_summary.py
"""


def main() -> None:
    points = [
        "iterable vs iterator：iter(x) 生成迭代器，next(it) 拉取元素",
        "iterator 必须实现 __iter__/__next__，耗尽时抛 StopIteration",
        "for 循环内部就是 iter + next + 捕获 StopIteration",
        "生成器函数：包含 yield 的函数，返回生成器对象（惰性）",
        "send/throw/close：双向通信与清理；next == send(None)",
        "yield from：委托子生成器，接收其 return 值",
        "一次性迭代器不可复用，需缓存或重建",
        "异步生成器只能用 async for 消费",
    ]
    print("== 关键规则清单 ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()