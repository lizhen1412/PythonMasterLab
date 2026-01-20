#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 21：数学函数全集。

运行：
    python3 02_Frameworks/02_Numpy/21_math_functions_complete.py

知识点：
- 三角函数：sin/cos/tan/arcsin/arccos/arctan/arctan2
- 双曲函数：sinh/cosh/tanh/arcsinh/arccosh/arctanh
- 指数对数：exp/expm1/log/log1p/log10/log2
- 舍入：round/floor/ceil/trunc/fix
- 算术：add/subtract/multiply/divide
- 符号与绝对值：sign/negative/positive/abs
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    # 创建测试数据
    angles = np.array([0, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2])
    values = np.array([0.1, 1.0, 2.0, 10.0, 100.0])

    print("=" * 70)
    print("1. 三角函数")
    print("=" * 70)

    print("\n角度（弧度）:", angles)
    print("角度（度）:", np.degrees(angles))

    print("\n1.1 基本三角函数")
    print("-" * 70)
    print("sin(angles):", np.sin(angles))
    print("cos(angles):", np.cos(angles))
    print("tan(angles):", np.tan(angles))

    print("\n1.2 反三角函数")
    print("-" * 70)
    x = np.array([-1, -0.5, 0, 0.5, 1])
    print(f"x: {x}")
    print(f"arcsin(x): {np.arcsin(x)}")
    print(f"arccos(x): {np.arccos(x)}")
    print(f"arctan(x): {np.arctan(x)}")

    print("\n1.3 arctan2 - 四象限反正切")
    print("-" * 70)
    y = np.array([1, 1, -1, -1])
    x = np.array([1, -1, -1, 1])
    print(f"y: {y}")
    print(f"x: {x}")
    print(f"arctan2(y, x): {np.arctan2(y, x)}")
    print(f"角度（度）: {np.degrees(np.arctan2(y, x))}")

    print("\n1.4 度数转换")
    print("-" * 70)
    radians = np.array([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
    print(f"弧度: {radians}")
    print(f"度: {np.degrees(radians)}")
    print(f"rad2deg: {np.rad2deg(radians)}")

    degrees = np.array([0, 90, 180, 270, 360])
    print(f"\n度: {degrees}")
    print(f"弧度: {np.radians(degrees)}")
    print(f"deg2rad: {np.deg2rad(degrees)}")

    print("\n1.5 双曲函数")
    print("-" * 70)
    x = np.array([-2, -1, 0, 1, 2])
    print(f"x: {x}")
    print(f"sinh(x): {np.sinh(x)}")
    print(f"cosh(x): {np.cosh(x)}")
    print(f"tanh(x): {np.tanh(x)}")

    print("\n1.6 反双曲函数")
    print("-" * 70)
    x = np.array([0, 1, 2, 3])
    print(f"x: {x}")
    print(f"arcsinh(x): {np.arcsinh(x)}")
    print(f"arccosh(x+1): {np.arccosh(x + 1)}")
    print(f"arctanh(x/4): {np.arctanh(x / 4)}")

    print("\n" + "=" * 70)
    print("2. 指数与对数函数")
    print("=" * 70)

    print("\n2.1 指数函数")
    print("-" * 70)
    x = np.array([0, 1, 2, 5, 10])
    print(f"x: {x}")
    print(f"exp(x): {np.exp(x)}")

    print("\nexpm1(x) = exp(x) - 1（小 x 时更精确）")
    print(f"x: [0.001, 0.01, 0.1]")
    x_small = np.array([0.001, 0.01, 0.1])
    print(f"exp(x) - 1: {np.exp(x_small) - 1}")
    print(f"expm1(x): {np.expm1(x_small)}")

    print("\n2.2 对数函数")
    print("-" * 70)
    x = np.array([0.1, 1, 2, 10, 100])
    print(f"x: {x}")
    print(f"loge(x) = log(x): {np.log(x)}")
    print(f"log10(x): {np.log10(x)}")
    print(f"log2(x): {np.log2(x)}")

    print("\nlog1p(x) = log(1 + x)（小 x 时更精确）")
    print(f"x: [0.001, 0.01, 0.1]")
    print(f"log(1 + x): {np.log(1 + x_small)}")
    print(f"log1p(x): {np.log1p(x_small)}")

    print("\n2.3 指数基数调整")
    print("-" * 70)
    print(f"exp2(x) = 2^x: {np.exp2(np.array([0, 1, 2, 3]))}")
    print(f"power(2, x) = 2^x: {np.power(2, np.array([0, 1, 2, 3]))}")

    print("\n" + "=" * 70)
    print("3. 舍入函数")
    print("=" * 70)

    x = np.array([-2.7, -1.5, -0.5, 0.5, 1.5, 2.7])
    print(f"x: {x}")

    print("\n3.1 round - 四舍五入")
    print("-" * 70)
    print(f"round(x): {np.round(x)}")
    print(f"round(x, 1): {np.round(x, 1)}")

    print("\n3.2 floor - 向下取整")
    print("-" * 70)
    print(f"floor(x): {np.floor(x)}")
    print(f"返回不大于 x 的最大整数")

    print("\n3.3 ceil - 向上取整")
    print("-" * 70)
    print(f"ceil(x): {np.ceil(x)}")
    print(f"返回不小于 x 的最小整数")

    print("\n3.4 trunc - 截断（向零取整）")
    print("-" * 70)
    print(f"trunc(x): {np.trunc(x)}")
    print(f"fix(x): {np.fix(x)}")
    print(f"截断小数部分")

    print("\n3.5 rint - 四舍五入到整数")
    print("-" * 70)
    print(f"rint(x): {np.rint(x)}")
    print(f"返回浮点数格式的整数")

    print("\n" + "=" * 70)
    print("4. 算术运算")
    print("=" * 70)

    a = np.array([10, 20, 30])
    b = np.array([2, 5, 3])

    print(f"a: {a}")
    print(f"b: {b}")

    print("\n4.1 基本运算")
    print("-" * 70)
    print(f"add(a, b): {np.add(a, b)}")
    print(f"subtract(a, b): {np.subtract(a, b)}")
    print(f"multiply(a, b): {np.multiply(a, b)}")
    print(f"divide(a, b): {np.divide(a, b)}")

    print("\n4.2 其他运算")
    print("-" * 70)
    print(f"power(a, 2): {np.power(a, 2)}")
    print(f"sqrt(a): {np.sqrt(a.astype(float))}")

    print("\n4.3 取余运算")
    print("-" * 70)
    print(f"remainder(a, b): {np.remainder(a, b)}")
    print(f"mod(a, b): {np.mod(a, b)}")
    print(f"fmod(a, b): {np.fmod(a, b)}")

    print("\n4.4 divmod - 商和余数")
    print("-" * 70)
    div, mod = np.divmod(a, b)
    print(f"divmod({a}, {b}):")
    print(f"  商: {div}")
    print(f"  余: {mod}")

    print("\n" + "=" * 70)
    print("5. 符号与绝对值")
    print("=" * 70)

    x = np.array([-5, -2.5, 0, 2.5, 5])
    print(f"x: {x}")

    print("\n5.1 abs / absolute - 绝对值")
    print("-" * 70)
    print(f"abs(x): {np.abs(x)}")
    print(f"absolute(x): {np.absolute(x)}")

    print("\n5.2 fabs - 浮点绝对值")
    print("-" * 70)
    print(f"fabs(x): {np.fabs(x)}")

    print("\n5.3 sign - 符号函数")
    print("-" * 70)
    print(f"sign(x): {np.sign(x)}")
    print(f"返回: -1(负), 0(零), 1(正)")

    print("\n5.4 negative / positive")
    print("-" * 70)
    print(f"negative(x): {np.negative(x)}")
    print(f"positive(x): {np.positive(x)}")

    print("\n5.5 copysign - 复制符号")
    print("-" * 70)
    a = np.array([-5, 5, -3])
    b = np.array([2, -2, 1])
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"copysign(a, b): {np.copysign(a, b)}")
    print("将 b 的符号复制到 a")

    print("\n" + "=" * 70)
    print("6. 最大最小与比较")
    print("=" * 70)

    a = np.array([1, 5, 3])
    b = np.array([2, 4, 6])

    print(f"a: {a}")
    print(f"b: {b}")

    print("\n6.1 maximum / minimum - 逐元素比较")
    print("-" * 70)
    print(f"maximum(a, b): {np.maximum(a, b)}")
    print(f"minimum(a, b): {np.minimum(a, b)}")

    print("\n6.2 fmax / fmin（忽略 NaN）")
    print("-" * 70)
    a_nan = np.array([1, np.nan, 3])
    b_nan = np.array([2, 4, np.nan])
    print(f"a: {a_nan}")
    print(f"b: {b_nan}")
    print(f"fmax(a, b): {np.fmax(a_nan, b_nan)}")
    print(f"fmin(a, b): {np.fmin(a_nan, b_nan)}")

    print("\n6.3 比较函数")
    print("-" * 70)
    print(f"greater(a, b): {np.greater(a, b)}")
    print(f"less(a, b): {np.less(a, b)}")
    print(f"equal(a, b): {np.equal(a, b)}")
    print(f"not_equal(a, b): {np.not_equal(a, b)}")

    print("\n6.4 近似比较")
    print("-" * 70)
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([1.0000001, 2.0000001, 3.0000001])
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"allclose(a, b): {np.allclose(a, b)}")
    print(f"isclose(a, b): {np.isclose(a, b)}")

    print("\n" + "=" * 70)
    print("7. 其他数学函数")
    print("=" * 70)

    print("\n7.1 clip - 裁剪值")
    print("-" * 70)
    x = np.array([0, 5, 10, 15, 20])
    print(f"x: {x}")
    print(f"clip(x, 5, 15): {np.clip(x, 5, 15)}")

    print("\n7.2 sqrt - 平方根")
    print("-" * 70)
    x = np.array([1, 4, 9, 16, 25])
    print(f"sqrt(x): {np.sqrt(x)}")

    print("\n7.3 square - 平方")
    print("-" * 70)
    x = np.array([1, 2, 3, 4, 5])
    print(f"square(x): {np.square(x)}")

    print("\n7.4 reciprocal - 倒数")
    print("-" * 70)
    x = np.array([1, 2, 4])
    print(f"reciprocal(x): {np.reciprocal(x)}")

    print("\n" + "=" * 70)
    print("8. 实际应用示例")
    print("=" * 70)

    # 示例 1: 计算两点间距离
    print("\n示例 1: 欧几里得距离")
    p1 = np.array([1, 2, 3])
    p2 = np.array([4, 5, 6])
    diff = p2 - p1
    distance = np.sqrt(np.sum(diff**2))
    print(f"点 {p1} 到点 {p2} 的距离: {distance:.4f}")

    # 示例 2: 向量归一化
    print("\n示例 2: 向量归一化")
    v = np.array([3, 4])
    norm = np.sqrt(np.sum(v**2))
    v_normalized = v / norm
    print(f"原向量: {v}, 模: {norm}")
    print(f"归一化: {v_normalized}, 新模: {np.sqrt(np.sum(v_normalized**2)):.4f}")

    # 示例 3: Sigmoid 函数
    print("\n示例 3: Sigmoid 激活函数")
    x = np.array([-2, -1, 0, 1, 2])
    sigmoid = 1 / (1 + np.exp(-x))
    print(f"x: {x}")
    print(f"sigmoid(x): {sigmoid}")

    # 示例 4: Softmax 函数
    print("\n示例 4: Softmax 函数")
    x = np.array([1, 2, 3, 4, 5])
    exp_x = np.exp(x - np.max(x))  # 数值稳定
    softmax = exp_x / np.sum(exp_x)
    print(f"x: {x}")
    print(f"softmax(x): {softmax}")
    print(f"总和: {np.sum(softmax):.4f}")

    # 示例 5: 极坐标转换
    print("\n示例 5: 直角坐标 -> 极坐标")
    x, y = 3, 4
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    print(f"直角坐标: ({x}, {y})")
    print(f"极坐标: (r={r:.4f}, θ={np.degrees(theta):.4f}°)")


if __name__ == "__main__":
    main()
