#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 60：Styler 样式进阶。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/60_styler_advanced.py

知识点：
- background_gradient - 背景渐变
- bar - 数据条
- set_properties - 设置 CSS 属性
- applymap / apply - 自定义样式函数
- 样式链式调用
- 导出样式
- 条件样式
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cathy", "David", "Eve"],
            "score": [88, 75, 92, 85, 90],
            "age": [20, 21, 19, 22, 20],
            "salary": [5000, 6000, 5500, 7000, 6500],
        }
    )

    print("=" * 70)
    print("原始数据")
    print("=" * 70)
    print(df)

    print("\n" + "=" * 70)
    print("1. background_gradient - 背景渐变")
    print("=" * 70)

    print("\n1.1 默认渐变（蓝色系）")
    print("-" * 70)
    styled = df.style.background_gradient(subset=["score", "age", "salary"])
    print("注意：需要在支持 HTML 的环境（如 Jupyter）中查看效果")
    print(f"HTML 长度: {len(styled.to_html())} 字符")

    print("\n1.2 指定颜色映射")
    print("-" * 70)
    styled = df.style.background_gradient(subset=["score"], cmap="RdYlGn")
    print("cmap='RdYlGn' -> 红-黄-绿渐变")

    styled = df.style.background_gradient(subset=["salary"], cmap="viridis")
    print("cmap='viridis' -> 紫色系渐变")

    print("\n1.3 渐变方向")
    print("-" * 70)
    styled = df.style.background_gradient(subset=["score"], axis=1)
    print("axis=1 -> 横向渐变（按行）")

    styled = df.style.background_gradient(subset=["score"], axis=0)
    print("axis=0 -> 纵向渐变（按列，默认）")

    print("\n1.4 设置渐变范围")
    print("-" * 70)
    styled = df.style.background_gradient(subset=["salary"], vmin=5000, vmax=8000)
    print("vmin=5000, vmax=8000 -> 限定渐变范围")

    print("\n1.5 文本色")
    print("-" * 70)
    styled = df.style.background_gradient(subset=["score"], text_color_threshold=0.8)
    print("text_color_threshold=0.8 -> 自动选择文本颜色（黑/白）")

    print("\n" + "=" * 70)
    print("2. bar - 数据条")
    print("=" * 70)

    print("\n2.1 默认数据条")
    print("-" * 70)
    styled = df.style.bar(subset=["score"])
    print("在单元格中显示水平条形图")

    print("\n2.2 指定颜色")
    print("-" * 70)
    styled = df.style.bar(subset=["salary"], color="#ff9999")
    print("color='#ff9999' -> 红色数据条")

    print("\n2.3 正负值不同颜色")
    print("-" * 70)
    df_pos_neg = pd.DataFrame({"A": [10, -5, 15, -10, 20], "B": [-3, 8, -12, 5, -8]})
    print("含正负值的数据:")
    print(df_pos_neg)

    styled = df_pos_neg.style.bar(axis=0)
    print("正值为蓝色（向右），负值为红色（向左）")

    print("\n2.4 设置数据条范围")
    print("-" * 70)
    styled = df.style.bar(subset=["salary"], vmin=0, vmax=10000)
    print("vmin=0, vmax=10000 -> 固定数据条范围")

    print("\n2.5 对齐方式")
    print("-" * 70)
    styled = df.style.bar(subset=["score"], align="mid")
    print("align='mid' -> 从中间向两侧")
    print("align='zero' -> 从零点开始（默认）")
    print("align='left' -> 左对齐")

    print("\n" + "=" * 70)
    print("3. set_properties - 设置 CSS 属性")
    print("=" * 70)

    print("\n3.1 设置所有单元格")
    print("-" * 70)
    styled = df.style.set_properties(**{"font-family": "Arial", "font-size": "12pt"})
    print("设置字体和大小")

    print("\n3.2 按列设置属性")
    print("-" * 70)
    styled = df.style.set_properties(subset=["name"], **{"font-weight": "bold", "color": "blue"})
    print("name 列加粗并显示为蓝色")

    print("\n3.3 按索引设置属性")
    print("-" * 70)
    styled = df.style.set_properties(subset=pd.IndexSlice[1, :], **{"background-color": "yellow"})
    print("第 1 行（索引为 1）的背景设为黄色")

    print("\n3.4 复杂选择")
    print("-" * 70)
    styled = df.style.set_properties(
        subset=pd.IndexSlice[:3, ["score", "salary"]], **{"border": "2px solid black"}
    )
    print("前 3 行的 score 和 salary 列添加边框")

    print("\n" + "=" * 70)
    print("4. applymap / apply - 自定义样式函数")
    print("=" * 70)

    print("\n4.1 applymap - 逐元素应用")
    print("-" * 70)

    def highlight_score(val):
        """根据分数返回颜色"""
        if val >= 90:
            return "background-color: lightgreen"
        elif val >= 80:
            return "background-color: lightyellow"
        elif val >= 70:
            return "background-color: lightcoral"
        else:
            return "background-color: lightpink"

    styled = df.style.applymap(highlight_score, subset=["score"])
    print("根据分数值应用不同背景色")

    print("\n4.2 apply - 按行/列应用")
    print("-" * 70)

    def highlight_max_row(s):
        """高亮每行的最大值"""
        is_max = s == s.max()
        return ["font-weight: bold" if v else "" for v in is_max]

    styled = df[["score", "age", "salary"]].style.apply(highlight_max_row, axis=1)
    print("高亮每行的最大值")

    print("\n4.3 按列应用")
    print("-" * 70)

    def highlight_below_threshold(s):
        """标记低于阈值的数据"""
        threshold = s.mean()
        is_below = s < threshold
        return ["color: red" if v else "color: black" for v in is_below]

    styled = df[["score", "age", "salary"]].style.apply(highlight_below_threshold, axis=0)
    print("红色标记低于列均值的数据")

    print("\n" + "=" * 70)
    print("5. 样式链式调用")
    print("=" * 70)

    print("组合多个样式效果")
    print("-" * 70)

    styled = (
        df.style.background_gradient(subset=["score"], cmap="RdYlGn")
        .bar(subset=["salary"], color="#lightblue")
        .applymap(lambda x: "font-weight: bold" if x > 85 else "", subset=["score"])
        .set_properties(**{"font-family": "Arial"})
    )
    print("组合效果：渐变 + 数据条 + 加粗 + 字体")

    print("\n" + "=" * 70)
    print("6. format - 格式化显示")
    print("=" * 70)

    df_nums = pd.DataFrame({"float_val": [3.14159, 2.71828, 1.41421], "percent": [0.1234, 0.5678, 0.9012]})

    print("\n原始数据:")
    print(df_nums)

    print("\n6.1 格式化浮点数")
    print("-" * 70)
    styled = df_nums.style.format({"float_val": "{:.2f}"})
    print("保留 2 位小数")

    print("\n6.2 格式化百分比")
    print("-" * 70)
    styled = df_nums.style.format({"percent": "{:.2%}"})
    print("显示为百分比")

    print("\n6.3 格式化整数")
    print("-" * 70)
    df_salary = pd.DataFrame({"salary": [5000, 6000, 7000]})
    styled = df_salary.style.format({"salary": "{:,}"})
    print("添加千位分隔符")

    print("\n6.4 自定义格式")
    print("-" * 70)
    df_currency = pd.DataFrame({"price": [1234.5, 5678.9]})
    styled = df_currency.style.format({"price": "¥{:.2f}"})
    print('格式化为货币: "¥{:.2f}"')

    print("\n6.5 格式化精度")
    print("-" * 70)
    styled = df.style.format(precision=1)
    print("precision=1 -> 所有数值保留 1 位小数")

    print("\n" + "=" * 70)
    print("7. highlight_* 方法")
    print("=" * 70)

    print("\n7.1 highlight_max - 高亮最大值")
    print("-" * 70)
    styled = df.style.highlight_max(subset=["score", "age", "salary"])
    print("最大值高亮为黄色")

    print("\n7.2 highlight_min - 高亮最小值")
    print("-" * 70)
    styled = df.style.highlight_min(subset=["score", "age", "salary"])
    print("最小值高亮为浅蓝色")

    print("\n7.3 highlight_null - 高亮空值")
    print("-" * 70)
    df_null = pd.DataFrame({"A": [1, np.nan, 3], "B": [np.nan, 5, 6]})
    print("含 NaN 的数据:")
    print(df_null)

    styled = df_null.style.highlight_null(null_color="red")
    print("NaN 值显示为红色")

    print("\n7.4 highlight_between - 高亮区间内的值")
    print("-" * 70)
    styled = df.style.highlight_between(subset=["score"], left=80, right=90, color="lightgreen")
    print("80-90 分之间的值显示为浅绿色")

    print("\n" + "=" * 70)
    print("8. set_sticky - 固定行列")
    print("=" * 70)

    df_large = pd.DataFrame(np.random.randn(20, 10), columns=[f"Col{i}" for i in range(10)])
    print("创建一个较大的 DataFrame")

    print("\n8.1 固定索引")
    print("-" * 70)
    styled = df_large.style.set_sticky(axis=0)
    print("滚动时索引列保持可见")

    print("\n8.2 固定列名")
    print("-" * 70)
    styled = df_large.style.set_sticky(axis=1)
    print("滚动时列名行保持可见")

    print("\n" + "=" * 70)
    print("9. set_table_styles - 设置表格样式")
    print("=" * 70)

    print("\n9.1 设置表格边框")
    print("-" * 70)
    table_styles = [{"selector": "", "props": [("border", "2px solid black")]}]
    styled = df.style.set_table_styles(table_styles)
    print("添加黑色边框")

    print("\n9.2 设置表头样式")
    print("-" * 70)
    table_styles = [
        {"selector": "th", "props": [("background-color", "lightblue"), ("color", "black"), ("font-weight", "bold")]}
    ]
    styled = df.style.set_table_styles(table_styles)
    print("表头蓝色背景，黑色粗体文字")

    print("\n9.3 悬停效果")
    print("-" * 70)
    table_styles = [
        {"selector": "tr:hover", "props": [("background-color", "yellow")]}
    ]
    styled = df.style.set_table_styles(table_styles)
    print("鼠标悬停时行背景变黄")

    print("\n" + "=" * 70)
    print("10. set_table_attributes - 设置表格属性")
    print("=" * 70)

    styled = df.style.set_table_attributes('class="my-table" id="data-table"')
    print('添加 class="my-table" id="data-table"')

    print("\n" + "=" * 70)
    print("11. set_caption - 设置标题")
    print("=" * 70)

    styled = df.style.set_caption("学生成绩表")
    print("为表格添加标题")

    print("\n" + "=" * 70)
    print("12. hide_index - 隐藏索引")
    print("=" * 70)

    styled = df.style.hide(axis="index")
    print("隐藏索引列")

    print("\n" + "=" * 70)
    print("13. 导出样式")
    print("=" * 70)

    print("\n13.1 导出为 HTML")
    print("-" * 70)
    styled = df.style.background_gradient(subset=["score"])
    html_str = styled.to_html()
    print(f"to_html() -> HTML 字符串长度: {len(html_str)}")

    print("\n13.2 导出到 Excel")
    print("-" * 70)
    # 注意：需要 openpyxl 库
    try:
        styled.to_excel("styled_output.xlsx", engine="openpyxl")
        print("成功导出到 styled_output.xlsx")
    except ImportError:
        print("需要安装 openpyxl: pip install openpyxl")

    print("\n" + "=" * 70)
    print("14. 实际应用示例")
    print("=" * 70)

    # 示例 1: 热力图样式的财务报表
    print("\n示例 1: 财务报表热力图")
    financial_df = pd.DataFrame(
        {
            "Q1": [10000, 8000, 6000],
            "Q2": [12000, 9000, 7000],
            "Q3": [15000, 11000, 8500],
            "Q4": [18000, 13000, 10000],
        },
        index=["收入", "成本", "利润"],
    )

    print("财务数据:")
    print(financial_df)

    styled_financial = financial_df.style.background_gradient(cmap="RdYlGn", axis=1).format("${:,.0f}")
    print("\n样式化效果：红色（低）-> 黄色（中）-> 绿色（高）")

    # 示例 2: 条件格式化的成绩表
    print("\n示例 2: 成绩等级表")
    grades_df = pd.DataFrame(
        {"语文": [85, 90, 78, 92, 88], "数学": [92, 88, 95, 85, 90], "英语": [88, 85, 90, 87, 93]},
        index=["张三", "李四", "王五", "赵六", "钱七"],
    )

    print("成绩数据:")
    print(grades_df)

    def grade_color(val):
        if val >= 90:
            return "color: green; font-weight: bold"
        elif val >= 80:
            return "color: blue"
        elif val >= 60:
            return "color: orange"
        else:
            return "color: red"

    styled_grades = grades_df.style.applymap(grade_color).set_caption("学生成绩表").set_properties(
        **{"font-size": "12pt", "text-align": "center"}
    )
    print("\n样式化：>=90绿色加粗，80-89蓝色，60-79橙色，<60红色")

    # 示例 3: KPI 仪表板
    print("\n示例 3: KPI 数据条展示")
    kpi_df = pd.DataFrame(
        {"指标": ["销售额", "利润率", "客户数", "满意度"], "目标": [100, 15, 500, 90], "实际": [120, 12, 450, 95]}
    )

    print("KPI 数据:")
    print(kpi_df)

    styled_kpi = (
        kpi_df.style.hide(axis="index")
        .bar(subset=["目标", "实际"], color=["#ff9999", "#99cc99"], axis=1)
        .format({"目标": "{:,.0f}", "实际": "{:,.0f}"})
        .set_properties(**{"font-size": "11pt"})
    )
    print("\n样式化：数据条对比目标与实际")

    print("\n" + "=" * 70)
    print("15. 样式最佳实践")
    print("=" * 70)

    print("""
最佳实践：

1. 性能考虑：
   - 大数据集慎用复杂样式
   - 优先使用内置方法（如 background_gradient）
   - 避免过度使用 applymap

2. 可读性：
   - 不要使用过多颜色
   - 保持一致的配色方案
   - 添加说明性标题

3. 导出：
   - HTML：完整保留样式
   - Excel：需要 openpyxl，支持部分样式
   - PDF：需要额外库（如 weasyprint）

4. 条件样式：
   - 使用 meaningful 的颜色（如红=坏，绿=好）
   - 考虑色盲友好配色
   - 提供图例说明

5. 链式调用：
   - 按逻辑顺序组织样式
   - 先应用全局样式，再应用特定样式
   - 测试中间结果
""")


if __name__ == "__main__":
    main()