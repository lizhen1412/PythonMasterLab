#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 53：Options API - Pandas 全局选项配置。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/53_options_api.py

Pandas 提供了丰富的全局选项，通过 `pd.set_option`、`pd.get_option` 和
`pd.reset_option` 来控制显示、计算、警告等行为。

本节演示：
1. 显示选项（行、列、宽度、精度）
2. 计算选项（精度、模式）
3. 性能选项
4. 格式化选项
5. 使用 with 上下文临时设置
6. 选项类别浏览
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. 显示选项 - 控制输出格式")
    print("=" * 60)

    # 创建一个较大的 DataFrame 用于演示
    df = pd.DataFrame(
        np.random.randn(20, 10),
        columns=[f"col_{i}" for i in range(10)],
        index=[f"row_{i}" for i in range(20)],
    )

    print("\n默认显示（可能被截断）:")
    print(df)

    # 显示更多行
    print("\n设置 display.max_rows = 25:")
    pd.set_option("display.max_rows", 25)
    print(df)

    # 显示所有列
    print("\n设置 display.max_columns = None (显示所有列):")
    pd.set_option("display.max_columns", None)
    print(df.head(3))

    # 重置
    pd.reset_option("display.max_rows")
    pd.reset_option("display.max_columns")

    print("\n" + "=" * 60)
    print("2. 列宽与精度")
    print("=" * 60)

    # 长文本列
    df_text = pd.DataFrame({
        "description": [
            "这是一个非常非常非常非常非常非常非常非常非常非常长的文本描述",
            "短文本",
            "中等长度文本描述"
        ]
    })

    print("\n默认列宽:")
    print(df_text)

    print("\n设置 display.max_colwidth = 50:")
    pd.set_option("display.max_colwidth", 50)
    print(df_text)

    # 浮点数精度
    df_float = pd.DataFrame({"value": [1.123456789, 2.987654321, 3.141592653]})
    print("\n默认浮点精度:")
    print(df_float)

    print("\n设置 display.precision = 2:")
    pd.set_option("display.precision", 2)
    print(df_float)

    # 重置
    pd.reset_option("display.max_colwidth")
    pd.reset_option("display.precision")

    print("\n" + "=" * 60)
    print("3. 显示格式选项")
    print("=" * 60)

    # 千分位分隔符
    df_large = pd.DataFrame({"population": [1000000, 2500000, 500000]})
    print("\n默认大数显示:")
    print(df_large)

    print("\n设置 display.float_format = '{:,.0f}':")
    pd.set_option("display.float_format", "{:,.0f}".format)
    print(df_large)

    pd.reset_option("display.float_format")

    # 科学计数法
    df_sci = pd.DataFrame({"tiny": [0.0000001, 0.0000002]})
    print("\n默认小数显示:")
    print(df_sci)

    print("\n设置 display.float_format = '{:.2e}':")
    pd.set_option("display.float_format", "{:.2e}".format)
    print(df_sci)

    pd.reset_option("display.float_format")

    print("\n" + "=" * 60)
    print("4. 数据框显示样式")
    print("=" * 60)

    # 表格边框样式
    df_style = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

    print("\ndisplay.notebook_repr_html (仅在 Jupyter 中有效):")
    print(f"当前值: {pd.get_option('display.notebook_repr_html')}")

    # 对齐
    print("\ndisplay.colheader_justify (right/left):")
    pd.set_option("display.colheader_justify", "right")
    print(df_style)
    pd.reset_option("display.colheader_justify")

    # 行索引显示
    print("\ndisplay.show_dimensions (truncate/show):")
    print(f"当前值: {pd.get_option('display.show_dimensions')}")

    print("\n" + "=" * 60)
    print("5. 计算与性能选项")
    print("=" * 60)

    # 计算引擎
    print("\n计算模式选项:")
    print(f"  mode.copy_on_write (实验性): {pd.get_option('mode.copy_on_write')}")

    # 性能相关
    print("\n性能选项:")
    print(f"  compute.use_bottleneck: {pd.get_option('compute.use_bottleneck')}")
    print(f"  compute.use_numexpr: {pd.get_option('compute.use_numexpr')}")

    # 警告控制
    print("\n警告选项:")
    print(f"  mode.chained_assignment: {pd.get_option('mode.chained_assignment')}")
    print(f"  mode.copy_on_write: {pd.get_option('mode.copy_on_write')}")

    print("\n" + "=" * 60)
    print("6. 使用 with 上下文临时设置")
    print("=" * 60)

    df_temp = pd.DataFrame({
        "value": [1.23456789, 2.3456789, 3.456789],
        "text": ["短", "中等长度文本", "这是一个非常长的文本内容"]
    })

    print("\n在 with 块中临时设置选项:")
    with pd.option_context("display.precision", 2, "display.max_colwidth", 10):
        print("with 块内:")
        print(df_temp)

    print("\nwith 块外（恢复原设置）:")
    print(df_temp)

    # 多个选项
    print("\n同时设置多个选项:")
    with pd.option_context(
        "display.max_rows", 5,
        "display.precision", 1,
        "display.max_colwidth", 20
    ):
        large_df = pd.DataFrame(np.random.randn(10, 3))
        print(large_df)

    print("\n" + "=" * 60)
    print("7. 常用选项速查")
    print("=" * 60)

    options_reference = {
        # 显示相关
        "display.max_rows": "最大显示行数",
        "display.min_rows": "最小显示行数",
        "display.max_columns": "最大显示列数",
        "display.max_colwidth": "最大列宽",
        "display.width": "显示宽度",
        "display.precision": "浮点精度",
        "display.float_format": "浮点格式化函数",
        "display.colheader_justify": "列标题对齐 (right/left)",
        "display.show_dimensions": "显示维度形状",
        "display.max_info_rows": "info() 最大行数",
        "display.max_info_columns": "info() 最大列数",
        "display.large_repr": "大数据框表示 (info/truncate)",

        # 性能相关
        "compute.use_bottleneck": "使用 bottleneck 加速",
        "compute.use_numexpr": "使用 numexpr 加速",
        "mode.copy_on_write": "写时复制模式",

        # 警告相关
        "mode.chained_assignment": "链式赋值警告 (warn/raise)",
        "mode.data_manager": "数据管理器模式",

        # 其他
        "display.html.table_schema": "HTML 表格 schema",
        "display.html.border": "HTML 表格边框",
    }

    print("\n常用选项参考:")
    for option, description in options_reference.items():
        current = pd.get_option(option)
        print(f"  {option:40s} = {current!r:20s} # {description}")

    print("\n" + "=" * 60)
    print("8. 浏览所有可用选项")
    print("=" * 60)

    print("\n选项类别:")
    print("  - display: 显示相关选项")
    print("  - compute: 计算性能选项")
    print("  - mode: 模式和行为选项")
    print("  - io: I/O 相关选项")

    print("\n获取特定类别的所有选项:")
    display_options = pd.describe_option("display")
    print(f"  display 类别有 {len(display_options)} 个选项")

    print("\n" + "=" * 60)
    print("9. 实用配置示例")
    print("=" * 60)

    print("\n配置1: 科学研究（高精度、完整显示）")
    print("  pd.set_option('display.precision', 10)")
    print("  pd.set_option('display.max_columns', None)")
    print("  pd.set_option('display.max_rows', None)")

    print("\n配置2: 快速预览（紧凑、简洁）")
    print("  pd.set_option('display.precision', 2)")
    print("  pd.set_option('display.max_rows', 10)")
    print("  pd.set_option('display.max_columns', 5)")
    print("  pd.set_option('display.width', 80)")

    print("\n配置3: 演示展示（格式化、美观）")
    print("  pd.set_option('display.float_format', '{:,.2f}'.format)")
    print("  pd.set_option('display.max_colwidth', 50)")
    print("  pd.set_option('display.colheader_justify', 'center')")

    print("\n配置4: 开发调试（详细信息）")
    print("  pd.set_option('mode.chained_assignment', 'raise')")
    print("  pd.set_option('display.max_info_rows', 10)")
    print("  pd.set_option('display.show_dimensions', True)")

    # 应用示例配置
    print("\n应用示例配置（快速预览）:")
    with pd.option_context(
        "display.precision", 2,
        "display.max_rows", 5,
        "display.max_columns", 4,
        "display.width", 60
    ):
        demo_df = pd.DataFrame(np.random.randn(10, 6))
        print(demo_df)

    print("\n" + "=" * 60)
    print("10. 永久配置（通过 pandas_profiling.py）")
    print("=" * 60)

    print("\n要在 ~/.ipython/profile_default/startup/pandas_config.py 中永久设置:")
    print("""
import pandas as pd

# 显示设置
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.precision', 2)
pd.set_option('display.width', 120)

# 性能设置
pd.set_option('compute.use_bottleneck', True)
pd.set_option('compute.use_numexpr', True)

# 警告设置
pd.set_option('mode.chained_assignment', 'warn')
    """)


if __name__ == "__main__":
    main()