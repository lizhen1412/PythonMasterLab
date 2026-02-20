#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 54：Advanced Plotting - 高级绘图。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/54_plotting_advanced.py

Pandas 内置了基于 Matplotlib 的绘图功能，提供快速可视化数据的方法。
注意：需要安装 matplotlib (pip install matplotlib)

本节演示：
1. 基础图表类型（线、柱、散点、饼、箱线、密度）
2. 子图布局 (subplots)
3. 图表自定义（标题、标签、样式）
4. 时间序列绘图
5. 多列分组绘图
6. 后端配置与保存
"""

from __future__ import annotations

import pandas as pd
import numpy as np

# 检查 matplotlib 是否可用
try:
    import matplotlib
    matplotlib.use("Agg")  # 使用非交互式后端
    import matplotlib.pyplot as plt

    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("警告: matplotlib 未安装，请运行 'pip install matplotlib'")


def main() -> None:
    if not MATPLOTLIB_AVAILABLE:
        print("\n本课程需要安装 matplotlib:")
        print("  pip install matplotlib")
        return

    print("=" * 60)
    print("1. 基础图表类型")
    print("=" * 60)

    # 创建示例数据
    df = pd.DataFrame(
        {
            "year": [2019, 2020, 2021, 2022, 2023],
            "sales": [100, 120, 150, 180, 200],
            "profit": [20, 25, 30, 35, 45],
            "expenses": [80, 95, 120, 145, 155],
        }
    )

    print("\n数据:")
    print(df)

    print("\n生成折线图:")
    df.plot(x="year", y=["sales", "profit", "expenses"], marker="o")
    plt.title("Sales, Profit, and Expenses (2019-2023)")
    plt.xlabel("Year")
    plt.ylabel("Amount ($K)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_line_plot.png", dpi=100)
    print("  保存到: /tmp/pandas_line_plot.png")
    plt.close()

    print("\n生成柱状图:")
    df.plot(x="year", y=["sales", "profit"], kind="bar")
    plt.title("Sales and Profit by Year")
    plt.xlabel("Year")
    plt.ylabel("Amount ($K)")
    plt.tight_layout()
    plt.savefig("/tmp/pandas_bar_plot.png", dpi=100)
    print("  保存到: /tmp/pandas_bar_plot.png")
    plt.close()

    print("\n生成堆叠柱状图:")
    df.plot(x="year", y=["sales", "expenses"], kind="bar", stacked=True)
    plt.title("Sales vs Expenses (Stacked)")
    plt.xlabel("Year")
    plt.ylabel("Amount ($K)")
    plt.tight_layout()
    plt.savefig("/tmp/pandas_stacked_bar.png", dpi=100)
    print("  保存到: /tmp/pandas_stacked_bar.png")
    plt.close()

    print("\n生成水平柱状图:")
    df.plot(x="year", y="sales", kind="barh")
    plt.title("Sales by Year")
    plt.tight_layout()
    plt.savefig("/tmp/pandas_barh_plot.png", dpi=100)
    print("  保存到: /tmp/pandas_barh_plot.png")
    plt.close()

    print("\n" + "=" * 60)
    print("2. 散点图和气泡图")
    print("=" * 60)

    # 创建散点图数据
    df_scatter = pd.DataFrame(
        {
            "x": np.random.randn(100),
            "y": np.random.randn(100),
            "size": np.random.randint(20, 200, 100),
            "category": np.random.choice(["A", "B", "C"], 100),
        }
    )

    print("\n散点图数据示例:")
    print(df_scatter.head())

    print("\n生成散点图:")
    df_scatter.plot.scatter(x="x", y="y", alpha=0.6)
    plt.title("Scatter Plot")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_scatter.png", dpi=100)
    print("  保存到: /tmp/pandas_scatter.png")
    plt.close()

    print("\n生成气泡图（size 用点的大小表示）:")
    df_scatter.plot.scatter(x="x", y="y", s="size", alpha=0.6)
    plt.title("Bubble Chart")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_bubble.png", dpi=100)
    print("  保存到: /tmp/pandas_bubble.png")
    plt.close()

    print("\n" + "=" * 60)
    print("3. 分布图（直方图、密度图、箱线图）")
    print("=" * 60)

    # 正态分布数据
    df_dist = pd.DataFrame({
        "normal": np.random.normal(0, 1, 1000),
        "uniform": np.random.uniform(-3, 3, 1000),
    })

    print("\n生成直方图:")
    df_dist.plot.hist(bins=30, alpha=0.7)
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("/tmp/pandas_hist.png", dpi=100)
    print("  保存到: /tmp/pandas_hist.png")
    plt.close()

    print("\n生成密度图:")
    df_dist.plot.density()
    plt.title("Density Plot")
    plt.xlabel("Value")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_density.png", dpi=100)
    print("  保存到: /tmp/pandas_density.png")
    plt.close()

    print("\n生成箱线图:")
    df_dist.plot.box()
    plt.title("Box Plot")
    plt.ylabel("Value")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_box.png", dpi=100)
    print("  保存到: /tmp/pandas_box.png")
    plt.close()

    print("\n生成面积图:")
    df.plot(x="year", y=["sales", "profit"], kind="area")
    plt.title("Sales and Profit (Area)")
    plt.tight_layout()
    plt.savefig("/tmp/pandas_area.png", dpi=100)
    print("  保存到: /tmp/pandas_area.png")
    plt.close()

    print("\n" + "=" * 60)
    print("4. 饼图")
    print("=" * 60)

    df_pie = pd.DataFrame(
        {"sales": [350, 250, 200, 150, 50]},
        index=["Product A", "Product B", "Product C", "Product D", "Product E"],
    )

    print("\n产品销售数据:")
    print(df_pie)

    print("\n生成饼图:")
    df_pie.plot.pie(y="sales", autopct="%.1f%%", figsize=(6, 6))
    plt.title("Sales by Product")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("/tmp/pandas_pie.png", dpi=100)
    print("  保存到: /tmp/pandas_pie.png")
    plt.close()

    print("\n" + "=" * 60)
    print("5. 子图布局 (subplots)")
    print("=" * 60)

    df_multi = pd.DataFrame(
        np.random.randn(100, 4),
        columns=["A", "B", "C", "D"],
    ).cumsum()

    print("\n多列数据:")
    print(df_multi.head())

    print("\n生成 2x2 子图:")
    axes = df_multi.plot(subplots=True, figsize=(10, 8), layout=(2, 2))
    plt.suptitle("Multiple Subplots", y=1.02)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_subplots.png", dpi=100)
    print("  保存到: /tmp/pandas_subplots.png")
    plt.close()

    print("\n生成共享 x 轴的子图:")
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    df_multi["A"].plot(ax=axes[0], title="Series A")
    df_multi["B"].plot(ax=axes[1], title="Series B")
    plt.tight_layout()
    plt.savefig("/tmp/pandas_shared_x.png", dpi=100)
    print("  保存到: /tmp/pandas_shared_x.png")
    plt.close()

    print("\n" + "=" * 60)
    print("6. 时间序列绘图")
    print("=" * 60)

    # 创建时间序列数据
    dates = pd.date_range("2023-01-01", periods=365, freq="D")
    df_ts = pd.DataFrame(
        {
            "value": np.random.randn(365).cumsum(),
            "smooth": np.random.randn(365).cumsum() + 10,
        },
        index=dates,
    )

    print("\n时间序列数据:")
    print(df_ts.head())

    print("\n生成时间序列折线图:")
    df_ts.plot(figsize=(12, 4))
    plt.title("Time Series (2023)")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_timeseries.png", dpi=100)
    print("  保存到: /tmp/pandas_timeseries.png")
    plt.close()

    print("\n生成月度重采样图:")
    df_ts.resample("ME").mean().plot(figsize=(12, 4))
    plt.title("Monthly Average")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_monthly.png", dpi=100)
    print("  保存到: /tmp/pandas_monthly.png")
    plt.close()

    print("\n" + "=" * 60)
    print("7. 图表样式和自定义")
    print("=" * 60)

    print("\n使用不同的样式:")
    styles = ["default", "seaborn-v0_8-darkgrid", "ggplot", "bmh"]
    for style in styles:
        try:
            with plt.style.context(style):
                df_sample = pd.DataFrame(
                    {"A": [1, 2, 3], "B": [3, 1, 2]}
                )
                df_sample.plot(kind="bar")
                plt.title(f"Style: {style}")
                plt.tight_layout()
                plt.savefig(f"/tmp/pandas_style_{style.replace('-', '_')}.png", dpi=100)
                plt.close()
                print(f"  保存样式 '{style}': /tmp/pandas_style_{style.replace('-', '_')}.png")
        except Exception as e:
            print(f"  样式 '{style}' 不可用: {e}")

    print("\n" + "=" * 60)
    print("8. 分组绘图")
    print("=" * 60)

    df_group = pd.DataFrame(
        {
            "category": np.repeat(["A", "B", "C"], 10),
            "value1": np.random.randn(30),
            "value2": np.random.randn(30) + 2,
        }
    )

    print("\n分组数据:")
    print(df_group.head())

    print("\n按类别分组的箱线图:")
    df_group.boxplot(column=["value1", "value2"], by="category", figsize=(10, 6))
    plt.suptitle("")
    plt.tight_layout()
    plt.savefig("/tmp/pandas_grouped_boxplot.png", dpi=100)
    print("  保存到: /tmp/pandas_grouped_boxplot.png")
    plt.close()

    print("\n按类别分组绘制多条线:")
    for cat, group in df_group.groupby("category"):
        plt.plot(group["value1"].values, label=f"Category {cat}", marker="o")
    plt.title("Value1 by Category")
    plt.xlabel("Index")
    plt.ylabel("Value1")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/pandas_grouped_lines.png", dpi=100)
    print("  保存到: /tmp/pandas_grouped_lines.png")
    plt.close()

    print("\n" + "=" * 60)
    print("9. 绘图后端配置")
    print("=" * 60)

    print("\n可用的 Matplotlib 后端:")
    print("  - Agg: 非交互式（保存到文件）")
    print("  - Qt5Agg: Qt5 交互式窗口")
    print("  - TkAgg: Tkinter 交互式窗口")
    print("  - MacOSX: macOS 原生窗口")
    print("  - notebook: Jupyter notebook 内嵌")

    print("\n设置后端的方法:")
    print("  import matplotlib")
    print("  matplotlib.use('Agg')  # 必须在 import pyplot 之前")
    print("  # 或在 Jupyter 中: %matplotlib widget")

    print("\n当前后端:", matplotlib.get_backend())

    print("\n" + "=" * 60)
    print("10. 常用绘图参数")
    print("=" * 60)

    print("\ndf.plot() 常用参数:")
    params = {
        "figsize": "(width, height) - 图表尺寸（英寸）",
        "title": "str - 图表标题",
        "grid": "bool - 是否显示网格",
        "legend": "bool - 是否显示图例",
        "logx/logy": "bool - 对数坐标轴",
        "xticks/yticks": "list - 刻度位置",
        "xlabel/ylabel": "str - 坐标轴标签",
        "xlim/ylim": "tuple - 坐标轴范围",
        "style": "list/dict - 线条样式",
        "alpha": "float - 透明度 (0-1)",
        "colormap": "str - 颜色映射",
        "secondary_y": "bool/list - 右侧 y 轴",
    }

    for param, desc in params.items():
        print(f"  {param:20s}: {desc}")

    print("\n示例：使用多个参数")
    df[["sales", "profit"]].plot(
        figsize=(10, 5),
        title="Sales & Profit Trend",
        grid=True,
        style=["-", "--"],
        alpha=0.8,
        marker="o",
    )
    plt.tight_layout()
    plt.savefig("/tmp/pandas_custom_params.png", dpi=100)
    print("\n保存自定义参数图表: /tmp/pandas_custom_params.png")
    plt.close()

    print("\n" + "=" * 60)
    print("完成！所有图表已保存到 /tmp/ 目录")
    print("=" * 60)


if __name__ == "__main__":
    main()