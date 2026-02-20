#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 22：聚合函数全集。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/22_aggregation_complete.py

知识点：
- argmin/argmax - 最小/最大值索引
- median - 中位数
- percentile/quantile - 分位数
- ptp - 峰峰值
- average - 加权平均
- std/var 详细参数
- nanmean/nanmedian - 忽略 NaN 的聚合
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.array([[3, 7, 1], [10, 2, 8], [5, 4, 6]])

    print("=" * 70)
    print("原始数据")
    print("=" * 70)
    print(arr)

    print("\n" + "=" * 70)
    print("1. argmin / argmax - 索引位置")
    print("=" * 70)

    print("\n1.1 全局最小/最大索引")
    print("-" * 70)
    print(f"argmin(): {np.argmin(arr)} (位置: {np.unravel_index(np.argmin(arr), arr.shape)})")
    print(f"argmax(): {np.argmax(arr)} (位置: {np.unravel_index(np.argmax(arr), arr.shape)})")

    print("\n1.2 按 axis")
    print("-" * 70)
    print(f"argmin(axis=0): {np.argmin(arr, axis=0)}")
    print(f"  每列最小值的行索引")

    print(f"\nargmin(axis=1): {np.argmin(arr, axis=1)}")
    print(f"  每行最小值的列索引")

    print("\n1.3 unravel_index - 扁平索引转多维索引")
    print("-" * 70)
    flat_idx = 5
    multi_idx = np.unravel_index(flat_idx, arr.shape)
    print(f"扁平索引 {flat_idx} -> 多维索引 {multi_idx}")
    print(f"arr[{multi_idx}] = {arr[multi_idx]}")

    print("\n" + "=" * 70)
    print("2. median - 中位数")
    print("=" * 70)

    arr_unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    print(f"数据: {arr_unsorted}")
    print(f"median: {np.median(arr_unsorted)}")

    print("\n2.1 按 axis")
    print("-" * 70)
    print(f"median(axis=0): {np.median(arr, axis=0)}")
    print(f"median(axis=1): {np.median(arr, axis=1)}")

    print("\n2.2 percentile - 百分位数")
    print("-" * 70)
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"数据: {data}")
    print(f"percentile(25): {np.percentile(data, 25)}")
    print(f"percentile(50): {np.percentile(data, 50)}")
    print(f"percentile(75): {np.percentile(data, 75)}")

    print("\n多个百分位数:")
    percentiles = np.percentile(data, [25, 50, 75])
    print(f"[25, 50, 75]: {percentiles}")

    print("\n2.3 quantile - 分位数（与 percentile 类似）")
    print("-" * 70)
    print(f"quantile(0.25): {np.quantile(data, 0.25)}")
    print(f"quantile(0.5): {np.quantile(data, 0.5)}")
    print(f"quantile(0.75): {np.quantile(data, 0.75)}")

    print("\n" + "=" * 70)
    print("3. ptp - 峰峰值")
    print("=" * 70)

    print(f"ptp(): {np.ptp(arr_unsorted)}")
    print(f"等于 max - min: {np.max(arr_unsorted) - np.min(arr_unsorted)}")

    print("\n按 axis:")
    print(f"ptp(axis=0): {np.ptp(arr, axis=0)}")
    print(f"ptp(axis=1): {np.ptp(arr, axis=1)}")

    print("\n" + "=" * 70)
    print("4. average - 加权平均")
    print("=" * 70)

    values = np.array([1, 2, 3, 4, 5])
    weights = np.array([1, 2, 3, 2, 1])

    print(f"values: {values}")
    print(f"weights: {weights}")

    print(f"\naverage(values, weights): {np.average(values, weights=weights)}")

    print("\n4.1 多维数组加权平均")
    print("-" * 70)
    arr_2d = np.array([[1, 2], [3, 4]])
    weights_2d = np.array([[1, 2], [3, 4]])

    print(f"arr_2d:\n{arr_2d}")
    print(f"weights_2d:\n{weights_2d}")

    print(f"\naverage(arr_2d, weights=weights_2d): {np.average(arr_2d, weights=weights_2d)}")

    print("\n4.2 返回权重和")
    print("-" * 70)
    avg, sum_of_weights = np.average(values, weights=weights, returned=True)
    print(f"average: {avg}, sum_of_weights: {sum_of_weights}")

    print("\n" + "=" * 70)
    print("5. std / var - 标准差和方差")
    print("=" * 70)

    data = np.array([1, 2, 3, 4, 5])

    print(f"data: {data}")
    print(f"mean: {np.mean(data)}")
    print(f"std: {np.std(data)}")
    print(f"var: {np.var(data)}")

    print("\n5.1 ddof 参数（自由度调整）")
    print("-" * 70)
    print(f"std(ddof=0) [总体标准差]: {np.std(data, ddof=0)}")
    print(f"std(ddof=1) [样本标准差]: {np.std(data, ddof=1)}")
    print(f"var(ddof=0) [总体方差]: {np.var(data, ddof=0)}")
    print(f"var(ddof=1) [样本方差]: {np.var(data, ddof=1)}")

    print("\n5.2 按 axis")
    print("-" * 70)
    print(f"std(axis=0): {np.std(arr, axis=0)}")
    print(f"std(axis=1): {np.std(arr, axis=1)}")

    print("\n" + "=" * 70)
    print("6. 忽略 NaN 的聚合函数")
    print("=" * 70)

    arr_with_nan = np.array([1, 2, np.nan, 4, 5, np.nan])

    print(f"data with NaN: {arr_with_nan}")

    print("\n6.1 nanmean / nanmedian")
    print("-" * 70)
    print(f"nanmean: {np.nanmean(arr_with_nan)}")
    print(f"nanmedian: {np.nanmedian(arr_with_nan)}")

    print("\n6.2 nanstd / nanvar")
    print("-" * 70)
    print(f"nanstd: {np.nanstd(arr_with_nan)}")
    print(f"nanvar: {np.nanvar(arr_with_nan)}")

    print("\n6.3 nansum / nanprod / nanmin / nanmax")
    print("-" * 70)
    print(f"nansum: {np.nansum(arr_with_nan)}")
    print(f"nanprod: {np.nanprod(arr_with_nan)}")
    print(f"nanmin: {np.nanmin(arr_with_nan)}")
    print(f"nanmax: {np.nanmax(arr_with_nan)}")

    print("\n6.4 nanpercentile / nanquantile")
    print("-" * 70)
    print(f"nanpercentile(50): {np.nanpercentile(arr_with_nan, 50)}")
    print(f"nanquantile(0.5): {np.nanquantile(arr_with_nan, 0.5)}")

    print("\n" + "=" * 70)
    print("7. 其他聚合函数")
    print("=" * 70)

    data = np.array([1, 2, 3, 4, 5])

    print(f"data: {data}")

    print("\n7.1 sum / prod")
    print("-" * 70)
    print(f"sum: {np.sum(data)}")
    print(f"prod: {np.prod(data)}")

    print("\n7.2 cumsum / cumprod")
    print("-" * 70)
    print(f"cumsum: {np.cumsum(data)}")
    print(f"cumprod: {np.cumprod(data)}")

    print("\n7.3 diff / ediff1d")
    print("-" * 70)
    print(f"diff: {np.diff(data)}")
    print(f"ediff1d: {np.ediff1d(data)}")

    print("\n7.4 all / any（逻辑聚合）")
    print("-" * 70)
    bool_arr = np.array([True, False, True])
    print(f"bool_arr: {bool_arr}")
    print(f"all: {np.all(bool_arr)}")
    print(f"any: {np.any(bool_arr)}")

    print("\n" + "=" * 70)
    print("8. 实际应用示例")
    print("=" * 70)

    # 示例 1: 统计分析
    print("\n示例 1: 描述性统计")
    data = np.array([23, 45, 67, 89, 12, 34, 56, 78, 90, 11])
    print(f"数据: {data}")
    print(f"均值: {np.mean(data):.2f}")
    print(f"中位数: {np.median(data):.2f}")
    print(f"标准差: {np.std(data, ddof=1):.2f}")
    print(f"四分位数: {np.percentile(data, [25, 50, 75])}")

    # 示例 2: 图像处理
    print("\n示例 2: 图像灰度统计")
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)
    print(f"图像形状: {image.shape}")
    print(f"平均灰度: {np.mean(image):.2f}")
    print(f"灰度范围: {np.min(image)} - {np.max(image)}")

    # 示例 3: 加权评分
    print("\n示例 3: 加权评分计算")
    scores = np.array([85, 90, 78, 92, 88])
    weights = np.array([0.2, 0.3, 0.2, 0.2, 0.1])
    weighted_avg = np.average(scores, weights=weights)
    print(f"成绩: {scores}")
    print(f"权重: {weights}")
    print(f"加权平均: {weighted_avg:.2f}")

    # 示例 4: 异常值检测
    print("\n示例 4: 基于标准差检测异常值")
    data = np.array([10, 12, 11, 13, 100, 12, 11, 14])
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    threshold = 3
    outliers = np.abs(data - mean) > threshold * std
    print(f"数据: {data}")
    print(f"异常值: {data[outliers]}")


if __name__ == "__main__":
    main()