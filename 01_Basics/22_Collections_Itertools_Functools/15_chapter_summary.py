#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：本章总结（collections / itertools / functools）。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/15_chapter_summary.py
"""


def main() -> None:
    points = [
        "deque：双端队列，适合队列/滑动窗口",
        "Counter：频率统计，most_common/top-k",
        "defaultdict：分组/计数更省心",
        "ChainMap：多层配置覆盖",
        "namedtuple：轻量不可变记录",
        "itertools：惰性组合工具（chain/islice/product/groupby 等）",
        "groupby 只分相邻元素：要先排序",
        "functools：partial/wraps/cache/singledispatch/reduce",
    ]
    print("== 关键规则清单 ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()
