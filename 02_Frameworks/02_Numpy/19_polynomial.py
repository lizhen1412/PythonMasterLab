#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 19：Polynomial - 多项式运算。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/19_polynomial.py

NumPy 的 polynomial 模块提供了完整的多项式操作功能，包括
多项式拟合、求值、求根、算术运算等。

本节演示：
1. 多项式表示与创建
2. 多项式求值
3. 多项式算术运算
4. 多项式求根
5. 多项式拟合
6. 切比雪夫和勒让德多项式
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. 多项式表示与创建")
    print("=" * 60)

    # 多项式: P(x) = 3x^2 + 2x + 1
    # 系数按幂次升序排列: [1, 2, 3]
    coefs = [1, 2, 3]
    p = np.poly1d(coefs)

    print(f"\n多项式 P(x) = 3x^2 + 2x + 1:")
    print(p)
    print(f"系数: {p.coefs}")
    print(f"阶数: {p.order}")

    # 另一种创建方式
    p2 = np.poly1d([1, -2, 1])  # x^2 - 2x + 1 = (x-1)^2
    print(f"\n多项式 Q(x) = x^2 - 2x + 1:")
    print(p2)

    # 从根创建多项式
    roots = [1, 2, 3]
    p_from_roots = np.poly(roots)
    print(f"\n从根 [1, 2, 3] 创建的多项式:")
    print(f"系数: {p_from_roots}")
    print(f"展开: (x-1)(x-2)(x-3) = {np.poly1d(p_from_roots)}")

    print("\n" + "=" * 60)
    print("2. 多项式求值")
    print("=" * 60)

    p = np.poly1d([1, 2, 3])  # 3x^2 + 2x + 1

    print(f"\n多项式: {p}")

    # 在单点求值
    x_values = [0, 1, 2, -1, 0.5]
    print(f"\n在多个点求值:")
    for x in x_values:
        y = p(x)
        print(f"  P({x}) = {y}")

    # 使用 polyval 批量求值
    x_array = np.array([0, 1, 2, 3, 4, 5])
    y_array = np.polyval(p.coefs, x_array)
    print(f"\n批量求值 P([0,1,2,3,4,5]):")
    print(f"  x = {x_array}")
    print(f"  P(x) = {y_array}")

    # 在多个点同时求值（使用 poly1d）
    y_direct = p(x_array)
    print(f"\n使用 poly1d 直接求值:")
    print(f"  P(x) = {y_direct}")

    print("\n" + "=" * 60)
    print("3. 多项式算术运算")
    print("=" * 60)

    p1 = np.poly1d([1, 2, 1])  # x^2 + 2x + 1 = (x+1)^2
    p2 = np.poly1d([1, -1])    # x - 1

    print(f"\nP1(x) = {p1}")
    print(f"P2(x) = {p2}")

    # 加法
    p_sum = p1 + p2
    print(f"\n加法: P1 + P2 = {p_sum}")

    # 减法
    p_diff = p1 - p2
    print(f"减法: P1 - P2 = {p_diff}")

    # 乘法
    p_prod = p1 * p2
    print(f"乘法: P1 * P2 = {p_prod}")

    # 除法（带余数）
    quotient, remainder = p1 / p2
    print(f"\n除法: P1 / P2")
    print(f"  商: {quotient}")
    print(f"  余数: {remainder}")
    print(f"  验证: P1 = P2 * 商 + 余数")

    # 幂运算
    p_power = p2 ** 3
    print(f"\n幂运算: P2^3 = {p_power}")

    print("\n" + "=" * 60)
    print("4. 多项式求根")
    print("=" * 60)

    # 二次方程: x^2 - 3x + 2 = 0
    p_quad = np.poly1d([1, -3, 2])
    print(f"\n多项式: {p_quad}")

    roots = np.roots(p_quad.coefs)
    print(f"根: {roots}")
    print(f"验证: P(1) = {p_quad(1)}, P(2) = {p_quad(2)}")

    # 三次方程
    p_cubic = np.poly1d([1, -6, 11, -6])  # (x-1)(x-2)(x-3)
    print(f"\n多项式: {p_cubic}")

    roots_cubic = np.roots(p_cubic.coefs)
    print(f"根: {roots_cubic}")

    # 复根情况
    p_complex = np.poly1d([1, 0, 1])  # x^2 + 1
    print(f"\n多项式: {p_complex}")
    print(f"根: {np.roots(p_complex.coefs)}")

    print("\n" + "=" * 60)
    print("5. 多项式导数和积分")
    print("=" * 60)

    p = np.poly1d([1, 3, 3, 1])  # x^3 + 3x^2 + 3x + 1 = (x+1)^3

    print(f"\n原多项式: {p}")

    # 一阶导数
    p_deriv1 = p.deriv()
    print(f"一阶导数: {p_deriv1}")

    # 二阶导数
    p_deriv2 = p.deriv(2)
    print(f"二阶导数: {p_deriv2}")

    # 积分
    p_integ = p.integ()
    print(f"不定积分: {p_integ} + C")

    # 定积分
    integral_value = p_integ(2) - p_integ(0)
    print(f"\n定积分 [0, 2]: {integral_value}")

    print("\n" + "=" * 60)
    print("6. 多项式拟合")
    print("=" * 60)

    # 创建带有噪声的数据
    np.random.seed(42)
    x = np.linspace(-5, 5, 50)
    # 真实函数: y = 2x^2 - 3x + 1 + 噪声
    y_true = 2 * x**2 - 3 * x + 1
    y = y_true + np.random.randn(len(x)) * 2

    print(f"\n数据点: {len(x)} 个")
    print(f"真实多项式: 2x^2 - 3x + 1")

    # 线性拟合
    coefs_linear = np.polyfit(x, y, 1)
    p_linear = np.poly1d(coefs_linear)
    print(f"\n一次拟合: {p_linear}")

    # 二次拟合
    coefs_quadratic = np.polyfit(x, y, 2)
    p_quadratic = np.poly1d(coefs_quadratic)
    print(f"二次拟合: {p_quadratic}")

    # 三次拟合
    coefs_cubic = np.polyfit(x, y, 3)
    p_cubic_fit = np.poly1d(coefs_cubic)
    print(f"三次拟合: {p_cubic_fit}")

    # 计算拟合误差
    mse_linear = np.mean((y - p_linear(x))**2)
    mse_quadratic = np.mean((y - p_quadratic(x))**2)
    mse_cubic = np.mean((y - p_cubic_fit(x))**2)

    print(f"\n均方误差:")
    print(f"  一次: {mse_linear:.3f}")
    print(f"  二次: {mse_quadratic:.3f}")
    print(f"  三次: {mse_cubic:.3f}")

    print("\n" + "=" * 60)
    print("7. Polynomial 类（新 API，推荐）")
    print("=" * 60)

    from numpy.polynomial import Polynomial

    # 创建多项式: P(x) = 2x^2 - 3x + 1
    p_new = Polynomial([1, -3, 2])
    print(f"\n多项式: {p_new}")
    print(f"系数: {p_new.coef()}")

    # 求值
    print(f"P(2) = {p_new(2)}")
    print(f"P([0, 1, 2]) = {p_new([0, 1, 2])}")

    # 算术运算
    p1_new = Polynomial([1, 2, 1])  # x^2 + 2x + 1
    p2_new = Polynomial([1, -1])    # x - 1

    print(f"\nP1 = {p1_new}")
    print(f"P2 = {p2_new}")
    print(f"P1 + P2 = {p1_new + p2_new}")
    print(f"P1 * P2 = {p1_new * p2_new}")

    # 求根
    roots_new = p_new.roots()
    print(f"\n根: {roots_new}")

    # 导数
    deriv_new = p_new.deriv()
    print(f"导数: {deriv_new}")

    print("\n" + "=" * 60)
    print("8. 切比雪夫多项式 (Chebyshev)")
    print("=" * 60)

    from numpy.polynomial import Chebyshev

    # 切比雪夫多项式在区间 [-1, 1] 上正交
    # T_n(x) = cos(n * arccos(x))

    # T_0(x) = 1
    # T_1(x) = x
    # T_2(x) = 2x^2 - 1
    # T_3(x) = 4x^3 - 3x

    print("\n切比雪夫多项式前几项在 x = 0.5 的值:")
    x = 0.5
    for n in range(5):
        # 创建第 n 个切比雪夫多项式
        t = Chebyshev.basis(n)
        y = t(x)
        print(f"  T_{n}({x}) = {y:.4f}")

    # 使用切比雪夫多项式拟合
    x_data = np.linspace(-1, 1, 20)
    y_data = np.cos(4 * np.arccos(x_data))  # T_4(x)

    # 用切比雪夫级数拟合
    t_fit = Chebyshev.fit(x_data, y_data, 4)
    print(f"\n拟合的切比雪夫系数:")
    print(f"  {t_fit.coef}")

    print("\n" + "=" * 60)
    print("9. 勒让德多项式 (Legendre)")
    print("=" * 60)

    from numpy.polynomial import Legendre

    # 勒让德多项式在区间 [-1, 1] 上正交
    # P_0(x) = 1
    # P_1(x) = x
    # P_2(x) = (3x^2 - 1) / 2
    # P_3(x) = (5x^3 - 3x) / 2

    print("\n勒让德多项式前几项在 x = 0.5 的值:")
    x = 0.5
    for n in range(5):
        p = Legendre.basis(n)
        y = p(x)
        print(f"  P_{n}({x}) = {y:.4f}")

    # 勒让德级数展开
    # 在 [-1, 1] 上的函数可以用勒让德多项式展开
    x_data = np.linspace(-1, 1, 100)
    y_data = x_data**3  # f(x) = x^3

    # 用勒让德级数拟合
    l_fit = Legendre.fit(x_data, y_data, 5)
    print(f"\n拟合的勒让德系数:")
    print(f"  {l_fit.coef}")

    print("\n" + "=" * 60)
    print("10. 实际应用")
    print("=" * 60)

    print("\n应用1: 数据插值")
    print("  - 使用多项式插值通过所有数据点")
    print("  - 高次多项式可能出现龙格现象")

    print("\n应用2: 曲线拟合")
    print("  - 低次多项式拟合平滑数据")
    print("  - 常用于趋势分析和预测")

    print("\n应用3: 信号处理")
    print("  - 切比雪夫滤波器设计")
    print("  - 勒让德多项式在球谐函数中的应用")

    print("\n应用4: 数值积分")
    print("  - 高斯求积使用勒让德多项式的零点")
    print("  - 切比雪夫节点用于插值")

    print("\n应用5: 近似理论")
    print("  - 函数逼近")
    print("  - 最优一致逼近")

    print("\n" + "=" * 60)
    print("11. 多项式操作速查")
    print("=" * 60)

    print("\n创建多项式:")
    print("  np.poly1d([c0, c1, ..., cn])  # 从系数创建")
    print("  Polynomial([c0, c1, ..., cn])  # 新 API")
    print("  np.poly([r1, r2, ...])        # 从根创建")

    print("\n多项式求值:")
    print("  p(x)                          # 单点或数组")
    print("  np.polyval(coefs, x)          # 从系数直接求值")

    print("\n多项式运算:")
    print("  p1 + p2, p1 - p2, p1 * p2     # 算术运算")
    print("  p1 / p2                       # 除法，返回 (商, 余数)")
    print("  p ** n                        # 幂运算")

    print("\n多项式属性:")
    print("  p.coefs / p.coef              # 系数")
    print("  p.order                       # 阶数")
    print("  np.roots(coefs)               # 求根")
    print("  p.deriv(), p.integ()          # 导数和积分")

    print("\n多项式拟合:")
    print("  np.polyfit(x, y, deg)         # 最小二乘拟合")
    print("  Chebyshev.fit(x, y, deg)      # 切比雪夫拟合")
    print("  Legendre.fit(x, y, deg)       # 勒让德拟合")

    print("\n特殊多项式基:")
    print("  Polynomial.basis(n)           # 普通多项式基")
    print("  Chebyshev.basis(n)            # 切比雪夫基")
    print("  Legendre.basis(n)             # 勒让德基")
    print("  Hermite.basis(n)              # 厄米特基")
    print("  Laguerre.basis(n)             # 拉盖尔基")


if __name__ == "__main__":
    main()