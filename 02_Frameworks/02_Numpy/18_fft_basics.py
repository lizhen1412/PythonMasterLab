#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 18：FFT (Fast Fourier Transform) - 快速傅里叶变换。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/18_fft_basics.py

傅里叶变换是信号处理的核心工具，用于将时域信号转换为频域表示。
NumPy 的 fft 模块提供了高效的 FFT 实现。

本节演示：
1. 一维 FFT (fft/ifft)
2. 频率和 fftfreq
3. FFT 频谱分析
4. 信号滤波应用
5. 二维 FFT (fft2/ifft2)
"""

from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main() -> None:
    print("=" * 60)
    print("1. 一维 FFT 基础")
    print("=" * 60)

    # 创建简单信号
    n = 8
    x = np.array([1, 2, 3, 4, 5, 4, 3, 2], dtype=float)

    print(f"\n原始信号 x: {x}")

    # FFT
    X = np.fft.fft(x)
    print(f"\nFFT 结果 X: {X}")
    print(f"类型: {X.dtype}")
    print(f"实部: {X.real}")
    print(f"虚部: {X.imag}")

    # IFFT (逆变换)
    x_reconstructed = np.fft.ifft(X)
    print(f"\nIFFF 重建 x: {x_reconstructed}")
    print(f"与原信号误差: {np.max(np.abs(x - x_reconstructed)):.2e}")

    print("\n" + "=" * 60)
    print("2. 频率分析 - fftfreq")
    print("=" * 60)

    # 采样参数
    sample_rate = 1000  # 采样率 1000 Hz
    duration = 1  # 1 秒
    n_samples = sample_rate * duration

    # 生成包含两个频率分量的信号
    t = np.linspace(0, duration, n_samples, endpoint=False)
    freq1, freq2 = 50, 120  # 50 Hz 和 120 Hz
    signal = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)

    print(f"\n信号参数:")
    print(f"  采样率: {sample_rate} Hz")
    print(f"  时长: {duration} 秒")
    print(f"  采样点数: {n_samples}")
    print(f"  频率分量: {freq1} Hz, {freq2} Hz")

    # FFT
    fft_result = np.fft.fft(signal)

    # 频率轴
    frequencies = np.fft.fftfreq(n_samples, d=1/sample_rate)

    print(f"\nFFT 结果形状: {fft_result.shape}")
    print(f"频率轴形状: {frequencies.shape}")
    print(f"频率范围: {frequencies.min():.1f} Hz ~ {frequencies.max():.1f} Hz")

    # 只取正频率部分
    positive_freq_idx = frequencies > 0
    positive_freqs = frequencies[positive_freq_idx]
    positive_fft = np.abs(fft_result[positive_freq_idx])

    print(f"\n正频率范围: {positive_freqs.min():.1f} ~ {positive_freqs.max():.1f} Hz")

    # 找到主要频率
    peak_indices = np.argsort(positive_fft)[-5:][::-1]
    print(f"\n能量最高的 5 个频率:")
    for idx in peak_indices:
        print(f"  {positive_freqs[idx]:.1f} Hz: 幅度 {positive_fft[idx]:.2f}")

    print("\n" + "=" * 60)
    print("3. 实际信号分析")
    print("=" * 60)

    # 创建更复杂的信号：正弦波 + 噪声
    np.random.seed(42)
    t = np.linspace(0, 1, 500, endpoint=False)
    clean_signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)
    noise = 0.3 * np.random.randn(len(t))
    noisy_signal = clean_signal + noise

    print(f"\n信号成分:")
    print(f"  10 Hz 正弦波 + 50 Hz 正弦波 + 高斯噪声")

    # FFT 分析
    fft_noisy = np.fft.fft(noisy_signal)
    freqs = np.fft.fftfreq(len(t), d=t[1] - t[0])

    # 功率谱
    power = np.abs(fft_noisy) ** 2

    # 正频率
    pos_mask = freqs > 0
    pos_freqs = freqs[pos_mask]
    pos_power = power[pos_mask]

    print(f"\n主要频率成分（功率谱）:")
    top_indices = np.argsort(pos_power)[-10:][::-1]
    for i, idx in enumerate(top_indices[:5], 1):
        print(f"  {i}. {pos_freqs[idx]:.1f} Hz: 功率 {pos_power[idx]:.2f}")

    print("\n" + "=" * 60)
    print("4. 信号滤波应用")
    print("=" * 60)

    # 创建带噪声的信号
    t = np.linspace(0, 1, 1000, endpoint=False)
    # 主信号 5 Hz
    signal_clean = np.sin(2 * np.pi * 5 * t)
    # 添加高频噪声 100 Hz
    noise_high = 0.5 * np.sin(2 * np.pi * 100 * t)
    noisy = signal_clean + noise_high

    print(f"\n滤波前:")
    print(f"  主信号: 5 Hz")
    print(f"  噪声: 100 Hz")

    # FFT
    fft_noisy = np.fft.fft(noisy)
    freqs = np.fft.fftfreq(len(t), d=t[1] - t[0])

    # 低通滤波：保留低于 20 Hz 的频率
    cutoff_freq = 20
    filter_mask = np.abs(freqs) < cutoff_freq
    fft_filtered = fft_noisy * filter_mask

    # IFFT 重建
    signal_filtered = np.fft.ifft(fft_filtered).real

    print(f"\n低通滤波 (截止频率 {cutoff_freq} Hz):")
    print(f"  保留频率点数: {filter_mask.sum()} / {len(filter_mask)}")

    # 计算信噪比改善
    noise_before = np.std(noisy - signal_clean)
    noise_after = np.std(signal_filtered - signal_clean)
    print(f"  噪声标准差: {noise_before:.3f} -> {noise_after:.3f}")
    print(f"  噪声降低: {(1 - noise_after/noise_before)*100:.1f}%")

    print("\n" + "=" * 60)
    print("5. fftshift - 零频率居中")
    print("=" * 60)

    signal = np.array([1, 2, 3, 4, 5, 4, 3, 2], dtype=float)
    fft_result = np.fft.fft(signal)

    print(f"\n原始 FFT 结果: {fft_result}")

    # fftshift 将零频率移到中心
    fft_shifted = np.fft.fftshift(fft_result)
    print(f"fftshift 后: {fft_shifted}")

    # 对应的频率
    freqs = np.fft.fftfreq(len(signal))
    freqs_shifted = np.fft.fftshift(freqs)
    print(f"原始频率: {freqs}")
    print(f"shift 频率: {freqs_shifted}")

    # ifftshift 反变换
    fft_unshifted = np.fft.ifftshift(fft_shifted)
    print(f"ifftshift 恢复: {fft_unshifted}")

    print("\n" + "=" * 60)
    print("6. 二维 FFT (图像处理基础)")
    print("=" * 60)

    # 创建简单的二维模式
    size = 8
    x = np.arange(size)
    xx, yy = np.meshgrid(x, x)

    # 创建条纹图案
    img = np.sin(2 * np.pi * xx / 4) + np.sin(2 * np.pi * yy / 8)

    print(f"\n原始图像 (8x8):")
    print(img.astype(int))

    # 2D FFT
    fft2 = np.fft.fft2(img)
    print(f"\n2D FFT 结果形状: {fft2.shape}")
    print(f"中心 (直流分量): {fft2[0, 0]:.2f}")

    # 频率居中
    fft2_shifted = np.fft.fftshift(fft2)

    # 2D IFFT 重建
    img_reconstructed = np.fft.ifft2(fft2).real
    print(f"\n重建误差: {np.max(np.abs(img - img_reconstructed)):.2e}")

    print("\n" + "=" * 60)
    print("7. FFT 窗函数")
    print("=" * 60)

    # 创建信号
    n = 100
    t = np.linspace(0, 1, n, endpoint=False)
    signal = np.sin(2 * np.pi * 10 * t)

    print(f"\n信号长度: {n}")
    print(f"不加窗时的频谱泄漏问题...")

    # 应用汉宁窗
    window = np.hanning(n)
    windowed_signal = signal * window

    print(f"窗函数: Hanning 窗")
    print(f"  窗的最大值: {window.max():.3f}")
    print(f"  窗的能量比: {np.sum(window**2) / n:.3f}")

    # FFT 比较
    fft_raw = np.fft.fft(signal)
    fft_windowed = np.fft.fft(windowed_signal)

    print(f"\n不加窗的最大旁瓣: {np.sort(np.abs(fft_raw))[-3]:.2f}")
    print(f"加窗后的最大旁瓣: {np.sort(np.abs(fft_windowed))[-3]:.2f}")

    print("\n" + "=" * 60)
    print("8. 实际应用示例")
    print("=" * 60)

    print("\n应用1: 音频音调检测")
    print("  - 使用 FFT 检测音频中的主频率")
    print("  - 可用于音高识别、和弦分析")

    print("\n应用2: 图像压缩")
    print("  - 2D FFT 用于 JPEG 压缩")
    print("  - 丢弃高频分量实现压缩")

    print("\n应用3: 信号去噪")
    print("  - 频域滤波去除特定频率噪声")
    print("  - 例如：去除 50/60 Hz 工频干扰")

    print("\n应用4: 快速卷积")
    print("  - 时域卷积 = 频域乘法")
    print("  - FFT 加速大信号卷积")

    print("\n" + "=" * 60)
    print("9. FFT 常用函数速查")
    print("=" * 60)

    print("\n一维 FFT:")
    print("  np.fft.fft(a)       - 正变换")
    print("  np.fft.ifft(a)      - 逆变换")
    print("  np.fft.rfft(a)      - 实数输入的 FFT（只返回正频率）")
    print("  np.fft.irfft(a)     - 实数输出的 IFFT")
    print("  np.fft.fftfreq(n, d) - 频率数组")
    print("  np.fft.fftshift(a)  - 零频率居中")
    print("  np.fft.ifftshift(a) - 反向 shift")

    print("\n二维 FFT:")
    print("  np.fft.fft2(a)      - 2D FFT")
    print("  np.fft.ifft2(a)     - 2D IFFT")
    print("  np.fft.fftn(a)      - N 维 FFT")
    print("  np.fft.ifftn(a)     - N 维 IFFT")

    print("\n窗函数:")
    print("  np.bartlett(M)      - Bartlett 窗")
    print("  np.blackman(M)      - Blackman 窗")
    print("  np.hamming(M)       - Hamming 窗")
    print("  np.hanning(M)       - Hanning 窗")
    print("  np.kaiser(M, beta)  - Kaiser 窗")

    print("\n" + "=" * 60)
    print("10. 性能提示")
    print("=" * 60)

    print("\nFFT 最快的情况:")
    print("  - 输入长度为 2 的幂次: 2^n")
    print("  - 输入长度为小质数的乘积: 2^m * 3^n * 5^p")

    # 性能测试
    sizes = [100, 128, 1000, 1024, 10000, 16384]
    print(f"\n不同长度 FFT 计算时间 (相对):")
    for size in sizes:
        x = np.random.randn(size)
        # 简单计时
        import time
        start = time.time()
        for _ in range(100):
            np.fft.fft(x)
        elapsed = time.time() - start
        print(f"  长度 {size:5d}: {elapsed*1000:.1f} ms")


if __name__ == "__main__":
    main()