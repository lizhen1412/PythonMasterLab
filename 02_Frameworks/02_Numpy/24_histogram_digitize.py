#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 24：Histogram and Digitize - 直方图与分箱。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/24_histogram_digitize.py

直方图是数据分析中重要的工具，用于理解数据分布。
NumPy 提供了强大的直方图计算和数据分箱功能。

本节演示：
1. histogram - 直方图计算
2. histogram2d - 二维直方图
3. histogramdd - N 维直方图
4. bincount - 计数统计
5. digitize - 数据分箱
6. 实际应用案例
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. histogram - 直方图计算")
    print("=" * 60)

    # 生成随机数据
    np.random.seed(42)
    data = np.random.randn(1000)  # 标准正态分布

    print(f"\n数据点数: {len(data)}")
    print(f"范围: [{data.min():.2f}, {data.max():.2f}]")

    # 计算直方图
    hist, bin_edges = np.histogram(data, bins=10)

    print(f"\n10 个等宽箱的直方图:")
    print(f"计数: {hist}")

    print(f"\n箱边界:")
    for i in range(len(bin_edges) - 1):
        print(f"  箱 {i+1}: [{bin_edges[i]:.2f}, {bin_edges[i+1]:.2f}) -> {hist[i]}")

    # 自定义箱边界
    custom_bins = [-3, -2, -1, 0, 1, 2, 3]
    hist_custom, bin_edges_custom = np.histogram(data, bins=custom_bins)

    print(f"\n自定义箱边界: {custom_bins}")
    print(f"计数: {hist_custom}")

    # 密度（归一化）
    hist_density, _ = np.histogram(data, bins=10, density=True)
    print(f"\n密度分布（面积和为1）:")
    print(f"  密度: {hist_density}")
    print(f"  验证: sum(density * bin_width) = {np.sum(hist_density * (bin_edges[1] - bin_edges[0])):.2f}")

    print("\n" + "=" * 60)
    print("2. histogram2d - 二维直方图")
    print("=" * 60)

    # 生成二维数据
    x = np.random.randn(1000)
    y = x + np.random.randn(1000) * 0.5  # y 与 x 相关

    print(f"\n数据点数: {len(x)}")

    # 计算二维直方图
    H, xedges, yedges = np.histogram2d(x, y, bins=20)

    print(f"\n二维直方图形状: {H.shape}")
    print(f"X 边界: {len(xedges)} 个")
    print(f"Y 边界: {len(yedges)} 个")

    print(f"\n最高频区域计数: {H.max()}")
    print(f"最高频位置: x_bin={np.unravel_index(H.argmax(), H.shape)[0]}, "
          f"y_bin={np.unravel_index(H.argmax(), H.shape)[1]}")

    # 显示部分直方图
    print(f"\n直方图（部分）:")
    print(H[:5, :5])

    print("\n" + "=" * 60)
    print("3. histogramdd - N 维直方图")
    print("=" * 60)

    # 三维数据
    x = np.random.randn(100)
    y = np.random.randn(100)
    z = np.random.randn(100)

    # 三维直方图
    H_3d, edges = np.histogramdd((x, y, z), bins=(5, 5, 5))

    print(f"\n三维直方图形状: {H_3d.shape}")
    print(f"总箱数: {H_3d.size}")

    print(f"\n非空箱数: {np.count_nonzero(H_3d)}")
    print(f"最高计数: {H_3d.max()}")

    print("\n" + "=" * 60)
    print("4. bincount - 计数统计")
    print("=" * 60)

    print("\nbincount 统计非负整数出现的次数")

    # 非负整数数组
    arr = np.array([0, 1, 1, 2, 2, 2, 3, 5])
    print(f"\n数组: {arr}")

    counts = np.bincount(arr)
    print(f"计数: {counts}")
    print(f"说明: 索引是值，元素是出现次数")

    # 解释
    print(f"\n详细解释:")
    for value, count in enumerate(counts):
        if count > 0:
            print(f"  值 {value} 出现 {count} 次")

    # weights 参数（加权计数）
    values = np.array([0, 1, 1, 2, 2, 2, 3, 5])
    weights = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    weighted_count = np.bincount(values, weights=weights)
    print(f"\n加权计数:")
    print(f"  值: {values}")
    print(f"  权重: {weights}")
    print(f"  加权计数: {weighted_count}")

    # minlength 参数
    arr_short = np.array([0, 1, 1])
    print(f"\n原数组: {arr_short}")
    print(f"bincount: {np.bincount(arr_short)}")
    print(f"bincount(minlength=6): {np.bincount(arr_short, minlength=6)}")

    print("\n" + "=" * 60)
    print("5. digitize - 数据分箱")
    print("=" * 60)

    print("\ndigitize 将数据分配到指定的箱中")

    # 分数分箱
    scores = np.array([45, 62, 78, 85, 92, 55, 68, 73, 88, 95])
    print(f"\n分数: {scores}")

    # 定义等级边界
    bins = [60, 70, 80, 90]
    print(f"箱边界: {bins}")

    # digitize 返回每个值属于哪个箱
    indices = np.digitize(scores, bins)
    print(f"\n箱索引: {indices}")
    print(f"说明: 0 表示 <60, 1 表示 [60,70), 等等")

    # 映射到等级
    grades = ['F', 'D', 'C', 'B', 'A']
    score_grades = [grades[i] for i in indices]
    print(f"\n等级映射:")
    for score, grade in zip(scores, score_grades):
        print(f"  {score:3d} -> {grade}")

    # right 参数控制边界包含
    print(f"\nright 参数效果:")
    print(f"  right=True (默认): {bins}")
    print(f"    区间: (-∞,60], (60,70], (70,80], (80,90], (90,∞)")

    indices_left = np.digitize(scores, bins, right=False)
    print(f"\nright=False:")
    print(f"    区间: (-∞,60), [60,70), [70,80), [80,90), [90,∞)")
    print(f"  箱索引: {indices_left}")

    print("\n" + "=" * 60)
    print("6. 实际应用案例")
    print("=" * 60)

    print("\n案例1: 图像直方图均衡化")
    print("-" * 40)

    # 模拟灰度图像 (0-255)
    np.random.seed(42)
    image = np.random.randint(0, 256, (100, 100))

    print(f"图像大小: {image.shape}")
    print(f"像素范围: [{image.min()}, {image.max()}]")

    # 计算直方图
    hist, bins = np.histogram(image.flatten(), bins=256, range=(0, 256))

    print(f"\n直方图统计:")
    print(f"  总像素: {hist.sum()}")
    print(f"  非空箱: {np.count_nonzero(hist)}")
    print(f"  最高计数: {hist.max()} (值 {np.argmax(hist)})")

    # 累积分布函数 (CDF)
    cdf = hist.cumsum()
    cdf_normalized = cdf / cdf.max()

    print(f"\n累积分布函数:")
    print(f"  前10个值: {cdf_normalized[:10]}")

    print("\n案例2: 年龄分组统计")
    print("-" * 40)

    ages = np.array([5, 12, 18, 25, 30, 35, 42, 50, 65, 70])
    print(f"年龄: {ages}")

    # 定义年龄段
    age_bins = [0, 18, 35, 50, 100]
    age_labels = ['儿童', '青年', '中年', '老年']

    indices = np.digitize(ages, age_bins)
    # 调整索引（digitize 从 1 开始）
    age_groups = [age_labels[min(i, len(age_labels)-1)] for i in indices]

    print(f"\n年龄分组:")
    for age, group in zip(ages, age_groups):
        print(f"  {age:2d} 岁 -> {group}")

    print("\n案例3: 搜索词热度分析")
    print("-" * 40)

    # 搜索词 ID (非负整数)
    search_terms = np.array([1, 5, 3, 1, 5, 5, 2, 3, 1, 5, 4, 5, 5])
    print(f"搜索词 ID: {search_terms}")

    # 统计每个词的搜索次数
    term_counts = np.bincount(search_terms)
    print(f"\n搜索次数:")
    for term_id, count in enumerate(term_counts):
        if count > 0:
            print(f"  词 {term_id}: {count} 次")

    # 找到最热门的词
    top_term = np.argmax(term_counts)
    print(f"\n最热门搜索: 词 {top_term}, {term_counts[top_term]} 次")

    print("\n案例4: 评分分布分析")
    print("-" * 40)

    # 电影评分 (1-5)
    ratings = np.array([5, 4, 3, 5, 4, 5, 2, 4, 3, 5, 1, 4, 5, 4, 3])
    print(f"评分: {ratings}")

    # 计算直方图
    rating_counts, rating_bins = np.histogram(ratings, bins=[1, 2, 3, 4, 5, 6])
    print(f"\n评分分布:")
    for i, (count, low, high) in enumerate(zip(rating_counts, rating_bins[:-1], rating_bins[1:])):
        print(f"  {int(low)} 星: {count} 次")

    # 平均评分
    avg_rating = np.mean(ratings)
    print(f"\n平均评分: {avg_rating:.2f}")

    print("\n案例5: 数据离散化（用于机器学习）")
    print("-" * 40)

    # 连续特征
    ages = np.array([5, 12, 18, 25, 30, 35, 42, 50, 65, 70, 22, 28, 45])
    print(f"原始年龄: {ages}")

    # 等宽分箱
    n_bins = 5
    age_hist, age_bins = np.histogram(ages, bins=n_bins)

    print(f"\n等宽分箱 (5 个):")
    print(f"  箱边界: {age_bins}")
    print(f"  每箱计数: {age_hist}")

    # digitize 分箱
    bin_indices = np.digitize(ages, age_bins[:-1])
    print(f"\n分箱结果:")
    for age, idx in zip(ages, bin_indices):
        print(f"  年龄 {age:2d} -> 箱 {idx}")

    # one-hot 编码
    print(f"\nOne-hot 编码:")
    for i, age in enumerate(ages[:5]):  # 只显示前5个
        bin_idx = bin_indices[i] - 1
        one_hot = np.zeros(n_bins)
        if 0 <= bin_idx < n_bins:
            one_hot[bin_idx] = 1
        print(f"  年龄 {age}: {one_hot.astype(int)}")

    print("\n" + "=" * 60)
    print("7. 函数速查")
    print("=" * 60)

    print("\n直方图函数:")
    print("  np.histogram(a, bins=10, range=None, density=False)")
    print("    返回: (hist, bin_edges)")

    print("  np.histogram2d(x, y, bins=10)")
    print("    返回: (H, xedges, yedges)")

    print("  np.histogramdd(sample, bins=10, density=False)")
    print("    返回: (H, edges)")

    print("\n计数与分箱:")
    print("  np.bincount(x, weights=None, minlength=0)")
    print("    返回: counts 数组")

    print("  np.digitize(x, bins, right=False)")
    print("    返回: 箱索引数组")

    print("\n参数说明:")
    print("  bins:")
    print("    - 整数: 等宽的箱数量")
    print("    - 序列: 自定义箱边界")
    print("    - 字符串: {'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges'}")

    print("\n  density:")
    print("    - True: 归一化，面积和为 1")
    print("    - False: 原始计数")

    print("\n  right (digitize):")
    print("    - True: 区间 (a, b] (右闭)")
    print("    - False: 区间 [a, b) (左闭)")

    print("\n" + "=" * 60)
    print("8. 应用场景")
    print("=" * 60)

    print("\n数据探索:")
    print("  - 了解数据分布")
    print("  - 发现异常值")
    print("  - 选择合适的箱宽")

    print("\n图像处理:")
    print("  - 直方图均衡化")
    print("  - 对比度增强")
    print("  - 颜色分析")

    print("\n机器学习:")
    print("  - 特征离散化")
    print("  - 数据分箱")
    print("  - One-hot 编码准备")

    print("\n统计分析:")
    print("  - 频率分析")
    print("  - 概率密度估计")
    print("  - 多变量联合分布")


if __name__ == "__main__":
    main()