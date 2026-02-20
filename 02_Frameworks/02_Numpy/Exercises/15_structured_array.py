#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 15：结构化数组。
Author: Lambert

题目：
创建一个包含 name (字符串), age (整数), score (浮点数) 的结构化数组，
并按 score 排序。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/15_structured_array.py
"""

from __future__ import annotations

import numpy as np


def create_and_sort_students() -> np.ndarray:
    """创建学生结构化数组并按分数排序"""
    # 定义 dtype
    dt = np.dtype([
        ("name", "U10"),
        ("age", "i4"),
        ("score", "f4")
    ])

    # 创建数组
    students = np.array([
        ("Alice", 20, 85.5),
        ("Bob", 21, 92.0),
        ("Charlie", 20, 88.5),
        ("David", 22, 76.0),
    ], dtype=dt)

    # 按 score 排序
    return np.sort(students, order="score")[::-1]  # 降序


def main() -> None:
    sorted_students = create_and_sort_students()

    print("学生按分数排序（降序）:")
    for student in sorted_students:
        print(f"  {student['name']}: {student['score']}")

    # 验证
    assert sorted_students[0]["name"] == "Bob"
    assert sorted_students[-1]["name"] == "David"
    print("[OK] structured array sorted correctly")


if __name__ == "__main__":
    main()