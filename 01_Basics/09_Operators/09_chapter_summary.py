#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：运算符——本章总结
Author: Lambert

运行（在仓库根目录执行）：
    python3 01_Basics/09_Operators/09_chapter_summary.py
"""

from __future__ import annotations


SUMMARY: list[str] = [
    "算术：含 @；/ 返回 float；// 向下取整；% 与 // 满足恒等式",
    "赋值：支持解包与增强赋值（含 @=）；可变对象的 += 可能原地修改（别名会被影响）",
    "比较：链式比较更清晰；浮点比较优先 math.isclose",
    "逻辑：and/or 短路且返回对象；不要滥用 x or default 处理 None",
    "位运算：适合掩码/标志位；READ = 1<<0 这种写法最常见",
    "成员：in/not in；dict 的 in 检查 key；is/is not 用于身份（特别是 None）",
    "优先级：不确定就加括号；尤其注意 -2**2、not/and/or、链式比较",
]


def main() -> None:
    print("本章总结（Operators）：")
    for i, line in enumerate(SUMMARY, start=1):
        print(f"{i}. {line}")
    print("\n下一步：运行练习题索引 -> python3 01_Basics/09_Operators/Exercises/01_overview.py")


if __name__ == "__main__":
    main()