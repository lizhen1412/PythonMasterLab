#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：collections / itertools / functools。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_deque_sliding_window.py", "deque 实现滑动窗口"),
    ("03_counter_top_k.py", "Counter 统计 top-k"),
    ("04_defaultdict_grouping.py", "defaultdict 分组"),
    ("05_chainmap_layered_config.py", "ChainMap 配置覆盖"),
    ("06_namedtuple_points.py", "namedtuple 表示点并计算距离"),
    ("07_itertools_chunked.py", "islice 实现分块"),
    ("08_itertools_combinations.py", "组合枚举"),
    ("09_itertools_groupby_runs.py", "groupby 连续分组"),
    ("10_functools_cache_fib.py", "lru_cache 斐波那契"),
    ("11_functools_singledispatch_format.py", "singledispatch 格式化"),
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