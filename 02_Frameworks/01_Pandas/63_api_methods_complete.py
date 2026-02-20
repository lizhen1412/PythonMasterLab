#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 63：DataFrame/Series API 方法补充 (clip, quantile, abs, diff, rank 等)。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/63_api_methods_complete.py
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def main() -> None:
    print("=== 创建示例数据 ===")

    df = pd.DataFrame(
        {
            "A": [1, -5, 3, -10, 5],
            "B": [10, 20, 30, 40, 50],
            "C": [100, 200, 300, 400, 500],
            "category": ["X", "Y", "X", "Y", "X"],
        }
    )

    print(df)

    # 1. clip - 裁剪值
    print("\n=== clip 裁剪 ===")
    print("将 A 列限制在 -3 到 3 之间:")
    print(df["A"].clip(-3, 3))
    print("\n下限裁剪 (只保留 > 0):")
    print(df["A"].clip(lower=0))

    # 2. clip_lower 和 clip_upper (已废弃，使用 clip)
    print("\n=== 按列裁剪 ===")
    print(df.clip(lower={"A": -5, "B": 15}, upper={"A": 3, "C": 350}))

    # 3. quantile - 分位数
    print("\n=== quantile 分位数 ===")
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("数据:", data.tolist())
    print(f"中位数 (0.5): {data.quantile(0.5)}")
    print(f"25% 分位: {data.quantile(0.25)}")
    print(f"75% 分位: {data.quantile(0.75)}")
    print(f"IQR (Q3-Q1): {data.quantile(0.75) - data.quantile(0.25)}")
    print("\n多个分位数:")
    print(data.quantile([0.25, 0.5, 0.75]))

    # 4. quantile 的 interpolation 参数
    print("\n=== quantile interpolation ===")
    s = pd.Series([1, 2, 3, 4])
    print("数据:", s.tolist())
    print("linear (默认):", s.quantile(0.5, interpolation="linear"))
    print("lower:", s.quantile(0.5, interpolation="lower"))
    print("higher:", s.quantile(0.5, interpolation="higher"))
    print("midpoint:", s.quantile(0.5, interpolation="midpoint"))
    print("nearest:", s.quantile(0.5, interpolation="nearest"))

    # 5. DataFrame quantile
    print("\n=== DataFrame quantile ===")
    print("每列的中位数:")
    print(df[["A", "B", "C"]].quantile(0.5))
    print("\n按行计算分位数:")
    print(df[["A", "B", "C"]].quantile(0.5, axis=1))

    # 6. abs - 绝对值
    print("\n=== abs 绝对值 ===")
    print("A 列绝对值:")
    print(df["A"].abs())

    # 7. diff - 差分
    print("\n=== diff 差分 ===")
    df_diff = pd.DataFrame({"value": [10, 15, 12, 20, 18]})
    print("原始:")
    print(df_diff)
    print("\n一阶差分:")
    print(df_diff["value"].diff())
    print("\n二阶差分:")
    print(df_diff["value"].diff(2))
    print("\n反向差分:")
    print(df_diff["value"].diff(-1))

    # 8. pct_change - 百分比变化
    print("\n=== pct_change 百分比变化 ===")
    print("原始:")
    print(df_diff)
    print("\n百分比变化:")
    print(df_diff["value"].pct_change())
    print("\n相对于2期前的百分比变化:")
    print(df_diff["value"].pct_change(periods=2))

    # 9. rank - 排名
    print("\n=== rank 排名 ===")
    df_rank = pd.DataFrame({"score": [88, 92, 88, 75, 92]})
    print("原始:")
    print(df_rank)
    print("\n平均排名 (默认):")
    print(df_rank["score"].rank())
    print("\n最小排名 (相同值取较小排名):")
    print(df_rank["score"].rank(method="min"))
    print("\n最大排名 (相同值取较大排名):")
    print(df_rank["score"].rank(method="max"))
    print("\n密集排名 (相同值排名相同，下一个连续):")
    print(df_rank["score"].rank(method="dense"))
    print("\n顺序排名 (按出现顺序):")
    print(df_rank["score"].rank(method="first"))
    print("\n降序排名:")
    print(df_rank["score"].rank(ascending=False))

    # 10. nunique - 唯一值数量
    print("\n=== nunique 唯一值数量 ===")
    print("每列唯一值数量:")
    print(df.nunique())
    print("\n按类别分组的唯一值数量:")
    print(df.groupby("category").nunique())

    # 11. value_counts - 值计数
    print("\n=== value_counts 值计数 ===")
    print("category 列的值计数:")
    print(df["category"].value_counts())
    print("\n归一化计数 (占比):")
    print(df["category"].value_counts(normalize=True))
    print("\n降序:")
    print(df["category"].value_counts(ascending=True))
    print("\n包含 NaN:")
    df_with_na = df.copy()
    df_with_na.loc[1, "category"] = None
    print(df_with_na["category"].value_counts(dropna=False))

    # 12. round - 四舍五入
    print("\n=== round 四舍五入 ===")
    df_decimals = pd.DataFrame({
        "A": [1.234, 2.567, 3.891],
        "B": [10.456, 20.789, 30.123]
    })
    print("原始:")
    print(df_decimals)
    print("\n保留1位小数:")
    print(df_decimals.round(1))
    print("\n按列指定小数位:")
    print(df_decimals.round({"A": 1, "B": 2}))

    # 13. mad - 平均绝对偏差
    print("\n=== mad 平均绝对偏差 ===")
    print("A 列的平均绝对偏差:")
    print(df["A"].mad())
    print("\n所有列的 mad:")
    print(df[["A", "B", "C"]].mad())

    # 14. sem - 标准误差
    print("\n=== sem 标准误差 ===")
    print("C 列的标准误差:")
    print(df["C"].sem())
    print("\n按类别分组的 sem:")
    print(df.groupby("category")["A"].sem())

    # 15. kurt - 峰度
    print("\n=== kurt 峰度 ===")
    print("C 列的峰度:")
    print(df["C"].kurt())
    print("\n所有列的峰度:")
    print(df[["A", "B", "C"]].kurt())

    # 16. skew - 偏度
    print("\n=== skew 偏度 ===")
    print("A 列的偏度:")
    print(df["A"].skew())
    print("\n所有列的偏度:")
    print(df[["A", "B", "C"]].skew())

    # 17. prod - 乘积
    print("\n=== prod 乘积 ===")
    print("A 列乘积:")
    print(df["A"].prod())
    print("\n累积乘积 cumprod:")
    print(df["A"].cumprod())

    # 18. cumsum - 累积和
    print("\n=== cumsum 累积和 ===")
    print("C 列累积和:")
    print(df["C"].cumsum())

    # 19. cummax - 累积最大值
    print("\n=== cummax 累积最大值 ===")
    print("C 列累积最大值:")
    print(df["C"].cummax())

    # 20. cummin - 累积最小值
    print("\n=== cummin 累积最小值 ===")
    print("A 列累积最小值:")
    print(df["A"].cummin())

    # 21. ptp - 峰峰值 (max - min)
    print("\n=== ptp 峰峰值 ===")
    print("A 列的 ptp (max-min):")
    print(df["A"].ptp())

    # 22. mode - 众数
    print("\n=== mode 众数 ===")
    df_mode = pd.DataFrame({"category": ["A", "B", "A", "A", "B", "C"]})
    print("category 列的众数:")
    print(df_mode["category"].mode())
    print("\nDataFrame 众数 (每列):")
    print(df[["category"]].mode())

    # 23. median - 中位数
    print("\n=== median 中位数 ===")
    print("A 列中位数:", df["A"].median())
    print("所有列中位数:")
    print(df[["A", "B", "C"]].median())

    # 24. corr - 相关系数
    print("\n=== corr 相关系数 ===")
    print("列之间的相关系数:")
    print(df[["A", "B", "C"]].corr())
    print("\n使用 spearman 方法:")
    print(df[["A", "B", "C"]].corr(method="spearman"))
    print("\n使用 kendall 方法:")
    print(df[["A", "B", "C"]].corr(method="kendall"))

    # 25. cov - 协方差
    print("\n=== cov 协方差 ===")
    print("列之间的协方差:")
    print(df[["A", "B", "C"]].cov())

    # 26. between - 判断值是否在区间内
    print("\n=== between 区间判断 ===")
    print("B 列值是否在 15-35 之间:")
    print(df["B"].between(15, 35))
    print("\n筛选符合条件的行:")
    print(df[df["B"].between(15, 35)])

    # 27. isin - 判断值是否在列表中
    print("\n=== isin 成员判断 ===")
    print("category 是否在 ['X', 'Z'] 中:")
    print(df["category"].isin(["X", "Z"]))
    print("\n筛选 category 为 X 或 Z 的行:")
    print(df[df["category"].isin(["X", "Z"])])


if __name__ == "__main__":
    main()