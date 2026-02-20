#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：标识符规则与命名约定（Naming）。
Author: Lambert

你会学到：
1) 什么字符串能当变量名：`str.isidentifier()`
2) 关键字不能当变量名：`keyword.iskeyword()`
3) 常见命名约定（PEP 8）：
   - 变量/函数：snake_case
   - 常量（约定）：UPPER_CASE
   - “内部使用”：_leading_underscore
   - 类名：CapWords（PascalCase）

运行：
    python3 01_Basics/02_Variables/03_identifiers_and_naming.py
"""

import keyword


def main() -> None:
    candidates = [
        "name",
        "_name",
        "name_2",
        "2name",
        "with-hyphen",
        "class",
        "变量",
        "__magic__",
    ]

    print("变量名合法性检查：")
    for s in candidates:
        print(
            f"- {s!r:<14} isidentifier={s.isidentifier():<5} iskeyword={keyword.iskeyword(s):<5}"
        )

    print("\nPython 关键字（部分展示）：")
    print(keyword.kwlist[:12], "... (total =", len(keyword.kwlist), ")")

    print("\n命名建议（工程习惯）：")
    print("- 用 snake_case 表达含义，例如 user_id, total_count")
    print("- 不要用 list/dict/str 等覆盖内置名（会影响后续使用）")
    print("- 尽量避免使用难懂的缩写；宁可写清楚")
    print("- Unicode 标识符（如中文变量名）在语法上允许，但团队协作通常不推荐")


if __name__ == "__main__":
    main()
