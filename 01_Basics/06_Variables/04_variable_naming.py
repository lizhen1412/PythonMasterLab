#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：变量命名（标识符规则 + 命名约定）。
Author: Lambert

你会学到：
1) 什么字符串能当变量名：`str.isidentifier()`
2) 关键字不能用：`keyword.iskeyword()`
3) Python 变量名区分大小写：`name` 和 `Name` 不同
4) 常见命名约定（PEP 8 风格）：
   - 变量/函数：snake_case
   - 常量：UPPER_CASE（约定，不是语法）
   - “内部用”：_leading_underscore
   - 避免使用内置名：list、dict、type、id、str 等（容易遮蔽）
5) Unicode 变量名是允许的，但工程里通常不推荐（可读性/输入法/协作成本）

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/04_variable_naming.py
"""

from __future__ import annotations

import keyword


def main() -> None:
    print("1) 合法标识符检查：")
    candidates = ["x", "_x", "user_name", "2bad", "with space", "你好", "class", "x-y"]
    for s in candidates:
        print(f"{s!r:<12} isidentifier={s.isidentifier()} iskeyword={keyword.iskeyword(s)}")

    print("\n2) 大小写敏感：")
    name = "lower"
    Name = "upper"
    print("name =", name)
    print("Name =", Name)

    print("\n3) 命名约定示例：")
    user_name = "Alice"  # snake_case
    MAX_RETRY = 3  # 常量约定
    _internal_cache = {"user": user_name}  # 内部变量约定
    print("user_name =", user_name)
    print("MAX_RETRY =", MAX_RETRY)
    print("_internal_cache =", _internal_cache)

    print("\n4) 避免遮蔽内置名：")
    print("不推荐写：list = 123（会遮蔽内置 list 类型）")
    print("推荐写：list_ = 123 或 items = [...]")

    print("\n5) Unicode 变量名（演示可行，不推荐滥用）：")
    中文变量 = 42
    print("中文变量 =", 中文变量)


if __name__ == "__main__":
    main()
