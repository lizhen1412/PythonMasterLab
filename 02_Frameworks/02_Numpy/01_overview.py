#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：numpy 2.4.0 学习索引。
Author: Lambert

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
    ("18_fft_basics.py", "FFT - 快速傅里叶变换"),
    ("19_polynomial.py", "Polynomial - 多项式运算"),
    ("20_masked_arrays.py", "Masked Arrays - 掩码数组"),
    ("21_financial.py", "Financial - 金融函数"),
    ("22_performance_optimization.py", "Performance - 性能优化"),
    ("23_signal_processing.py", "Signal Processing - 信号处理（convolve/correlate/gradient/trapz）"),
    ("24_histogram_digitize.py", "Histogram & Digitize - 直方图与分箱"),
    ("25_memmap.py", "Memmap - 内存映射文件"),
    ("26_structured_arrays.py", "Structured Arrays - 结构化数组"),
    ("27_advanced_indexing.py", "Advanced Indexing - 高级索引（ix_/mgrid/ogrid/select）"),
    ("28_numpy_complete.py", "NumPy Complete - einsum/pad/char/corrcoef/interp/trim_zeros/nanpercentile"),
    ("29_linalg_advanced.py", "Linear Algebra Advanced - QR/Schur/Cholesky/伪逆/条件数"),
    ("30_fft_advanced.py", "FFT Advanced - rfft/rfft2/窗函数/零填充"),
    ("31_ufunc_advanced.py", "Ufunc Advanced - outer/at/reduceat/accumulate/自定义"),
    ("32_datetime64.py", "DateTime64 - datetime64/timedelta64 完整操作"),
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