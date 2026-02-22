#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 20：Masked Arrays - 掩码数组。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/20_masked_arrays.py

掩码数组（Masked Array）是 NumPy 中处理含有缺失值或无效数据的数组。
与使用 NaN 表示缺失值不同，掩码数组使用独立的布尔掩码来标记无效值。

本节演示：
1. 创建掩码数组
2. 掩码数组的基本操作
3. 掩码数组的统计计算
4. 掩码操作与修改
5. 掩码数组与普通数组互转
"""

from __future__ import annotations

import numpy as np
import numpy.ma as ma


def main() -> None:
    print("=" * 60)
    print("1. 创建掩码数组")
    print("=" * 60)

    # 方法1: 从普通数组创建，指定掩码
    data = np.array([1, 2, 3, 4, 5])
    mask = [False, False, True, False, True]  # True 表示该位置无效
    ma_arr = ma.array(data, mask=mask)

    print("\n原始数据:", data)
    print("掩码:", mask)
    print("掩码数组:", ma_arr)
    print("有效值:", ma_arr.compressed())

    # 方法2: 使用 masked_value 指定无效值
    ma_arr2 = ma.array([1, -999, 3, -999, 5], mask=-999)
    print("\n使用 mask=-999 标记无效值:")
    print("数组:", ma_arr2)

    # 方法3: 从已有数组创建，掩码特定条件
    data = np.array([1, 2, 999, 4, 5, 999])
    ma_arr3 = ma.masked_values(data, 999)
    print("\n掩码等于 999 的值:")
    print("数组:", ma_arr3)

    # 方法4: 使用 masked_invalid 掩码 NaN/Inf
    data_with_nan = np.array([1.0, 2.0, np.nan, 4.0, np.inf])
    ma_arr4 = ma.masked_invalid(data_with_nan)
    print("\n掩码 NaN 和 Inf:")
    print("数组:", ma_arr4)

    # 方法5: 创建全掩码或空掩码数组
    ma_masked_all = ma.masked_all((3, 3))
    print("\n全掩码数组:")
    print(ma_masked_all)

    ma_empty = ma.empty((2, 3))
    print("\n空掩码数组:")
    print(ma_empty)

    print("\n" + "=" * 60)
    print("2. 掩码数组的基本操作")
    print("=" * 60)

    # 创建示例数组
    x = ma.array([1, 2, 3, 4, 5], mask=[False, True, False, False, True])
    y = ma.array([10, 20, 30, 40, 50], mask=[False, False, True, False, False])

    print(f"x = {x}")
    print(f"y = {y}")

    # 算术运算（掩码会传播）
    print(f"\nx + y = {x + y}")
    print(f"x * y = {x * y}")
    print(f"x ** 2 = {x ** 2}")

    # 比较运算
    print(f"\nx > 2 = {x > 2}")
    print(f"x == y = {x == y}")

    # 索引和切片
    print(f"\nx[0] = {x[0]}")
    print(f"x[1:4] = {x[1:4]}")
    print(f"x[[0, 2, 4]] = {x[[0, 2, 4]]}")

    # 修改值
    x[0] = 100
    print(f"\nx[0] = 100 后: {x}")

    # 掩码某个位置
    x[2] = ma.masked
    print(f"x[2] = masked 后: {x}")

    print("\n" + "=" * 60)
    print("3. 掩码数组的统计计算")
    print("=" * 60)

    # 创建带有掩码的数组
    data = ma.array([1, 2, -999, 4, 5, -999], mask=[0, 0, 1, 0, 0, 1])

    print(f"数据: {data}")
    print(f"有效值: {data.compressed()}")

    # 统计函数（自动忽略掩码值）
    print(f"\n均值: {data.mean():.2f}")
    print(f"标准差: {data.std():.2f}")
    print(f"方差: {data.var():.2f}")
    print(f"总和: {data.sum()}")
    print(f"最小值: {data.min()}")
    print(f"最大值: {data.max()}")
    print(f"中位数: {ma.median(data)}")

    # 累计操作
    print(f"\n累计和: {data.cumsum()}")
    print(f"累计积: {data.cumprod()}")

    # 比较普通数组和掩码数组的统计
    normal_arr = np.array([1, 2, np.nan, 4, 5])
    masked_arr = ma.array([1, 2, np.nan, 4, 5])

    print(f"\n普通数组含 NaN: {normal_arr}")
    print(f"  np.mean(): {np.mean(normal_arr)}")  # 会是 nan
    print(f"  np.nanmean(): {np.nanmean(normal_arr)}")  # 需要用 nanmean

    print(f"\n掩码数组: {masked_arr}")
    print(f"  ma.mean(): {masked_arr.mean()}")  # 自动忽略掩码

    print("\n" + "=" * 60)
    print("4. 掩码操作与修改")
    print("=" * 60)

    data = ma.array([1, 2, 3, 4, 5])

    print(f"原始数组: {data}")

    # 设置掩码
    ma.masked_where(data > 3, data, copy=False)
    print(f"\n掩码 > 3 的值后: {data}")

    # 取消掩码
    data[3] = ma.nomask  # 取消索引 3 的掩码
    print(f"取消索引 3 的掩码: {data}")

    # 获取掩码
    print(f"\n掩码: {data.mask}")

    # 填充掩码值
    filled = data.filled(0)  # 用 0 填充
    print(f"用 0 填充掩码: {filled}")

    # 软掩码 vs 硬掩码
    soft = ma.array([1, 2, 3], soft_mask=True)
    print(f"\n软掩码数组: {soft}")
    soft[0] = ma.masked
    print(f"软掩码 [0] = masked: {soft}")

    hard = ma.array([1, 2, 3], hard_mask=True)
    print(f"\n硬掩码数组: {hard}")
    hard[0] = ma.masked
    # hard[0] = 100  # 这会报错，硬掩码不能修改掩码位置的值

    print("\n" + "=" * 60)
    print("5. 掩码数组与普通数组互转")
    print("=" * 60)

    # 普通数组 -> 掩码数组
    normal = np.array([1, 2, 3, 4, 5])
    masked = ma.array(normal)
    print(f"普通数组 -> 掩码数组: {masked}")

    # 掩码数组 -> 普通数组
    back_to_normal = masked.filled(np.nan)  # 用 nan 填充掩码
    print(f"掩码数组 -> 普通数组: {back_to_normal}")

    # 只获取有效值
    compressed = masked.compressed()
    print(f"只获取有效值: {compressed}")

    # 获取数据视图（不含掩码信息）
    data_view = masked.data
    print(f"数据视图: {data_view}")

    print("\n" + "=" * 60)
    print("6. 二维掩码数组")
    print("=" * 60)

    # 创建二维掩码数组
    data_2d = np.arange(12).reshape(3, 4)
    mask_2d = [[False, True, False, True],
               [False, False, True, False],
               [True, False, False, False]]
    ma_2d = ma.array(data_2d, mask=mask_2d)

    print("\n二维数组:")
    print(ma_2d)

    print("\n掩码:")
    print(ma_2d.mask)

    print("\n沿 axis 0 求和:")
    print(ma_2d.sum(axis=0))

    print("\n沿 axis 1 求和:")
    print(ma_2d.sum(axis=1))

    print("\n整体求和:")
    print(ma_2d.sum())

    # 按条件掩码
    ma_2d_cond = ma.masked_where(ma_2d < 5, ma_2d)
    print("\n掩码小于 5 的元素:")
    print(ma_2d_cond)

    print("\n" + "=" * 60)
    print("7. 常用掩码数组函数")
    print("=" * 60)

    # 创建示例数据
    x = ma.array([1, -999, 3, -999, 5, -999])
    x = ma.masked_values(x, -999)

    print(f"数据: {x}")

    # common_masked - 两个数组的共同掩码
    y = ma.array([10, 20, 30, 40, 50, 60], mask=[0, 1, 0, 1, 0, 1])
    print(f"y: {y}")

    common = ma.common_masked(x, y)
    print(f"\n共同掩码位置: {common}")

    # masked_outside - 掩码范围外的值
    arr = ma.array([1, 2, 5, 10, 15, 20])
    outside = ma.masked_outside(arr, 5, 15)
    print(f"\n掩码 [5, 15] 范围外的值: {outside}")

    # masked_inside - 掩码范围内的值
    inside = ma.masked_inside(arr, 5, 15)
    print(f"掩码 [5, 15] 范围内的值: {inside}")

    # masked_equal - 掩码等于某值的元素
    equal = ma.masked_equal(arr, 10)
    print(f"掩码等于 10 的值: {equal}")

    # masked_not_equal - 掩码不等于某值的元素
    not_equal = ma.masked_not_equal(arr, 10)
    print(f"掩码不等于 10 的值: {not_equal}")

    # masked_greater - 掩码大于某值的元素
    greater = ma.masked_greater(arr, 10)
    print(f"掩码大于 10 的值: {greater}")

    # masked_less - 掩码小于某值的元素
    less = ma.masked_less(arr, 10)
    print(f"掩码小于 10 的值: {less}")

    print("\n" + "=" * 60)
    print("8. 实际应用场景")
    print("=" * 60)

    print("\n场景1: 传感器数据清洗")
    sensor_data = ma.array([
        23.5, 24.1, -999, 23.8, 24.2, -999, 23.9, 24.0
    ])
    sensor_data = ma.masked_values(sensor_data, -999)
    print(f"  原始数据: {sensor_data}")
    print(f"  有效数据: {sensor_data.compressed()}")
    print(f"  平均温度: {sensor_data.mean():.2f}°C")

    print("\n场景2: 超出范围的数据标记")
    measurements = ma.array([0.1, 0.5, 1.5, 0.8, 2.1, 0.3])
    # 假设有效范围是 [0, 1]
    valid = ma.masked_outside(measurements, 0, 1)
    print(f"  测量值: {measurements}")
    print(f"  掩码超范围后: {valid}")
    print(f"  有效值平均: {valid.mean():.2f}")

    print("\n场景3: 处理异常值")
    data = ma.array([10, 12, 11, 100, 13, 12, 9])
    mean = data.mean()
    std = data.std()
    # 掩码超过 3 倍标准差的值
    outliers = ma.masked_outside(data, mean - 3*std, mean + 3*std)
    print(f"  原始数据: {data}")
    print(f"  去除异常值: {outliers}")

    print("\n场景4: 缺失数据插值")
    incomplete = ma.array([1, 2, ma.masked, 4, ma.masked, 6])
    print(f"  不完整数据: {incomplete}")
    print(f"  线性插值填充: {ma.interpolate(incomplete)}")

    print("\n" + "=" * 60)
    print("9. 掩码数组 vs NaN 数组")
    print("=" * 60)

    print("\n对比掩码数组和 NaN 数组:")

    # NaN 数组（仅适用于浮点类型）
    nan_arr = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
    print(f"\nNaN 数组: {nan_arr}")
    print(f"  类型: {nan_arr.dtype}")
    print(f"  np.nanmean(): {np.nanmean(nan_arr)}")

    # 掩码数组（适用于任何类型）
    masked_arr = ma.array([1, 2, 3, 4, 5], mask=[0, 1, 0, 1, 0])
    print(f"\n掩码数组: {masked_arr}")
    print(f"  类型: {masked_arr.dtype}")
    print(f"  mean(): {masked_arr.mean()}")

    print("\n选择建议:")
    print("  - 浮点数据、需要与其他库兼容: 使用 NaN")
    print("  - 整数或其他类型、需要精确控制掩码: 使用掩码数组")
    print('  - 需要区分"缺失"和"无限"时: 使用掩码数组')

    print("\n" + "=" * 60)
    print("10. 掩码数组速查")
    print("=" * 60)

    print("\n创建掩码数组:")
    print("  ma.array(data, mask=mask)           # 指定掩码")
    print("  ma.masked_values(data, value)       # 掩码指定值")
    print("  ma.masked_invalid(data)             # 掩码 NaN/Inf")
    print("  ma.masked_where(condition, data)    # 按条件掩码")
    print("  ma.masked_all(shape)                # 全掩码数组")

    print("\n掩码操作:")
    print("  ma.masked_greater(arr, threshold)   # 掩码大于阈值")
    print("  ma.masked_less(arr, threshold)      # 掩码小于阈值")
    print("  ma.masked_outside(arr, v1, v2)      # 掩码范围外")
    print("  ma.masked_inside(arr, v1, v2)       # 掩码范围内")

    print("\n获取数据:")
    print("  arr.compressed()                    # 只获取有效值")
    print("  arr.filled(fill_value)              # 用值填充掩码")
    print("  arr.data                            # 数据视图")
    print("  arr.mask                            # 掩码数组")

    print("\n统计函数:")
    print("  arr.mean(), arr.std(), arr.var()    # 自动忽略掩码")
    print("  arr.min(), arr.max(), arr.sum()     # 自动忽略掩码")
    print("  ma.median(arr)                      # 中位数")
    print("  ma.average(arr, weights=w)          # 加权平均")

    print("\n修改掩码:")
    print("  arr[idx] = ma.masked                # 设置掩码")
    print("  arr[idx] = ma.nomask                # 取消掩码")
    print("  arr.soft_mask = True                # 软掩码模式")


if __name__ == "__main__":
    main()