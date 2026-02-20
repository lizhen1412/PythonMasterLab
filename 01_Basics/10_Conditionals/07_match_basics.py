#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：match 基础（字面量/单例/OR/guard/默认分支）
Author: Lambert

你会学到：
1) `match subject:` / `case pattern:` 的基本结构
2) 从上到下匹配，第一个命中就执行；不会贯穿（no fallthrough）
3) 常用 pattern：字面量、None/True/False、OR（|）、默认分支 `_`
4) guard：`case pattern if cond: ...`
5) 一个重要坑：`case NAME:` 是“捕获模式”，不是“常量匹配”（几乎总是会匹配）

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/07_match_basics.py
"""

from __future__ import annotations


def http_status_label(code: int) -> str:
    match code:
        case 200 | 201 | 204:
            return "OK"
        case 301 | 302:
            return "Redirect"
        case 400:
            return "Bad Request"
        case 401 | 403:
            return "Auth Error"
        case 404:
            return "Not Found"
        case _:
            return "Other"


def sign(n: int) -> str:
    match n:
        case int() as x if x < 0:
            return "negative"
        case 0:
            return "zero"
        case int() as x if x > 0:
            return "positive"
        case _:
            return "not-int"


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) match 基础：HTTP 状态码分类")
    for code in [200, 201, 204, 302, 400, 401, 404, 500]:
        print(code, "->", http_status_label(code))

    show("2) guard：用 if 细化匹配（例如范围判断）")
    for n in [-3, 0, 7]:
        print(n, "->", sign(n))

    show("3) 重要坑提示：case NAME 是捕获，不是常量")
    print("提示：要匹配常量，请用字面量（case 'x':）或限定名（case Color.RED:）。")


if __name__ == "__main__":
    main()
