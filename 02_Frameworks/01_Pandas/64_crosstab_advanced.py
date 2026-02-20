#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 64：crosstab 高级操作。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/64_crosstab_advanced.py
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    print("=== 创建示例数据 ===")

    df = pd.DataFrame(
        {
            "gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Male"],
            "age_group": ["Young", "Young", "Middle", "Middle", "Old", "Old", "Young", "Middle"],
            "city": ["Beijing", "Shanghai", "Beijing", "Shanghai", "Beijing", "Shanghai", "Beijing", "Shanghai"],
            "purchase": [1, 1, 0, 1, 1, 0, 1, 1],
            "amount": [100, 150, 0, 200, 120, 0, 80, 180],
        }
    )

    print(df)

    # 1. 基础 crosstab
    print("\n=== 基础 crosstab ===")
    print("性别 vs 年龄组的交叉表:")
    print(pd.crosstab(df["gender"], df["age_group"]))

    # 2. crosstab with margins (总计)
    print("\n=== crosstab with margins ===")
    print("带行/列总计:")
    print(pd.crosstab(df["gender"], df["age_group"], margins=True, margins_name="总计"))

    # 3. crosstab with normalize
    print("\n=== crosstab with normalize ===")
    print("按行归一化 (占比):")
    print(pd.crosstab(df["gender"], df["age_group"], normalize="index"))
    print("\n按列归一化:")
    print(pd.crosstab(df["gender"], df["age_group"], normalize="columns"))
    print("\n按全部归一化:")
    print(pd.crosstab(df["gender"], df["age_group"], normalize="all"))

    # 4. crosstab with values (聚合)
    print("\n=== crosstab with values ===")
    print("性别 vs 年龄组，统计购买金额:")
    print(pd.crosstab(df["gender"], df["age_group"], values=df["amount"], aggfunc="sum"))
    print("\n统计平均金额:")
    print(pd.crosstab(df["gender"], df["age_group"], values=df["amount"], aggfunc="mean"))
    print("\n统计购买次数:")
    print(pd.crosstab(df["gender"], df["age_group"], values=df["purchase"], aggfunc="sum"))

    # 5. crosstab with multiple aggregation
    print("\n=== crosstab with multiple aggfunc ===")
    print("同时统计总和和计数:")
    result = pd.crosstab(
        df["gender"], df["age_group"],
        values=df["amount"],
        aggfunc=["sum", "count", "mean"]
    )
    print(result)

    # 6. crosstab with rownames and colnames
    print("\n=== crosstab with custom names ===")
    print("自定义行列名称:")
    print(pd.crosstab(
        df["gender"],
        df["age_group"],
        rownames=["性别"],
        colnames=["年龄组"],
        values=df["amount"],
        aggfunc="sum"
    ))

    # 7. 三维 crosstab
    print("\n=== 三维 crosstab ===")
    print("性别 vs 年龄组 vs 城市:")
    # 使用多个索引创建三维交叉表
    three_way = pd.crosstab(
        [df["gender"], df["age_group"]],
        df["city"],
        values=df["amount"],
        aggfunc="sum"
    )
    print(three_way)

    # 8. crosstab with dropna
    print("\n=== crosstab with dropna ===")
    df_na = df.copy()
    df_na.loc[1, "age_group"] = None
    print("包含 NaN 的数据:")
    print(df_na)
    print("\ndropna=True (默认):")
    print(pd.crosstab(df_na["gender"], df_na["age_group"], dropna=True))
    print("\ndropna=False:")
    print(pd.crosstab(df_na["gender"], df_na["age_group"], dropna=False))

    # 9. crosstab 的百分比格式化
    print("\n=== crosstab 百分比格式 ===")
    ct = pd.crosstab(df["gender"], df["age_group"], normalize="index") * 100
    print("百分比 (格式化):")
    print(ct.round(2).astype(str) + "%")

    # 10. crosstab 与 pivot_table 的对比
    print("\n=== crosstab vs pivot_table ===")
    print("crosstab (简洁计数):")
    print(pd.crosstab(df["gender"], df["age_group"]))
    print("\npivot_table (同样功能):")
    print(df.pivot_table(
        index="gender",
        columns="age_group",
        values="purchase",
        aggfunc="count",
        fill_value=0
    ))

    # 11. crosstab 组合示例：实际业务场景
    print("\n=== 实际业务场景 ===")
    # 分析不同性别和年龄组的购买情况
    analysis = pd.crosstab(
        [df["gender"], df["age_group"]],
        df["purchase"],
        values=df["amount"],
        aggfunc=["sum", "mean", "count"],
        margins=True,
        margins_name="总计"
    )
    print("购买分析 (性别 x 年龄组):")
    print(analysis)

    # 12. 按城市分层分析
    print("\n=== 按城市分层 ===")
    for city in df["city"].unique():
        city_data = df[df["city"] == city]
        print(f"\n{city} - 性别 vs 年龄组:")
        print(pd.crosstab(
            city_data["gender"],
            city_data["age_group"],
            values=city_data["amount"],
            aggfunc="sum",
            margins=True
        ))

    # 13. 使用 crosstab 做卡方检验的准备
    print("\n=== 卡方检验数据准备 ===")
    contingency_table = pd.crosstab(df["gender"], df["age_group"])
    print("列联表:")
    print(contingency_table)
    print("\n转置:")
    print(contingency_table.T)

    # 14. crosstab 的样式美化
    print("\n=== 样式美化提示 ===")
    print("可以使用 Styler 美化 crosstab 输出:")
    print("pd.crosstab(df['gender'], df['age_group']).style.background_gradient()")

    # 15. 交叉表的累计百分比
    print("\n=== 累计百分比 ===")
    ct = pd.crosstab(df["gender"], df["age_group"], normalize="index")
    cumsum = ct.cumsum(axis=1)
    print("累计百分比:")
    print(cumsum.round(3))


if __name__ == "__main__":
    main()