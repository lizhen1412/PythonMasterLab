#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 20：结构化数组。

运行：
    python3 02_Frameworks/02_Numpy/20_structured_arrays.py

知识点：
- 创建结构化数组（dtype指定）
- 字段访问/字段名
- 嵌套字段
- 结构化数组操作
- 记录数组（np.recarray）
- 与pandas DataFrame对比
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. 创建结构化数组")
    print("=" * 70)

    print("\n1.1 使用元组列表指定 dtype")
    print("-" * 70)
    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    print(f"dtype: {dt}")

    arr = np.array([("Alice", 20, 88.5), ("Bob", 21, 92.0), ("Cathy", 19, 85.5)], dtype=dt)
    print(f"结构化数组:")
    print(arr)

    print("\n1.2 使用字典指定 dtype")
    print("-" * 70)
    dt = np.dtype({"names": ["name", "age", "score"], "formats": ["U10", "i4", "f4"]})
    arr = np.array([("David", 22, 90.0), ("Eve", 20, 87.5)], dtype=dt)
    print(arr)

    print("\n1.3 使用简写字符串")
    print("-" * 70)
    dt = np.dtype("U10,i4,f4")  # 等价于 ("names": ["f0", "f1", "f2"], ...)
    arr = np.array([("Frank", 23, 89.0)], dtype=dt)
    print(f"简写 dtype: {arr.dtype}")
    print(arr)

    print("\n1.4 指定对齐")
    print("-" * 70)
    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f8")], align=True)
    print(f"对齐的 dtype: {dt}")
    print(f"每个字段偏移: {dt.fields}")
    arr = np.array([("Grace", 21, 91.5)], dtype=dt)
    print(f"数组大小: {arr.nbytes} 字节")

    print("\n" + "=" * 70)
    print("2. 访问字段")
    print("=" * 70)

    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    arr = np.array([("Alice", 20, 88.5), ("Bob", 21, 92.0), ("Cathy", 19, 85.5)], dtype=dt)

    print("\n2.1 访问单个字段")
    print("-" * 70)
    print(f"arr['name'] -> {arr['name']}")
    print(f"arr['age'] -> {arr['age']}")
    print(f"arr['score'] -> {arr['score']}")

    print("\n2.2 访问单个元素")
    print("-" * 70)
    print(f"arr[0] -> {arr[0]}")
    print(f"arr[1] -> {arr[1]}")

    print("\n2.3 访问元素的特定字段")
    print("-" * 70)
    print(f"arr[0]['name'] -> {arr[0]['name']}")
    print(f"arr[1]['score'] -> {arr[1]['score']}")

    print("\n2.4 获取字段名")
    print("-" * 70)
    print(f"arr.dtype.names -> {arr.dtype.names}")

    print("\n" + "=" * 70)
    print("3. 修改字段")
    print("=" * 70)

    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    arr = np.array([("Alice", 20, 88.5), ("Bob", 21, 92.0)], dtype=dt)

    print("原始数组:")
    print(arr)

    # 修改整个字段
    arr["age"] = [25, 26]
    print("\n修改 age 字段后:")
    print(arr)

    # 修改单个元素的字段
    arr[0]["score"] = 95.0
    print("\n修改 arr[0]['score'] 后:")
    print(arr)

    # 添加新字段（需要创建新数组）
    print("\n添加新字段:")
    new_dt = np.dtype(
        [("name", "U10"), ("age", "i4"), ("score", "f4"), ("grade", "U2")]
    )
    new_arr = np.empty(len(arr), dtype=new_dt)
    for name in arr.dtype.names:
        new_arr[name] = arr[name]
    new_arr["grade"] = ["A", "A"]
    print(new_arr)

    print("\n" + "=" * 70)
    print("4. 嵌套字段")
    print("=" * 70)

    print("\n4.1 创建嵌套结构")
    print("-" * 70)
    dt = np.dtype(
        [
            ("name", "U10"),
            (
                "scores",
                [
                    ("midterm", "f4"),
                    ("final", "f4"),
                    ("homework", "f4"),
                ],
            ),
        ]
    )

    arr = np.array([("Alice", (85.0, 90.0, 88.0)), ("Bob", (78.0, 85.0, 82.0))], dtype=dt)
    print("嵌套结构:")
    print(arr)

    print("\n4.2 访问嵌套字段")
    print("-" * 70)
    print(f"arr['scores'] ->")
    print(arr["scores"])

    print(f"\narr['scores']['midterm'] -> {arr['scores']['midterm']}")

    print(f"\narr[0]['scores'] -> {arr[0]['scores']}")
    print(f"arr[0]['scores']['final'] -> {arr[0]['scores']['final']}")

    print("\n4.3 多层嵌套")
    print("-" * 70)
    dt = np.dtype(
        [
            ("student", "U10"),
            (
                "info",
                [
                    ("age", "i4"),
                    (
                        "address",
                        [("city", "U20"), ("zip", "U10")],
                    ),
                ],
            ),
        ]
    )

    arr = np.array(
        [("Alice", (20, ("Beijing", "100000"))), ("Bob", (21, ("Shanghai", "200000")))], dtype=dt
    )
    print("多层嵌套:")
    print(arr)
    print(f"\narr['info']['address'] ->")
    print(arr["info"]["address"])

    print("\n" + "=" * 70)
    print("5. 结构化数组操作")
    print("=" * 70)

    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    arr = np.array(
        [("Alice", 20, 88.5), ("Bob", 21, 92.0), ("Cathy", 19, 85.5), ("David", 22, 90.0)], dtype=dt
    )

    print("原始数组:")
    print(arr)

    print("\n5.1 排序")
    print("-" * 70)
    sorted_arr = np.sort(arr, order="score")
    print("按 score 排序:")
    print(sorted_arr)

    sorted_arr = np.sort(arr, order=["age", "score"])
    print("\n按 age 和 score 排序:")
    print(sorted_arr)

    print("\n5.2 筛选")
    print("-" * 70)
    mask = arr["score"] > 88
    print(f"score > 88: {arr[mask]}")

    print("\n5.3 字段计算")
    print("-" * 70)
    avg_score = np.mean(arr["score"])
    print(f"平均分: {avg_score:.2f}")

    print("\n5.4 添加计算字段")
    print("-" * 70)
    # 方法 1: 使用列表推导
    grades = np.array(["A" if s >= 90 else "B" if s >= 85 else "C" for s in arr["score"]], dtype="U2")
    print(f"成绩等级: {grades}")

    # 方法 2: 创建新数组
    new_dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4"), ("grade", "U2")])
    new_arr = np.empty(len(arr), dtype=new_dt)
    for name in arr.dtype.names:
        new_arr[name] = arr[name]
    new_arr["grade"] = grades
    print("\n添加 grade 字段后:")
    print(new_arr)

    print("\n" + "=" * 70)
    print("6. 记录数组（recarray）")
    print("=" * 70)

    print("\n6.1 创建记录数组")
    print("-" * 70)
    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    arr = np.array([("Alice", 20, 88.5), ("Bob", 21, 92.0)], dtype=dt)

    rec_arr = arr.view(np.recarray)
    print("recarray:")
    print(rec_arr)

    print("\n6.2 属性访问字段")
    print("-" * 70)
    print("结构化数组访问: arr['name']")
    print(f"  {arr['name']}")

    print("\n记录数组访问: rec_arr.name")
    print(f"  {rec_arr.name}")
    print(f"  {rec_arr.age}")
    print(f"  {rec_arr.score}")

    print("\n6.3 修改字段")
    print("-" * 70)
    rec_arr.age = [25, 26]
    print("修改 age 后:")
    print(rec_arr)

    print("\n6.4 recarray 性能注意事项")
    print("-" * 70)
    print("recarray 的属性访问比标准结构化数组慢")
    print("适合交互式使用，不适合性能关键代码")

    print("\n" + "=" * 70)
    print("7. 结构化数组 vs pandas DataFrame")
    print("=" * 70)

    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    struct_arr = np.array([("Alice", 20, 88.5), ("Bob", 21, 92.0)], dtype=dt)

    print("\n结构化数组:")
    print(struct_arr)
    print(f"内存: {struct_arr.nbytes} 字节")
    print(f"类型固定，性能高，适合数值计算")

    # 对比 DataFrame（需要 pandas）
    try:
        import pandas as pd

        df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [20, 21], "score": [88.5, 92.0]})
        print("\npandas DataFrame:")
        print(df)
        print(f"功能丰富，适合数据分析")
    except ImportError:
        print("\n(pandas 未安装，跳过 DataFrame 对比)")

    print("\n" + "=" * 70)
    print("8. 文件 I/O")
    print("=" * 70)

    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    arr = np.array([("Alice", 20, 88.5), ("Bob", 21, 92.0)], dtype=dt)

    print("\n8.1 保存到文件")
    print("-" * 70)
    np.save("structured_array.npy", arr)
    print("保存到 structured_array.npy")

    loaded = np.load("structured_array.npy")
    print("加载后:")
    print(loaded)

    print("\n8.2 保存为文本")
    print("-" * 70)
    np.savetxt("structured_array.txt", arr, fmt="%s,%d,%.2f")
    print("保存为文本（需要指定格式）")

    print("\n8.3 从 CSV 加载")
    print("-" * 70)
    # 假设有 CSV 文件
    # data = np.genfromtxt('data.csv', delimiter=',', dtype=dt)
    # print(data)

    print("\n" + "=" * 70)
    print("9. 高级操作")
    print("=" * 70)

    dt = np.dtype([("name", "U10"), ("age", "i4"), ("score", "f4")])
    arr = np.array(
        [("Alice", 20, 88.5), ("Bob", 21, 92.0), ("Cathy", 19, 85.5), ("David", 22, 90.0)], dtype=dt
    )

    print("\n9.1 按字段分组统计")
    print("-" * 70)
    # 按 age 分组
    unique_ages = np.unique(arr["age"])
    for age in unique_ages:
        mask = arr["age"] == age
        avg_score = np.mean(arr[mask]["score"])
        print(f"年龄 {age}: 平均分 {avg_score:.2f}")

    print("\n9.2 多字段筛选")
    print("-" * 70)
    mask = (arr["age"] >= 20) & (arr["score"] >= 90)
    print(f"age >= 20 且 score >= 90:")
    print(arr[mask])

    print("\n9.3 字段重命名")
    print("-" * 70)
    new_dt = np.dtype([("student_name", "U10"), ("student_age", "i4"), ("test_score", "f4")])
    new_arr = np.empty(len(arr), dtype=new_dt)
    for old_name, new_name in zip(arr.dtype.names, new_dt.names):
        new_arr[new_name] = arr[old_name]
    print("重命名字段后:")
    print(new_arr)

    print("\n" + "=" * 70)
    print("10. 实际应用示例")
    print("=" * 70)

    # 示例 1: 数据库表表示
    print("\n示例 1: 模拟数据库表")
    employee_dt = np.dtype(
        [
            ("id", "i4"),
            ("name", "U20"),
            ("department", "U20"),
            ("salary", "f8"),
            ("hire_date", "datetime64[D]"),
        ]
    )

    employees = np.array(
        [
            (1, "Alice", "Engineering", 80000.0, "2020-01-15"),
            (2, "Bob", "Sales", 65000.0, "2019-06-01"),
            (3, "Cathy", "Engineering", 85000.0, "2021-03-10"),
        ],
        dtype=employee_dt,
    )

    print("员工表:")
    for emp in employees:
        print(f"  {emp['id']}: {emp['name']}, {emp['department']}, ${emp['salary']:.2f}")

    # 示例 2: 科学数据记录
    print("\n示例 2: 实验数据记录")
    experiment_dt = np.dtype(
        [
            ("timestamp", "datetime64[s]"),
            ("temperature", "f8"),
            ("pressure", "f8"),
            ("humidity", "f8"),
        ]
    )

    experiments = np.array(
        [("2024-01-01T12:00", 25.5, 101325.0, 45.0), ("2024-01-01T13:00", 26.0, 101300.0, 47.5)],
        dtype=experiment_dt,
    )

    print("实验数据:")
    for exp in experiments:
        print(f"  {exp['timestamp']}: T={exp['temperature']}°C, P={exp['pressure']}Pa")

    # 示例 3: 图像元数据
    print("\n示例 3: 图像元数据")
    image_dt = np.dtype([("filename", "U50"), ("width", "i4"), ("height", "i4"), ("channels", "i4")])

    images = np.array(
        [("image1.jpg", 1920, 1080, 3), ("image2.png", 800, 600, 4), ("image3.bmp", 1024, 768, 3)],
        dtype=image_dt,
    )

    print("图像信息:")
    total_pixels = np.sum(images["width"] * images["height"])
    print(f"  总像素数: {total_pixels:,}")

    # 示例 4: 金融交易记录
    print("\n示例 4: 交易记录")
    transaction_dt = np.dtype(
        [
            ("transaction_id", "i8"),
            ("timestamp", "datetime64[ns]"),
            ("symbol", "U5"),
            ("quantity", "i4"),
            ("price", "f8"),
        ]
    )

    transactions = np.array(
        [
            (1001, "2024-01-01T09:30:00", "AAPL", 100, 150.25),
            (1002, "2024-01-01T09:31:00", "GOOGL", 50, 2800.50),
            (1003, "2024-01-01T09:32:00", "AAPL", -50, 150.50),
        ],
        dtype=transaction_dt,
    )

    print("交易记录:")
    for txn in transactions:
        action = "买入" if txn["quantity"] > 0 else "卖出"
        print(f"  {txn['timestamp']}: {action} {abs(txn['quantity'])} {txn['symbol']} @ ${txn['price']:.2f}")


if __name__ == "__main__":
    main()
