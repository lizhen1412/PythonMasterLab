#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：迭代器与生成器。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/21_Iterators_Generators/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_safe_next_with_default.py", "实现安全的 next_or（StopIteration -> 默认值）"),
    ("03_countdown_iterator.py", "自定义倒计时迭代器"),
    ("04_iter_callable_sentinel.py", "iter(callable, sentinel) 读取到哨兵"),
    ("05_generator_even_squares.py", "生成器：偶数平方的惰性序列"),
    ("06_yield_from_flatten.py", "yield from 扁平化嵌套列表"),
    ("07_generator_send_step.py", "send 改变生成器步长"),
    ("08_exhaustion_fix.py", "修复一次性迭代器被耗尽的 bug"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()