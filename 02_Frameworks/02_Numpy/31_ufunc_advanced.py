#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 31：NumPy ufunc 高级操作 (outer, at, reduceat, accumulate)。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/31_ufunc_advanced.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=== ufunc.outer - 外积 ===")

    # 1. outer - 外积操作
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])

    print("数组 a:", a)
    print("数组 b:", b)
    print("\nadd.outer (加法外积):")
    print(np.add.outer(a, b))
    print("\nmultiply.outer (乘法外积):")
    print(np.multiply.outer(a, b))

    # 2. 各种 ufunc 的 outer
    print("\n=== 不同 ufunc 的 outer ===")
    print("subtract.outer:")
    print(np.subtract.outer(a, b))
    print("\npower.outer:")
    print(np.power.outer(a, b))

    # 3. ufunc.at - 原地操作
    print("\n=== ufunc.at ===")
    data = np.zeros(10)
    indices = np.array([1, 3, 5, 3, 1])  # 重复索引
    values = np.array([10, 20, 30, 40, 50])

    print("初始 data:", data)
    print("索引:", indices)
    print("值:", values)

    # 普通 assignment 会覆盖
    data_copy = data.copy()
    data_copy[indices] = values
    print("\n普通 assignment (有覆盖):", data_copy)

    # 使用 at 累加
    data_at = data.copy()
    np.add.at(data_at, indices, values)
    print("\nnp.add.at (累加):", data_at)
    print("注意: 重复索引的值被累加而不是覆盖")

    # 4. ufunc.reduceat - 部分归约
    print("\n=== ufunc.reduceat ===")

    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    indices = np.array([0, 3, 7])

    print("数组:", arr)
    print("归约位置:", indices)

    # reduceat 在 indices 指定的位置进行分段归约
    result = np.add.reduceat(arr, indices)
    print("\nadd.reduceat 结果:", result)

    # 解释：
    # [0:3] -> 0+1+2 = 3
    # [3:7] -> 3+4+5+6 = 18
    # [7:] -> 7+8+9 = 24
    print("解释: [0:3]=3, [3:7]=18, [7:]=24")

    # 5. ufunc.accumulate - 累积操作
    print("\n=== ufunc.accumulate ===")

    arr = np.array([1, 2, 3, 4, 5])
    print("数组:", arr)

    print("\nadd.accumulate (累加和):")
    print(np.add.accumulate(arr))

    print("\nmultiply.accumulate (累乘):")
    print(np.multiply.accumulate(arr))

    print("\nmaximum.accumulate (累积最大):")
    print(np.maximum.accumulate(arr))

    # 6. 自定义 ufunc
    print("\n=== 自定义 ufunc ===")

    # 使用 frompyfunc 创建自定义 ufunc
    def my_func(x, y):
        return x**2 + y**2

    # frompyfunc 返回 object dtype
    ufunc_custom = np.frompyfunc(my_func, 2, 1)  # 2输入，1输出
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    result = ufunc_custom(a, b)
    print("自定义函数 (x² + y²):")
    print(result)

    # 使用 vectorize (更灵活)
    vfunc_custom = np.vectorize(my_func)
    result2 = vfunc_custom(a, b)
    print("\n使用 vectorize:")
    print(result2)

    # 7. ufunc 方法和属性
    print("\n=== ufunc 方法和属性 ===")

    add_ufunc = np.add
    print("np.add 的属性:")
    print(f"  name: {add_ufunc.name}")
    print(f"  nin (输入数): {add_ufunc.nin}")
    print(f"  nout (输出数): {add_ufunc.nout}")
    print(f"  nargs (参数类型数): {add_ufunc.nargs}")

    # 8. ufunc 的 reduce 方法
    print("\n=== ufunc.reduce ===")

    arr = np.array([1, 2, 3, 4, 5])
    print("数组:", arr)
    print("add.reduce (求和):", np.add.reduce(arr))
    print("multiply.reduce (求积):", np.multiply.reduce(arr))
    print("maximum.reduce (最大值):", np.maximum.reduce(arr))
    print("minimum.reduce (最小值):", np.minimum.reduce(arr))

    # 9. 带初始值的 reduce
    print("\n=== 带初始值的 reduce ===")
    print("add.reduce with initial=100:", np.add.reduce(arr, initial=100))
    print("multiply.reduce with initial=2:", np.multiply.reduce(arr, initial=2))

    # 10. where 参数
    print("\n=== ufunc 的 where 参数 ===")

    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])
    mask = np.array([True, False, True, False, True])

    print("数组 a:", a)
    print("数组 b:", b)
    print("mask:", mask)

    # 只在 mask 为 True 的地方相加
    result = np.where(mask, a + b, a)
    print("\n条件相加 (mask 为 True 时 a+b，否则 a):")
    print(result)

    # 11. dtype 参数
    print("\n=== ufunc 的 dtype 参数 ===")

    a = np.array([1.1, 2.2, 3.3])
    print("原始:", a, "dtype:", a.dtype)

    # 指定输出 dtype
    result_int = np.add(a, 1, dtype=int)
    print("转换为 int:", result_int, "dtype:", result_int.dtype)

    # 12. out 参数 (预分配输出)
    print("\n=== out 参数 ===")

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    out = np.zeros(3)  # 预分配

    print("out 数组初始:", out)
    np.add(a, b, out=out)
    print("np.add(a, b, out=out):", out)

    # 13. 链式 ufunc 操作
    print("\n=== 链式 ufunc 操作 ===")

    a = np.array([1, 2, 3, 4, 5])
    # 多个 ufunc 可以链式调用
    result = np.add(np.multiply(a, 2), 10)
    print("(a * 2) + 10:", result)

    # 14. ufunc 性能考虑
    print("\n=== ufunc 性能提示 ===")
    print("- ufunc 是向量化的，比 Python 循环快得多")
    print("- 大数组操作优先使用 ufunc 而不是 Python 循环")
    print("- 复杂运算可组合多个 ufunc")
    print("- 使用 outer/accumulate/reduce 等方法表达复杂操作")

    # 15. 位运算 ufunc
    print("\n=== 位运算 ufunc ===")

    a = np.array([5, 10, 15], dtype=int)
    b = np.array([3, 6, 9], dtype=int)

    print("a:", a)
    print("b:", b)
    print("bitwise_and:", np.bitwise_and(a, b))
    print("bitwise_or:", np.bitwise_or(a, b))
    print("bitwise_xor:", np.bitwise_xor(a, b))
    print("left_shift:", np.left_shift(a, 1))


if __name__ == "__main__":
    main()