#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 57：Extended I/O Formats - 扩展 I/O 格式。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/57_io_formats_extended.py

Pandas 支持多种数据格式读写。本节补充一些高级格式的使用，
这些格式在特定场景下非常有用。

注意：某些格式需要安装额外的依赖库。

本节演示：
1. Feather 格式（高性能二进制格式）
2. Parquet 格式（列式存储，大数据首选）
3. Stata 格式（统计软件数据交换）
4. SAS 格式（统计软件数据交换）
5. JSON Lines 格式（jsonl）
6. Pickle 高级用法
7. 格式性能对比
8. 选择合适的格式
"""

from __future__ import annotations

import pandas as pd
import numpy as np
import os
from pathlib import Path


def create_sample_data() -> pd.DataFrame:
    """创建示例数据"""
    np.random.seed(42)
    return pd.DataFrame({
        'id': range(1, 1001),
        'name': [f'Item_{i}' for i in range(1, 1001)],
        'category': np.random.choice(['A', 'B', 'C', 'D'], 1000),
        'value': np.random.randn(1000),
        'score': np.random.randint(0, 100, 1000),
        'date': pd.date_range('2020-01-01', periods=1000, freq='D')
    })


def main() -> None:
    print("=" * 60)
    print("1. Feather 格式")
    print("=" * 60)

    print("\nFeather 特点:")
    print("  - 快速读写性能")
    print("  - 轻量级二进制格式")
    print("  - 适合临时存储和进程间通信")
    print("  - 依赖: pyarrow 或 feather-format")

    # 检查依赖
    try:
        import pyarrow.feather as feather
        feather_available = True
    except ImportError:
        feather_available = False
        print("\n注意: pyarrow 未安装，跳过 Feather 示例")
        print("安装命令: pip install pyarrow")

    df = create_sample_data()

    if feather_available:
        # 写入 Feather
        feather_file = '/tmp/data.feather'
        df.to_feather(feather_file)
        print(f"\n写入 Feather: {feather_file}")

        # 读取 Feather
        df_read = pd.read_feather(feather_file)
        print(f"读取成功，形状: {df_read.shape}")
        print(f"数据一致: {df.equals(df_read)}")

        # 文件大小
        file_size = os.path.getsize(feather_file) / 1024
        print(f"文件大小: {file_size:.1f} KB")

    print("\n" + "=" * 60)
    print("2. Parquet 格式")
    print("=" * 60)

    print("\nParquet 特点:")
    print("  - 列式存储格式")
    print("  - 高压缩比")
    print("  - 适合大数据和分析查询")
    print("  - 支持谓词下推和列裁剪")
    print("  - 依赖: pyarrow 或 fastparquet")

    # 检查依赖
    try:
        import pyarrow.parquet as pq
        parquet_available = True
    except ImportError:
        parquet_available = False
        print("\n注意: pyarrow 未安装，跳过 Parquet 示例")
        print("安装命令: pip install pyarrow")

    if parquet_available:
        # 写入 Parquet
        parquet_file = '/tmp/data.parquet'
        df.to_parquet(parquet_file, index=False)
        print(f"\n写入 Parquet: {parquet_file}")

        # 读取 Parquet
        df_read = pd.read_parquet(parquet_file)
        print(f"读取成功，形状: {df_read.shape}")

        # 只读取部分列（列裁剪优势）
        df_partial = pd.read_parquet(parquet_file, columns=['id', 'name', 'value'])
        print(f"\n只读取 3 列，形状: {df_partial.shape}")

        # 文件大小
        file_size = os.path.getsize(parquet_file) / 1024
        print(f"文件大小: {file_size:.1f} KB")

        # 压缩选项
        print("\n不同压缩算法:")
        for compression in ['snappy', 'gzip', 'brotli']:
            try:
                file = f'/tmp/data_{compression}.parquet'
                df.to_parquet(file, index=False, compression=compression)
                size = os.path.getsize(file) / 1024
                print(f"  {compression:10s}: {size:6.1f} KB")
                os.remove(file)
            except Exception as e:
                print(f"  {compression:10s}: 不支持 ({e})")

    print("\n" + "=" * 60)
    print("3. Stata 格式")
    print("=" * 60)

    print("\nStata 特点:")
    print("  - 统计分析软件常用格式")
    print("  - 支持 .dta 格式")
    print("  - 适合与 Stata 用户交换数据")
    print("  - 支持 Stata 8-17 版本")

    # Stata 更适合小数据集
    df_stata = pd.DataFrame({
        'id': range(1, 101),
        'income': np.random.randn(100) * 10000 + 50000,
        'education': np.random.randint(1, 6, 100),  # 1-5 年教育
        'experience': np.random.randint(0, 40, 100),
        'gender': np.random.choice(['M', 'F'], 100)
    })

    stata_file = '/tmp/data.dta'
    try:
        # 写入 Stata
        df_stata.to_stata(stata_file, write_index=False)
        print(f"\n写入 Stata: {stata_file}")

        # 读取 Stata
        df_read = pd.read_stata(stata_file)
        print(f"读取成功，形状: {df_read.shape}")

        # 转换类别
        df_read['gender'] = df_read['gender'].astype(str)
        print(f"\n数据预览:")
        print(df_read.head())
    except Exception as e:
        print(f"\nStata 操作失败: {e}")
        print("可能需要安装: pip install pandas")

    print("\n" + "=" * 60)
    print("4. SAS 格式")
    print("=" * 60)

    print("\nSAS 特点:")
    print("  - 统计分析软件格式")
    print("  - 支持 SAS7BDAT (.sas7bdat) 和 XPORT (.xpt) 格式")
    print("  - 适合与 SAS 用户交换数据")

    print("\n注意: SAS 格式支持有限，主要用于读取")
    print("  SAS7BDAT: pd.read_sas('file.sas7bdat')")
    print("  XPORT: pd.read_sas('file.xpt')")

    print("\nSAS 格式通常只用于读取，不建议写入")
    print("如需与 SAS 交换数据，推荐使用 CSV 或 XPORT 格式")

    print("\n" + "=" * 60)
    print("5. JSON Lines 格式 (jsonl)")
    print("=" * 60)

    print("\nJSON Lines 特点:")
    print("  - 每行一个独立 JSON 对象")
    print("  - 适合日志数据和流式处理")
    print("  - Pandas 通过 lines=True 参数支持")

    # 创建 JSON Lines 数据
    jsonl_file = '/tmp/data.jsonl'
    with open(jsonl_file, 'w') as f:
        for i in range(10):
            f.write(f'{{"id": {i}, "name": "Item_{i}", "value": {i * 1.5}}}\n')

    print(f"\nJSON Lines 文件内容:")
    with open(jsonl_file, 'r') as f:
        print(f.read()[:200] + "...")

    # 读取 JSON Lines
    df_jsonl = pd.read_json(jsonl_file, lines=True)
    print(f"\n读取成功，形状: {df_jsonl.shape}")
    print(df_jsonl)

    # 写入 JSON Lines
    output_jsonl = '/tmp/output.jsonl'
    df_jsonl.to_json(output_jsonl, orient='records', lines=True)
    print(f"\n写入 JSON Lines: {output_jsonl}")

    print("\nJSON Lines vs 普通 JSON:")
    print("  JSON Lines:  每行一个对象，流式友好")
    print("  普通 JSON:   整个数组，需要一次性加载")

    print("\n" + "=" * 60)
    print("6. Pickle 高级用法")
    print("=" * 60)

    print("\nPickle 特点:")
    print("  - Python 对象序列化")
    print("  - 支持所有 Python 数据类型")
    print("  - 注意：存在安全风险，只加载可信来源")

    # 创建复杂数据
    df_complex = pd.DataFrame({
        'data': [np.random.randn(10) for _ in range(5)],
        'mixed': [{'a': 1, 'b': 2}, {'c': 3}, None, [1, 2], 'text'],
        'timestamp': pd.date_range('2024-01-01', periods=5)
    })

    pickle_file = '/tmp/complex.pkl'
    df_complex.to_pickle(pickle_file)
    print(f"\n写入复杂对象到 Pickle: {pickle_file}")

    # 读取
    df_read = pd.read_pickle(pickle_file)
    print(f"读取成功，类型保持: {type(df_read['mixed'].iloc[0])}")

    # 压缩 Pickle
    import zlib

    pickle_compressed = '/tmp/complex_compressed.pkl'
    df_complex.to_pickle(pickle_compressed, compression='gzip')
    print(f"\n压缩 Pickle: {pickle_compressed}")

    # 对比大小
    normal_size = os.path.getsize(pickle_file) / 1024
    compressed_size = os.path.getsize(pickle_compressed) / 1024
    print(f"  未压缩: {normal_size:.1f} KB")
    print(f"  压缩后: {compressed_size:.1f} KB")
    print(f"  压缩率: {(1 - compressed_size/normal_size)*100:.1f}%")

    print("\n" + "=" * 60)
    print("7. 格式性能对比")
    print("=" * 60)

    # 创建较大数据集进行测试
    large_df = pd.DataFrame({
        'id': range(100000),
        'value': np.random.randn(100000),
        'category': np.random.choice(['A', 'B', 'C', 'D', 'E'], 100000),
        'score': np.random.randint(0, 1000, 100000),
        'flag': np.random.choice([True, False], 100000)
    })

    import time

    formats_to_test = []

    # CSV
    formats_to_test.append(('CSV', 'csv', lambda f: large_df.to_csv(f, index=False),
                             lambda f: pd.read_csv(f)))

    # Pickle
    formats_to_test.append(('Pickle', 'pkl', lambda f: large_df.to_pickle(f),
                             lambda f: pd.read_pickle(f)))

    # Parquet (如果可用)
    if parquet_available:
        formats_to_test.append(('Parquet', 'parquet',
                                 lambda f: large_df.to_parquet(f, index=False),
                                 lambda f: pd.read_parquet(f)))

    # Feather (如果可用)
    if feather_available:
        formats_to_test.append(('Feather', 'feather',
                                 lambda f: large_df.to_feather(f),
                                 lambda f: pd.read_feather(f)))

    print(f"\n测试数据: {len(large_df):,} 行 x {len(large_df.columns)} 列")
    print("\n性能对比:")

    results = []

    for name, ext, write_fn, read_fn in formats_to_test:
        file_path = f'/tmp/benchmark.{ext}'

        # 写入时间
        start = time.time()
        write_fn(file_path)
        write_time = time.time() - start

        # 文件大小
        file_size = os.path.getsize(file_path) / 1024

        # 读取时间
        start = time.time()
        df_read = read_fn(file_path)
        read_time = time.time() - start

        results.append({
            'format': name,
            'write_time': write_time,
            'read_time': read_time,
            'total_time': write_time + read_time,
            'file_size': file_size
        })

        print(f"\n{name:10s}:")
        print(f"  写入: {write_time*1000:6.1f} ms")
        print(f"  读取: {read_time*1000:6.1f} ms")
        print(f"  总计: {(write_time+read_time)*1000:6.1f} ms")
        print(f"  大小: {file_size:6.1f} KB")

        # 清理
        os.remove(file_path)

    print("\n" + "=" * 60)
    print("8. 格式选择指南")
    print("=" * 60)

    print("\n根据场景选择合适的格式:")
    print()
    print("┌─────────────────────┬──────────┬──────────┬─────────┬────────────┐")
    print("│ 格式                 │ 速度     │ 压缩率   │ 兼容性  │ 适用场景   │")
    print("├─────────────────────┼──────────┼──────────┼─────────┼────────────┤")
    print("│ CSV                  │ ★★☆      │ ★☆☆      │ ★★★    │ 通用交换   │")
    print("│ Pickle               │ ★★★      │ ★★☆      │ ★☆☆    │ Python内部 │")
    print("│ Feather              │ ★★★      │ ★★☆      │ ★★☆    │ 临时存储   │")
    print("│ Parquet              │ ★★☆      │ ★★★      │ ★★☆    │ 大数据分析 │")
    print("│ JSON/JSONL           │ ★☆☆      │ ★☆☆      │ ★★★    │ Web API    │")
    print("│ Excel                │ ★☆☆      │ ★☆☆      │ ★★★    │ 办公用户   │")
    print("│ Stata/SAS            │ ★★☆      │ ★★☆      │ ★☆☆    │ 统计软件   │")
    print("└─────────────────────┴──────────┴──────────┴─────────┴────────────┘")

    print("\n详细建议:")
    print()
    print("1. 数据交换/协作:")
    print("   - 首选 CSV（最通用）")
    print("   - Excel 用于非技术人员")
    print()
    print("2. Python 进程间通信:")
    print("   - Pickle（最方便）")
    print("   - Feather（更快）")
    print()
    print("3. 大数据存储:")
    print("   - Parquet（列式，高压缩）")
    print("   - Feather（读取快）")
    print()
    print("4. 长期存储:")
    print("   - CSV 或 Parquet（开放格式）")
    print("   - 避免使用 Pickle（安全风险）")
    print()
    print("5. Web API:")
    print("   - JSON（标准格式）")
    print("   - JSON Lines（流式日志）")
    print()
    print("6. 与统计软件交换:")
    print("   - Stata: .dta 格式")
    print("   - SAS: .xpt 格式")
    print("   - R: CSV 或 RDS（用 pyreadr）")

    print("\n" + "=" * 60)
    print("9. 速查表")
    print("=" * 60)

    formats = {
        'to_csv()': 'CSV 格式，最通用',
        'to_json()': 'JSON 格式，适合 Web',
        'to_excel()': 'Excel 格式，办公使用',
        'to_pickle()': 'Pickle，Python 对象',
        'to_parquet()': 'Parquet，大数据',
        'to_feather()': 'Feather，高性能',
        'to_stata()': 'Stata .dta 格式',
        'to_html()': 'HTML 表格',
        'to_sql()': 'SQL 数据库',
        'to_dict()': 'Python 字典',
        'to_string()': '字符串表示',
    }

    print("\n输出方法:")
    for method, desc in formats.items():
        print(f"  {method:20s} # {desc}")

    read_methods = {
        'read_csv()': 'CSV 文件',
        'read_json()': 'JSON 文件',
        'read_excel()': 'Excel 文件',
        'read_pickle()': 'Pickle 文件',
        'read_parquet()': 'Parquet 文件',
        'read_feather()': 'Feather 文件',
        'read_stata()': 'Stata 文件',
        'read_sas()': 'SAS 文件',
        'read_html()': 'HTML 表格',
        'read_sql()': 'SQL 查询',
        'read_table()': '通用文本表格',
        'read_fwf()': '固定宽度格式',
    }

    print("\n读取方法:")
    for method, desc in read_methods.items():
        print(f"  {method:20s} # {desc}")

    print("\n" + "=" * 60)
    print("10. 注意事项")
    print("=" * 60)

    print("\n安全性:")
    print("  - 不要加载不可信来源的 Pickle 文件")
    print("  - 使用 CSV/JSON/Parquet 等文本或标准格式更安全")

    print("\n性能:")
    print("  - 大数据使用 Parquet（列式存储）")
    print("  - 频繁读写使用 Feather（速度快）")
    print("  - 考虑压缩以节省空间")

    print("\n兼容性:")
    print("  - CSV 最通用，但类型信息可能丢失")
    print("  - Parquet 是大数据生态标准")
    print("  - Excel 方便但性能差")

    print("\n类型保持:")
    print("  - Pickle: 完美保持 Python 类型")
    print("  - Parquet: 支持大多数数据类型")
    print("  - CSV: 需要指定类型")


if __name__ == "__main__":
    main()