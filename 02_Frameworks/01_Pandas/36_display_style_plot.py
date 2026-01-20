#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 36：展示设置与样式（set_option/Styler/plot）。

运行：
    python3 02_Frameworks/01_Pandas/36_display_style_plot.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy"],
            "score": [88.5, 75.2, 92.0],
            "age": [20, 21, 19],
        }
    )

    pd.set_option("display.max_columns", 10)
    print("display.max_columns ->", pd.get_option("display.max_columns"))
    print("\nDataFrame ->")
    print(df)

    print("\nStyler ->")
    try:
        style = df.style.format({"score": "{:.1f}"}).highlight_max("score")
        html = style.to_html()
        print("Styler HTML 长度 ->", len(html))
    except Exception as exc:
        print("Styler 依赖缺失 ->", type(exc).__name__)

    print("\nplot (需要 matplotlib) ->")
    try:
        import matplotlib.pyplot as plt

        ax = df.plot(x="name", y="score", kind="bar", title="Score")
        print("plot 结果类型 ->", type(ax).__name__)
        plt.close()
    except Exception as exc:
        print("plot 依赖缺失 ->", type(exc).__name__)


if __name__ == "__main__":
    main()
