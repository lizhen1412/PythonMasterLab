#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：使用 FFT 进行频谱分析。
Author: Lambert

题目：
创建一个包含 10Hz 和 50Hz 两个频率成分的信号，
使用 FFT 找出主要的频率成分。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/10_fft_filter.py
"""

from __future__ import annotations

import numpy as np


def find_dominant_frequency(signal: np.ndarray, sample_rate: float) -> float:
    """找出信号中的主频率"""
    spectrum = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), d=1/sample_rate)

    # 找最大幅值对应的频率（跳过直流分量）
    peak_idx = np.argmax(np.abs(spectrum[1:])) + 1
    return float(freqs[peak_idx])


def check(label: str, got: float, expected: float, tol: float = 1.0) -> None:
    ok = abs(got - expected) < tol
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got:.2f}Hz expected={expected:.2f}Hz")


def main() -> None:
    # 创建 10Hz 信号
    sample_rate = 1000
    duration = 1
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal_10hz = np.sin(2 * np.pi * 10 * t)

    freq = find_dominant_frequency(signal_10hz, sample_rate)
    check("10Hz signal", freq, 10.0)

    # 创建 50Hz 信号
    signal_50hz = np.sin(2 * np.pi * 50 * t)
    freq = find_dominant_frequency(signal_50hz, sample_rate)
    check("50Hz signal", freq, 50.0)


if __name__ == "__main__":
    main()