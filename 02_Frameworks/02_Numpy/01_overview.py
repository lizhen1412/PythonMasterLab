#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：numpy 2.4.0 学习索引。

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/02_Numpy/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_install_and_version.py", "安装与版本检查"),
    ("03_array_basics.py", "数组创建与基础属性"),
    ("04_index_slice.py", "索引与切片"),
    ("05_boolean_fancy_index.py", "布尔/花式索引与 where"),
    ("06_reshape_transpose.py", "reshape 与转置"),
    ("07_broadcasting_ops.py", "广播与向量化运算"),
    ("08_aggregation_axis.py", "聚合与 axis"),
    ("09_nan_inf_handling.py", "NaN/Inf 处理"),
    ("10_sort_unique.py", "排序/去重/searchsorted"),
    ("11_stack_split.py", "拼接与拆分"),
    ("12_random_sampling.py", "随机数（可重复）"),
    ("13_linear_algebra.py", "线性代数入门"),
    ("14_io_save_load.py", "保存/读取（内存 I/O）"),
    ("15_views_copies.py", "视图与拷贝"),
    ("16_vectorize_ufunc.py", "ufunc 与条件处理"),
    ("17_chapter_summary.py", "本章总结"),
    ("Exercises/01_overview.py", "练习索引"),
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
