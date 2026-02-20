#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 迭代器与生成器（Iterators & Generators）示例索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/21_Iterators_Generators/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_iterable_and_iterator.py", "可迭代对象 vs 迭代器：iter/next 与协议"),
    ("03_iter_next_and_stop_iteration.py", "手动迭代与 StopIteration；for 循环如何工作"),
    ("04_custom_iterator_class.py", "自定义迭代器类：__iter__/__next__ 模式"),
    ("05_iter_callable_sentinel.py", "iter(callable, sentinel)：哨兵迭代"),
    ("06_generator_function_basics.py", "生成器函数基础：yield、惰性与状态保留"),
    ("07_generator_send_and_two_way.py", "send 双向通信：next() 等价 send(None)"),
    ("08_generator_throw_and_close.py", "throw/close 与清理：GeneratorExit 与 finally"),
    ("09_yield_from_delegation.py", "yield from：委托生成器与返回值"),
    ("10_generator_expression_vs_list.py", "生成器表达式 vs 列表推导式"),
    ("11_iterator_exhaustion_and_reuse.py", "一次性迭代器的耗尽与复用策略"),
    ("12_async_generator_basics.py", "异步生成器：async def + yield + async for"),
    ("13_chapter_summary.py", "本章总结：关键规则与常见误区"),
    ("Exercises/01_overview.py", "本章练习索引（每题一个文件）"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()