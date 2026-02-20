#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 30：NumPy FFT 高级操作 (实数FFT、DCT、窗函数等)。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/30_fft_advanced.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=== 实数 FFT (rfft/irfft) ===")

    # 1. rfft - 实数输入的优化 FFT
    signal = np.array([0, 1, 0, 0, 0, 0, 0, 0], dtype=float)
    print("原始信号 (实数):", signal)

    # 普通 FFT (复数输出)
    fft_full = np.fft.fft(signal)
    print("\n完整 FFT (复数):")
    print(fft_full)

    # rfft - 只返回非负频率部分 (实数输入时效率更高)
    rfft_result = np.fft.rfft(signal)
    print("\nrFFT (只非负频率):")
    print(rfft_result)

    # 逆变换
    reconstructed_rfft = np.fft.irfft(rfft_result)
    print("\nirFFT 重构:")
    print(reconstructed_rfft)

    # 2. rfft 的应用 - 频谱分析
    print("\n=== 频谱分析 (实数信号) ===")
    # 创建一个包含两个频率成分的实数信号
    t = np.linspace(0, 1, 1000, endpoint=False)
    signal_real = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)

    # 使用 rfft
    spectrum = np.fft.rfft(signal_real)
    freqs = np.fft.rfftfreq(len(t), d=t[1] - t[0])

    print(f"信号长度: {len(signal_real)}")
    print(f"rFFT 输出长度: {len(spectrum)} (约为原始长度的一半)")
    print(f"频率分辨率: {freqs[1] - freqs[0]:.4f} Hz")

    # 找主要频率
    main_freq_idx = np.argmax(np.abs(spectrum[1:])) + 1  # 跳过直流分量
    print(f"主频率: {freqs[main_freq_idx]:.2f} Hz")

    # 3. 不同类型的 FFT
    print("\n=== 不同类型的 FFT ===")

    signal_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=float)
    print("2D 信号:")
    print(signal_2d)

    # fft2 - 2D FFT
    fft2_result = np.fft.fft2(signal_2d)
    print("\nfft2 结果形状:", fft2_result.shape)

    # rfft2 - 实数 2D FFT
    rfft2_result = np.fft.rfft2(signal_2d)
    print("rfft2 结果形状:", rfft2_result.shape)

    # 4. FFT 窗口函数
    print("\n=== FFT 窗口函数 ===")

    N = 64
    n = np.arange(N)

    # 窗口函数用于减少频谱泄漏
    windows = {
        "矩形窗": np.ones(N),
        "汉宁窗": np.hanning(N),
        "汉明窗": np.hamming(N),
        "布莱克曼窗": np.blackman(N),
        "巴特利特窗": np.bartlett(N),
    }

    for name, window in windows.items():
        print(f"{name}: 峰值 = {window.max():.4f}, 旁瓣衰减特性不同")

    # 5. 窗函数的效果
    print("\n=== 窗函数对 FFT 的影响 ===")
    # 创建一个截断的正弦波
    t = np.linspace(0, 1, 100, endpoint=False)
    signal_truncated = np.sin(2 * np.pi * 10 * t)
    # 只取前 50 个点 (相当于加矩形窗)
    signal_truncated[50:] = 0

    # 加窗
    window = np.hanning(100)
    signal_windowed = signal_truncated * window

    # 比较 FFT
    fft_rect = np.fft.rfft(signal_truncated)
    fft_windowed = np.fft.rfft(signal_windowed)

    print("矩形窗 FFT - 最大幅值:", np.abs(fft_rect).max())
    print("汉宁窗 FFT - 最大幅值:", np.abs(fft_windowed).max())

    # 6. FFT 频率定位
    print("\n=== FFT 频率定位 ===")
    sample_rate = 1000  # 采样率 1kHz
    duration = 1  # 1秒
    N = int(sample_rate * duration)
    t = np.linspace(0, duration, N, endpoint=False)

    # 100 Hz 信号
    signal_100hz = np.sin(2 * np.pi * 100 * t)
    fft_result = np.fft.fft(signal_100hz)
    freqs = np.fft.fftfreq(N, d=1/sample_rate)

    # 找到最大幅值对应的频率
    peak_idx = np.argmax(np.abs(fft_result))
    peak_freq = np.abs(freqs[peak_idx])
    print(f"实际频率: 100 Hz, FFT 识别频率: {peak_freq:.2f} Hz")

    # 7. rfft 用于滤波
    print("\n=== 使用 rfft 进行滤波 ===")

    # 创建带噪声的信号
    t = np.linspace(0, 1, 1000, endpoint=False)
    clean_signal = np.sin(2 * np.pi * 10 * t)
    noise = 0.5 * np.sin(2 * np.pi * 100 * t)
    noisy_signal = clean_signal + noise

    # FFT
    spectrum = np.fft.rfft(noisy_signal)
    freqs = np.fft.rfftfreq(len(t), d=t[1] - t[0])

    # 低通滤波：去除高频
    cutoff = 30  # 截止频率 30Hz
    spectrum_filtered = spectrum.copy()
    spectrum_filtered[freqs > cutoff] = 0

    # IFFT 重构
    filtered_signal = np.fft.irfft(spectrum_filtered)

    print("原始信号能量:", np.sum(noisy_signal**2))
    print("滤波后信号能量:", np.sum(filtered_signal**2))
    print("高频噪声被抑制")

    # 8. STFT (短时傅里叶变换) 概念
    print("\n=== STFT 概念 ===")
    # 将信号分成重叠窗口，对每个窗口做 FFT
    signal = np.random.randn(1000)
    window_size = 100
    overlap = 50

    n_windows = (len(signal) - window_size) // (window_size - overlap) + 1
    print(f"信号长度: {len(signal)}")
    print(f"窗口大小: {window_size}")
    print(f"重叠: {overlap}")
    print(f"窗口数量: {n_windows}")
    print("每个窗口独立做 FFT 可得时频谱")

    # 9. 零填充 FFT
    print("\n=== 零填充 FFT (提高频率分辨率) ===")

    signal_short = np.array([1, 2, 3, 4], dtype=float)
    print("短信号长度:", len(signal_short))

    # 普通 FFT
    fft_short = np.fft.fft(signal_short)
    print("FFT 长度:", len(fft_short))

    # 零填充到 16 点
    fft_padded = np.fft.fft(signal_short, n=16)
    print("零填充 FFT 长度:", len(fft_padded))
    print("零填充提供了更密集的频率网格")

    # 10. 实数 FFT 的对称性
    print("\n=== 实数 FFT 的对称性 ===")
    real_signal = np.array([1, 2, 3, 4, 3, 2, 1], dtype=float)
    fft_complex = np.fft.fft(real_signal)

    print("实数信号:", real_signal)
    print("\nFFT 结果:")
    print(fft_complex)
    print("\n注意: 实数信号的 FFT 具有共轭对称性")
    print("即 FFT[k] = conj(FFT[N-k])")

    # 11. 逆 FFT 的归一化
    print("\n=== 逆 FFT 归一化 ===")
    original = np.array([1, 2, 3, 4], dtype=float)
    fft_forward = np.fft.fft(original)
    fft_backward = np.fft.ifft(fft_forward)

    print("原始:", original)
    print("FFT -> IFFT:", fft_backward)
    print("误差:", np.max(np.abs(original - fft_backward)))


if __name__ == "__main__":
    main()