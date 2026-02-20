#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：组合数据类型——本章总结
Author: Lambert

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/12_chapter_summary.py
"""

from __future__ import annotations


SUMMARY: list[str] = [
    "序列共性：索引/切片/遍历/len/in/解包/拼接与重复",
    "list：可变；append/extend/insert/remove/pop/sort/copy；遍历时不要原地增删元素",
    "tuple：不可变（但可包含可变对象）；常用于“不可变记录/多返回值/可哈希 key”",
    "range：惰性整数序列；支持 len/索引/切片；step 不能为 0；空 range 的 len=0",
    "str：不可变序列；文本处理优先 split/join/replace/strip",
    "dict：key->value；in 检查 key；get/setdefault/update/|= 是高频操作",
    "set：去重与集合运算；空集合用 set()；remove vs discard 的差异要记住",
    "可变性：b=a 不是复制；嵌套结构要理解浅拷贝/深拷贝",
]


def main() -> None:
    print("本章总结（Composite Types）：")
    for i, line in enumerate(SUMMARY, start=1):
        print(f"{i}. {line}")
    print("\n下一步：运行练习题索引 -> python3 01_Basics/12_Composite_Types/Exercises/01_overview.py")


if __name__ == "__main__":
    main()