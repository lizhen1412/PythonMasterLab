#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 23：Signal Processing - 信号处理函数。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/23_signal_processing.py

NumPy 提供了一系列信号处理相关的函数，包括卷积、相关、
梯度计算等。这些函数在信号处理、图像处理和科学计算中非常重要。

本节演示：
1. convolve - 卷积运算
2. correlate - 互相关运算
3. gradient - 梯度计算
4. trapz - 梯形积分
5. diff - 离散差分
6. 实际应用案例
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. convolve - 卷积运算")
    print("=" * 60)

    print("\n卷积是信号处理中的基本运算，用于滤波、平滑等")

    # 一维卷积
    signal = np.array([1, 2, 3, 4, 5])
    kernel = np.array([1, 0.5, 0.25])

    print(f"\n信号: {signal}")
    print(f"卷积核: {kernel}")

    # mode='valid': 只计算完全重叠的部分
    result_valid = np.convolve(signal, kernel, mode='valid')
    print(f"\nconvolve (mode='valid'): {result_valid}")

    # mode='same': 输出与输入长度相同
    result_same = np.convolve(signal, kernel, mode='same')
    print(f"convolve (mode='same'): {result_same}")

    # mode='full': 完整卷积（默认）
    result_full = np.convolve(signal, kernel, mode='full')
    print(f"convolve (mode='full'): {result_full}")

    # 移动平均（卷积应用）
    data = np.array([3, 5, 7, 2, 8, 4, 6, 9])
    window_size = 3
    moving_avg_kernel = np.ones(window_size) / window_size

    print(f"\n原始数据: {data}")
    print(f"移动平均窗口: {window_size}")

    smoothed = np.convolve(data, moving_avg_kernel, mode='valid')
    print(f"平滑后: {np.round(smoothed, 2)}")

    print("\n" + "=" * 60)
    print("2. correlate - 互相关运算")
    print("=" * 60)

    print("\n互相关用于检测两个信号的相似性")

    signal1 = np.array([1, 2, 3, 4, 5])
    signal2 = np.array([2, 3, 4])

    print(f"\n信号1: {signal1}")
    print(f"信号2: {signal2}")

    # 互相关
    corr = np.correlate(signal1, signal2, mode='valid')
    print(f"\ncorrelate (mode='valid'): {corr}")

    # 寻找模式
    print("\n应用：在长信号中查找模式")
    long_signal = np.array([1, 2, 3, 1, 2, 3, 4, 1, 2, 3])
    pattern = np.array([1, 2, 3])

    correlation = np.correlate(long_signal, pattern, mode='valid')
    print(f"长信号: {long_signal}")
    print(f"模式: {pattern}")
    print(f"相关系数: {correlation}")

    # 找到最大相关位置
    max_idx = np.argmax(correlation)
    print(f"最佳匹配位置: 索引 {max_idx}")
    print(f"该位置的值: {long_signal[max_idx:max_idx+len(pattern)]}")

    print("\n" + "=" * 60)
    print("3. gradient - 梯度计算")
    print("=" * 60)

    print("\ngradient 计算离散数据的导数/梯度")

    # 一维梯度
    x = np.array([1, 2, 4, 7, 11, 16])
    print(f"\n值: {x}")

    grad = np.gradient(x)
    print(f"梯度: {grad}")
    print(f"说明: {x[1]-x[0]}, {x[2]-x[1]}, ...")

    # 多维梯度
    z = np.array([[1, 2, 4],
                  [2, 4, 8],
                  [3, 6, 12]])

    print(f"\n二维数组:")
    print(z)

    grad_y, grad_x = np.gradient(z)
    print(f"\nX 方向梯度 (列方向):")
    print(grad_x)
    print(f"Y 方向梯度 (行方向):")
    print(grad_y)

    # 物理应用：速度和加速度
    t = np.array([0, 1, 2, 3, 4])  # 时间
    position = np.array([0, 3, 8, 15, 24])  # 位置: x = t²

    print(f"\n位置随时间变化:")
    print(f"时间: {t}")
    print(f"位置: {position}")

    velocity = np.gradient(position, t)
    print(f"速度 (ds/dt): {velocity}")

    acceleration = np.gradient(velocity, t)
    print(f"加速度 (dv/dt): {acceleration}")

    print("\n" + "=" * 60)
    print("4. trapz - 梯形积分")
    print("=" * 60)

    print("\ntrapz 使用梯形法则计算定积分")

    # 简单积分
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])  # y = x²

    print(f"\nx = {x}")
    print(f"y = {y}")

    integral = np.trapz(y, x)
    print(f"\n∫x²dx 从 0 到 4: {integral:.2f}")
    print(f"精确值: 4³/3 = {64/3:.2f}")

    # 不指定 x（假设间隔为1）
    integral_unit = np.trapz(y)
    print(f"\ntrapz(y) [默认 dx=1]: {integral_unit:.2f}")

    # 二维积分
    z = np.array([[1, 2, 3],
                  [2, 4, 6],
                  [3, 6, 9]])

    print(f"\n二维数组:")
    print(z)

    integral_2d = np.trapz(np.trapz(z))
    print(f"二维积分: {integral_2d}")

    print("\n" + "=" * 60)
    print("5. diff - 离散差分")
    print("=" * 60)

    print("\ndiff 计算相邻元素的差分")

    arr = np.array([1, 5, 3, 8, 2, 9])
    print(f"\n原数组: {arr}")

    # 一阶差分
    diff1 = np.diff(arr)
    print(f"一阶差分: {diff1}")

    # 二阶差分
    diff2 = np.diff(arr, n=2)
    print(f"二阶差分: {diff2}")

    # 指定 n
    diff_n = np.diff(arr, n=3)
    print(f"三阶差分: {diff_n}")

    # 多维差分
    arr_2d = np.array([[1, 3, 6, 10],
                       [2, 6, 12, 20]])

    print(f"\n二维数组:")
    print(arr_2d)

    print(f"\n沿 axis=0 差分:")
    print(np.diff(arr_2d, axis=0))

    print(f"沿 axis=1 差分:")
    print(np.diff(arr_2d, axis=1))

    print("\n" + "=" * 60)
    print("6. ediff1d - 差分扩展")
    print("=" * 60)

    arr = np.array([1, 3, 6, 10])
    print(f"原数组: {arr}")

    ediff = np.ediff1d(arr)
    print(f"ediff1d: {ediff}")
    print(f"说明: [3-1, 6-3, 10-6]")

    # 指定预填充值
    ediff_fill = np.ediff1d(arr, to_begin=-99, to_end=999)
    print(f"\nediff1d (to_begin=-99, to_end=999):")
    print(ediff_fill)

    print("\n" + "=" * 60)
    print("7. 实际应用案例")
    print("=" * 60)

    print("\n案例1: 图像边缘检测（梯度）")
    print("-" * 40)

    # 简单的 5x5 图像
    image = np.array([[0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0],
                      [0, 1, 2, 1, 0],
                      [0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0]])

    print("原图像:")
    print(image)

    # 计算梯度（边缘强度）
    grad_y, grad_x = np.gradient(image)
    edge_strength = np.sqrt(grad_x**2 + grad_y**2)

    print("\n边缘强度:")
    print(edge_strength)

    print("\n案例2: 信号平滑（卷积）")
    print("-" * 40)

    # 带噪声的信号
    t = np.linspace(0, 2*np.pi, 50)
    clean_signal = np.sin(t)
    noise = np.random.randn(50) * 0.3
    noisy_signal = clean_signal + noise

    print(f"信号长度: {len(noisy_signal)}")

    # 高斯平滑核
    gaussian_kernel = np.array([0.05, 0.1, 0.2, 0.3, 0.2, 0.1, 0.05])
    gaussian_kernel /= gaussian_kernel.sum()  # 归一化

    smoothed = np.convolve(noisy_signal, gaussian_kernel, mode='same')

    print(f"\n前 10 点:")
    print(f"  原始: {noisy_signal[:10]}")
    print(f"  平滑: {smoothed[:10]}")

    print("\n案例3: 数值积分")
    print("-" * 40)

    # 计算曲线下的面积
    x = np.linspace(0, np.pi, 100)
    y = np.sin(x)

    integral = np.trapz(y, x)
    print(f"\n∫sin(x)dx 从 0 到 π: {integral:.4f}")
    print(f"精确值: 2.0000")

    print("\n案例4: 数据变化检测")
    print("-" * 40)

    stock_prices = np.array([100, 102, 101, 105, 110, 108, 112])
    print(f"股价: {stock_prices}")

    changes = np.diff(stock_prices)
    print(f"每日变化: {changes}")

    # 找到最大上涨日
    max_increase_idx = np.argmax(changes)
    print(f"\n最大上涨: 第 {max_increase_idx + 1} -> {max_increase_idx + 2} 天")
    print(f"上涨: {changes[max_increase_idx]}")

    print("\n案例5: 卷积核设计")
    print("-" * 40)

    print("不同卷积核的效果:")

    signal = np.array([0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0])

    # 平滑核
    smooth_kernel = np.ones(3) / 3

    # 锐化核
    sharpen_kernel = np.array([0, -1, 0, -1, 5, -1, 0, -1, 0])

    print(f"\n原信号: {signal}")

    print(f"\n平滑核: {smooth_kernel}")
    print(f"平滑结果: {np.convolve(signal, smooth_kernel, mode='same')}")

    # 简单锐化
    simple_sharpen = np.array([0, -1, 1])
    print(f"\n锐化核: {simple_sharpen}")
    print(f"锐化结果: {np.convolve(signal, simple_sharpen, mode='same')}")

    print("\n" + "=" * 60)
    print("8. 信号处理函数速查")
    print("=" * 60)

    print("\n卷积与相关:")
    print("  np.convolve(a, v, mode='valid')   # 一维卷积")
    print("  np correlate(a, v, mode='valid')  # 一维互相关")
    print("  mode: 'valid' | 'same' | 'full'")

    print("\n梯度与差分:")
    print("  np.gradient(f)                    # 梯度")
    print("  np.diff(a, n=1)                   # 差分")
    print("  np.ediff1d(a, to_begin, to_end)   # 扩展差分")

    print("\n积分:")
    print("  np.trapz(y, x=None, dx=1.0)       # 梯形积分")
    print("  np.trapz(np.trapz(z))             # 二维积分")

    print("\n" + "=" * 60)
    print("9. 性能提示")
    print("=" * 60)

    print("\n性能考虑:")
    print("  1. 大数组使用 mode='same' 或 mode='valid' 更快")
    print("  2. 使用 scipy.signal 可获得更多信号处理函数")
    print("  3. 二维卷积使用 scipy.signal.convolve2d")
    print("  4. 频域卷积（FFT）对大核更高效")

    print("\n与 scipy 的关系:")
    print("  NumPy: 基础函数")
    print("  scipy.signal: 高级信号处理（滤波器设计、频谱分析等）")

    print("\n常用场景:")
    print("  - 图像处理: 平滑、锐化、边缘检测")
    print("  - 时间序列: 去噪、趋势分析")
    print("  - 科学计算: 数值微分、数值积分")
    print("  - 特征提取: 梯度特征、变化率")


if __name__ == "__main__":
    main()