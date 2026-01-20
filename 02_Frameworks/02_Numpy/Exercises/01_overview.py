#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：numpy 2.4.0。

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/02_Numpy/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_arange_reshape.py", "arange + reshape"),
    ("03_mask_even.py", "布尔过滤"),
    ("04_broadcast_add_row.py", "广播相加"),
    ("05_mean_axis0.py", "按列均值"),
    ("06_fill_nan_mean.py", "NaN 均值填充"),
    ("07_stack_columns.py", "列拼接"),
    ("08_dot_product.py", "向量点积"),
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
