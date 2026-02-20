#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 19：数据类型完整版。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/19_dtype_complete.py

知识点：
- 所有 dtype 类型详解
- 字节序
- 类型转换规则表
- astype 详细参数
- can_cast / isdtype
- datetime64 / timedelta64
- string_ / object 类型
- 结构化数据类型
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. NumPy 数据类型完整列表")
    print("=" * 70)

    print("""
整数类型：
  bool        - 布尔值 (True/False)
  int8        - 8位有符号整数 (-128 到 127)
  int16       - 16位有符号整数 (-32768 到 32767)
  int32       - 32位有符号整数 (-2^31 到 2^31-1)
  int64       - 64位有符号整数 (-2^63 到 2^63-1)
  uint8       - 8位无符号整数 (0 到 255)
  uint16      - 16位无符号整数 (0 到 65535)
  uint32      - 32位无符号整数 (0 到 2^32-1)
  uint64      - 64位无符号整数 (0 到 2^64-1)

浮点类型：
  float16     - 半精度浮点 (5位指数，10位尾数)
  float32     - 单精度浮点 (8位指数，23位尾数)
  float64     - 双精度浮点 (11位指数，52位尾数，默认)

复数类型：
  complex64   - 两个 float32 (实部和虚部)
  complex128  - 两个 float64 (实部和虚部)

其他类型：
  object      - Python 对象
  string_     - 固定长度字符串 (如 'U5' 表示5字符)
  bytes_      - 固定长度字节
  datetime64  - 日期时间 (如 'datetime64[D]')
  timedelta64 - 时间差 (如 'timedelta64[D]')
""")

    print("\n" + "=" * 70)
    print("2. 基础数据类型使用")
    print("=" * 70)

    print("\n2.1 整数类型")
    print("-" * 70)
    arr_int8 = np.array([127, -128], dtype=np.int8)
    print(f"int8: {arr_int8}, 范围 -128 到 127")

    arr_uint8 = np.array([0, 255], dtype=np.uint8)
    print(f"uint8: {arr_uint8}, 范围 0 到 255")

    print("\n2.2 浮点类型")
    print("-" * 70)
    arr_f32 = np.array([1.0, 2.0, 3.0], dtype=np.float32)
    print(f"float32: {arr_f32}, 内存: {arr_f32.nbytes} 字节")

    arr_f64 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    print(f"float64: {arr_f64}, 内存: {arr_f64.nbytes} 字节")

    print("\n2.3 复数类型")
    print("-" * 70)
    arr_c64 = np.array([1 + 2j, 3 + 4j], dtype=np.complex64)
    print(f"complex64: {arr_c64}")

    arr_c128 = np.array([1 + 2j, 3 + 4j], dtype=np.complex128)
    print(f"complex128: {arr_c128}")

    print("\n" + "=" * 70)
    print("3. 字符串和对象类型")
    print("=" * 70)

    print("\n3.1 固定长度字符串")
    print("-" * 70)
    arr_str = np.array(["hello", "world"], dtype="U5")
    print(f"U5 (最多5个字符): {arr_str}")
    print(f"每个元素长度: {[len(s) for s in arr_str]}")

    # 截断
    arr_str_trunc = np.array(["hello", "world!"], dtype="U5")
    print(f"\n截断示例: {arr_str_trunc}")

    print("\n3.2 可变长度字符串 (object)")
    print("-" * 70)
    arr_obj = np.array(["hello", "world!"], dtype=object)
    print(f"object 类型: {arr_obj}")

    # 不同类型
    arr_mixed = np.array([1, "hello", 3.14], dtype=object)
    print(f"混合类型: {arr_mixed}")

    print("\n3.3 字节类型")
    print("-" * 70)
    arr_bytes = np.array([b"hello", b"world"], dtype="S5")
    print(f"S5 (固定5字节): {arr_bytes}")

    print("\n" + "=" * 70)
    print("4. 日期时间类型")
    print("=" * 70)

    print("\n4.1 datetime64 基础")
    print("-" * 70)
    arr_date = np.array(["2024-01-01", "2024-01-02"], dtype="datetime64[D]")
    print(f"日期 (D): {arr_date}")

    arr_datetime = np.array(["2024-01-01T12:00", "2024-01-02T12:00"], dtype="datetime64[s]")
    print(f"日期时间 (s): {arr_datetime}")

    arr_ms = np.array(["2024-01-01T12:00:00.500"], dtype="datetime64[ms]")
    print(f"毫秒 (ms): {arr_ms}")

    print("\n4.2 timedelta64 基础")
    print("-" * 70)
    arr_delta = np.array([1, 2, 3], dtype="timedelta64[D]")
    print(f"时间差 (天): {arr_delta}")

    arr_delta_s = np.array([3600, 7200], dtype="timedelta64[s]")
    print(f"时间差 (秒): {arr_delta_s}")

    print("\n4.3 日期时间运算")
    print("-" * 70)
    date1 = np.datetime64("2024-01-01")
    date2 = np.datetime64("2024-01-10")
    delta = date2 - date1
    print(f"{date2} - {date1} = {delta}")

    print("\n" + "=" * 70)
    print("5. 字节序")
    print("=" * 70)

    print("\n5.1 字节序标记")
    print("-" * 70)
    arr_little = np.array([1], dtype="<i4")  # 小端
    arr_big = np.array([1], dtype=">i4")  # 大端
    arr_native = np.array([1], dtype="=i4")  # 本机

    print(f"< 小端: {arr_little.tobytes().hex()}")
    print(f"> 大端: {arr_big.tobytes().hex()}")
    print(f"= 本机: {arr_native.tobytes().hex()}")

    print("\n5.2 检测字节序")
    print("-" * 70)
    print(f"本机字节序: {'小端' if np.little_endian else '大端'}")
    print(f"本机字节序字符: {'<' if np.little_endian else '>'}")

    print("\n" + "=" * 70)
    print("6. 类型转换")
    print("=" * 70)

    print("\n6.1 astype 基础")
    print("-" * 70)
    arr_int = np.array([1, 2, 3], dtype=np.int32)
    arr_float = arr_int.astype(np.float64)
    print(f"int32 -> float64: {arr_float}")

    print("\n6.2 浮点转整数")
    print("-" * 70)
    arr_f = np.array([1.9, 2.5, 3.1])
    arr_i = arr_f.astype(np.int32)
    print(f"float -> int: {arr_f} -> {arr_i}")
    print("（截断，不四舍五入）")

    print("\n6.3 字符串转数值")
    print("-" * 70)
    arr_str = np.array(["1.5", "2.7", "3.9"])
    arr_num = arr_str.astype(np.float64)
    print(f"string -> float: {arr_str} -> {arr_num}")

    print("\n6.4 数值转字符串")
    print("-" * 70)
    arr_num = np.array([1.5, 2.7, 3.9])
    arr_str = arr_num.astype("U5")
    print(f"float -> string: {arr_num} -> {arr_str}")

    print("\n6.5 astype 参数")
    print("-" * 70)
    arr = np.array([1.5, 2.7, 3.9])
    arr_i = arr.astype(np.int32, casting="unsafe", copy=False)
    print(f"astype(int32, casting='unsafe', copy=False)")

    print("\ncasting 选项:")
    print("  'no' - 只允许安全转换（不改变值）")
    print("  'equiv' - 允许字节序和类型更改")
    print("  'safe' - 允许安全转换（可能丢失精度）")
    print("  'same_kind' - 允许同类转换（如 float32->float64）")
    print("  'unsafe' - 允许任何转换")

    print("\n" + "=" * 70)
    print("7. 类型检查")
    print("=" * 70)

    print("\n7.1 can_cast - 检查是否可以安全转换")
    print("-" * 70)
    print(f"int32 -> float64: {np.can_cast(np.int32, np.float64)}")
    print(f"float64 -> int32: {np.can_cast(np.float64, np.int32)}")
    print(f"int32 -> uint32: {np.can_cast(np.int32, np.uint32)}")

    print("\n7.2 isdtype - 检查类型匹配")
    print("-" * 70)
    arr = np.array([1, 2, 3])
    print(f"is int: {np.issubdtype(arr.dtype, np.integer)}")
    print(f"is float: {np.issubdtype(arr.dtype, np.floating)}")
    print(f"is numeric: {np.issubdtype(arr.dtype, np.number)}")

    print("\n7.3 类型层次")
    print("-" * 70)
    print("类型层次结构:")
    print("  number")
    print("    ├── integer (int8, int16, int32, int64, uint8, uint16, uint32, uint64)")
    print("    ├── floating (float16, float32, float64)")
    print("    ├── complex (complex64, complex128)")
    print("    └── bool")

    print("\n" + "=" * 70)
    print("8. 结构化数据类型")
    print("=" * 70)

    print("\n8.1 创建结构化类型")
    print("-" * 70)
    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    print(f"dtype: {dt}")
    print(f"字段名: {dt.names}")
    print(f"字段类型: {dt.fields}")

    arr_struct = np.array([("Alice", 20, 88.5), ("Bob", 21, 92.0)], dtype=dt)
    print(f"\n结构化数组:")
    print(arr_struct)

    print("\n8.2 访问字段")
    print("-" * 70)
    print(f"names: {arr_struct['name']}")
    print(f"ages: {arr_struct['age']}")
    print(f"scores: {arr_struct['score']}")

    print("\n8.3 嵌套结构")
    print("-" * 70)
    dt_nested = np.dtype([("position", [("x", "f4"), ("y", "f4")]), ("value", "f4")])
    arr_nested = np.array([((1.0, 2.0), 3.0), ((4.0, 5.0), 6.0)], dtype=dt_nested)
    print(f"嵌套结构:")
    print(arr_nested)
    print(f"position: {arr_nested['position']}")
    print(f"x 坐标: {arr_nested['position']['x']}")

    print("\n" + "=" * 70)
    print("9. 类型属性和查询")
    print("=" * 70)

    arr = np.array([1, 2, 3, 4], dtype=np.int32)

    print(f"dtype: {arr.dtype}")
    print(f"dtype.name: {arr.dtype.name}")
    print(f"dtype.itemsize: {arr.dtype.itemsize} 字节")
    print(f"dtype.kind: {arr.dtype.kind} (i=整数, f=浮点, u=无符号整数, b=布尔)")
    print(f"dtype.char: {arr.dtype.char}")

    print("\n类型代码对照:")
    type_codes = [
        ("b", "boolean"),
        ("i", "signed integer"),
        ("u", "unsigned integer"),
        ("f", "floating-point"),
        ("c", "complex-floating"),
        ("O", "object"),
        ("S", "byte string"),
        ("U", "Unicode string"),
        ("V", "raw data"),
    ]
    for code, name in type_codes:
        print(f"  {code} -> {name}")

    print("\n" + "=" * 70)
    print("10. 特殊类型")
    print("=" * 70)

    print("\n10.1 void 类型（原始数据）")
    print("-" * 70)
    arr = np.array([b"hello"], dtype="V5")
    print(f"void 类型: {arr}, dtype: {arr.dtype}")

    print("\n10.2 Unicode 字符串长度")
    print("-" * 70)
    for n in [1, 5, 10, 100]:
        arr = np.array(["a"], dtype=f"U{n}")
        print(f"U{n}: {arr.dtype} ({arr.nbytes} 字节)")

    print("\n" + "=" * 70)
    print("11. 数组标量")
    print("=" * 70)

    print("数组标量 vs Python 标量")
    print("-" * 70)
    np_int = np.int32(42)
    py_int = 42

    print(f"numpy.int32(42): {np_int}, type: {type(np_int)}")
    print(f"Python int(42): {py_int}, type: {type(py_int)}")
    print(f"相等性: {np_int == py_int}")
    print(f"类型: {type(np_int)} vs {type(py_int)}")

    print("\n" + "=" * 70)
    print("12. 实际应用示例")
    print("=" * 70)

    # 示例 1: 内存优化
    print("\n示例 1: 使用合适的类型节省内存")
    arr_small = np.array([0, 1, 2, 3], dtype=np.uint8)  # 0-255
    arr_large = np.array([0, 1, 2, 3], dtype=np.int64)  # 默认

    print(f"uint8 数组: {arr_small.nbytes} 字节")
    print(f"int64 数组: {arr_large.nbytes} 字节")
    print(f"内存节省: {arr_large.nbytes / arr_small.nbytes:.1f}x")

    # 示例 2: 数据加载时的类型指定
    print("\n示例 2: 加载数据时指定类型")
    data = np.loadtxt("dummy.txt", dtype=np.float32)  # 如果存在
    print("使用 float32 而非 float64 可以节省一半内存")

    # 示例 3: 结构化数组表示表格数据
    print("\n示例 3: 结构化数组表示表格")
    dt = np.dtype([("id", "i4"), ("name", "U20"), ("value", "f8")])
    table = np.array([(1, "Alice", 100.0), (2, "Bob", 200.0)], dtype=dt)
    print(table)

    # 示例 4: 日期时间序列
    print("\n示例 4: 日期时间序列")
    dates = np.arange("2024-01", "2024-02", dtype="datetime64[D]")
    print(f"一月所有日期: {dates[:5]} ... (共 {len(dates)} 天)")

    # 示例 5: 类型安全的数值数组
    print("\n示例 5: 使用无符号整数防止负数")
    unsigned = np.array([0, 100, 255], dtype=np.uint8)
    print(f"uint8: {unsigned}")
    print("注意：溢出会绕回（256 -> 0）")


if __name__ == "__main__":
    main()