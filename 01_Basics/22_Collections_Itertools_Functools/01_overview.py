#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ collections / itertools / functools 示例索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/22_Collections_Itertools_Functools/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_collections_deque.py", "collections.deque：双端队列与滑动窗口"),
    ("03_collections_counter.py", "collections.Counter：计数与频率统计"),
    ("04_collections_defaultdict.py", "collections.defaultdict：分组与默认工厂"),
    ("05_collections_chainmap.py", "collections.ChainMap：分层配置"),
    ("06_collections_namedtuple.py", "collections.namedtuple：轻量记录类型"),
    ("07_itertools_building_blocks.py", "itertools 基本积木：count/islice/chain/repeat/cycle"),
    ("08_itertools_combinatorics.py", "itertools 组合：product/permutations/combinations"),
    ("09_itertools_groupby.py", "itertools.groupby：按键分组（需排序）"),
    ("10_itertools_accumulate_zip_longest.py", "accumulate/pairwise/zip_longest 等实用工具"),
    ("11_functools_partial_and_wraps.py", "functools.partial 与 wraps"),
    ("12_functools_cache_lru_cache.py", "cache/lru_cache：记忆化"),
    ("13_functools_singledispatch.py", "singledispatch：按类型分发"),
    ("14_functools_reduce_and_cmp_to_key.py", "reduce 与 cmp_to_key：聚合与排序"),
    ("15_chapter_summary.py", "本章总结：关键规则与常见误区"),
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