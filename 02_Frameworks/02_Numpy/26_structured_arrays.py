#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 26：Structured Arrays - 结构化数组。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/26_structured_arrays.py

结构化数组允许在单个数组中存储不同类型的字段，类似于
数据库表或 C 语言的 struct。这在处理表格数据时非常有用。

本节演示：
1. 创建结构化数组
2. 访问和修改字段
3. 数据类型定义
4. 嵌套结构
5. 记录数组 (recarray)
6. 实际应用案例
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. 创建结构化数组")
    print("=" * 60)

    print("\n方法1: 使用 dtype 定义字段")

    # 定义数据类型
    dt = np.dtype([
        ('name', 'U20'),    # 最多20个字符的Unicode字符串
        ('age', 'i4'),      # 32位整数
        ('height', 'f4'),   # 32位浮点
        ('weight', 'f8'),   # 64位浮点
    ])

    # 创建结构化数组
    people = np.array([
        ('Alice', 25, 165.5, 55.0),
        ('Bob', 30, 180.0, 75.5),
        ('Charlie', 35, 175.5, 68.0),
    ], dtype=dt)

    print(f"\n数组形状: {people.shape}")
    print(f"数据类型:\n{dt}")

    print("\n数据内容:")
    print(people)

    print("\n方法2: 使用字典定义 dtype")
    dt_dict = np.dtype({
        'names': ['name', 'age', 'salary'],
        'formats': ['U20', 'i4', 'f8'],
    })

    employees = np.array([
        ('Alice', 28, 50000.0),
        ('Bob', 35, 75000.0),
    ], dtype=dt_dict)

    print("\n员工数据:")
    print(employees)

    print("\n方法3: 使用元组列表指定格式")
    dt_tuple = np.dtype([
        ('id', 'i4'),
        ('value', ('f8', (3,))),  # 3个浮点数的子数组
        ('flag', '?'),            # 布尔值
    ])

    complex_data = np.array([
        (1, [1.1, 2.2, 3.3], True),
        (2, [4.4, 5.5, 6.6], False),
    ], dtype=dt_tuple)

    print("\n复杂数据:")
    print(complex_data)

    print("\n" + "=" * 60)
    print("2. 访问字段")
    print("=" * 60)

    print("\n访问单个字段:")
    print(f"names: {people['name']}")
    print(f"ages: {people['age']}")
    print(f"heights: {people['height']}")

    print("\n访问单个元素:")
    print(f"第0个人: {people[0]}")
    print(f"第0个人的名字: {people[0]['name']}")
    print(f"第0个人的年龄: {people[0]['age']}")

    print("\n字段切片:")
    print(f"前2个名字: {people['name'][:2]}")
    print(f"年龄>30的人: {people[people['age'] > 30]}")

    print("\n多字段访问:")
    print(f"名字和年龄:")
    print(people[['name', 'age']])

    print("\n" + "=" * 60)
    print("3. 修改字段")
    print("=" * 60)

    print("\n原始数据:")
    print(people)

    # 修改单个字段
    people['age'] += 1
    print(f"\n所有人年龄+1:")
    print(people)

    # 修改特定元素
    people[0]['name'] = 'Alice Smith'
    print(f"\n修改第0个人名字:")
    print(people)

    # 条件修改
    mask = people['age'] > 30
    people['salary'] = 50000.0  # 添加新字段会报错，需要先定义
    print(f"\n注意: 不能直接添加新字段")

    print("\n" + "=" * 60)
    print("4. 数据类型详解")
    print("=" * 60)

    print("\n常用数据类型代码:")

    types = {
        '?': 'bool',
        'i1': 'int8',
        'i2': 'int16',
        'i4': 'int32',
        'i8': 'int64',
        'u1': 'uint8',
        'u2': 'uint16',
        'u4': 'uint32',
        'u8': 'uint64',
        'f2': 'float16',
        'f4': 'float32',
        'f8': 'float64',
        'c8': 'complex64',
        'c16': 'complex128',
        'U': 'Unicode string',
        'S': 'Bytes string',
        'O': 'Python object',
    }

    print("\n类型代码:")
    for code, name in types.items():
        print(f"  '{code}' -> {name}")

    print("\n字符串类型:")
    print("  'U10' - 最多10个字符的Unicode字符串")
    print("  'S20' - 最多20个字节的字节字符串")

    print("\n数组类型:")
    print("  ('i4', (3,)) - 3个整数的数组")
    print("  ('f8', (2, 3)) - 2x3的浮点数数组")

    print("\n" + "=" * 60)
    print("5. 字段操作")
    print("=" * 60)

    # 创建示例
    dt = np.dtype([
        ('id', 'i4'),
        ('name', 'U20'),
        ('score', 'f4'),
    ])

    students = np.array([
        (1, 'Alice', 85.5),
        (2, 'Bob', 92.0),
        (3, 'Charlie', 78.5),
    ], dtype=dt)

    print("\n学生数据:")
    print(students)

    # 获取字段名
    print(f"\n字段名: {students.dtype.names}")

    # 获取字段类型
    print(f"\n字段类型:")
    for name in students.dtype.names:
        print(f"  {name}: {students.dtype.fields[name][0]}")

    # 按字段排序
    sorted_by_score = np.sort(students, order='score')
    print(f"\n按 score 排序:")
    print(sorted_by_score)

    # 反向排序
    sorted_desc = np.sort(students, order='score')[::-1]
    print(f"\n按 score 降序:")
    print(sorted_desc)

    print("\n" + "=" * 60)
    print("6. 嵌套结构")
    print("=" * 60)

    # 嵌套 dtype
    nested_dt = np.dtype([
        ('person', [
            ('name', 'U20'),
            ('age', 'i4'),
        ]),
        ('address', [
            ('street', 'U30'),
            ('city', 'U20'),
            ('zip', 'U10'),
        ]),
    ])

    records = np.array([
        (('Alice', 25), ('123 Main St', 'Springfield', '12345')),
        (('Bob', 30), ('456 Oak Ave', 'Shelbyville', '54321')),
    ], dtype=nested_dt)

    print("\n嵌套结构数据:")
    print(records)

    print("\n访问嵌套字段:")
    print(f"person: {records['person']}")
    print(f"person['name']: {records['person']['name']}")
    print(f"address: {records['address']}")
    print(f"address['city']: {records['address']['city']}")

    print("\n访问单个记录的嵌套字段:")
    print(f"第0个人的城市: {records[0]['address']['city']}")

    print("\n" + "=" * 60)
    print("7. 记录数组 (recarray)")
    print("=" * 60)

    print("\nrecarray 允许使用属性访问字段")

    # 创建 recarray
    dt = np.dtype([
        ('name', 'U20'),
        ('age', 'i4'),
        ('salary', 'f8'),
    ])

    # 从结构化数组创建
    employees_sa = np.array([
        ('Alice', 28, 50000.0),
        ('Bob', 35, 75000.0),
        ('Charlie', 32, 60000.0),
    ], dtype=dt)

    employees_rec = employees_sa.view(np.recarray)

    print("\n结构化数组访问:")
    print(f"  employees_sa['name']: {employees_sa['name']}")

    print("\nrecarray 访问:")
    print(f"  employees_rec.name: {employees_rec.name}")
    print(f"  employees_rec.age: {employees_rec.age}")

    print(f"\nrecarray 属性访问:")
    print(f"  employees_rec[0].name: {employees_rec[0].name}")

    print("\n注意: recarray 开销略大，访问稍慢")

    print("\n" + "=" * 60)
    print("8. 实际应用案例")
    print("=" * 60)

    print("\n案例1: CSV 数据的内存表示")
    print("-" * 40)

    # 定义类似 CSV 的结构
    csv_dt = np.dtype([
        ('id', 'i4'),
        ('product_name', 'U50'),
        ('category', 'U20'),
        ('price', 'f8'),
        ('in_stock', '?'),
        ('last_updated', 'M8[D]'),  # 日期类型
    ])

    products = np.array([
        (1, 'Laptop', 'Electronics', 999.99, True, np.datetime64('2024-01-15')),
        (2, 'Mouse', 'Electronics', 29.99, True, np.datetime64('2024-01-16')),
        (3, 'Desk', 'Furniture', 299.99, False, np.datetime64('2024-01-14')),
    ], dtype=csv_dt)

    print("\n产品数据:")
    print(products)

    print(f"\n查询: 价格 < 100 的产品:")
    cheap = products[products['price'] < 100]
    for p in cheap:
        print(f"  {p['product_name']}: ${p['price']:.2f}")

    print("\n案例2: 时间序列数据")
    print("-" * 40)

    ts_dt = np.dtype([
        ('timestamp', 'M8[ns]'),
        ('sensor_id', 'U10'),
        ('temperature', 'f4'),
        ('humidity', 'f4'),
        ('pressure', 'f4'),
    ])

    # 生成模拟传感器数据
    base_time = np.datetime64('2024-01-01T00:00:00')
    sensor_data = np.array([
        (base_time + np.timedelta64(i, 'h'), f'Sensor_{i%3}', 20 + i*0.1, 50 + i, 1013 + i*0.01)
        for i in range(24)
    ], dtype=ts_dt)

    print("\n传感器数据 (前5条):")
    print(sensor_data[:5])

    print(f"\n统计摘要:")
    print(f"  平均温度: {sensor_data['temperature'].mean():.2f}")
    print(f"  平均湿度: {sensor_data['humidity'].mean():.2f}")
    print(f"  平均气压: {sensor_data['pressure'].mean():.2f}")

    print("\n案例3: 金融数据")
    print("-" * 40)

    trade_dt = np.dtype([
        ('trade_id', 'i8'),
        ('symbol', 'U10'),
        ('price', 'f8'),
        ('quantity', 'i4'),
        ('timestamp', 'M8[ns]'),
        ('buy_sell', '?'),  # True=Buy, False=Sell
    ])

    trades = np.array([
        (1001, 'AAPL', 150.25, 100, np.datetime64('2024-01-15T09:30:00'), True),
        (1002, 'GOOGL', 140.50, 50, np.datetime64('2024-01-15T09:31:00'), True),
        (1003, 'AAPL', 150.20, 50, np.datetime64('2024-01-15T09:32:00'), False),
    ], dtype=trade_dt)

    print("\n交易数据:")
    print(trades)

    print(f"\n按 symbol 分组:")
    for symbol in np.unique(trades['symbol']):
        symbol_trades = trades[trades['symbol'] == symbol]
        print(f"\n  {symbol}:")
        total_volume = symbol_trades['quantity'].sum()
        print(f"    总成交量: {total_volume}")

    print("\n案例4: 与 Pandas 的互操作")
    print("-" * 40)

    # 结构化数组可以轻松转换为 DataFrame
    try:
        import pandas as pd

        df = pd.DataFrame(people)
        print("\n转换为 DataFrame:")
        print(df)

        print("\nDataFrame 转 结构化数组:")
        arr_back = df.to_records(index=False)
        print(arr_back)

    except ImportError:
        print("\nPandas 未安装，跳过此示例")

    print("\n" + "=" * 60)
    print("9. 性能考虑")
    print("=" * 60)

    print("\n结构化数组 vs 独立数组:")

    n = 100000

    # 结构化数组
    sa_dt = np.dtype([('x', 'f8'), ('y', 'f8'), ('z', 'f8')])
    struct_arr = np.zeros(n, dtype=sa_dt)

    # 独立数组
    x = np.zeros(n)
    y = np.zeros(n)
    z = np.zeros(n)

    print(f"\n内存占用对比 ({n} 元素):")
    print(f"  结构化数组: {struct_arr.nbytes / 1024:.1f} KB")
    print(f"  独立数组: {(x.nbytes + y.nbytes + z.nbytes) / 1024:.1f} KB")

    print("\n使用场景:")
    print("  结构化数组适合:")
    print("    - 相关字段需要一起存储")
    print("    - 需要按记录操作")
    print("    - 与 C 代码交互")

    print("\n  独立数组适合:")
    print("    - 独立处理每个字段")
    print("    - 追求最大性能")
    print("    - 使用 NumPy 向量化")

    print("\n" + "=" * 60)
    print("10. 速查表")
    print("=" * 60)

    print("\n创建结构化数组:")
    print("  dt = np.dtype([('name', 'U20'), ('age', 'i4')])")
    print("  arr = np.array([('Alice', 25)], dtype=dt)")

    print("\n访问字段:")
    print("  arr['name']        # 获取字段")
    print("  arr[['name', 'age']]  # 获取多个字段")
    print("  arr[0]['name']     # 获取元素的字段")

    print("\nrecarray:")
    print("  rec = arr.view(np.recarray)")
    print("  rec.name           # 属性访问")

    print("\n常用操作:")
    print("  np.sort(arr, order='age')              # 按字段排序")
    print("  arr.dtype.names                        # 字段名")
    print("  arr.dtype.fields['name'][0]            # 字段类型")
    print("  arr[arr['age'] > 25]                  # 布尔索引")


if __name__ == "__main__":
    main()